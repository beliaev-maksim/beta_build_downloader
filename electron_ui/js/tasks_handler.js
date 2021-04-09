var path = require('path');
const { remote } = require('electron');
const { app, dialog } = remote;
const { exec, execSync} = require('child_process');
var parser = require('fast-xml-parser');

if (app.isPackaged) {
      backend_exe = path.join(app.getAppPath() + ".unpacked", "python_build", "downloader_backend.exe"); // production
} else {
      backend_exe = path.join(app.getAppPath(), "python_build", "downloader_backend.exe");  // develop
}

function get_task_details(task) {
      let task_data_dict = {}

      clean_task = task.replace(/(\r\n|\n|\r)/gm,""); //make it single line
      clean_task = clean_task.replace(/(^\s*<!--.*?-->)/g,""); //Remove comments

      if( parser.validate(clean_task) === true) {
            var jsonObj = parser.parse(clean_task, { ignoreNameSpace : false });

            let long_days = Object.keys(jsonObj.Task.Triggers.CalendarTrigger.ScheduleByWeek.DaysOfWeek);
            let short_days = [];
            for (let i in long_days){
                  short_days.push(long_days[i].slice(0, 2));
            }        
            task_data_dict.days = short_days;

            task_data_dict.time = jsonObj.Task.Triggers.CalendarTrigger.StartBoundary.split("T")[1].slice(0, -3);
            
            let task_name = jsonObj.Task.RegistrationInfo.URI.split("\\")[2].split("_");           
            task_data_dict.version = task_name[0];
            task_data_dict.product = task_name[1];
      } else {
            console.log("failed validation");
      }
      return task_data_dict;
}

function get_active_tasks() {
      let all_tasks = execSync('schtasks /query /xml').toString();
      all_tasks = all_tasks.split("\r\n\r\n\r\n");
      let ansys_tasks = [];

      for(var i = 0; i < all_tasks.length; i++){
            if (all_tasks[i].includes("AnsysDownloader")){
                  task_data_dict = get_task_details(all_tasks[i]);
                  task_data_dict["schedule_time"] = (task_data_dict["days"]).join(", ") + " at " + 
                        task_data_dict["time"];
                  ansys_tasks.push(task_data_dict);
            }
      }
      add_task_rows(ansys_tasks);
}

function delete_task(task_name) {
      command = `schtasks /DELETE /TN "AnsysDownloader\\${task_name}" /f`;  // /f - silent
      execSync(command);
}
    
function schedule_task(settings_file) {
      unpack_days = {
            "mo": "MON",
            "tu": "TUE",
            "we": "WED",
            "th": "THU",
            "fr": "FRI",
            "sa": "SAT",
            "su": "SUN"
      }
      days = [];
      for (let i in settings["days"]) {
            short_day = settings["days"][i];
            days.push(unpack_days[short_day]);
      }

      command = (`schtasks /CREATE /TN "AnsysDownloader\\${settings.version}" /RL HIGHEST ` +
                  `/TR "${backend_exe} -p ${settings_file}" /d ${days.join(",")} /sc WEEKLY /st ${settings["time"]} /f`)

      execSync(command);
}

function install_once(settings_file) {
      command = `"${backend_exe}" -p "${settings_file}"`
      // some issue with SharePoint. Better to put some timeout
      exec(command);  // async
}

function get_sharepoint_builds() {
      let installed = execSync("powershell.exe Get-Module SharePointPnPPowerShellOnline -ListAvailable").toString();

      if (installed == 0) {
            dialog.showMessageBox(null, {
                  type: 'info',
                  buttons: ['OK'],
                  defaultId: 2,
                  title: 'First time configuration',
                  detail: "First time configuration. Installing required modules, this may take up to 5 min. " +
                  "Interface will be blocked. Wait until Version and Product list will be filled with data"
            });

            // install module
            let command = 'powershell.exe ';
            command += "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;";
            command += "Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force;";
            command += "Set-PSRepository -Name 'PSGallery' -InstallationPolicy Trusted;";
            command += "Install-Module SharePointPnPPowerShellOnline;";
            execSync(command);
      }

      let command = 'powershell.exe ';
      command += 'Connect-PnPOnline -Url https://ansys.sharepoint.com/sites/BetaDownloader -UseWebLogin; '; 
      command += 'Get-PnPListItem -List product_list -Fields Title; ';

      let builds_query = execSync(command).toString();
      builds_query = builds_query.split("\n").slice(3);
      let builds = [];
      for(var i = 0; i < builds_query.length; i++){
            var new_build = builds_query[i].split(" ");
            new_build = new_build.filter((item) => item.includes("Electronics") || item.includes("Workbench"));
            if (new_build.length == 1) {
                  new_build = new_build[0];
                  if (!builds.includes(new_build)){
                        builds.push(new_build);
                  }
            } 
      }
      fill_versions(builds);
      update_ipc_products(builds);
}