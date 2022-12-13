# Gv3GEWRF Plugin
# Copyright (c) 2022 Odycloud.

from PyQt5.QtWidgets import QTabWidget

from Gv3GEWRF.plugin.ui.helpers import WhiteScroll
#from Gv3GEWRF.plugin.ui.widget_general import GeneralWidget
from Gv3GEWRF.plugin.ui.met_download.widget_metinstructions import MetInstructions
from Gv3GEWRF.plugin.ui.met_download.widget_gfs import GFSToolsDownloadManager
#from Gv3GEWRF.plugin.ui.met_download.widget_rda import RdaToolsDownloadManager
from Gv3GEWRF.plugin.ui.widget_process import Process

import datetime
from datetime import timedelta, date
from Gv3GEWRF.core.project import Project

class DownloadTab(QTabWidget):
    def __init__(self, iface, ancilla, project) -> None:
        super().__init__()
        self.ancilla = ancilla
        self.project = project

        self.general_tab = MetInstructions()
#        down_met = WhiteScroll(self.general_tab)
        gfs = WhiteScroll(GFSToolsDownloadManager(iface, self.ancilla, self.project))
#        nam = WhiteScroll(self.domain_tab)
#        rda = WhiteScroll(RdaToolsDownloadManager(iface))

#        self.addTab(down_met, 'How to down-\nload met data')
        self.addTab(gfs, 'Download')
#        self.addTab(nam, 'NAM')
#        self.addTab(rda, 'RDA')
#        self.currentChanged.connect(self.on_tab_changed)       

    def on_tab_changed(self, index: int) -> None:
        pass
#        self.GenCharTab.refresh()
