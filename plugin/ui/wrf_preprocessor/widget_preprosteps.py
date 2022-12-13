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
from PyQt5.QtGui import QPixmap, QFont

from Gv3GEWRF.core import Project
from Gv3GEWRF.plugin.options import get_options
###from Gv3GEWRF.plugin.constants import Gv3GEWRF_LOGO_PATH

class PreproStepsWidget(QWidget):
    create_project = pyqtSignal(str)
    open_project = pyqtSignal(str)
    close_project = pyqtSignal()
    tab_active = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()

        self.options = get_options()

#        btn_new = QPushButton("Create Project",
#            clicked=self.on_create_project_button_clicked)

#        btn_existing = QPushButton("Open Project",
#            clicked=self.on_open_project_button_clicked)

        self.current_project_label = QLabel()

        vbox = QVBoxLayout()
        title = """
                    <html>
                        <h2>Preprocessing Tools</h2>
                    </html>
                """
        text = """
                    <html>
                        <p>Running WRF requires files detailing the initial and boundary conditions for the simulations.
                        These files must hold the data matching the parameters described in the <textarea style='color:#196F3D'>
                        namelist.input</textarea> file.
                        Before generating these files, it is necessary to create intermediate files describing the meteorological 
                        conditions during the forecast simulation. Most WRF model users generate these files using WPS 
                        The following steps create these files from scratch via WPS:
                        <ul>
                        <li>Generate the domain(s) and using the widget in the <textarea style='background-color:#bfc9ca; color:#00004F>
                        Preprocessor</textarea> tab. You can create the finest child domain by inputting geographical parameters (different 
                        projections are allowed) and any parent domain(s) by introducing the aspects ratios; the map will show the 
                        domain boundaries so that you can refine any of the domain(s) accordingly.   
                        Alternatively, it is feasible to import <textarea style='color:brown'>namelist.wps</textarea> from a previous   
                        simulation or created manually.Once the domains are defined, you can export the <b>namelist.wps</b> file to the WPS subdirectory.</li>
                        <li>Running <b>geogrid</b> generates the geographical file(s) in NetCDF form (e.g. 
                        <textarea style='color:#196F3D'>geo_em.d01.nc</textarea>). This step  only requires having the  
                        domain(s) defined and can be completed without downloading any meteorological data. </li>
                        <li>Running <b>ungrib</b> will generate the intermediate files necessary to generate the 
                        meteorological data. Here, and depending on your selection of data type, the 
                        <textarea style='color:#196F3D'> Vtable </textarea> file will also be generated.  </li>
                        <li>Running <b>metgrid</b> will generate the meteorological files needed by
                        <b>real</b> to generate the <textarea style='color:#196F3D'> met_em</textarea> files. </li>
                        </ul> 
                        If you already have either preprocessed meteorological files or boundary condition files, you can place them in the 
                        <textarea style='color:brown'> /home/ubuntu/WRF-4.4/test/em_real</textarea> subdirectory.
                  </html>
               """

        #                        <li>Create a project in the <b>Project</b> tab (this step is not necessary but it helps to track down the steps
#                        and/or reproduce the case) </li>

        label_title = QLabel(title)
        label_text = QLabel(text)
        label_text.setWordWrap(True)
        label_text.setOpenExternalLinks(True)
        label_text.setFont(QFont('Verdana', 12))
        vbox.addWidget(label_title)
        vbox.addWidget(label_text)
        vbox.addStretch()

        self.setLayout(vbox)

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
        
