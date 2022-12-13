# Gv3GEWRF 
# Copyright (c) Odycloud.

from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtCore import pyqtSignal

from qgis.gui import QgisInterface

from Gv3GEWRF.core import Project

from Gv3GEWRF.plugin.constants import PLUGIN_NAME
from Gv3GEWRF.plugin.options import get_options
from Gv3GEWRF.plugin.broadcast import Broadcast
from Gv3GEWRF.plugin.ui.helpers import WhiteScroll, ensure_folder_empty
#from Gv3GEWRF.plugin.ui.widget_domains import DomainWidget
#from Gv3GEWRF.plugin.ui.widget_datasets import DatasetsWidget
from Gv3GEWRF.plugin.ui.wrf_run.widget_wrfdescription import WRFDescriptionWidget
from Gv3GEWRF.plugin.ui.wrf_run.widget_WRFrun import RunWidget
from Gv3GEWRF.plugin.ui.wrf_run.widget_view import ViewWidget

class WRFTab(QTabWidget):
    view_wrf_nc_file = pyqtSignal(str)

    def __init__(self, iface: QgisInterface, ancilla, project) -> None:
        super().__init__()

        self.iface = iface
        self.project = project

        self.options = get_options()

# WRF description
        self.WRFDescription_tab = WRFDescriptionWidget()
# Run widget
        self.run_tab = RunWidget(iface, ancilla, self.project)
# Visualization widget
        self.visual_tab = ViewWidget(iface, ancilla)
# 
        self.run_tab.view_wrf_nc_file.connect(self.view_wrf_nc_file)

        self.addTab(WhiteScroll(self.WRFDescription_tab), 'Description')
        self.addTab(WhiteScroll(self.run_tab), 'Run WRF')
        self.addTab(WhiteScroll(self.visual_tab), 'Visualization')

#        self.tabs = [self.general_tab, self.domain_tab, self.datasets_tab, self.run_tab]
        self.tabs = [self.WRFDescription_tab, self.run_tab, self.visual_tab]

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
