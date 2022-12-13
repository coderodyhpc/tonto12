# Gv3GEWRF 
# Copyright (c) Odycloud.

from typing import Tuple, Callable
import os
import platform
import multiprocessing
import subprocess
import webbrowser

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import ( 
    QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QGroupBox,
    QCheckBox, QPushButton, QSpinBox, QMessageBox, QSizePolicy
)

from qgis.gui import QgsOptionsWidgetFactory, QgsOptionsPageWidget

#from Gv3GEWRF.core import get_wps_dist_url, get_wrf_dist_url, download_and_extract_dist, WRF_WPS_DIST_VERSION, find_mpiexec
from Gv3GEWRF.core import find_mpiexec
from Gv3GEWRF.core.util import export
from Gv3GEWRF.plugin.options import get_options
from Gv3GEWRF.plugin.constants import PLUGIN_NAME, Gv3GEWRF_LOGO_PATH
from Gv3GEWRF.plugin.ui.helpers import WaitDialog, create_file_input, reraise
from Gv3GEWRF.plugin.ui.thread import TaskThread

@export
class OptionsFactory(QgsOptionsWidgetFactory):
    def __init__(self):
        super().__init__()
        self.setTitle(PLUGIN_NAME)

    def icon(self):
        print ( "Icon" )
        print (Gv3GEWRF_LOGO_PATH)
        return QIcon(Gv3GEWRF_LOGO_PATH)

    def createWidget(self, parent):
        return ConfigOptionsPage(parent)

class ConfigOptionsPage(QgsOptionsPageWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.options = get_options()

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.working_dir, layout = create_file_input(
            is_folder=True, input_label='Working directory',
            value=self.options.working_dir, start_folder=self.options.working_dir)
        self.vbox.addLayout(layout)

#        self.mpi_enabled, self.mpi_processes, self.wps_dir, self.wrf_dir, gbox = \
#            self.create_distribution_box()
#        self.vbox.addWidget(gbox)

        self.rda_username, self.rda_password, gbox = self.create_rda_auth_input()
        self.vbox.addWidget(gbox)

        self.vbox.addStretch()

    def apply(self) -> None:
        ''' Called when the options dialog is accepted. '''
        self.options.working_dir = self.working_dir.text()
        self.options.rda_username = self.rda_username.text()
        self.options.rda_password = self.rda_password.text()
        self.options.save()


    def create_rda_auth_input(self) -> Tuple[QLineEdit, QLineEdit, QGroupBox]:
        username = QLineEdit(self.options.rda_username)
        password = QLineEdit(self.options.rda_password)
        password.setEchoMode(QLineEdit.Password)

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel('Username: '))
        hbox.addWidget(username)
        hbox.addWidget(QLabel('Password: '))
        hbox.addWidget(password)

        gbox = QGroupBox("NCAR's Research Data Archive (RDA)")
        text = """<html>Downloading meteorological data is usually much faster using 
                the app found in the Download tab. However, you still have the option 
                to download data from 
                <a href="https://rda.ucar.edu/">NCAR's Reseach Data Archive (RDA)</a>
                through the use of its API. If you do not have an RDA account, you need to
                <a href="https://rda.ucar.edu/index.html?hash=data_user&amp;action=register">register for a Data Account</a> first.
                Once you have completed your registration and your account is live you can save your log-in information to download meteorological
                data from GIS4WRF > Datasets > Met.</html>"""
        label = QLabel(text)
        label.setWordWrap(True)
        label.setOpenExternalLinks(True)
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addLayout(hbox)
        gbox.setLayout(vbox)

        return username, password, gbox
