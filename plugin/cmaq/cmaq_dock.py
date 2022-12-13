# Gv3GEWRF 
# Copyright (c) Odycloud.

import subprocess
import datetime
from datetime import timedelta, date, datetime

from PyQt5.QtWidgets import QDockWidget, QTabWidget
from PyQt5.QtCore import pyqtSignal, QEvent
from PyQt5.QtGui import QMouseEvent

from qgis.gui import QgisInterface

#from Gv3GEWRF.plugin.ui.cmaq.tab_CMAQhome import CMAQHomeTab
#from Gv3GEWRF.plugin.ui.tab_download import DownloadTab
#from Gv3GEWRF.plugin.ui.tab_preprocessorIII import PreprocessorTab
from Gv3GEWRF.plugin.cmaq.tab_CMAQgenchar import CMAQCharTab
from Gv3GEWRF.plugin.cmaq.tab_CMAQhome import CMAQHomeTab
from Gv3GEWRF.plugin.cmaq.tab_CMAQrunI import CMAQRunTab
from Gv3GEWRF.plugin.cmaq.cmaq_widget_view import CMAQViewWidget
#from Gv3GEWRF.plugin.ui.tab_S3 import S3Tab
#from Gv3GEWRF.plugin.ui.widget_view import ViewWidget
from Gv3GEWRF.plugin.ui.helpers import WhiteScroll
from Gv3GEWRF.plugin.cmaq.cmaq_tempus import CTempus
from Gv3GEWRF.plugin.cmaq.cmaq_tempus import CCpu

class CmaqDock(QDockWidget):
    def __init__(self, iface: QgisInterface, dock_widget: QDockWidget) -> None:   
        super().__init__('Graphical Interface on Graviton3 for Numerical Predictions: CMAQ')
        
        self.nunc = CTempus()  
        str2016 = '7/1/16'
        self.nunc.satus_dies = datetime.strptime(str2016, '%m/%d/%y')
        str22016 = '7/2/16'
        self.nunc.finis_dies = datetime.strptime(str22016, '%m/%d/%y')
        self.cmaq_coros = CCpu()
#_____ TABS SET UP _____#
        tabs = QTabWidget()
        tabs.setStyleSheet('''QTabBar::tab {font-size: 10pt; font-family: Verdana; font-weight: bold; color: #004F00; height: 40px; width: 140px;}''')
        tabs.addTab(WhiteScroll(CMAQHomeTab()), 'CMAQ')
# General Characteristics Tab
        self.genchar_tab = CMAQCharTab(iface, self.nunc, self.cmaq_coros)
        tabs.addTab(self.genchar_tab, "CMAQ\nVARIABLES")
# Download
#        self.download_tab = DownloadTab(iface, diebus, self.project)
#        tabs.addTab(self.download_tab, "DOWNLOAD\nMET DATA")
# Preprocessor
#        self.preprocessor_tab = PreprocessorTab(iface, diebus, self.project)
#        self.preprocessor_tab = PreprocessorTab(iface)
#        tabs.addTab(self.preprocessor_tab, "PREPROCESSOR")
# CMAQ
        self.CMAQ_tab = CMAQRunTab(iface, self.nunc, self.cmaq_coros)
        tabs.addTab(self.CMAQ_tab, "CMAQ\nSIMULATIONS")
# S3
#        self.S3_tab = S3Tab(iface, diebus)
#        tabs.addTab(self.S3_tab, "S3 INTERFACE")
        self.setWidget(tabs)
        self.tabs = tabs
#        self.currentChanged.connect(self.on_tab_changed)  
        
#        self.simulation_tab.view_wrf_nc_file.connect(self.view_wrf_nc_file)   # Not sure what this line does

    def open_view_tab(self):
        self.tabs.setCurrentIndex(3)

#    def view_wrf_nc_file(self, path: str) -> None:
#        self.view_tab.add_dataset(path)
#        self.open_view_tab()

#    def on_tab_changed(self, index: int) -> None:
#        print ("It is at tab changed")
#        self.tabs[index].tab_active.emit()
#        self.GenCharTab.refresh()
