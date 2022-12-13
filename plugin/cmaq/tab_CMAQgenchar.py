# Gv3GEWRF Plugin
# Copyright (c) 2022 Odycloud.
import datetime

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QDateEdit, QDateTimeEdit
from PyQt5.QtGui import QFont

from Gv3GEWRF.plugin.ui.helpers import WhiteScroll
#from Gv3GEWRF.plugin.cmaq.cmaq_tempus import CTempus
#from Gv3GEWRF.plugin.cmaq.cmaq_tempus import Cpu
from Gv3GEWRF.core.util import export
from Gv3GEWRF.core.project import Project

#####--------------------------------------------------------------------------------------------#####
class DuodateI(QWidget):               
    def __init__(self, value):            
        super().__init__()
        layout = QHBoxLayout()
        self.dies_novus = value
#- Label        
        nuntius = "Start date for CMAQ simulations"
        nuntium=QLabel(nuntius)
        nuntium.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntium)
#- Combo DateEdit        
        self.dies = QDateTimeEdit(self.dies_novus.satus_dies)                 # Input any time correction
        self.dies.setFont(QFont('Verdana', 14))
##        self.dies.dateChanged.connect(self.CMAQ_on_date_changed)  # Here, it's where I need to feedback the new date
        self.dies.setStyleSheet("background-color:#228B22; color:#FFFFFF")
        layout.addWidget(self.dies)

        self.setLayout(layout)

#    def CMAQ_on_date_changed(self, newDate):
#        CONVERSION = newDate.toPyDate()
#        self.dies_novus.satus_dies = DuodateI.extra_change(CONVERSION)
        
#    def extra_change(value):
#        return value
        
#####--------------------------------------------------------------------------------------------#####
class DuodateII(QWidget):               
    def __init__(self, value):            
        super().__init__()
        layout = QHBoxLayout()
        self.value = value
#- Label        
        nuntius = "End date for CMAQ simulation"
        nuntium=QLabel(nuntius)
        nuntium.setFont(QFont('Verdana', 14))
        layout.addWidget(nuntium)
#- Combo DateEdit        
#        self.dies = QDateTimeEdit(self.value.finis_dies)                 # Input any time correction
#        self.dies.setFont(QFont('Verdana', 14))
##        self.dies.dateChanged.connect(self.on_date_changed)  # Here, it's where I need to feedback the new date
#        layout.addWidget(self.dies)
        self.nuntiusDATE = self.value.finis_dies.strftime("%b %d %Y %H:%M:%S")
        nuntiumDATE=QLabel(self.nuntiusDATE)
        nuntiumDATE.setFont(QFont('Verdana', 14))
        nuntiumDATE.setStyleSheet(border: 1px solid black; "background-color:#228B22; color:#FFFFFF")
        layout.addWidget(nuntiumDATE)
        
        self.setLayout(layout)

#    def on_date_changed(self, newDate):
#        CONVERSION = newDate.toPyDate()
#        self.dies_novus.finis_dies = DuodateVI.extra_change(CONVERSION)
        
#    def extra_change(value):
#        return value

#####--------------------------------------------------------------------------------------------#####
#####--------------------------------------------------------------------------------------------#####
#####--------------------------------------------------------------------------------------------#####
class CMAQCharTab(QWidget):
    def __init__(self, iface, ancilla, servus) -> None:  # ancilla & servus hold the passed classes 
        super().__init__()
        self.ancilla = ancilla
        self.servus =servus
#___ Layout set-up ___#
        layout = QVBoxLayout()
#___ This is the first block: Paragraph with some information ___#
        text = """
                    <html>
                        <p><b>CMAQ simulation - General variables</b></p>
                        \n  
                        </p>
                    </html>
               """
        label_text = QLabel(text)
        label_text.setWordWrap(True)
        label_text.setFont(QFont('Verdana', 16))
        label_text.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_text)
#___ BLOCK 2: CMAQ simulation type ___#
        H2layout = QHBoxLayout()
        nuntium2=QLabel("CMAQ simulation type")
        nuntium2.setFont(QFont('Verdana', 14))
        H2layout.addWidget(nuntium2)
        optio2=QComboBox()         
        self.list=["CMAQ standard simulation", "ISAM", "DDM3D"]
        optio2.addItems(self.list)
        optio2.setFont(QFont('Verdana', 14)) 
        optio2.setStyleSheet("background-color:#228B22; color:#FFFFFF")
##        optio2.currentTextChanged.connect(self.text_changed)
        H2layout.addWidget(optio2)
        layout.addLayout(H2layout)
#___ BLOCK 3: CODE version ___#
        H2layout = QHBoxLayout()
        nuntium2=QLabel("CMAQ version")
        nuntium2.setFont(QFont('Verdana', 14))
        H2layout.addWidget(nuntium2)
        optio2=QLabel(" 5.3.3.1")         
        optio2.setFont(QFont('Verdana', 14)) 
        optio2.setStyleSheet("background-color:#228B22; color:#FFFFFF")
##        optio2.currentTextChanged.connect(self.text_changed)
        H2layout.addWidget(optio2)
        layout.addLayout(H2layout)
#___ BLOCK 4: Mechanism ID ___#
        H4layout = QHBoxLayout()
        nuntium4=QLabel("Mechanism ID")
        nuntium4.setFont(QFont('Verdana', 14))
        H4layout.addWidget(nuntium4)
        optio4=QComboBox()         
        optio4.addItem("cb6r3_ae7_aq")
        optio4.setFont(QFont('Verdana', 14)) 
        optio4.setStyleSheet("background-color:#228B22; color:#FFFFFF")
        H4layout.addWidget(optio4)
        layout.addLayout(H4layout)
#___ BLOCK 5: Application name ___#
        H5layout = QHBoxLayout()
        nuntium5=QLabel("Application name")
        nuntium5.setFont(QFont('Verdana', 14))
        H5layout.addWidget(nuntium5)
        optio5=QComboBox()         
        optio5.addItem("Bench_2016_12SE1")
        optio5.setFont(QFont('Verdana', 14)) 
        optio5.setStyleSheet("background-color:#228B22; color:#FFFFFF")
##        optio5.currentTextChanged.connect(self.text_changed)
        H5layout.addWidget(optio5)
        layout.addLayout(H5layout)

#___ BLOCK 6: START DATE ___#
        self.start_dies=DuodateI(self.ancilla)
        self.start_dies.setFont(QFont('Verdana', 14))
        layout.addWidget(self.start_dies)

#___ BLOCK 8: Simulation time properties ___#
        H8layout = QHBoxLayout()
        nuntium8=QLabel("  Simulation starting hour")
        nuntium8.setFont(QFont('Verdana', 14))
        H8layout.addWidget(nuntium8)
        optio8=QComboBox()         
        optio8.addItem("00")
        optio8.setFont(QFont('Verdana', 14)) 
        optio8.setStyleSheet("background-color:#228B22; color:#FFFFFF")
##        optio5.currentTextChanged.connect(self.text_changed)
        H8layout.addWidget(optio8)
        nuntium9=QLabel("   Duration of the simulation")
        nuntium9.setFont(QFont('Verdana', 14))
        H8layout.addWidget(nuntium9)
        optio9=QComboBox()         
        optio9.addItem("24")
        optio9.setFont(QFont('Verdana', 14)) 
        optio9.setStyleSheet("background-color:#228B22; color:#FFFFFF")
##        optio5.currentTextChanged.connect(self.text_changed)
        H8layout.addWidget(optio9)
        nuntiumA=QLabel("hours")
        nuntiumA.setFont(QFont('Verdana', 14))
        H8layout.addWidget(nuntiumA)
        optio9B=QComboBox()         
        optio9B.addItem("00")
        optio9B.setFont(QFont('Verdana', 14)) 
        optio9B.setStyleSheet("background-color:#228B22; color:#FFFFFF")
##        optio5.currentTextChanged.connect(self.text_changed)
        H8layout.addWidget(optio9B)
        nuntiumB=QLabel("minutes")
        nuntiumB.setFont(QFont('Verdana', 14))
        H8layout.addWidget(nuntiumB)
        optio9C=QComboBox()         
        optio9C.addItem("00")
        optio9C.setFont(QFont('Verdana', 14)) 
        optio9C.setStyleSheet("background-color:#228B22; color:#FFFFFF")
##        optio5.currentTextChanged.connect(self.text_changed)
        H8layout.addWidget(optio9C)
        nuntiumC=QLabel("seconds")
        nuntiumC.setFont(QFont('Verdana', 14))
        H8layout.addWidget(nuntiumC)
        layout.addLayout(H8layout)

#___ BLOCK: END DATE ___#
        self.end_dies=DuodateII(self.ancilla)
        self.end_dies.setFont(QFont('Verdana', 14))
        layout.addWidget(self.end_dies)

#___ BLOCK: TIME STEP ___# I need to set up the time step

#___ BLOCK: Grid name ___#
        H10layout = QHBoxLayout()
        nuntium10=QLabel("Grid name")
        nuntium10.setFont(QFont('Verdana', 14))
        H10layout.addWidget(nuntium10)
        optio10=QComboBox()
        self.nomen10 = self.ancilla.GRID_NAME()
        optio10.addItem(self.nomen10)
        optio10.setFont(QFont('Verdana', 14)) 
        optio10.setStyleSheet("background-color:#228B22; color:#FFFFFF")
##        optio5.currentTextChanged.connect(self.text_changed)
        H10layout.addWidget(optio10)
        layout.addLayout(H10layout)

#___ BLOCK: Grid dimensions ___#
        H11layout = QHBoxLayout()
    
        nuntium11=QLabel("Nx")
        nuntium11.setFont(QFont('Verdana', 14))
        H11layout.addWidget(nuntium11)
        self.nomen11 = self.ancilla.nx()
        nuntium11W=QLabel(self.nomen11)
        nuntium11W.setFont(QFont('Verdana', 14))
        nuntium11W.setStyleSheet("border: 1px solid black; background-color:#228B22; color:#FFFFFF")
        H11layout.addWidget(nuntium11W)

        nuntium11X=QLabel("Ny")
        nuntium11X.setFont(QFont('Verdana', 14))
        H11layout.addWidget(nuntium11X)
        self.nomen11Y = self.ancilla.ny()
        nuntium11Y=QLabel(self.nomen11Y)
        nuntium11Y.setFont(QFont('Verdana', 14))
        nuntium11Y.setStyleSheet("border: 0.5px solid black; background-color:#228B22; color:#FFFFFF")
        H11layout.addWidget(nuntium11Y)

        nuntium11L=QLabel("Layers")
        nuntium11L.setFont(QFont('Verdana', 14))
        H11layout.addWidget(nuntium11L)
        self.nomen11Z = self.ancilla.nz()
        nuntium11Z=QLabel(self.nomen11Z)
        nuntium11Z.setFont(QFont('Verdana', 14))
        nuntium11Z.setStyleSheet("border: 0.25px solid black; background-color:#228B22; color:#FFFFFF")
        H11layout.addWidget(nuntium11Z)

        layout.addLayout(H11layout)
        
#___ BLOCK i: Blank space
        textB = """
                    <html>
                        <p><b> </b></p>
                    </html>
               """
        nuntiumB=QLabel(textB)
        nuntiumB.setFont(QFont('Verdana', 12))
        layout.addWidget(nuntiumB)
        
#___ BLOCK i: Science options#
        textS = """
                    <html>
                        <p><b>\nScience options</b></p>
                    </html>
               """
        nuntiumi=QLabel(textS)
        nuntiumi.setFont(QFont('Verdana', 12))
        layout.addWidget(nuntiumi)

        Hilayout = QHBoxLayout()
        nuntiumia=QLabel("CTM_OCEAN_CHEM")
        nuntiumia.setFont(QFont('Verdana', 10))
        Hilayout.addWidget(nuntiumia)
        optioia=QComboBox()         
        optioia.addItem("Y")
        optioia.setFont(QFont('Verdana', 10)) 
        optioia.setStyleSheet("background-color:#228B22; color:#FFFFFF")
##        optio5.currentTextChanged.connect(self.text_changed)
        Hilayout.addWidget(optioia)
        nuntiumib=QLabel("CTM_WB_DUST")
        nuntiumib.setFont(QFont('Verdana', 10))
        Hilayout.addWidget(nuntiumib)
        optioic=QComboBox()         
        optioic.addItem("N")
        optioic.setFont(QFont('Verdana', 10)) 
        optioic.setStyleSheet("background-color:#228B22; color:#FFFFFF")
        Hilayout.addWidget(optioic)

        nuntiumid=QLabel("CTM_WBDUST_BELD")
        nuntiumid.setFont(QFont('Verdana', 10))
        Hilayout.addWidget(nuntiumid)
        optioie=QComboBox()         
        optioie.addItem("BELD3")
        optioie.setFont(QFont('Verdana', 10)) 
        optioie.setStyleSheet("background-color:#228B22; color:#FFFFFF")
##        optio5.currentTextChanged.connect(self.text_changed)
        Hilayout.addWidget(optioie)
        nuntiumif=QLabel("CTM_LTNG_NO")
        nuntiumif.setFont(QFont('Verdana', 10))
        Hilayout.addWidget(nuntiumif)
        optioig=QComboBox()         
        optioig.addItem("N")
        optioig.setFont(QFont('Verdana', 10)) 
        optioig.setStyleSheet("background-color:#228B22; color:#FFFFFF")
        Hilayout.addWidget(optioig)

        Hiilayout = QHBoxLayout()
        nuntiumih=QLabel("KZMIN")
        nuntiumih.setFont(QFont('Verdana', 10))
        Hiilayout.addWidget(nuntiumih)
        optioii=QComboBox()         
        optioii.addItem("Y")
        optioii.setFont(QFont('Verdana', 10)) 
        optioii.setStyleSheet("background-color:#228B22; color:#FFFFFF")
##        optio5.currentTextChanged.connect(self.text_changed)
        Hiilayout.addWidget(optioii)
        nuntiumij=QLabel("CTM_MOSAIC")
        nuntiumij.setFont(QFont('Verdana', 10))
        Hiilayout.addWidget(nuntiumij)
        optioik=QComboBox()         
        optioik.addItem("N")
        optioik.setFont(QFont('Verdana', 10)) 
        optioik.setStyleSheet("background-color:#228B22; color:#FFFFFF")
        Hiilayout.addWidget(optioik)

        nuntiumil=QLabel("CTM_FST")
        nuntiumil.setFont(QFont('Verdana', 10))
        Hiilayout.addWidget(nuntiumil)
        optioik=QComboBox()         
        optioik.addItem("N")
        optioik.setFont(QFont('Verdana', 10)) 
        optioik.setStyleSheet("background-color:#228B22; color:#FFFFFF")
##        optio5.currentTextChanged.connect(self.text_changed)
        Hiilayout.addWidget(optioik)
        nuntiumim=QLabel("PX_VERSION")
        nuntiumim.setFont(QFont('Verdana', 10))
        Hiilayout.addWidget(nuntiumim)
        optioin=QComboBox()         
        optioin.addItem("Y")
        optioin.setFont(QFont('Verdana', 10)) 
        optioin.setStyleSheet("background-color:#228B22; color:#FFFFFF")
        Hiilayout.addWidget(optioin)
        
        Hiiilayout = QHBoxLayout()
        nuntiumio=QLabel("CLM_VERSION")
        nuntiumio.setFont(QFont('Verdana', 10))
        Hiiilayout.addWidget(nuntiumio)
        optioip=QComboBox()         
        optioip.addItem("N")
        optioip.setFont(QFont('Verdana', 10)) 
        optioip.setStyleSheet("background-color:#228B22; color:#FFFFFF")
##        optio5.currentTextChanged.connect(self.text_changed)
        Hiiilayout.addWidget(optioip)
        nuntiumiq=QLabel("NOAH_VERSION")
        nuntiumiq.setFont(QFont('Verdana', 10))
        Hiiilayout.addWidget(nuntiumiq)
        optioir=QComboBox()         
        optioir.addItem("N")
        optioir.setFont(QFont('Verdana', 10)) 
        optioir.setStyleSheet("background-color:#228B22; color:#FFFFFF")
        Hiiilayout.addWidget(optioir)
        
        nuntiumis=QLabel("CTM_ABFLUX")
        nuntiumis.setFont(QFont('Verdana', 10))
        Hiiilayout.addWidget(nuntiumis)
        optioit=QComboBox()         
        optioit.addItem("Y")
        optioit.setFont(QFont('Verdana', 10)) 
        optioit.setStyleSheet("background-color:#228B22; color:#FFFFFF")
##        optio5.currentTextChanged.connect(self.text_changed)
        Hiiilayout.addWidget(optioit)
        nuntiumiu=QLabel("CTM_BIDI_FERT_NH3")
        nuntiumiu.setFont(QFont('Verdana', 10))
        Hiiilayout.addWidget(nuntiumiu)
        optioiv=QComboBox()         
        optioiv.addItem("T")
        optioiv.setFont(QFont('Verdana', 10)) 
        optioiv.setStyleSheet("background-color:#228B22; color:#FFFFFF")
        Hiiilayout.addWidget(optioiv)

#        Hivlayout = QHBoxLayout()
        
        layout.addLayout(Hilayout)
        layout.addLayout(Hiilayout)
        layout.addLayout(Hiiilayout)
#        layout.addLayout(Hivlayout)

        textTTT = """
                    <html>
                        <p>   </p>
                    </html>
               """
        nuntiumTTT=QLabel(textTTT)
        nuntiumTTT.setFont(QFont('Verdana', 8))
        layout.addWidget(nuntiumTTT)
        
#___ BLOCK I: Multiprocessing variables#
        textM = """
                    <html>
                        <p><b>\n Multiprocessing variables</b></p>
                    </html>
               """
        nuntiumMPI=QLabel(textM)
        nuntiumMPI.setFont(QFont('Verdana', 12))
        layout.addWidget(nuntiumMPI)
        
#___ BLOCK I: MPI distribution ___#
        HIlayout = QHBoxLayout()
        nuntiumIa=QLabel("Number of cores")
        nuntiumIa.setFont(QFont('Verdana', 14))
        HIlayout.addWidget(nuntiumIa)
        self.num_coros = self.servus.ncoros()
        nuntiumIb=QLabel(str(self.num_coros))
        nuntiumIb.setFont(QFont('Verdana', 14))
        nuntiumIb.setStyleSheet("border: 1px solid black; background-color:#555566; color:#FFFFFF")
        nuntiumIb.setAlignment(Qt.AlignCenter)
        HIlayout.addWidget(nuntiumIb)
        nuntiumIc=QLabel("Columns")
        nuntiumIc.setFont(QFont('Verdana', 14))
        HIlayout.addWidget(nuntiumIc)
        self.num_ordines = self.servus.nordines()
        nuntiumId=QLabel(str(self.num_ordines))
        nuntiumId.setFont(QFont('Verdana', 14))
        nuntiumId.setStyleSheet("border: 1px solid black; background-color:#555566; color:#FFFFFF")
        nuntiumId.setAlignment(Qt.AlignCenter)
        HIlayout.addWidget(nuntiumId)
        nuntiumIe=QLabel("Rows")
        nuntiumIe.setFont(QFont('Verdana', 14))
        HIlayout.addWidget(nuntiumIe)
        self.num_columnae = self.servus.ncolumnae()
        nuntiumIf=QLabel(str(self.num_columnae))
        nuntiumIf.setFont(QFont('Verdana', 14))
        nuntiumIf.setStyleSheet("border: 1px solid black; background-color:#555566; color:#FFFFFF")
        nuntiumIf.setAlignment(Qt.AlignCenter)
        HIlayout.addWidget(nuntiumIf)
        layout.addLayout(HIlayout)
        
#        version_line = self.find_line('VR')
#        print ("version_line ",version_line)
        
        self.setLayout(layout)
        self.layout().setAlignment(Qt.AlignTop)
        
    def find_line(self, content):
        with open(r'/home/ubuntu/CMAQ533_ncores1_12SE.sh', 'r') as fp:
    # read all lines using readline()
            lines = fp.readlines()
            for row in lines:
                if row.find(content) == 0:
                    print('string exists in file ',row)
                    print('line Number:', lines.index(line))
#                print (row)
        # check if string present on a current line
#        word = 'Line 3'
#         print(row.find(word))
        # find() method returns -1 if the value is not found,
        # if found it return 0
#        if row.find(word) == 0:
#            print('string exists in file')
#              print('line Number:', lines.index(line))
                
#                searchfile = '/home/ubuntu/CMAQ533_ncores1_12SE.sh'
#        for line in searchfile:
#            print (line)
#            if content in line: return line
#        searchfile.close()
        print ("CMAQ PROJECT ",content)
