# Gv3GEWRF 
# Copyright (c) Odycloud.

from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QWidget, QTabWidget, QPushButton, QLayout, QVBoxLayout, QDialog, QGridLayout, QGroupBox, QSpinBox,
    QLabel, QHBoxLayout, QComboBox, QScrollArea, QFileDialog, QRadioButton, QLineEdit, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem
)
from PyQt5.QtGui import QFont

from Gv3GEWRF.core import Project
from Gv3GEWRF.plugin.options import get_options
###from Gv3GEWRF.plugin.constants import Gv3GEWRF_LOGO_PATH

class MetInstructions(QWidget):
#    create_project = pyqtSignal(str)
#    open_project = pyqtSignal(str)
#    close_project = pyqtSignal()
    tab_active = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()

        self.options = get_options()

        self.current_project_label = QLabel()

        vbox = QVBoxLayout()
        titulus = """
                    <html>
                        <h3>Downloading meteorological data</h3>
                    </html>
                """
        nuntius = """
                    <html>
                        <p>This tab allows you to easily download meteorological data for preprocessing with WPS.
                        <b'>geogrid</b> does not require meteorological data so you can proceed with it 
                        once your domain(s) is defined. However, running <b>ungrib</b> and
                        <b>metgrid</b> requires the meteorological data files to be downloaded and placed 
                        in the WPS subdirectory. WRF accepts meteorological data from different sources and with different 
                        resolutions. Among all the sources, the Global Forecast System (GFS) is the most common.   
                        In general, downloading meteorological data from different sources can take a significant amount 
                        of time and even longer if the request needs to wait in a line. However, using a specialized tool 
                        such that found in the GFS tab will accelerate data downloading substantially with rates up to more 
                        than 10 times faster than regular downloads. At the current time, available resolutions for GFS are
                        0.25 and 0.5 degrees. Keep in mind that these files are pretty large at the time of choosing
                        the SSD attached to your instance. For example, for a 0.5 degree resolution, the files for each time 
                        slot are about 20 GiB so each day needs roughly 80 GiB (or 100 GiB including the data at 00 hours
                        for the next day). For a 0.25 degree resolution, the files for each time 
                        slot are about 107 GiB. If you prefer to use your own meteorological files, you can transfer them to the 
                        <i style='color:brown'>/home/ubuntu/WRF-4.4/test/em_real</i> subdirectory.\n\n
                        </p>
                  </html>
               """

        nuntiusII = """
                    <html>
                        <i style='color:gray'>NOTE: This beta version only allows the direct download of GFS data. 
                        New sources will be added in upcoming versions.\n</i>
                        </p>
                  </html>
               """

#                        The following tabs allow you to download the following meteorological data:
#                        <ul>
#                        <li>GFS download: This will allow you to download GFS data in an accelerated fashion.  </li>
#                        <li>RDA  file </li>
#                        </ul> 

        nomen = QLabel(titulus)
        nomen.setFont(QFont('Verdana', 12))
        nuntium = QLabel(nuntius)
        nuntium.setWordWrap(True)
#        nuntium.setOpenExternalLinks(True)
        nuntium.setFont(QFont('Verdana', 12))
        nuntiumII = QLabel(nuntiusII)
        nuntiumII.setWordWrap(True)
#        nuntium.setOpenExternalLinks(True)
        nuntiumII.setFont(QFont('Verdana', 12))
        vbox.addWidget(nomen)
        vbox.addWidget(nuntium)
        vbox.addWidget(nuntiumII)
        vbox.addStretch()
        self.setLayout(vbox)

#    @property
#    def project(self) -> Project:
#        return self._project

#    @project.setter
#    def project(self, val: Project) -> None:
#        ''' Sets the currently active project. See tab_simulation. '''
#        self._project = val
#        self.update_project_path_label()

#    def on_create_project_button_clicked(self):
#        folder = QFileDialog.getExistingDirectory(
#            caption='Select new project folder', directory=self.options.projects_dir)
#        if not folder:
#            return
#        self.create_project.emit(folder)

#    def on_open_project_button_clicked(self):
#        folder = QFileDialog.getExistingDirectory(
#            caption='Select existing project folder', directory=self.options.projects_dir)
#        if not folder:
#            return
#        self.open_project.emit(folder)

#    def update_project_path_label(self) -> None:
#        path = self.project.path
#        if path is None:
#            path = 'N/A'
#        self.current_project_label.setText('Project path: ' + path)
