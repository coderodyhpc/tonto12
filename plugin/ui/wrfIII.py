# Gv3GEWRF 
# Copyright (c) Odycloud.

import subprocess

from PyQt5.QtWidgets import QDockWidget, QTabWidget
from PyQt5.QtCore import pyqtSignal, QEvent
from PyQt5.QtGui import QMouseEvent

from qgis.gui import QgisInterface

from Gv3GEWRF.plugin.ui.tab_home import HomeTab
from Gv3GEWRF.plugin.ui.tab_download import DownloadTab
from Gv3GEWRF.plugin.ui.tab_preprocessorIII import PreprocessorTab
#from Gv3GEWRF.plugin.ui.tab_gencharIV import GenCharTab
#from Gv3GEWRF.plugin.ui.tab_physics import PhysicsTab
from Gv3GEWRF.plugin.ui.tab_propertiesIV import PropertiesTab
from Gv3GEWRF.plugin.ui.tab_WRFIII import WRFTab
from Gv3GEWRF.plugin.ui.tab_S3 import S3Tab
#from Gv3GEWRF.plugin.ui.wrf_run.widget_view import ViewWidget
from Gv3GEWRF.plugin.ui.helpers import WhiteScroll
from Gv3GEWRF.plugin.tempus import Tempus
#from Gv3GEWRF.plugin.tempus import Cpu
from Gv3GEWRF.core import Project

class OdyWidget(QDockWidget):

    hasFocus = pyqtSignal([QDockWidget])

    def __init__(self, text, parent=None):
        super().__init__(text, parent=parent)
        self.setObjectName(text)

    def event(self, event):
        if event.type() == QEvent.MouseButtonPress and event.button() == 1:
            self.hasFocus.emit(self)
        return super().event(event)

class WrfDock(OdyWidget):
#class WrfDock(QDockWidget):
    def __init__(self, iface: QgisInterface, dock_widget: QDockWidget, diebus) -> None: #@# I'm getting diebus  
        super().__init__('Graphical User Interface for Numerical Predictions on Graviton3: WRF')

        self.project = Project.create()
        print ('WRF-III ',self.project,diebus,diebus.satus_dies,diebus.satus_hora,diebus.finis_dies,diebus.finis_hora)
#_____ TABS SET UP _____#
        tabs = QTabWidget()
        tabs.setStyleSheet('''QTabBar::tab {font-size: 10pt; font-family: Verdana; font-weight: bold; color: #00004F; height: 40px; width: 140px;}''')
        tabs.addTab(WhiteScroll(HomeTab()), 'HOME')
# Properties Tab
        self.properties_tab = PropertiesTab(iface, diebus, self.project)
        tabs.addTab(self.properties_tab, "SIMULATION\nPROPERTIES")
# General Characteristics Tab
#        self.genchar_tab = GenCharTab(iface, diebus, self.project)
#        tabs.addTab(self.genchar_tab, "GENERAL\nVARIABLES")
# Physics & Dynamics Tab
#        self.physdyn_tab = PhysicsTab(iface, diebus, self.project)
#        tabs.addTab(self.physdyn_tab, "PHYSICS/ \n DYNAMICS")
# Download
        self.download_tab = DownloadTab(iface, diebus, self.project)
        tabs.addTab(self.download_tab, "DOWNLOAD\nMET DATA")
# Preprocessor
        self.preprocessor_tab = PreprocessorTab(iface, diebus, self.project)
#        self.preprocessor_tab = PreprocessorTab(iface)
        tabs.addTab(self.preprocessor_tab, "PREPROCESSOR")
# WRF
        self.WRF_tab = WRFTab(iface, diebus, self.project)
        tabs.addTab(self.WRF_tab, "WRF\nSIMULATIONS")
# S3
        self.S3_tab = S3Tab(iface, diebus)
#        self.S3_tab.setTabDisabled(True)
        tabs.addTab(self.S3_tab, "S3 INTERFACE")
        self.setWidget(tabs)
        self.tabs = tabs
#        self.currentChanged.connect(self.on_tab_changed)  
        
#        self.simulation_tab.view_wrf_nc_file.connect(self.view_wrf_nc_file)   # Not sure what this line does

    def open_view_tab(self):
        self.tabs.setCurrentIndex(3)

    def view_wrf_nc_file(self, path: str) -> None:
        self.view_tab.add_dataset(path)
        self.open_view_tab()

#    def on_tab_changed(self, index: int) -> None:
#        print ("It is at tab changed")
#        self.tabs[index].tab_active.emit()
#        self.GenCharTab.refresh()
