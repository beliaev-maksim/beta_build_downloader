# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Feb 17 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class Ansys_Beta_Downloader_UI
###########################################################################

class Ansys_Beta_Downloader_UI (wx.Frame):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size(700,550), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer261 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer261.SetMinSize( wx.Size(100,50) )

		bSizer261.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1221 = wx.StaticText( self, wx.ID_ANY, u"Configuration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1221.Wrap( -1 )

		self.m_staticText1221.SetFont( wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString) )

		bSizer261.Add( self.m_staticText1221, 0, wx.ALL, 5 )


		bSizer261.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer261, 0, wx.EXPAND, 5 )

		self.m_staticline14 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Installation Path", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer4.Add( self.m_staticText1, 0, wx.ALL, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.install_path = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300,-1), 0 )
		bSizer15.Add( self.install_path, 0, wx.ALL, 5 )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.set_install_path_but = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size(30,30), 0 )
		bSizer15.Add( self.set_install_path_but, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer15, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer4, 2, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Artifactory Encrypted Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer43.Add( self.m_staticText13, 0, wx.ALL, 5 )

		bSizer152 = wx.BoxSizer( wx.HORIZONTAL )

		self.password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300,-1), wx.TE_PASSWORD )
		self.password.SetToolTip( u"Retrieval of Artifactory Encrypted Password Instructions:\n\n1. Log into Artifactory\n\n2. Click on your username (top right)\n\n3. Enter your password to Unlock Artifactory Encrypted Password\n\n[Note] You cannot use the same artifactory password for other artifactories. Also, your encrypted password will change anytime your SSO password changes." )

		bSizer152.Add( self.password, 0, wx.ALL, 5 )


		bSizer152.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer43.Add( bSizer152, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer43, 2, wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer45 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Delete downloaded ZIP and directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer45.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )

		self.download_path = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300,-1), 0 )
		bSizer151.Add( self.download_path, 0, wx.ALL, 5 )


		bSizer151.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.set_download_path_but = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size(30,30), 0 )
		bSizer151.Add( self.set_download_path_but, 0, wx.ALL, 5 )


		bSizer45.Add( bSizer151, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer45, 2, wx.EXPAND, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Artifactory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer41.Add( self.m_staticText11, 0, wx.ALL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		artifactory_dropmenuChoices = []
		self.artifactory_dropmenu = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.Size(250,-1), artifactory_dropmenuChoices, 0 )
		bSizer41.Add( self.artifactory_dropmenu, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer41, 1, wx.EXPAND, 5 )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Version", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer42.Add( self.m_staticText12, 0, wx.ALL, 5 )


		bSizer42.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		version_dropmenuChoices = []
		self.version_dropmenu = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.Size(250,-1), version_dropmenuChoices, 0 )
		bSizer42.Add( self.version_dropmenu, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer42, 1, wx.EXPAND, 5 )

		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer421 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText121 = wx.StaticText( self, wx.ID_ANY, u"Date (EDT Only)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		bSizer421.Add( self.m_staticText121, 0, wx.ALL, 5 )


		bSizer421.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		date_dropmenuChoices = []
		self.date_dropmenu = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.Size(250,-1), date_dropmenuChoices, 0 )
		bSizer421.Add( self.date_dropmenu, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer421, 1, wx.EXPAND, 5 )

		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer271 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"WB Silent Installation Flags", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer271.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300,-1), 0 )
		self.m_textCtrl10.SetToolTip( u"Product    Product Flag\nMechanical APDL    -mechapdl\nANSYS Customization Files    -ansyscust\nANSYS Autodyn    -autodyn\nANSYS LS-DYNA    -lsdyna\nANSYS CFD-Post    -cfdpost\nANSYS CFX    -cfx\nANSYS EnSight    -ensight\nANSYS TurboGrid    -turbogrid\nANSYS Fluent    -fluent\nANSYS Polyflow    -polyflow\nANSYS ICEM CFD    -icemcfd\nANSYS Forte    -forte\nANSYS Chemkin    -chemkinpro\nANSYS Energico    -energico\nANSYS FENSAP-ICE    -fensapice\nANSYS Reaction Workbench    -reactionwb\nANSYS Model Fuel Library (Encrypted)    -mfl\n# Note Installing any of the above products will install ANSYS Workbench\nANSYS Remote Solve Manager Standalone Services    -rsm\nParasolid Geometry Interface    -parasolid\nACIS Geometry Interface    -acis\nNX Geometry Interface Plugin    -ug_plugin\nANSYS Icepak    -icepak\nCATIA 5 Reader    -catia5_reader" )

		bSizer271.Add( self.m_textCtrl10, 3, wx.ALL, 5 )


		bSizer271.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer271, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 5, wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer56 = wx.BoxSizer( wx.VERTICAL )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer26.SetMinSize( wx.Size(100,50) )

		bSizer26.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText122 = wx.StaticText( self, wx.ID_ANY, u"Autoupdate Scheduler", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText122.Wrap( -1 )

		self.m_staticText122.SetFont( wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString) )

		bSizer26.Add( self.m_staticText122, 0, wx.ALL, 5 )


		bSizer26.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer56.Add( bSizer26, 0, wx.EXPAND, 5 )

		self.m_staticline12 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer56.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer50 = wx.BoxSizer( wx.HORIZONTAL )

		self.mo_check = wx.CheckBox( self, wx.ID_ANY, u"Mo", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer50.Add( self.mo_check, 0, wx.ALL, 5 )

		self.tu_check = wx.CheckBox( self, wx.ID_ANY, u"Tu", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer50.Add( self.tu_check, 0, wx.ALL, 5 )

		self.we_check = wx.CheckBox( self, wx.ID_ANY, u"We", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer50.Add( self.we_check, 0, wx.ALL, 5 )

		self.th_check = wx.CheckBox( self, wx.ID_ANY, u"Th", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer50.Add( self.th_check, 0, wx.ALL, 5 )

		self.fr_check = wx.CheckBox( self, wx.ID_ANY, u"Fr", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer50.Add( self.fr_check, 0, wx.ALL, 5 )

		self.sa_check = wx.CheckBox( self, wx.ID_ANY, u"Sa", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer50.Add( self.sa_check, 0, wx.ALL, 5 )

		self.so_check = wx.CheckBox( self, wx.ID_ANY, u"So", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer50.Add( self.so_check, 0, wx.ALL, 5 )


		bSizer56.Add( bSizer50, 0, wx.EXPAND, 5 )

		bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Update at:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer51.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.m_timePicker1 = wx.adv.TimePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.TP_DEFAULT )
		bSizer51.Add( self.m_timePicker1, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"(24h format)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer51.Add( self.m_staticText20, 0, wx.ALL, 5 )


		bSizer56.Add( bSizer51, 0, wx.EXPAND, 5 )


		bSizer56.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer521 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer521.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button201 = wx.Button( self, wx.ID_ANY, u"Schedule Autoupdate EDT", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer521.Add( self.m_button201, 1, wx.EXPAND, 5 )


		bSizer521.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer56.Add( bSizer521, 0, wx.EXPAND, 5 )


		bSizer56.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer52.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Schedule Autoupdate WB", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer52.Add( self.m_button20, 1, wx.EXPAND, 5 )


		bSizer52.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer56.Add( bSizer52, 0, wx.EXPAND, 5 )


		bSizer56.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer56.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer56.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer56, 1, wx.EXPAND, 5 )

		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer57 = wx.BoxSizer( wx.VERTICAL )

		bSizer262 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer262.SetMinSize( wx.Size(100,50) )

		bSizer262.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1222 = wx.StaticText( self, wx.ID_ANY, u"Manual Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1222.Wrap( -1 )

		self.m_staticText1222.SetFont( wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString) )

		bSizer262.Add( self.m_staticText1222, 0, wx.ALL, 5 )


		bSizer262.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer57.Add( bSizer262, 0, wx.EXPAND, 5 )

		self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer57.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.install_edt_but = wx.Button( self, wx.ID_ANY, u"Install Electronics Desktop", wx.DefaultPosition, wx.Size(-1,-1), 0 )
		bSizer30.Add( self.install_edt_but, 0, 0, 5 )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer27.Add( bSizer30, 3, wx.EXPAND, 5 )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer57.Add( bSizer27, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		bSizer301 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer301.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.install_wb_but = wx.Button( self, wx.ID_ANY, u"Install Workbench (latest)", wx.DefaultPosition, wx.Size(-1,-1), 0 )
		bSizer301.Add( self.install_wb_but, 0, 0, 5 )


		bSizer301.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer57.Add( bSizer301, 1, wx.EXPAND, 5 )


		bSizer57.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer57.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer57, 1, wx.EXPAND, 5 )

		bSizer62 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer62.Add( ( 0, 0), 5, wx.EXPAND, 5 )

		self.m_button25 = wx.Button( self, wx.ID_ANY, u"Save settings as Default", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer62.Add( self.m_button25, 4, wx.ALL, 5 )


		bSizer62.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer62, 0, wx.ALIGN_BOTTOM|wx.BOTTOM, 5 )


		bSizer1.Add( bSizer3, 5, wx.EXPAND, 5 )


		self.SetSizer(bSizer1)
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

	def __del__(self):
		pass


