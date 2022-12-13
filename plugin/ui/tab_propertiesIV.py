# Gv3GEWRF Plugin
# Copyright (c) 2022 Odycloud.
import datetime

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QLabel, QComboBox, QSpinBox, QDateEdit, QDateTimeEdit, QFrame
from PyQt5.QtGui import QFont

from Gv3GEWRF.plugin.ui.helpers import WhiteScroll
from Gv3GEWRF.plugin.tempus import Tempus, Cpu
#from Gv3GEWRF.plugin.ui.met_download.widget_gfs import DuodateVI, DuohourII
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
class DuodateI(QWidget):               
    def __init__(self, value):            
        super().__init__()
        layout = QHBoxLayout()
        self.dies_novus = value
#- Label        
        nuntius = "Simulation start date     "
        nuntium=QLabel(nuntius)
        nuntium.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntium)
#- Combo DateEdit        
        self.dies = QDateTimeEdit(self.dies_novus.satus_dies)                 # Input any time correction
        self.dies.setFont(QFont('Verdana', 14))
        self.dies.setStyleSheet("background-color:#555566; color:#FFFFFF ")
        self.dies.dateChanged.connect(self.on_date_changed)  # Here, it's where I need to feedback the new date
        layout.addWidget(self.dies)
#- Label        
        nuntiusI = "Simulation start hour          "
        nuntiumI=QLabel(nuntiusI)
        nuntiumI.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntiumI)
#- Combo DateEdit        
        self.hora = QComboBox()        
        self.hora.addItem(str(self.dies_novus.satus_hora))
        self.hora.addItem("00")
        self.hora.addItem("06")
        self.hora.addItem("12")
        self.hora.addItem("18")
        self.hora.setFont(QFont('Verdana', 14))
        self.hora.setStyleSheet("background-color:#555566; color:#FFFFFF ")
        self.hora.currentIndexChanged.connect(self.selectionchange)
        layout.addWidget(self.hora)
#- Blank label        
#        nuntiumII=QLabel("                                                                      ")
#        nuntiumII.setFont(QFont('Verdana', 14))
#        layout.addWidget(nuntiumII)
        self.setLayout(layout)
        
    def on_date_changed(self, newDate):
        CONVERSION = newDate.toPyDate()
        self.dies_novus.satus_dies = DuodateI.extra_change(CONVERSION)
        
    def extra_change(value):
        return value

    def selectionchange(self,i):
        if (i == 1):
            novus_hora = 0
        elif (i == 2):
            novus_hora = 6
        elif (i == 3):
            novus_hora = 12
        elif (i == 4):
            novus_hora = 18
        self.dies_novus.satus_hora = DuodateI.extra_hora(novus_hora)
        
    def extra_hora(value):
        return value

#####--------------------------------------------------------------------------------------------#####
class DuodateII(QWidget):               
    def __init__(self, value):            
        super().__init__()
        layout = QHBoxLayout()
        self.dies_novus = value
#- Label        
        nuntius = "Simulation end date     "
        nuntium=QLabel(nuntius)
        nuntium.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntium)
#- Combo DateEdit        
        self.dies = QDateTimeEdit(self.dies_novus.finis_dies)                 
        self.dies.setFont(QFont('Verdana', 14))
        self.dies.setStyleSheet("background-color:#555566; color:#FFFFFF ")
        self.dies.dateChanged.connect(self.on_end_date_changed)  
        layout.addWidget(self.dies)
#- Label        
        nuntiusI = "Simulation end hour          "
        nuntiumI=QLabel(nuntiusI)
        nuntiumI.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntiumI)
#- Combo DateEdit        
        self.hora = QComboBox()        
        self.hora.addItem(str(self.dies_novus.satus_hora))
        self.hora.addItem("00")
        self.hora.addItem("06")
        self.hora.addItem("12")
        self.hora.addItem("18")
        self.hora.setFont(QFont('Verdana', 14))
        self.hora.setStyleSheet("background-color:#555566; color:#FFFFFF ")
        self.hora.currentIndexChanged.connect(self.endselectionchange)
        layout.addWidget(self.hora)
        self.setLayout(layout)
        
    def on_end_date_changed(self, newDate):
        CONVERSION = newDate.toPyDate()
        self.dies_novus.finis_dies = DuodateII.end_extra_change(CONVERSION)
        
    def end_extra_change(value):
        return value

    def endselectionchange(self,i):
        if (i == 1):
            novus_hora = 0
        elif (i == 2):
            novus_hora = 6
        elif (i == 3):
            novus_hora = 12
        elif (i == 4):
            novus_hora = 18
        self.dies_novus.finis_hora = DuodateII.end_extra_hora(novus_hora)
        
    def end_extra_hora(value):
        return value
    
#####--------------------------------------------------------------------------------------------#####
#####--------------------------------------------------------------------------------------------#####
#####--------------------------------------------------------------------------------------------#####
class PropertiesTab(QWidget):
    def __init__(self, iface, ancilla, project) -> None:  # ancilla holds the passed class (e.g. tempus) 
        super().__init__()
        self.ancilla = ancilla
        self.project = project
#        print ("AT PropertiesTab ",self.ancilla,self.ancilla.satus_dies,self.ancilla.vertical_points, \
#              self.ancilla.finis_dies,self.ancilla.vertical_points)
#___ The next lines set up the layout ___#
        layout = QGridLayout()
#___ BL1: Paragraph with some information ___#
        text = """
                    <html>
                        <p><b>WRF simulation properties</b></p>
                        \n  
                        </p>
                    </html>
               """
        label_text = QLabel(text)
        label_text.setWordWrap(True)
        label_text.setFont(QFont('Verdana', 16))
        label_text.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_text,0,0)
        
#___ BL2: WRF simulation type ___#
        simtype = Classic("WRF simulation type","ARW - Advanced Research WRF")
        layout.addWidget(simtype,1,0)

#___ BL3: MET data type ___#
        simtype = Classic("Meteorological data type","GFS")
        layout.addWidget(simtype,2,0)
        
#___ BL3: Time Step ___#
        self.widget_ts = QHBoxLayout()
        tsnuntium = QLabel("Time step (s) [Min: 15 s; max: 300 s]")
        tsnuntium.setFont(QFont('Verdana', 14))
        self.widget_ts.addWidget(tsnuntium)
        ts_ini = int(self.ancilla.time_delta)
        self.tsoptio = QSpinBox()
        self.tsoptio.setFont(QFont('Verdana', 14))
        self.tsoptio.setStyleSheet("background-color:#777777; color:#FFFFFF ")
        self.tsoptio.setAlignment(Qt.AlignCenter)
        self.tsoptio.setRange(15,300)
        self.tsoptio.setValue = ts_ini
        self.tsoptio.valueChanged.connect(self.tschange)
        self.widget_ts.addWidget(self.tsoptio)
        layout.addLayout(self.widget_ts,3,0)

#___ Block 4: Input of the start date ___#
        self.start_dies=DuodateI(self.ancilla)
        self.start_dies.setFixedHeight(65)
#        print ("It's supposed to call DuodateIV ",self.start_dies)
#        self.start_dies.setFont(QFont('Verdana', 14))
        layout.addWidget(self.start_dies,4,0)

#___ Block 5: Input of the end date ___#
        self.end_dies=DuodateII(self.ancilla)
        self.end_dies.setFixedHeight(65)
        layout.addWidget(self.end_dies,5,0)

#___ BL5:  ___#
#        self.numerus_v = Classic("Number of vertical points","35")
#        layout.addWidget(self.numerus_v,4,0)
        self.numerus_v = QHBoxLayout()
        vnuntium = QLabel("Number of vertical points [Min: 25; max: 100]")
        vnuntium.setFont(QFont('Verdana', 14))
        self.numerus_v.addWidget(vnuntium)
#        ts_ini = int(self.ancilla.time_delta)
#        self.tsoptio=QSpinBox(ts_ini)
        self.voptio=QSpinBox()
        self.voptio.setValue = 35
        self.voptio.setFont(QFont('Verdana', 14))
        self.voptio.setStyleSheet("background-color:#999999; color:#FFFFFF ")
        self.voptio.setAlignment(Qt.AlignCenter)
        self.voptio.setRange(25,100)
        self.voptio.valueChanged.connect(self.verticalchange)
        self.numerus_v.addWidget(self.voptio)
        layout.addLayout(self.numerus_v,6,0)

        Separador = QFrame()
        Separador.setFrameShape(QFrame.HLine)
#        Separador.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
        Separador.setLineWidth(3)
        layout.addWidget(Separador,7,0)
#___ BL1:  ___#
        text = """
                    <html>
                        <p><b>\nParallel Computing (cores task distribution)</b></p>
                        \n  
                        </p>
                    </html>
               """
        label_text = QLabel(text)
        label_text.setWordWrap(True)
        label_text.setFont(QFont('Verdana', 14))
        label_text.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_text,8,0)

 #___ BL6: Number of cores  ___#
        text = "Number of cores"
        options=["1","2","4","8","16","24","32","48","64"]
        ncores = TetraCores(text,options)
        layout.addWidget(ncores,9,0)

        Separador2 = QFrame()
        Separador2.setFrameShape(QFrame.HLine)
#        Separador.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
        Separador2.setLineWidth(5)
        layout.addWidget(Separador2,10,0)

#___ BL1:  ___#
        text = """
                    <html>
                        <p><b>\nPhysics & dynamics</b></p>
                        \n  
                        </p>
                    </html>
               """
        label_text = QLabel(text)
        label_text.setWordWrap(True)
        label_text.setFont(QFont('Verdana', 12))
        label_text.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_text,11,0)
        
#___ :  ___#
#        simtype = Classic12X("Physics_suite:","CONUS","Hybrid_opt:","2","mp_physics:","-1", \
#                             "w_damping:","0","cu_physics:", "-1", "diff_opt:", "1")
#        layout.addWidget(simtype,11,0)
        
#___ This is the third block:  ___#
#        GFScall = Classic8W("mp_physics:","-1","w_damping:","0")
#        layout.addWidget(GFScall,7,0)

#___ This is the third block:  ___#
#        TScall = Classic8W("cu_physics:", "-1", "diff_opt:", "1")
#        layout.addWidget(TScall,8,0)

#___ :  ___#
#        simtypeII = Classic12X("ra_lw_physics:","-1","km_opt:","4","ra_sw_physics:","-1", \
#                               "diff_6th_opt:","0","bl_pbl_physics:","-1","diff_6th_factor:","0.12")
#___ :  ___#
#        simtypeIII = Classic12X("sf_sfclay_physics:","-1","base_temp:","290.","radt:","30", \
#                                "zdamp:","5000","bldt:","0","dampcoef:","0.2")
#        layout.addWidget(simtypeIII,13,0)
        
        simtypeI = self.output_Classic12X("Physics_suite:","CONUS","Hybrid_opt:","2","mp_physics:","-1", \
                             "w_damping:","0","cu_physics:", "-1", "diff_opt:", "1")
        layout.addLayout(simtypeI,12,0)
        simtypeII = self.output_Classic12X("ra_lw_physics:","-1","km_opt:","4","ra_sw_physics:","-1", \
                               "diff_6th_opt:","0","bl_pbl_physics:","-1","diff_6th_factor:","0.12")
        layout.addLayout(simtypeII,13,0)
        simtypeIII = self.output_Classic12X("sf_sfclay_physics:","-1","base_temp:","290.","radt:","30", \
                                "zdamp:","5000","bldt:","0","dampcoef:","0.2")
        layout.addLayout(simtypeIII,14,0)
        simtypeIV = self.output_Classic12X("cudt:","5","khdif:","0","icloud:","1","kvdif:","0"," "," "," "," ")
        layout.addLayout(simtypeIV,15,0)
        
        
        self.setLayout(layout)
        self.layout().setAlignment(Qt.AlignTop)
        
    def tschange(self):
        print("current value:"+str(self.tsoptio.value()))
        self.ancilla.time_delta = self.tsoptio.value()

    def verticalchange(self):
        print("Verical value:"+str(self.voptio.value()))
        self.ancilla.vertical_points = self.voptio.value()

    def redire_ancilla(self):
        self.aaa = self.ancilla.satus_dies.strftime("%m/%d/%Y")
        print ("At redire ancilla ",self.aaa)
        return self.aaa
        
#####||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#####
    def output_Classic12X(self, nuntius, nota, nuntiusII, notaII, nuntiusIII, notaIII, nuntiusIV, \
                          notaIV, nuntiusV, notaV, nuntiusVI, notaVI):
#        Q12X = QWidget()
        Cl12X = QHBoxLayout()
        albinus = "                     "
        albinum = QLabel(albinus)
        albinum.setFont(QFont('Verdana', 12))
        
        nuntium=QLabel(nuntius)
        nuntium.setFont(QFont('Verdana', 12))
        nuntium.setAlignment(Qt.AlignLeft)
        Cl12X.addWidget(nuntium)
        optio=QLabel(nota)
        optio.setFont(QFont('Verdana', 12))
        optio.setAlignment(Qt.AlignLeft)
        optio.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        Cl12X.addWidget(optio)

        albinusI=QLabel(nuntiusII)
        albinusI.setFont(QFont('Verdana', 12))
        albinusI.setAlignment(Qt.AlignLeft)
        Cl12X.addWidget(albinusI)
        albinusII=QLabel(notaII)
        albinusII.setFont(QFont('Verdana', 12))
        albinusII.setAlignment(Qt.AlignLeft)
        albinusII.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        Cl12X.addWidget(albinusII)

        albinusIII=QLabel(nuntiusIII)
        albinusIII.setFont(QFont('Verdana', 12))
        albinusIII.setAlignment(Qt.AlignLeft)
        Cl12X.addWidget(albinusIII)
        albinusIV=QLabel(notaIII)
        albinusIV.setFont(QFont('Verdana', 12))
        albinusIV.setAlignment(Qt.AlignLeft)
        albinusIV.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        Cl12X.addWidget(albinusIV)

        albinusV=QLabel(nuntiusIV)
        albinusV.setFont(QFont('Verdana', 12))
        albinusV.setAlignment(Qt.AlignLeft)
        Cl12X.addWidget(albinusV)
        albinusVI=QLabel(notaIV)
        albinusVI.setFont(QFont('Verdana', 12))
        albinusVI.setAlignment(Qt.AlignLeft)
        albinusVI.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        Cl12X.addWidget(albinusVI)
        
        albinusVII=QLabel(nuntiusV)
        albinusVII.setFont(QFont('Verdana', 12))
        albinusVII.setAlignment(Qt.AlignLeft)
        Cl12X.addWidget(albinusVII)
        albinusVIII=QLabel(notaV)
        albinusVIII.setFont(QFont('Verdana', 12))
        albinusVIII.setAlignment(Qt.AlignLeft)
        albinusVIII.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        Cl12X.addWidget(albinusVIII)
        
        albinusIX=QLabel(nuntiusVI)
        albinusIX.setFont(QFont('Verdana', 12))
        albinusIX.setAlignment(Qt.AlignLeft)
        Cl12X.addWidget(albinusIX)
        albinusX=QLabel(notaVI)
        albinusX.setFont(QFont('Verdana', 12))
        albinusX.setAlignment(Qt.AlignLeft)
        albinusX.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        Cl12X.addWidget(albinusX)

#        Q12X.addLayout(Cl12X)
        return Cl12X
#        return Q12X
#        self.setLayout(layout)
        
#####||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#####
    def fun_diebus(self):
        output_diebus = QGridLayout()

        nuntium=QLabel("Simulation start date")
        nuntium.setFont(QFont('Verdana', 14))
        output_diebus.addWidget(nuntium,0,0)

        print ("FUN_DIEBUS ")
#        nuntiusI = self.ancilla.satus_dies.strftime("%m/%d/%Y") 
        nuntiusI = PropertiesTab.redire_ancilla 
        nuntiumI = QLabel(nuntiusI)
        nuntiumI.setFont(QFont('Verdana', 14))
        nuntiumI.setStyleSheet("background-color:#000000; color:#FFFFFF ")
        nuntiumI.setAlignment(Qt.AlignCenter)
        output_diebus.addWidget(nuntiumI,0,1)
        
#        nuntiumII=QLabel("               Start hour")
#        nuntiumII.setFont(QFont('Verdana', 14))
#        output_diebus.addWidget(nuntiumII,0,2)

#        if (self.ancilla.satus_hora == 0):
#            nuntiumIII=QLabel("00")
#        elif (self.ancilla.satus_hora == 6):
#            nuntiumIII=QLabel("06")
#        elif (self.ancilla.satus_hora == 12):
#            nuntiumIII=QLabel("12")
#        elif (self.ancilla.satus_hora == 18):
#            nuntiumIII=QLabel("18")
#        nuntiumIII.setFont(QFont('Verdana', 14))
#        nuntiumIII.setStyleSheet("background-color:#000000; color:#FFFFFF ")
#        nuntiumIII.setAlignment(Qt.AlignCenter)
#        output_diebus.addWidget(nuntiumIII,0,3)
        
#        nuntiumIV=QLabel("Simulation end date")
#        nuntiumIV.setFont(QFont('Verdana', 14))
#        output_diebus.addWidget(nuntiumIV,1,0)

#        nuntiusV = self.ancilla.finis_dies.strftime("%m/%d/%Y")
#        nuntiumV = QLabel(nuntiusV)
#        nuntiumV.setFont(QFont('Verdana', 14))
#        nuntiumV.setStyleSheet("background-color:#000000; color:#FFFFFF ")
#        nuntiumV.setAlignment(Qt.AlignCenter)
#        output_diebus.addWidget(nuntiumV,1,1)

#        nuntiumVI=QLabel("               End hour")
#        nuntiumVI.setFont(QFont('Verdana', 14))
#        output_diebus.addWidget(nuntiumVI,1,2)

#        if (self.ancilla.finis_hora == 0):
#            nuntiumVII=QLabel("00")
#        elif (self.ancilla.finis_hora == 6):
#            nuntiumVII=QLabel("06")
#        elif (self.ancilla.finis_hora == 12):
#            nuntiumVII=QLabel("12")
#        elif (self.ancilla.finis_hora == 18):
#            nuntiumVII=QLabel("18")
#        nuntiumVII.setFont(QFont('Verdana', 14))
#        nuntiumVII.setStyleSheet("background-color:#000000; color:#FFFFFF ")
#        nuntiumVII.setAlignment(Qt.AlignCenter)
#        output_diebus.addWidget(nuntiumVII,1,3)

        return output_diebus
#        self.setLayout(layout)
        
