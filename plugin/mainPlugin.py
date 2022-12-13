# Gv3GECMAQ Plugin
# Copyright (c) 2022 Odycloud.

from typing import List, Callable
import webbrowser
import time
import logging

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QWidget

from qgis.core import QgsMessageLog, Qgis
from qgis.gui import QgisInterface

from Gv3GEWRF.core import (logger)

# Initialize Qt resources from auto-generated file resources.py
###import Gv3GEWRF.plugin.resources
from Gv3GEWRF.plugin.ui.thread import TaskThread
from Gv3GEWRF.plugin.ui.helpers import install_user_error_handler

#__ Loading of the docks for the different apps ___#
from Gv3GEWRF.plugin.ui.options import OptionsFactory   #!!!!#  THIS IS GOING TO BE CRITICAL & I NEED TO CHECK IT
from Gv3GEWRF.plugin.ui.wrfIII import WrfDock
from Gv3GEWRF.plugin.mpas.mpas_dock import MpasDock
from Gv3GEWRF.plugin.cmaq.cmaq_dock import CmaqDock
from Gv3GEWRF.plugin.ui.dialog_about import AboutDialog

from Gv3GEWRF.plugin.options import get_options
from Gv3GEWRF.plugin.geo import add_default_basemap, load_wps_binary_layer
###from Gv3GEWRF.plugin.constants import (
###    PLUGIN_NAME, GIS4WRF_LOGO_PATH, ADD_WRF_NETCDF_LAYER_ICON_PATH, 
###    ADD_BINARY_LAYER_ICON_PATH, ABOUT_ICON_PATH, BUG_ICON_PATH)
from Gv3GEWRF.plugin.constants import (PLUGIN_NAME) #!!!!#  I ELIMINATED A BUNCH OF VARIABLES

from Gv3GEWRF.plugin.tempus import Tempus
from Gv3GEWRF.core.project import Project


#__ Initialization of the graphic environment ___#
class QGISPlugin():
    def __init__(self, iface: QgisInterface) -> None:
        self.iface = iface
        self.actions = []  # type: List[QAction]
        self.dock_widget = None # type: WrfDock
        self.dies = Tempus() # I'm defining it with 'self' because w/o it, WrfDock was complaining 
        
    def initGui(self) -> None:
        """Create the menu entries and toolbar icons inside the QGIS GUI.
           Note: This method is called by QGIS.
        """
        self.init_logging() #This is probably to track what happens while running the plugin A.F. 

#        install_user_error_handler(self.iface) #This is at plugin/ui/helpers.py
#___ These are the actions defining the different options at the Gv3GEWRF menu 
#___ (maybe I should get rid of it and simply start the app w/o asking any Qs) 
        self.menu = '&' + PLUGIN_NAME
        self.add_action(icon_path='/home/ubuntu/.local/share/QGIS/QGIS3/profiles/default/python/plugins/Gv3GEWRF/plugin/resources/WRF_logo16B.png',
                        text="WRF", callback=self.show_dock, add_to_toolbar=True,
                        parent=self.iface.mainWindow(), status_tip='Run WRF')
        self.add_action(icon_path='/home/ubuntu/.local/share/QGIS/QGIS3/profiles/default/python/plugins/Gv3GEWRF/plugin/resources/CMAQ_logo16B.png',
                        text="CMAQ", callback=self.show_cmaq, add_to_toolbar=True,
                        parent=self.iface.mainWindow(), status_tip='Run CMAQ')
#        self.add_action(icon_path='/home/ubuntu/.local/share/QGIS/QGIS3/profiles/default/python/plugins/Gv3GEWRF/plugin/resources/MPAS_logo16.png',
#                        text="MPAS", callback=self.show_mpas, add_to_toolbar=True,
#                        parent=self.iface.mainWindow(), status_tip='Run MPAS')
#        self.add_action(icon_path='/home/ubuntu/.local/share/QGIS/QGIS3/profiles/default/python/plugins/Gv3GEWRF/plugin/resources/icon512.png',
#                        text='Add WRF NetCDF Layer...', add_to_add_layer=True, add_to_menu=False,
#                        parent=self.iface.mainWindow(), callback=self.add_wrf_layer)
#        self.add_action(icon_path='/home/ubuntu/.local/share/QGIS/QGIS3/profiles/default/python/plugins/Gv3GEWRF/plugin/resources/QGIS_logo64.png',
#                        text='Report a bug', callback=self.report_bug,
#                        parent=self.iface.mainWindow(), status_tip='Report a bug')
#!#!# These last 2 will add components at the layer menu, not at the Gv3GEWRF menu 
#        self.add_action(icon_path='/home/ubuntu/.local/share/QGIS/QGIS3/profiles/default/python/plugins/Gv3GEWRF/plugin/resources/icon512.png',
#                        text='Add WPS Binary Layer...', add_to_add_layer=True, add_to_menu=False,
#                        parent=self.iface.mainWindow(), callback=self.add_wps_binary_layer)

#__ I believe that this might be to set up the Settings/options ___#
        self.options_factory = OptionsFactory() # This is at gis4wrf/plugin/ui/options.py
        self.iface.registerOptionsWidgetFactory(self.options_factory)
        self.options = get_options()

#        self.check_versions() #I'm deactivating check_versions - probably needs to be erased

    def unload(self) -> None:
        """Removes the plugin menu item and icon from QGIS GUI.
           Note: This method is called by QGIS.
        """
###        for action in self.actions:
###            self.iface.removePluginMenu('&' + PLUGIN_NAME, action)
###            self.iface.removeToolBarIcon(action)
###            self.iface.removeAddLayerAction(action)
###        if self.dock_widget:
###            self.iface.removeDockWidget(self.dock_widget)
###        self.iface.unregisterOptionsWidgetFactory(self.options_factory)

        self.destroy_logging()

#__ Functions  ___#
    def show_dock(self) -> None:
        if not self.dock_widget:
            self.dock_widget = WrfDock(self.iface, self.dock_widget, self.dies)
#            self.dock_widget = WrfDockII(self.iface)
#! What happens if I change Right with Left
        self.iface.addDockWidget(
            Qt.RightDockWidgetArea, self.dock_widget)
        add_default_basemap()
        self.dock_widget.hasFocus.connect(self.on_dock_focus)
#        self.iface.addWidget(
#            self.dock_widget)

    def show_mpas(self) -> None:
        if not self.dock_widget:
            self.dock_widget = MpasDock(self.iface, self.dock_widget)
        self.iface.addDockWidget(
            Qt.RightDockWidgetArea, self.dock_widget)
        add_default_basemap()

    def show_cmaq(self) -> None:
        if not self.dock_widget:
            self.dock_widget = CmaqDock(self.iface, self.dock_widget)
        self.iface.addDockWidget(
            Qt.RightDockWidgetArea, self.dock_widget)
        add_default_basemap()

        
        ###    def show_about(self) -> None:
###        AboutDialog().exec_()

###    def add_wrf_layer(self) -> None:
###        path, _ = QFileDialog.getOpenFileName(caption='Open WRF NetCDF File')
###        if not path:
###            return
###        if not self.dock_widget:
###            self.show_dock()
###        self.dock_widget.view_tab.add_dataset(path)
###        self.dock_widget.open_view_tab()

###    def add_wps_binary_layer(self) -> None:
###        folder = QFileDialog.getExistingDirectory(caption='Select WPS Binary Dataset Folder')
###        if not folder:
###            return
###        load_wps_binary_layer(folder)

    def report_bug(self) -> None:
        print ('Report any issue to support@odyhpc.com')

    def on_dock_focus(self):
        self.project = Project.create()
        project = self.project
#        self.servus = servus() 
#        print ('START DATE ',self.servus,self.servus.satus_dies)
        print ("At MAINPLUGIN ",project,project.data)
#        diebus2 = Manipulator.handle_diebus.diebus
        print ("SATUS_DIES ",self.dies,self.dies.satus_dies)
        print ("HoraI ",self.dies.satus_hora)
        print ("FINIS_DIES ",self.dies.finis_dies)
        print ("HoraII ",self.dies.finis_hora)

    def init_logging(self) -> None:

        levels = {
            # https://github.com/qgis/QGIS/issues/42996
            logging.NOTSET: Qgis.NoLevel if hasattr(Qgis, 'NoLevel') else Qgis.Info,
            
            logging.DEBUG: Qgis.Info,
            logging.INFO: Qgis.Info,
            logging.WARN: Qgis.Warning,
            logging.ERROR: Qgis.Critical,
            logging.CRITICAL: Qgis.Critical,
        }
        class QgsLogHandler(logging.Handler):
            def emit(self, record: logging.LogRecord) -> None:
                log_entry = self.format(record)
                level = levels[record.levelno]                
                QgsMessageLog.logMessage(log_entry, PLUGIN_NAME, level, False)
        
        self.log_handler = QgsLogHandler()
        logger.addHandler(self.log_handler)

    def destroy_logging(self) -> None:
        logger.removeHandler(self.log_handler)

    def add_action(self, icon_path: str, text: str, callback: Callable,
                   enabled_flag: bool=True, add_to_menu: bool=True,
                   add_to_toolbar: bool=False, add_to_add_layer: bool=False,
                   status_tip: str=None, whats_this: str=None, parent: QWidget=None
                   ) -> QAction:
        """Helper function for creating menu items
        Parameters
        ----------
        icon_path: Path to the icon for this action. Can be a resource
            path (e.g. `:/plugins/foo/bar.png`) or a normal file system path.
        text: Text that should be shown in menu items for this action.
        callback: Function to be called when the action is triggered.
        enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        add_to_toolbar: Flag indicating whether the action should also
            be added to the Plugins toolbar. Defaults to False.
        add_to_layer: Flag indicating whether the action should also
            be added to the Layer > Add Layer menu. Defaults to False.
        status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action after clicking on `?`.
        parent: Parent widget for the new action. Defaults None.
        Returns
        -------
        out: The action that was created. Note that the action is
            also added to `self.actions` list.
        """
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        if add_to_add_layer:
            self.iface.insertAddLayerAction(action)

        self.actions.append(action)

        return action
