# Gv3GECMAQ 
# Copyright (c) Odycloud.

from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap, QFont

from Gv3GEWRF.core import Project

######from Gv3GEWRF.plugin.constants import Gv3GEWRF_LOGO_PATH

class CMAQHomeTab(QWidget):
    """Class for creating the Home tab"""
    def __init__(self) -> None:
        super().__init__()
        
#___ Automatic creation of the project ___#
#        self.project = Project.create()
#        self.on_create_project('/home/ubuntu/WRF-4.4/project')
#___ Set-up of the HOME tab ___#
#        vbox = QVBoxLayout()
        layout = QGridLayout()
        title = """
                    <html>
                        <h2>CMAQ Simulations</h2>
                    </html>
                """
        text = """
                    <html>
                        <p>This beta version for CMAQ allows you to perform the U.S. Southeast benchmark and 
                        visualize the results. Further functionality will be added in coming weeks.\n
                        The GUI will adjust the number of MPI ranks based on the number of Graviton3
                        cores.</p>
                  </html>
               """

#        text2 = """
#                    <html>
#                        <p> Once the simulations have completed, it is feasible to visualize the results or store the output files in a
#                        S3 bucket (you will need your credentials for this task). \n \n
#                        </p>
#                  </html>
#               """

#        text3 = """
#                    <html>
#                        <p> <i style='color:DimGray'> NOTE: This is a beta version for Graphical Interface on Graviton3 for Numerical Predictions 
#                        with limited capabilities. It can perform WRF simulations of any size (limited only by the memory of the instance) but MPAS,
#                        CMAQ, WRF-CMAQ and CAMx are disabled. You can use any type of meteorological data but download is limited to GFS data. 
#                        </i> </p>
#                  </html>
#               """

        label_title = QLabel(title)
        label_text = QLabel(text)
#        label_text2 = QLabel(text2)
#        label_text3 = QLabel(text3)
        label_text.setWordWrap(True)
        label_text.setOpenExternalLinks(True)
        label_text.setFont(QFont('Verdana', 12))
#        label_text2.setWordWrap(True)
#        label_text2.setOpenExternalLinks(True)
#        label_text2.setFont(QFont('Verdana', 12))
#        label_text3.setWordWrap(True)
#        label_text3.setOpenExternalLinks(True)
#        label_text3.setFont(QFont('Verdana', 10))

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
#        layout.addWidget(label_text2,2,0)
#        layout.addWidget(label_text3,3,0)
        self.setLayout(layout)
        self.layout().setAlignment(Qt.AlignTop)
        
