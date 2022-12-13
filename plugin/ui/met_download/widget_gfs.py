# Gv3GE Plugin
# Copyright (c) 2022 Odycloud.

import datetime, os
import subprocess
from PyQt5.QtCore import Qt, QDate, QTime, QDateTime
from PyQt5.QtGui import QDoubleValidator, QFont
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QGridLayout, QGroupBox, QLabel, QHBoxLayout, 
    QComboBox, QRadioButton, QTreeWidget, QTreeWidgetItem, QDateTimeEdit, QTreeWidgetItemIterator,
    QListWidget, QListWidgetItem, QProgressBar, QMessageBox, QDateEdit, QProgressBar
)
from datetime import timedelta
from Gv3GEWRF.core import (
    met_datasets, get_met_products, is_met_dataset_downloaded, get_met_dataset_path, download_met_dataset,
    CRS, UserError, logger)
from Gv3GEWRF.plugin.options import get_options
from Gv3GEWRF.plugin.geo import rect_to_bbox
from Gv3GEWRF.plugin.broadcast import Broadcast
from Gv3GEWRF.plugin.ui.helpers import add_grid_lineedit, MessageBar, reraise
from Gv3GEWRF.plugin.ui.thread import TaskThread
from Gv3GEWRF.plugin.ui.tab_propertiesIV import PropertiesTab
from Gv3GEWRF.plugin.tempus import Tempus

StyleSheet = '''
#QProgressBar {
    border: 2px solid #2196F3;
    border-radius: 5px;
    background-color: #E0E0E0;
}
#QProgressBar::chunk {
    background-color: #afcbe0;
    width: 10px; 
    margin: 0.5px;
}
'''

#####--------------------------------------------------------------------------------------------#####
class duo(QWidget):
    def __init__(self,parent, text,choice):
        super().__init__(parent)

        layoutC = QHBoxLayout()
        layoutC.addWidget(QLabel(text))
        options=QComboBox()
        options.addItems(choice)
        options.currentTextChanged.connect(self.text_changed)
        layoutC.addWidget(options)
        self.setLayout(layoutC)

    def text_changed(self):
        global choice1_is_selected,choice2_is_selected
        choice1_is_selected = True
        self.parent().download_toggling()

#####--------------------------------------------------------------------------------------------#####
class duocombo(QWidget):
    def __init__(self, parent, nuntium, spatium, gradi):           # nuntium and spatium are used to hold the Label and Combo content
        super().__init__(parent)
        self.gradi = gradi
        print ("self.gradi ",gradi,self.gradi)
        layout = QHBoxLayout()
        nuntis=QLabel(nuntium)                           # This seems to work both as an instance or a regular variable
        nuntis.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntis)
        nuntius=QComboBox()                               # nuntius points to the Combo
        nuntius.addItems(spatium)
        nuntius.setFont(QFont('Verdana', 14))
        nuntius.currentTextChanged.connect(self.on_text_changed)
        layout.addWidget(nuntius)
        self.setLayout(layout)

    def on_text_changed(self, s):
        global resolution_is_selected
        if s == "Not selected":
            resolution_is_selected = False
        elif s == "0.25 degrees":
            resolution_is_selected = True
            self.gradi = 0.25
            print ("self.gradi at text_changed ",self.gradi)
        elif s == "0.5 degrees":
            resolution_is_selected = True
            self.gradi = 0.5
            print ("self.gradi at text_changed ",gradi,self.gradi)
        else:
            resolution_is_selected = False
        
        self.parent().download_toggling()


#####--------------------------------------------------------------------------------------------#####
class DiebusOutput(QWidget):
    def __init__(self, dies1):
        super().__init__()
        layout = QGridLayout()

        nuntium=QLabel("Simulation start date")
        nuntium.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntium,0,0)

        self.dies1 = dies1
        print ("DIEBUS1 at tetra ",self.dies1)
        nuntiusI = self.dies1.satus_dies.strftime("%m/%d/%Y") 
        nuntiumI = QLabel(nuntiusI)
        nuntiumI.setFont(QFont('Verdana', 14))
        nuntiumI.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        nuntiumI.setAlignment(Qt.AlignCenter)
        layout.addWidget(nuntiumI,0,1)
        
        nuntiumII=QLabel("               Start hour")
        nuntiumII.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntiumII,0,2)

        if (self.dies1.satus_hora == 0):
            nuntiumIII=QLabel("00")
        elif (self.dies1.satus_hora == 6):
            nuntiumIII=QLabel("06")
        elif (self.dies1.satus_hora == 12):
            nuntiumIII=QLabel("12")
        elif (self.dies1.satus_hora == 18):
            nuntiumIII=QLabel("18")
        nuntiumIII.setFont(QFont('Verdana', 14))
        nuntiumIII.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        nuntiumIII.setAlignment(Qt.AlignCenter)
        layout.addWidget(nuntiumIII,0,3)
        
        nuntiumIV=QLabel("Simulation end date")
        nuntiumIV.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntiumIV,1,0)

        nuntiusV = self.dies1.finis_dies.strftime("%m/%d/%Y")
        nuntiumV = QLabel(nuntiusV)
        nuntiumV.setFont(QFont('Verdana', 14))
        nuntiumV.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        nuntiumV.setAlignment(Qt.AlignCenter)
        layout.addWidget(nuntiumV,1,1)

        nuntiumVI=QLabel("               End hour")
        nuntiumVI.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntiumVI,1,2)

        if (self.dies1.finis_hora == 0):
            nuntiumVII=QLabel("00")
        elif (self.dies1.finis_hora == 6):
            nuntiumVII=QLabel("06")
        elif (self.dies1.finis_hora == 12):
            nuntiumVII=QLabel("12")
        elif (self.dies1.finis_hora == 18):
            nuntiumVII=QLabel("18")
        nuntiumVII.setFont(QFont('Verdana', 14))
        nuntiumVII.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        nuntiumVII.setAlignment(Qt.AlignCenter)
        layout.addWidget(nuntiumVII,1,3)

        self.setLayout(layout)
        
#####--------------------------------------------------------------------------------------------#####
#####--------------------------------------------------------------------------------------------#####
#####--------------------------------------------------------------------------------------------#####
class GFSToolsDownloadManager(QWidget):
    def __init__(self, iface, servus, project) -> None:
        super().__init__()

        self.iface = iface
        self.options = get_options()
        self.msg_bar = MessageBar(iface)
        self.servus = servus
        self.project = project
        print ('It is at GFS Download ',self.servus,self.servus.satus_dies)
#        PropertiesTab.fun_diebus(self)

#___ These lines are to set up the layout ___#
        layout = QGridLayout()

#___ Block 0: Paragraph with some information ___#
#        text = """
#                    <html>
#                        <p><b>GFS download</b></p>
#                        <p>This tab allows you to download GFS data in an accelerated fashion. You need to select 
#                        the start and end times (in units of 6 hours).In addition to these times, it is necessary 
#                        to select the resolution from the two available ones of 0.25 and 0.5 degrees.   
#                        Then, data download will start automatically by clicking the Download buttom. 
#                        \n \n  
#                        </p>
#                    </html>
#               """

        titulus = """
                    <html>
                        <h3>Meteorological data download </h3>
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
                        <i style='color:DimGray'>NOTE: This version only allows the direct download of GFS data. 
                        New sources will be added in upcoming versions.\n</i>
                        </p>
                  </html>
               """    

        label_text = QLabel(titulus)
        label_text.setWordWrap(True)
#        label_text.setOpenExternalLinks(True)
        label_text.setFont(QFont('Verdana', 12))
        layout.addWidget(label_text,0,0)

        label_text2 = QLabel(nuntius)
        label_text2.setWordWrap(True)
#        label_text.setOpenExternalLinks(True)
        label_text2.setFont(QFont('Verdana', 12))
        layout.addWidget(label_text2,1,0)
  
#___ Block space ___#
        textN = "               "
        label_textN = QLabel(textN)
        label_textN.setWordWrap(True)
        label_textN.setFont(QFont('Verdana', 12))
        layout.addWidget(label_textN,2,0)

#___ Block: Download GFS-0.25 button ___#
        self.btn_download25 = QPushButton('Download GFS data (0.25 deg resolution)')
        self.btn_download25.setFixedHeight(40)
        self.btn_download25.setFont(QFont('Verdana', 22))
        self.btn_download25.clicked.connect(self.on_download_button_clicked25)
        layout.addWidget(self.btn_download25,3,0)

#___ Block space ___#
#        layout.addWidget(label_textN,4,0)

#___ Block: Download GFS-0.50 button ___#
        self.btn_download = QPushButton('Download GFS data (0.5 deg resolution)')
        self.btn_download.setFixedHeight(40)
        self.btn_download.setFont(QFont('Verdana', 22))
        self.btn_download.clicked.connect(self.on_download_button_clicked)
        layout.addWidget(self.btn_download,5,0)

#___ Block space ___#
#        layout.addWidget(label_textN,7,0)

#___ Block: Download NAM button ___#
        self.btn_downloadNAM = QPushButton('Download NAM data')
        self.btn_downloadNAM.setFixedHeight(40)
        self.btn_downloadNAM.setFont(QFont('Verdana', 22))
#        self.btn_downloadNAM.clicked.connect(self.on_downloadNAM_button_clicked)
        layout.addWidget(self.btn_downloadNAM,8,0)

#___ Block space ___#
#        layout.addWidget(label_textN,9,0)

#___ Block: Download RDA button ___#
        self.btn_downloadRDA = QPushButton('Download meteorological data from NCAR Research Data Archive')
        self.btn_downloadRDA.setFixedHeight(40)
        self.btn_downloadRDA.setFont(QFont('Verdana', 20))
#        self.btn_downloadRDA.clicked.connect(self.on_downloadRDA_button_clicked)
        layout.addWidget(self.btn_downloadRDA,10,0)
        
#___ Double-Block space ___#
#        layout.addWidget(label_textN,11,0)
        layout.addWidget(label_textN,12,0)
    
#___ Block: Download progress text ___#
        textP = "Download progress"
        label_textP = QLabel(textP)
        label_textP.setWordWrap(True)
        label_textP.setFont(QFont('Verdana', 18))
        label_textP.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_textP,13,0)
        
#___ Block 8: Progress bar ___#
        self.PROGRESS_BAR_MAX = 1000
        self.progressus = QProgressBar()
        self.progressus.setRange(0, self.PROGRESS_BAR_MAX)
        self.progressus.setFixedHeight(45)
        self.progressus.setFont(QFont('Verdana', 18))
#        self.progressus.setStyleSheet("QProgressBar"
#                          "{"
#                          "border: solid grey;"
#                          "border-radius: 15px;"
#                          " color: black; "
#                          "}"
#                          "QProgressBar::chunk "
#                          "{background-color: # 008800;"
#                          "border-radius :15px;"
#                          "}")
        self.progressus.setStyleSheet(StyleSheet)
#        self.progressus.setTextVisible(False)
#        self.progressus.hide()
        layout.addWidget(self.progressus,14,0)

        label_text3 = QLabel(nuntiusII)
        label_text3.setWordWrap(True)
        label_text3.setFont(QFont('Verdana', 10))
        layout.addWidget(label_text3,15,0)
    
        self.setLayout(layout)
        self.layout().setAlignment(Qt.AlignTop)
        self.download_toggling()
        
    def on_download_button_clicked(self):
        print ("on_download_button_clicked\nCalculating number of days ")
        os.chdir('/home/ubuntu/DATA')
        #! Here, I need to create the algorithm for data downloading
        diff = self.servus.finis_dies - self.servus.satus_dies
        n_days = int(diff.days)
        n_slots = int((6+self.servus.finis_hora-self.servus.satus_hora)/6+(n_days*4))
#        print ("Number of days & slots ",n_days, n_slots)
        nunc_dies = self.servus.satus_dies
        hic_dies = nunc_dies.strftime("%Y%m%d")
        nunc = self.servus.satus_hora
        hic_hora = str(nunc).rjust(2, '0')
        nomen_GFS1=[]   
        numerus_GFS1=[] #It's a list
        for i in range(1, n_slots+1):
#            self.gradi = GFSToolsDownloadManager.redire_gradus()
#            print ("LOOP ",i, hic_dies, hic_hora,self.gradi)
            hic_nomen = 'aws s3 cp s3://noaa-gfs-bdp-pds/gfs.'+hic_dies+'/'+hic_hora+'/atmos ' \
            ' /home/ubuntu/DATA --recursive --exclude "*" --include "gfs.t'+hic_hora+'z.pgrb2.0p50.f*" \
            --exclude "*.idx" --no-sign-request --only-show-errors'
#            if (self.gradus == 0.25):
#                hic_nomen = 'aws s3 cp s3://noaa-gfs-bdp-pds/gfs.'+hic_dies+'/'+hic_hora+'/atmos ' \
#                ' /home/ubuntu/DATA --recursive --exclude "*" --include "gfs.t'+hic_hora+'z.pgrb2.0p25.f*" \
#                --exclude "*.idx" --only-show-errors --no-sign-request'
#            elif (self.gradus == 0.5):
#                hic_nomen = 'aws s3 cp s3://noaa-gfs-bdp-pds/gfs.'+hic_dies+'/'+hic_hora+'/atmos ' \
#                ' /home/ubuntu/DATA --recursive --exclude "*" --include "gfs.t'+hic_hora+'z.pgrb2.0p50.f*" \
#                --exclude "*.idx" --only-show-errors --no-sign-request'
            nomen_GFS1.append(hic_nomen)
            numerus_GFS1.append(hic_dies)
            if (nunc == 18):
                nunc_dies = nunc_dies + timedelta(days = 1)
                nunc = 0
                hic_dies = nunc_dies.strftime("%Y%m%d")
                hic_hora = str(nunc).rjust(2, '0')
            else:
                nunc = nunc + 6
                hic_dies = nunc_dies.strftime("%Y%m%d")
                hic_hora = str(nunc).rjust(2, '0')
#        print ("NOMEN ", nomen_GFS1, numerus_GFS1)    
        for j in range(len(nomen_GFS1)):
            self.ratio = float(j/(len(nomen_GFS1)))
            self.on_progress_download(self.ratio)
            aux = 'gfs'+str(numerus_GFS1[j])+'.'
            os.system(nomen_GFS1[j])
            for fileName in os.listdir("/home/ubuntu/DATA"):
                os.rename(fileName,fileName.replace("gfs.",aux))
        self.ratio = 1.0
        self.on_progress_download(self.ratio)    
        cmd1 = 'ln -sf /home/ubuntu/PREPRO/WPS/ungrib/Variable_Tables/Vtable.GFS /home/ubuntu/PREPRO/WPS/Vtable'
        cmd3 = '/home/ubuntu/PREPRO/WPS/link_grib.csh /home/ubuntu/DATA/gfs*'
        os.system(cmd1)
        os.chdir('/home/ubuntu/PREPRO/WPS')
        os.system(cmd3)

    def on_download_button_clicked25(self):
        print ("on_download_button_clicked\nCalculating number of days ")
        os.chdir('/home/ubuntu/DATA')
        #! Here, I need to create the algorithm for data downloading
        diff = self.servus.finis_dies - self.servus.satus_dies
        n_days = int(diff.days)
        n_slots = int((6+self.servus.finis_hora-self.servus.satus_hora)/6+(n_days*4))
        nunc_dies = self.servus.satus_dies
        hic_dies = nunc_dies.strftime("%Y%m%d")
        nunc = self.servus.satus_hora
        hic_hora = str(nunc).rjust(2, '0')
        nomen_GFS1=[]   
        numerus_GFS1=[] #It's a list
        for i in range(1, n_slots+1):
            hic_nomen = 'aws s3 cp s3://noaa-gfs-bdp-pds/gfs.'+hic_dies+'/'+hic_hora+'/atmos ' \
            ' /home/ubuntu/DATA --recursive --exclude "*" --include "gfs.t'+hic_hora+'z.pgrb2.0p25.f*" \
            --exclude "*.idx" --no-sign-request --only-show-errors'
            nomen_GFS1.append(hic_nomen)
            numerus_GFS1.append(hic_dies)
            if (nunc == 18):
                nunc_dies = nunc_dies + timedelta(days = 1)
                nunc = 0
                hic_dies = nunc_dies.strftime("%Y%m%d")
                hic_hora = str(nunc).rjust(2, '0')
            else:
                nunc = nunc + 6
                hic_dies = nunc_dies.strftime("%Y%m%d")
                hic_hora = str(nunc).rjust(2, '0')
        for j in range(len(nomen_GFS1)):
            self.ratio = float(j/(len(nomen_GFS1)))
            self.on_progress_download(self.ratio)
            aux = 'gfs'+str(numerus_GFS1[j])+'.'
            os.system(nomen_GFS1[j])
            for fileName in os.listdir("/home/ubuntu/DATA"):
                os.rename(fileName,fileName.replace("gfs.",aux))
        self.ratio = 1.0
        self.on_progress_download(self.ratio)    
        cmd1 = 'ln -sf /home/ubuntu/PREPRO/WPS/ungrib/Variable_Tables/Vtable.GFS /home/ubuntu/PREPRO/WPS/Vtable'
        cmd3 = '/home/ubuntu/PREPRO/WPS/link_grib.csh /home/ubuntu/DATA/gfs*'
        os.system(cmd1)
        os.chdir('/home/ubuntu/PREPRO/WPS')
        os.system(cmd3)

    def download_toggling(self):
        self.btn_download.setDisabled(False)
        self.btn_download.setStyleSheet("background-color:#008800; color:black")
        self.btn_download25.setDisabled(False)
        self.btn_download25.setStyleSheet("background-color:#008800; color:black")
        self.btn_downloadNAM.setDisabled(False)
        self.btn_downloadNAM.setStyleSheet("background-color:#888888; color:white")
        self.btn_downloadRDA.setDisabled(False)
        self.btn_downloadRDA.setStyleSheet("background-color:#888888; color:white")
#        if (resolution_is_selected == True):
#            self.btn_download.setDisabled(False)
#            self.btn_download.setStyleSheet("background-color:#008800; color:black");
#        else:
#            self.btn_download.setDisabled(True)
#            self.btn_download.setStyleSheet("background-color:#888888; color:white");
        
    def on_progress_download(self, progress: float) -> None:
        bar_value = int(progress * self.PROGRESS_BAR_MAX)
        self.progressus.setValue(bar_value)
        self.progressus.repaint() # otherwise just updates in 1% steps
