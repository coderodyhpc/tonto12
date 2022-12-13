# Gv3GEWRF 
# Copyright (c) Odycloud.

from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtCore import pyqtSignal

from qgis.gui import QgisInterface

#from Gv3GEWRF.core import Project

#from Gv3GEWRF.plugin.constants import PLUGIN_NAME
#from Gv3GEWRF.plugin.options import get_options
#from Gv3GEWRF.plugin.broadcast import Broadcast
from Gv3GEWRF.plugin.ui.helpers import WhiteScroll, ensure_folder_empty
#from Gv3GEWRF.plugin.ui.widget_domains import DomainWidget
#from Gv3GEWRF.plugin.ui.widget_datasets import DatasetsWidget
#from Gv3GEWRF.plugin.ui.wrf_run.widget_wrfdescription import WRFDescriptionWidget
from Gv3GEWRF.plugin.cmaq.cmaq_run.widget_CMAQrun import CMAQRunWidget
from Gv3GEWRF.plugin.cmaq.cmaq_widget_view import CMAQViewWidget

class CMAQRunTab(QTabWidget):
    view_cmaq_nc_file = pyqtSignal(str)

    def __init__(self, iface: QgisInterface, ancilla, servus) -> None:
        super().__init__()
        
        self.ancilla = ancilla
        self.servus =servus
        self.iface = iface
#        self.project = project

#        self.options = get_options()

# CMAQ description
#        self.CMAQDescription_tab = CMAQDescriptionWidget()
# Run widget
        self.run_tab = CMAQRunWidget(iface, self.ancilla, self.servus)
# Visualization widget
#        self.cmaq_visual_tab = CMAQViewWidget(iface, dock_widget)
        self.cmaq_visual_tab = CMAQViewWidget(iface, ancilla)
# 
#        self.run_tab.view_cmaq_nc_file.connect(self.view_wrf_nc_file)

#        self.addTab(WhiteScroll(self.CMAQDescription_tab), 'Description')
        self.addTab(WhiteScroll(self.run_tab), 'Run CMAQ')
        self.addTab(WhiteScroll(self.cmaq_visual_tab), 'CMAQ\nVisualization')

        self.tabs = [self.run_tab, self.cmaq_visual_tab]

#$#        self.disable_project_dependent_tabs()

        
        self.currentChanged.connect(self.on_tab_changed)
#$#        Broadcast.options_updated.connect(self.update_project)
#$#        Broadcast.open_project_from_object.connect(self.open_project_from_object)

    def open_data_tab(self):
        self.setCurrentIndex(2)

    def open_run_tab(self):
        self.setCurrentIndex(3)

    def on_tab_changed(self, index: int) -> None:
        self.tabs[index].tab_active.emit()

#$#    def enable_project_dependent_tabs(self) -> None:
#$#        pass
#$##        self.datasets_tab.setEnabled(True)
#$##        self.run_tab.setEnabled(True)

#$#    def disable_project_dependent_tabs(self) -> None:
#$#        pass
#$##        self.datasets_tab.setEnabled(False)
#$##        self.run_tab.setEnabled(False)
