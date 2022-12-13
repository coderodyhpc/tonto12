# Gv3GEWRF 
# Copyright (c) Odycloud.
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap, QFont

from Gv3GEWRF.core import Project

######from Gv3GEWRF.plugin.constants import Gv3GEWRF_LOGO_PATH

class HomeTab(QWidget):
    """Class for creating the Home tab"""
    def __init__(self) -> None:
        super().__init__()
        
#___ Automatic creation of the project ___#
        self.project = Project.create()
        self.on_create_project('/home/ubuntu/WRF-4.4/project')
#___ Set-up of the HOME tab ___#
#        vbox = QVBoxLayout()
        layout = QGridLayout()
        title = """
                    <html>
                        <h2>GUI for Numerical Predictions on <b>Graviton3</b></h2>
                    </html>
                """
        text = """
                    <html>
                        <p>The integrated graphical interface allows you to perform WRF simulations completing different 
                        steps based on which data you need to generate or which are already available. The 
                        <textarea style='background-color:#bfc9ca; color:#00004F'>SIMULATION PROPERTIES</textarea> allows model
                        users to input the most important parameters for the simulations. By default, the start and end days are set to one
                        week ago and today, respectively. The interface also reads the number of available cores and sets this value
                        to the default number of MPI ranks for the WRF simulation. After setting 
                        up these parameters, follow the different procedures based on your goals:</p>
                        <ul>
                            <li>Complete the full simulation process when no previous data are available. This process 
                            involves the download of the meteorological data, the creation of the domain(s), preprocessing the data 
                            for that domain(s) (i.e. running <b>geogrid</b>, <b>ungrib</b>, 
                            and <b>metgrid</b>, generation of the initial and boundary conditions 
                            files with <b>real </b>, and running <b> wrf </b> to perform the actual simulations. </li>
                            <li>If the <textarea style='color:#196F3D'> namelist.input </textarea> file and meteorological files are 
                            available in the <textarea style='color:brown'> /home/ubuntu/WRF-4.4/test/em_real</textarea> 
                            subdirectory, then you can directly click on the 
                            <textarea style='background-color:#bfc9ca; color:#00004F'>WRF</textarea> 
                            tab and run <b> real </b> and <b> wrf </b>.
                            </li>
                            <li>If the initial and boundary conditions files are located at the project subdirectory,
                             you can directly click on the <textarea style='background-color:#bfc9ca; color:#00004F'>WRF</textarea>  
                             tab, select the number of cores and run <b>wrf</b>. The simulation will start and you will  
                             be able to check the progress of the simulation with the visualization tool.
                            </li>
                        </ul> 
                  </html>
               """

        text2 = """
                    <html>
                        <p> Once the simulations have completed, it is feasible to visualize the results or store the output files in a
                        S3 bucket (you will need your credentials for this task). \n
                        </p>
                  </html>
               """

        text3 = """
                    <html>
                        <p> <i style='color:DimGray'> \n NOTE: This is a development version for GUI for Numerical Predictions on Graviton3  
                        with restricted capabilities. It can perform WRF simulations of any size (limited only by the memory of the instance) 
                        and it includes a beta version of CMAQ, which allows to perform the U.S. Southeast benmchmark. However, most CMAQ 
                        features along with MPAS, WRF-CMAQ and CAMx are disabled.  
                        </i> </p>
                  </html>
               """

        label_title = QLabel(title)
        label_text = QLabel(text)
        label_text2 = QLabel(text2)
        label_text3 = QLabel(text3)
        label_text.setWordWrap(True)
        label_text.setOpenExternalLinks(True)
        label_text.setFont(QFont('Verdana', 12))
        label_text2.setWordWrap(True)
        label_text2.setOpenExternalLinks(True)
        label_text2.setFont(QFont('Verdana', 12))
        label_text3.setWordWrap(True)
        label_text3.setOpenExternalLinks(True)
        label_text3.setFont(QFont('Verdana', 10))
#        label_pixmap = QLabel()
#        pixmap = QPixmap('/home/ubuntu/.local/share/QGIS/QGIS3/profiles/default/python/plugins/Gv3GEWRF/plugin/resources/QGIS_logo64.png')
#        label_pixmap.setPixmap(pixmap)
#        label_pixmap.setAlignment(Qt.AlignCenter)
#        vbox.addWidget(label_title)
###        vbox.addWidget(label_pixmap)
#        vbox.addWidget(label_text)
#        vbox.addWidget(label_text2)
#        vbox.addStretch()
#        self.setLayout(vbox)

        layout.addWidget(label_title,0,0)
        layout.addWidget(label_text,1,0)
        layout.addWidget(label_text2,2,0)
        layout.addWidget(label_text3,3,0)
        self.setLayout(layout)
        self.layout().setAlignment(Qt.AlignTop)
        
    def on_create_project(self, path: str) -> None:
#$#        if not ensure_folder_empty(path, self.iface):
#$#            return
#$#        if self.project.path is None:
#$#            # TODO notify user that Domain tab inputs are kept
#$#            self.project.path = path
#$#        else:
#$#            self.project = Project.create(path)
        self.project.path = '/home/ubuntu/WRF-4.4/project'
        self.project.save()
#$#        self.set_project_in_tabs()
#$#        self.enable_project_dependent_tabs()        
