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
from PyQt5.QtGui import QPixmap,QFont

#from PyQt5.QtCore import *
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui import *

from Gv3GEWRF.core import Project
from Gv3GEWRF.plugin.options import get_options
###from Gv3GEWRF.plugin.constants import Gv3GEWRF_LOGO_PATH

class WRFDescriptionWidget(QWidget):
    create_project = pyqtSignal(str)
    open_project = pyqtSignal(str)
    close_project = pyqtSignal()
    tab_active = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()

        self.options = get_options()

#        btn_new = QPushButton("Create Project",
#            clicked=self.on_create_project_button_clicked)
#        btn_new.setFont(QFont('Exo 2'))

#        btn_existing = QPushButton("Open Project",
#            clicked=self.on_open_project_button_clicked)

        self.current_project_label = QLabel()

#        vbox = QVBoxLayout()
        layout = QGridLayout()
        title = """
                    <html>
                        <h3>WRF Simulations</h3>
                    </html>
                """
        text = """
                    <html>
                        <br>
                        <p>These are the different options to run WRF.</p>
                        <ul>
                        <li><b>Full procedure<b></li>
                        If you are building the case from square one, you must complete all the preprocessing 
                        steps including selection of starting and end dates, download of the GFS data, generation 
                        of the <textarea style='color:#196F3D'> namelist.wps </textarea>, and run
                        all the preprocessing (WPS) tools.
                        These steps will also generate the meteorological files. Then, you must generate the 
                        <textarea style='color:#196F3D'> namelist.input </textarea> file. 
                        <textarea style='color:#FF0000'> (The system will generate an error if either 
                        <b>geogrid</b>, <b>ungrib</b> or <b>metgrid</b> were not previously completed succesfully). 
                        </textarea> Once the <textarea style='color:#196F3D'> namelist.input </textarea> file is 
                        available, you can proceed to complete the next steps. \n
                        <li><b>Generation of the initial/boundary conditions</b></li>
                        If the meteorological files are already available, you need to make sure 
                        that the right <textarea style='color:#196F3D'> namelist.input </textarea> is in the 
                        <textarea style='color:brown'> /home/ubuntu/WRF-4.4/test/em_real </textarea> 
                        subdirectory. This can be achieved either manually or exporting <i>namelist.wps</i>.
                        Then, you can run <b>real</b> to generate the initial and boundary condition files 
                        before running <b>wrf</b>. \n
                        <li><b>Complete the wrf simulations</b></li>
                        Once the boundary and initial condition files have been generated (or transferred)
                        to the <textarea style='color:brown'> /home/ubuntu/WRF-4.4/test/em_real </textarea> 
                        subdirectory, you can run <b>wrf</b> by simply clicking on the button.
                        </ul> 
                  </html>
               """

#                         <li><b>Build the input file from the preprocessor tab<b></li>
        label_title = QLabel(title)
        label_text = QLabel(text)
#        label_text2 = QLabel(text2)
        label_title.setFont(QFont('Verdana', 12))
        label_text.setFont(QFont('Verdana', 12))
        label_text.setWordWrap(True)
        label_text.setOpenExternalLinks(True)
#        label_text2.setWordWrap(True)
#        label_text2.setOpenExternalLinks(True)
        layout.addWidget(label_title,0,0)
#        vbox.addWidget(label_pixmap)
        layout.addWidget(label_text,1,0)
#        vbox.addWidget(label_text2)
#        vbox.addStretch()

#        vbox.addWidget(btn_new)
#        vbox.addWidget(btn_existing)
#        vbox.addWidget(self.current_project_label)
#        self.setLayout(vbox)
        self.setLayout(layout)
        self.layout().setAlignment(Qt.AlignTop)


    @property
    def project(self) -> Project:
        return self._project

    @project.setter
    def project(self, val: Project) -> None:
        ''' Sets the currently active project. See tab_simulation. '''
        self._project = val
        self.update_project_path_label()

    def on_create_project_button_clicked(self):
        folder = QFileDialog.getExistingDirectory(
            caption='Select new project folder', directory=self.options.projects_dir)
        if not folder:
            return
        self.create_project.emit(folder)

    def on_open_project_button_clicked(self):
        folder = QFileDialog.getExistingDirectory(
            caption='Select existing project folder', directory=self.options.projects_dir)
        if not folder:
            return
        self.open_project.emit(folder)

    def update_project_path_label(self) -> None:
        path = self.project.path
        if path is None:
            path = 'N/A'
        self.current_project_label.setText('Project path: ' + path)
        
