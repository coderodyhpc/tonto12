# Gv3GEWRF 
# Copyright (c) Odycloud.

from PyQt5.QtWidgets import QDockWidget, QTabWidget

from qgis.gui import QgisInterface

from Gv3GEWRF.plugin.ui.tab_home import HomeTab
#from Gv3GEWRF.plugin.ui.tab_management import ManagementTab
#from Gv3GEWRF.plugin.ui.tab_download import DownloadTab
#from Gv3GEWRF.plugin.ui.tab_datasets import DatasetsTab
#from Gv3GEWRF.plugin.ui.tab_preprocessor import PreprocessorTab
#from Gv3GEWRF.plugin.ui.tab_simulation import SimulationTab
#from Gv3GEWRF.plugin.ui.tab_WRF import WRFTab
from Gv3GEWRF.plugin.ui.wrf_run.widget_view import ViewWidget
from Gv3GEWRF.plugin.ui.helpers import WhiteScroll

class MpasDock(QDockWidget):
    """Set up the MPAS dock"""
    def __init__(self, iface: QgisInterface, dock_widget: QDockWidget) -> None:
        super().__init__('MPAS')
 
        print ("It is at MPAS Dock")
        tabs = QTabWidget()
        tabs.addTab(WhiteScroll(HomeTab()), 'MPAS')
# Management
#        self.management_tab = ManagementTab(iface)
#        tabs.addTab(self.management_tab, "Project management")
# Download
#        self.download_tab = DownloadTab(iface)
#        tabs.addTab(DatasetsTab(iface), "Download")
# Datasets
#        tabs.addTab(DatasetsTab(iface), "Datasets")
# Preprocessor
#        self.preprocessor_tab = PreprocessorTab(iface)
#        tabs.addTab(self.preprocessor_tab, "Preprocessor")
# Simulation
#        self.simulation_tab = SimulationTab(iface)
#        tabs.addTab(self.simulation_tab, "Simulation")
# WRF
#        self.WRF_tab = WRFTab(iface)
#        tabs.addTab(self.WRF_tab, "WRF")
# View
#        self.view_tab = ViewWidget(iface, dock_widget)
#        tabs.addTab(self.view_tab, "View")
#        self.setWidget(tabs)
#        self.tabs = tabs

###        self.simulation_tab.view_wrf_nc_file.connect(self.view_wrf_nc_file)

    def open_view_tab(self):
        self.tabs.setCurrentIndex(3)

#    def view_wrf_nc_file(self, path: str) -> None:
#        self.view_tab.add_dataset(path)
#        self.open_view_tab()
