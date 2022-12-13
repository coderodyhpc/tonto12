# Gv3GEWRF Plugin
# Copyright (c) 2022 Odycloud.
import datetime

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QLabel, QComboBox, QDateEdit, QFrame
from PyQt5.QtGui import QFont

from Gv3GEWRF.plugin.ui.helpers import WhiteScroll
from Gv3GEWRF.plugin.tempus import Tempus
from Gv3GEWRF.plugin.tempus import Cpu
from Gv3GEWRF.core.util import export
from Gv3GEWRF.core.project import Project

#####--------------------------------------------------------------------------------------------#####
class Classic(QWidget):
    def __init__(self, nuntius, nota):
        super().__init__()

        layout = QHBoxLayout()
        nuntium=QLabel(nuntius)
        nuntium.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntium)

        optio=QLabel(nota)
        optio.setFont(QFont('Verdana', 14))
        optio.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        optio.setAlignment(Qt.AlignCenter)
        layout.addWidget(optio)
        self.setLayout(layout)

#####--------------------------------------------------------------------------------------------#####
class Classic4(QWidget):
    def __init__(self, nuntius, nota):
        super().__init__()

        layout = QHBoxLayout()
        nuntium=QLabel(nuntius)
        nuntium.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntium)
        optio=QLabel(nota)
        optio.setFont(QFont('Verdana', 14))
        optio.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        optio.setAlignment(Qt.AlignCenter)
        layout.addWidget(optio)
        albinusI=QLabel(" ")
        albinusI.setFont(QFont('Verdana', 14))
        layout.addWidget(albinusI)
        albinusII=QLabel(" ")
        albinusII.setFont(QFont('Verdana', 14))
        layout.addWidget(albinusII)

        self.setLayout(layout)

#####--------------------------------------------------------------------------------------------#####
class Tetra(QWidget):
    def __init__(self, nuntius, nota):
        super().__init__()

        layout = QHBoxLayout()
        nuntium=QLabel(nuntius)
        nuntium.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntium)
        nuntiumI=QLabel("")
        nuntiumI.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntiumI)
        aux1=str(int(nota))
        aux2=aux1+(" seconds")
        aux3=(int(nota))/3600
        aux4=str(aux3)+(" hours")
        optio=QLabel(aux2)
        optio.setFont(QFont('Verdana', 14))
        optio.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        optio.setAlignment(Qt.AlignCenter)
        layout.addWidget(optio)
        optioI=QLabel(aux4)
        optioI.setFont(QFont('Verdana', 14))
        optioI.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        optioI.setAlignment(Qt.AlignCenter)
        layout.addWidget(optioI)
        self.setLayout(layout)

#####--------------------------------------------------------------------------------------------#####
class DiesOutput(QWidget):
    def __init__(self, dies1):
#    def __init__(self):
        super().__init__()
        layout = QGridLayout()

        nuntium=QLabel("Simulation start date")
        nuntium.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntium,0,0)

#        nuntiusI = dies1.satus_dies
#        nuntiumI=QLabel(nuntiusI)
#        nuntiumI.setFont(QFont('Verdana', 14))
#        nuntiumI.setFrameShape(QFrame.NoFrame)
#        layout.addWidget(nuntiumI,0,1)

#        nuntiusI = dies1.satus_dies.strftime("%m/%d/%Y")
        self.dies1 = dies1
#        print ("DIES1 at tetra ",self.dies1)
        nuntiusI = self.dies1.satus_dies.strftime("%m/%d/%Y") 
#        print ("NEW NUNTIUS I ",nuntiusI)
        nuntiumI = QLabel(nuntiusI)
        nuntiumI.setFont(QFont('Verdana', 14))
#        self.frame.resize(300,300)
        nuntiumI.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        nuntiumI.setAlignment(Qt.AlignCenter)
        layout.addWidget(nuntiumI,0,1)
        
        nuntiumII=QLabel("               Start hour")
#        nuntiumII=QLabel("Start hour (00-06-12-18)")
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
##        nuntiumIII.resize(100,50)
        layout.addWidget(nuntiumIII,0,3)
        
        nuntiumIV=QLabel("Simulation end date")
        nuntiumIV.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntiumIV,1,0)

        nuntiusV = self.dies1.finis_dies.strftime("%m/%d/%Y")
        nuntiumV = QLabel(nuntiusV)
        nuntiumV.setFont(QFont('Verdana', 14))
##        self.frame.resize(300,300)
        nuntiumV.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        nuntiumV.setAlignment(Qt.AlignCenter)
        layout.addWidget(nuntiumV,1,1)

#        nuntiumVI=QLabel("End hour (00-06-12-18)")
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
class TetraCores(QWidget):
    def __init__(self, nuntius, choice):
        super().__init__()
        layoutC = QHBoxLayout()
#        nuntium=QLabel(nuntius)
        nuntium=QLabel("Cores (total)")
        nuntium.setFont(QFont('Verdana', 14))
        layoutC.addWidget(nuntium)
#        options=QComboBox()        # In case I need to make it an option 
#        options.addItems(choice)
#        options.setFont(QFont('Verdana', 14)) 
#        options.currentTextChanged.connect(self.text_changed)
#        layoutC.addWidget(options)
        self.ranks = Cpu()
        self.ncoros = self.ranks.ncores()
        summa = QLabel(str(self.ncoros))
        summa.setFont(QFont('Verdana', 14)) 
        summa.setStyleSheet("background-color:#000033; color:#FFFFFF")
        summa.setAlignment(Qt.AlignCenter)
        layoutC.addWidget(summa)
        
        nuntiumI=QLabel("Cores (computing)")
        nuntiumI.setFont(QFont('Verdana', 14))
        layoutC.addWidget(nuntiumI)

        summaI=QLabel(str(self.ncoros))
        summaI.setFont(QFont('Verdana', 14))
        summaI.setStyleSheet("background-color:#000066; color:#FFFFFF")
        summaI.setAlignment(Qt.AlignCenter)
        layoutC.addWidget(summaI)

        nuntiumII=QLabel("Cores (visualization)")
        nuntiumII.setFont(QFont('Verdana', 14))
        layoutC.addWidget(nuntiumII)
        summaII=QLabel("0")
#        albinusIV=QLabel(str(self.ncoros))
        summaII.setFont(QFont('Verdana', 14))
        summaII.setStyleSheet("background-color:#000099; color:#FFFFFF")
        summaII.setAlignment(Qt.AlignCenter)
        layoutC.addWidget(summaII)
        
        self.setLayout(layoutC)

    def text_changed(self):
        pass
#        global choice1_is_selected,choice2_is_selected
#        choice1_is_selected = True
#        self.parent().download_toggling()

#####--------------------------------------------------------------------------------------------#####
#####--------------------------------------------------------------------------------------------#####
#####--------------------------------------------------------------------------------------------#####
class GenCharTab(QWidget):
    def __init__(self, iface, ancilla, project) -> None:  # ancilla holds the passed class (e.g. tempus) 
        super().__init__()
        self.ancilla = ancilla
        self.project = project
#___ The next lines set up the layout ___#
        layout = QGridLayout()
#___ This is the first block: Paragraph with some information ___#
        text = """
                    <html>
                        <p><b>WRF simulation general characteristics</b></p>
                        \n  
                        </p>
                    </html>
               """
        label_text = QLabel(text)
        label_text.setWordWrap(True)
        label_text.setFont(QFont('Verdana', 16))
        label_text.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_text,0,0)
#___ This is the second block: WRF simulation type ___#
        simtype = Classic("WRF simulation type","ARW - Advanced Research WRF")
        layout.addWidget(simtype,1,0)
        
#___ This is the third block:  ___#
#        text = "Meteorological data"
#        options=["GFS"]
        GFScall = Classic("Meteorological data","GFS")
        layout.addWidget(GFScall,2,0)

#___ This is the third block:  ___#
#        TScall = Classic("Time step ", self.ancilla.time_delta)
        TScall = Classic("Time step ", "45")
        layout.addWidget(TScall,3,0)

#___ This is the fourth block: Start Dates ___#
#        dies2 = QDateEdit(famulus.finis_dies)
#        self.dies_duo2=duodate(dies2)
#        self.dies_duo2.setFixedHeight(65)
#        self.dies_duo2.setFont(QFont('Verdana', 14))
#        layout.addWidget(self.dies_duo2,4,0)
#        self.dies_tetra = DiesOutput(famulus)
        self.dies_tetra = DiesOutput(self.ancilla)
#        self.dies_tetra.setFixedHeight(65)
        layout.addWidget(self.dies_tetra,4,0)
    
#___ : Intervals ___#
        bl_5 = Tetra("Meteorological data intervals","21600")
        layout.addWidget(bl_5,5,0)

#___ History:  ___#
        bl_7 = Classic("History intervals","60")
        layout.addWidget(bl_7,6,0)
        
#___ Number of domains:  ___#
#        text = "Number of domains"
#        options=["1","2","4","8","16","24","32","48","64"]
#        GFScall = duometdata(text,options)
#        layout.addWidget(GFScall,5,0)

#        self.bl_8 = Classic4("Number of domains","1")
        self.Hdomain = QHBoxLayout()
        Hnuntium = QLabel("Number of domains")
        Hnuntium.setFont(QFont('Verdana', 14))
        self.Hdomain.addWidget(Hnuntium)
        Hoptio=QLabel("1")
        Hoptio.setFont(QFont('Verdana', 14))
        Hoptio.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        Hoptio.setAlignment(Qt.AlignCenter)
        self.Hdomain.addWidget(Hoptio)
        HalbinusI = QLabel(" ")
        HalbinusI.setFont(QFont('Verdana', 14))
        self.Hdomain.addWidget(HalbinusI)
        self.llll = self.ancilla.satus_dies.strftime("%m/%d/%Y") 
        self.Hlll = QLabel(self.llll)
        self.Hlll.setFont(QFont('Verdana', 14))
#        self.Hdomain.addWidget(HalbinusI)
        self.Hdomain.addWidget(self.Hlll)

        layout.addLayout(self.Hdomain,7,0)

#___ 9th block:  ___#
        bl_9 = Classic4("Number of vertical points","35")
        layout.addWidget(bl_9,8,0)
        
#___ Physics suite  ___#
        bl_physics = Classic("Physics suite","CONUS")
        layout.addWidget(bl_physics,9,0)
        
#___ Number of cores  ___#
        text = "Number of cores"
        options=["1","2","4","8","16","24","32","48","64"]
        ncores = TetraCores(text,options)
        layout.addWidget(ncores,10,0)
        
        self.setLayout(layout)
        self.layout().setAlignment(Qt.AlignTop)
        
        self.refresh()

    def refresh(self):
#        print ("\nPROJECT REFRESH ",Project.create.data,"\n")
#        aux = Tempus()
        print ("REFRESH2!!! \n", self.project, self.Hlll)
#        self.dies_tetra.setDisabled(True)
#        self.Hdomain.setDisabled(True)
        self.Hlll.setStyleSheet("background-color:#880000; color:black");
