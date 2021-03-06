var os_path = require('path');
var fs = require('fs');
var { remote, ipcRenderer } = require('electron');
const { app, dialog } = remote;

settings_path = os_path.join(app.getPath("appData"), "build_downloader", "default_settings.json");
hpc_options_folder = os_path.join(app.getPath("appData"), "build_downloader", "HPC_Options")

$("#install_path, #download_path").click(
    /**
     * when click in the input box for download and installation path => open Electron dialog to select directory.
     * In HTML cursor is blurred to disable direct change in input field: see settings.html
     */
    function(){
        dialog.showOpenDialog(remote.getCurrentWindow(), {
                defaultPath: this.value,
                properties: [ 'openDirectory' ]
            }).then(
            result => {
                if (result.canceled == false) {
                    let selected_path = result.filePaths[0];
                    if (this.id == "install_path"){
                        if (selected_path.toLowerCase().endsWith("ansysem")){
                            selected_path = truncate_path("AnsysEM", selected_path);
                        } else if (selected_path.toLowerCase().endsWith("ansys inc")){
                            selected_path = truncate_path("Ansys Inc", selected_path);
                        }
                    }

                    this.value = selected_path;
                    save_settings.call(this);
                }
            }).catch(err => {
                  console.log(err)
                })
    }
);

function truncate_path(name, selected_path){
    /**
     * truncates end of the path.
     * name (str): what should be removed
     * selected_path (str): path that user selected. Would be truncated
     */
    let truncated_path = selected_path.slice(0, selected_path.length - name.length - 1);
    answer = dialog.showMessageBoxSync(remote.getCurrentWindow(), {
            type: "question",
            buttons: ["Yes", "No"],
            message: "Path contains '" + name + "', Do you want to use '" + truncated_path + "' instead?"
        }
    )

    if (answer == 0) {
        return truncated_path;
    }
    return selected_path;
}

$(document).ready(function() {
    /**
     * On load of the page set settings from JSON file.
     * Enable tooltips
     * If not directory with HPC options => create one
     */
    if (fs.existsSync(settings_path)) {
        var settings_data = fs.readFileSync(settings_path);
        settings = JSON.parse(settings_data);

        if (!("replace_shortcut" in settings)){
            settings.replace_shortcut = true;  // for backwards compatibility
        }

        $("#install_path").val(settings.install_path);
        $("#download_path").val(settings.download_path);
        $("#delete_zip").prop("checked", settings.delete_zip);
        $("#force_install").prop("checked", settings.force_install);
        $("#replace_shortcut").prop("checked", settings.replace_shortcut);
    }

    set_default_tooltips_settings();

    if (!fs.existsSync(hpc_options_folder)) fs.mkdirSync(hpc_options_folder);
});

$(document).ready(function() {
    /**
     * Create JQuery DataTables for EDT HPC options file.
     * Update table rows, see tables_setter.js
     */
    hpc_table = $('#hpc-options-table').DataTable( {
        "scrollY": "165px",
        "scrollCollapse": true,
        "paging": false,
        "filter": false,
        "info": false,
        "order": [[ 0, "desc" ]]
    } );
    add_hpc_files_rows();
} );

var save_settings = function(){
    /** 
     * Save settings to the file on every UI change
    */
    if (this.id == "force_install" || this.id == "delete_zip" || this.id == "replace_shortcut"){
        settings[this.id] = this.checked;
    } else {
        settings[this.id] = this.value;
    }

    let data = JSON.stringify(settings, null, 4);
    fs.writeFileSync(settings_path, data);
};

$("#add-file-button").click(
    /**
     * When click on the button to append options => 
     * 1. open Electron dialog with filter for .acf files
     * 2. read user input, might be multiple selection
     * 3. synchronously copy files to settings folder/HPC_options
     * 4. update table rows, see tables_setter.js
     */
    function(){
        dialog.showOpenDialog(remote.getCurrentWindow(), {
                properties: ['openFile', 'multiSelections'],
                filters: [
                    { name: 'HPC Options', extensions: ['acf'] },
                    { name: 'Registry Options', extensions: ['txt'] }
                ]
            }).then(
            result => {
                if (result.canceled == false) {
                    var files_selected = result.filePaths;
                    for (var i in files_selected) {
                        var destination = os_path.join(hpc_options_folder, os_path.basename(result.filePaths[i]));
                        fs.copyFileSync(result.filePaths[i], destination , (err) => {
                          if (err) throw err;
                        });
                    }
                    add_hpc_files_rows();
                }
            }).catch(err => {
                  console.log(err)
                })
    }
);

$('#select-all-checkbox').on('click', function(){
    // Check/uncheck all checkboxes in the table
    var rows = flags_table.rows({ 'search': 'applied' }).nodes();
    $('input[type="checkbox"]', rows).prop('checked', this.checked);
});



$('#wb-flags-button').on('click', function(){
    /**
     * when click on save button go through all rows and those that are selected add to the list and update settings
     */
     ipcRenderer.send('wb_flags_show');
});


$("#install_path, #download_path, #password, #force_install, #delete_zip, #replace_shortcut").bind("change", save_settings);
