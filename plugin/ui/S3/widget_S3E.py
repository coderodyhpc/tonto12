from pathlib import Path
import os
import subprocess
import boto3
import logging
from os.path import exists
from botocore.exceptions import ClientError
# Let's use Amazon S3
s3 = boto3.client('s3')

from PyQt5.QtCore import (Qt)
from PyQt5.QtWidgets import (QWidget, QListWidget, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QComboBox, QErrorMessage, QInputDialog)
from PyQt5.QtGui import (QFont)
from Gv3GEWRF.plugin.options import get_options

class CheckPass():
    def checking(filename):
        path = Path(filename)
        if path.is_file():
            return True
        else:
            return False

#####--------------------------------------------------------------------------------------------#####
class Aws_credentials(QWidget):
    def __init__(self, parent, terris):           
        super().__init__(parent)
        self.switch_credentials = False

        layout = QVBoxLayout()

#        nuntiumI = "Click here to use the instance current credentials"
#        self.nuntisI=QPushButton(nuntiumI)                    
#        self.nuntisI.setFont(QFont('Verdana', 14))
##        self.nuntisI.clicked.connect(self.input_credentials)
#        layout.addWidget(self.nuntisI)

        nuntiumII = "Click here to enter credentials"
        self.nuntisII=QPushButton(nuntiumII)                    
        self.nuntisII.setFont(QFont('Verdana', 14))
        self.nuntisII.clicked.connect(self.input_credentials)
        layout.addWidget(self.nuntisII)

        self.cred1 = 'YYYYYYYYYYYYYYYYYYYY'
        self.cred2 = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
        self.cred3 = 'us-east-1'

        self.arca1 = QHBoxLayout()
        nuntiumC = QLabel("     AWS Access Key ID                                                ")
        nuntiumC.setFont(QFont('Verdana', 12))
        self.arca1.addWidget(nuntiumC)
        self.scriptumC = self.cred1
        self.valorem = QLineEdit(self.scriptumC)
        self.valorem.setAlignment(Qt.AlignRight) 
        self.valorem.setFont(QFont('Verdana', 12))
        self.arca1.addWidget(self.valorem)
        self.valorem.textChanged[str].connect(self.DCtext_changed)
        layout.addLayout(self.arca1)

        self.arca2 = QHBoxLayout()
        nuntiumD = QLabel("     AWS Secret Access Key                    ")
        nuntiumD.setFont(QFont('Verdana', 12))
        self.arca2.addWidget(nuntiumD)
        self.scriptumD = self.cred2
        self.valorem2 = QLineEdit(self.scriptumD)
        self.valorem2.setAlignment(Qt.AlignRight) 
        self.valorem2.setFont(QFont('Verdana', 12))
        self.arca2.addWidget(self.valorem2)
        self.valorem2.textChanged[str].connect(self.DC2text_changed)
        layout.addLayout(self.arca2)

#        self.arca3 = QHBoxLayout()
#        nuntiumR = QLabel("     Region                                                              ")
#        nuntiumR.setFont(QFont('Verdana', 14))
#        self.arca3.addWidget(nuntiumR)
#        self.region = QComboBox()
##        self.region.addItems(["us-east-1","us-east-2","us-west-1","us-west-2","eu-central-1","eu-west-1","eu-west-2",       \
##                              "eu-south-1","eu-west-3","eu-north-1","me-south-1","me-central-1","sa-east-1","ca-central-1", \
##                              "ap-southeast-3","ap-south-1","ap-northeast-3","ap-northeast-2","ap-southeast-1",             \
##                              "ap-southeast-2","ap-northeast-1","af-south-1","ap-east-1"])
#        self.region.addItems(terris)
#        self.region.setFont(QFont('Verdana', 12))
#        self.region.currentTextChanged.connect(self.Area_changed)
#        self.arca3.addWidget(self.region)
#        layout.addLayout(self.arca3)
        
        self.ahaha = QPushButton("Save credentials")                    
        self.ahaha.setFont(QFont('Verdana', 14))
        self.ahaha.clicked.connect(self.save_credentials)
        layout.addWidget(self.ahaha)

#        spatium = QLabel("\n")
#        spatium.setFont(QFont('Verdana', 12))
#        layout.addWidget(spatium)

        self.setLayout(layout)
        self.credentials_toggling()
        
    def input_credentials(self):
        print ("Insert credentials ",self.switch_credentials)
        self.switch_credentials = True
        self.credentials_toggling()

    def save_credentials(self):
        print ("Save credentials ",self.switch_credentials, self.cred1, self.cred2, self.cred3)
        nuntiumLI = "aws_access_key_id = "+self.cred1+"\n"
        nuntiumLII = "aws_secret_access_key = "+self.cred2+"\n"
        nuntiumLIII = "region = "+self.cred3+"\n"
        with open('/home/ubuntu/.aws/credentials', 'w') as outfile:
            f.write("[default]")
            f.write(nuntiumLI)                  
            f.write(nuntiumLII)                  
        with open('/home/ubuntu/.aws/config', 'w') as outfile:
            f.write("[default]")
            f.write(nuntiumLIII)                  

    def DCtext_changed(self):
        print ("DCtext_changed ",self.valorem.text(),self.cred1)
        self.cred1 = self.valorem.text() 
    def DC2text_changed(self):
        print ("DCtext_changed ",self.valorem2.text(),self.cred1)
        self.cred2 = self.valorem2.text() 
#    def Area_changed(self):
#        print ("Region_changed ",self.region.currentText(),self.cred3)
#        self.cred3 = self.region.currentText() 
        
    def credentials_toggling(self):
        print ("I'm at credentials toggling ",self.cred1,self.cred2)
        if (self.switch_credentials == True):
            print ("Input credentials is true")
#            self.scriptumC.setDisabled(False)
#            self.scriptumC.setStyleSheet("background-color:black; color:white");
            self.valorem.setDisabled(False)
            self.valorem.setStyleSheet("background-color:black; color:white");
            self.valorem2.setDisabled(False)
            self.valorem2.setStyleSheet("background-color:black; color:white");
#            self.cred3.setDisabled(False)
#            self.cred3.setStyleSheet("background-color:black; color:white");
#            self.region.setDisabled(False)
#            self.region.setStyleSheet("background-color:black; color:white");
            self.ahaha.setDisabled(False)
            self.ahaha.setStyleSheet("background-color:black; color:white");
        else:
            print ("Input credentials is false")
#            self.scriptumC.setDisabled(True)
#            self.scriptumC.setStyleSheet("background-color:#444444; color:white");
            self.valorem.setDisabled(True)
            self.valorem.setStyleSheet("background-color:#444444; color:white");
            self.valorem2.setDisabled(True)
            self.valorem2.setStyleSheet("background-color:#444444; color:white");
#            self.cred3.setDisabled(True)
#            self.cred3.setStyleSheet("background-color:#444444; color:white");
#            self.region.setDisabled(True)
#            self.region.setStyleSheet("background-color:#444444; color:white");
            self.ahaha.setDisabled(True)
            self.ahaha.setStyleSheet("background-color:#444444; color:white");

       
#####--------------------------------------------------------------------------------------------#####
###class S3_bucket_creation(QWidget):
###    def __init__(self, parent):           # nuntium and spatium are used to hold the Label and Combo content
###        super().__init__(parent)
###        layout = QHBoxLayout()
###        hamam = "Create S3 bucket"
###        self.hama=QPushButton(hamam)                    
###        self.hama.setFont(QFont('Verdana', 14))
###        layout.addWidget(self.hama)
###        self.hama.clicked.connect(self.bucket_creation)
###        self.setLayout(layout)
        
###    def bucket_creation(self):         # I cannot include other variables so 'region' & 'bucket_name' must be predetermined
###        self.region = S3_controller.chorda_meus('/home/ubuntu/.aws/config')
###        try:
###            if self.region is None:
####                print ('Region by default ',bucket_name)
####                s3_client = boto3.client('s3')
####                s3_client.create_bucket(Bucket=bucket_name)
###                s3.create_bucket(Bucket='wrf_bucket')
###            else:
####                s3_client = boto3.client('s3', region_name=region)
####                location = {'LocationConstraint': region}
####                s3_client.create_bucket(Bucket=bucket_name,
####                                    CreateBucketConfiguration=location)
###                self.nomen = QInputDialog.getText(self, 'Input_Dialog', 'Enter bucket name:')
###                self.bucket_name = self.nomen[0]
###                s3X = boto3.resource('s3')
###                location = {'LocationConstraint': self.region}
###                if (self.region[0] == 'u' and self.region[1] == 's' and self.region[3] == 'e' and self.region[8] == '1'):
####                    print ("useast1")
###                    s3X.create_bucket(Bucket=self.bucket_name)
###                else:
####                    print ("NONuseast1")
###                    s3X.create_bucket(Bucket=self.bucket_name
###                                        ,CreateBucketConfiguration=location)
###                S3_controller.S3_toggling(self)
###        except ClientError as e:
###            logging.error(e)
###            return False
###        return True

#####--------------------------------------------------------------------------------------------#####
class Aws_transfer(QWidget):
    def __init__(self, parent, situla_regio, situla_nomen):           # nuntium and spatium are used to hold the Label and Combo content
        super().__init__(parent)
        self.situla_nomen = situla_nomen
        self.situla_regio = situla_regio
        print ("SITULA ", situla_nomen, situla_regio)
        layout = QVBoxLayout()
#___ Block 4A: S3 transfer namelist/wps files ___#
        Hlayout = QHBoxLayout()
        nuntiumI = 'Transfer namelist.wps to S3 bucket'
        self.nuntisI=QPushButton(nuntiumI)                    
        self.nuntisI.setFont(QFont('Verdana', 12))
        self.nuntisI.setStyleSheet("background-color:#B0C4DE; color:black")
        self.nuntisI.clicked.connect(self.transfer_wps)
        Hlayout.addWidget(self.nuntisI)
        RnuntiumI = 'Transfer namelist.wps files from S3 bucket'
        self.RnuntisI=QPushButton(RnuntiumI)                    
        self.RnuntisI.setFont(QFont('Verdana', 12))
        self.RnuntisI.setStyleSheet("background-color:#99AABB; color:black")
        self.RnuntisI.clicked.connect(self.from_wps)
        Hlayout.addWidget(self.RnuntisI)
        layout.addLayout(Hlayout)
#___ Block 4AA: S3 transfer namelist/wps files ___#
        HAAlayout = QHBoxLayout()
        nuntiumIAA = 'Transfer met files to S3 bucket'
        self.nuntisIAA=QPushButton(nuntiumIAA)                    
        self.nuntisIAA.setFont(QFont('Verdana', 12))
        self.nuntisIAA.setStyleSheet("background-color:#B0C4DE; color:black")
        self.nuntisIAA.clicked.connect(self.transfer_met)
        HAAlayout.addWidget(self.nuntisIAA)
        RnuntiumIAA = "Transfer met files from S3 bucket"
        self.RnuntisIAA=QPushButton(RnuntiumIAA)                    
        self.RnuntisIAA.setFont(QFont('Verdana', 12))
        self.RnuntisIAA.setStyleSheet("background-color:#99AABB; color:black")
        self.RnuntisIAA.clicked.connect(self.from_met)
        HAAlayout.addWidget(self.RnuntisIAA)
        layout.addLayout(HAAlayout)
#___ Block 4B: S3 transfer namelist input files ___#
        H4Blayout = QHBoxLayout()
        nuntiumII = 'Transfer namelist.input to S3 bucket'
        self.nuntisII=QPushButton(nuntiumII)                    
        self.nuntisII.setFont(QFont('Verdana', 12))
        self.nuntisII.setStyleSheet("background-color:#B0C4DE; color:black")
        H4Blayout.addWidget(self.nuntisII)
        RnuntiumII = "Transfer namelist.input from S3 bucket"
        self.RnuntisII=QPushButton(RnuntiumII)                    
        self.RnuntisII.setFont(QFont('Verdana', 12))
        self.RnuntisII.setStyleSheet("background-color:#99AABB; color:black")
        H4Blayout.addWidget(self.RnuntisII)
        layout.addLayout(H4Blayout)
#___ Block 4C: S3 transfer namelist/wps files ___#
        H4Clayout = QHBoxLayout()
        nuntiumIII = 'Transfer boundary/initial condition files to S3 bucket'
        self.nuntisIII=QPushButton(nuntiumIII)                    
        self.nuntisIII.setFont(QFont('Verdana', 10))
        self.nuntisIII.setStyleSheet("background-color:#B0C4DE; color:black")
        H4Clayout.addWidget(self.nuntisIII)
        RnuntiumIII = 'Transfer boundary/initial condition files from S3 bucket'
        self.RnuntisIII=QPushButton(RnuntiumIII)                    
        self.RnuntisIII.setFont(QFont('Verdana', 10))
        self.RnuntisIII.setStyleSheet("background-color:#99AABB; color:black")
        H4Clayout.addWidget(self.RnuntisIII)
        layout.addLayout(H4Clayout)
#___ Block 4D: S3 transfer namelist/wps files ___#
        H4Dlayout = QHBoxLayout()
        nuntiumIV = 'Transfer result files to S3 bucket'
        self.nuntisIV=QPushButton(nuntiumIV)                    
        self.nuntisIV.setFont(QFont('Verdana', 12))
        self.nuntisIV.setStyleSheet("background-color:#B0C4DE; color:black")
        H4Dlayout.addWidget(self.nuntisIV)
        RnuntiumIV = "Transfer result files from S3 bucket"
        self.RnuntisIV=QPushButton(RnuntiumIV)                    
        self.RnuntisIV.setFont(QFont('Verdana', 12))
        self.RnuntisIV.setStyleSheet("background-color:#99AABB; color:black")
        H4Dlayout.addWidget(self.RnuntisIV)
        layout.addLayout(H4Dlayout)
        self.setLayout(layout)

    def transfer_wps(self):         # I cannot include other variables so 'region' & 'bucket_name' must be predetermined
#        self.situla_nomen = S3_controller.bucket_return()
        print ("TRANSFER WPS ",self.situla_nomen)
        copyS3 = boto3.client("s3")
        copyS3.upload_file("/home/ubuntu/PREPRO/WPS/namelist.wps", self.situla_nomen(), "namelist.wps")
#        s3.upload_file('/home/ubuntu/PREPRO/WPS/namelist.wps', "wrf-bucket", "path/to/key.txt")
#        s3.upload_file('/home/ubuntu/PREPRO/WPS/namelist.wps', "wrf-bucket")
    def from_wps(self):         # I cannot include other variables so 'region' & 'bucket_name' must be predetermined
        print ("FROM WPS ")
#        s3.upload_file('/home/ubuntu/PREPRO/WPS/namelist.wps', "wrf-bucket", "path/to/key.txt")
#        s3.upload_file('/home/ubuntu/PREPRO/WPS/namelist.wps', "wrf-bucket")
    def transfer_met(self):         # I cannot include other variables so 'region' & 'bucket_name' must be predetermined
        print ("TRANSFER MET ")
#        s3.upload_file('/home/ubuntu/PREPRO/WPS/namelist.wps', "wrf-bucket", "path/to/key.txt")
#        s3.upload_file('/home/ubuntu/PREPRO/WPS/namelist.wps', "wrf-bucket")
    def from_met(self):         # I cannot include other variables so 'region' & 'bucket_name' must be predetermined
        print ("FROM MET ")
#        s3.upload_file('/home/ubuntu/PREPRO/WPS/namelist.wps', "wrf-bucket", "path/to/key.txt")
#        s3.upload_file('/home/ubuntu/PREPRO/WPS/namelist.wps', "wrf-bucket")

#####--------------------------------------------------------------------------------------------#####
#####--------------------------------------------------------------------------------------------#####
#####--------------------------------------------------------------------------------------------#####
class S3_controller(QWidget):
    def __init__(self, iface) -> None:
#    def __init__(self, iface, ancilla) -> None:
        super().__init__()

        self.iface = iface
        self.options = get_options()
        self.regio = 'us-east-1'
        self.terris = ["us-east-1","us-east-2","us-west-1","us-west-2","eu-central-1","eu-west-1","eu-west-2",       \
                              "eu-south-1","eu-west-3","eu-north-1","me-south-1","me-central-1","sa-east-1","ca-central-1", \
                              "ap-southeast-3","ap-south-1","ap-northeast-3","ap-northeast-2","ap-southeast-1",             \
                              "ap-southeast-2","ap-northeast-1","af-south-1","ap-east-1"]
        self.bucket = None

#___ These lines are to set up the layout ___#
        layout = QVBoxLayout()

#___ Block 0: Paragraph with some information ___#
        text = """
                    <html>
                        <p><b>S3 INTERFACE</b></p>
                        <p>  The system must have your credentialsto list and transfer files from your S3 buckets. 
                        You can enter them either manually or using the option below. As required by AWS, the keys 
                        must be kept always secured.
                        Once the credentials are available, the interface will unlock the buttons for performing 
                        different tasks with S3.  
                        </p>
                    </html>
               """

        label_text = QLabel(text)
        label_text.setWordWrap(True)
#        label_text.setOpenExternalLinks(True)
        label_text.setFont(QFont('Verdana', 12))
        layout.addWidget(label_text)

        text3 = """
                    <html>
                        NOTE: The current available regions for the S3 interface are us-east-1, us-east-2, us-west-1,
                        us-west-2, eu-central-1, eu-west-1, eu-west-2, eu-south-1, eu-west-3, eu-north-1, me-south-1,
                        me-central-1, sa-east-1, ca-central-1, ap-southeast-3, ap-south-1, ap-northeast-3,
                        ap-northeast-2, ap-southeast-1, ap-southeast-2, ap-northeast-1, af-south-1 and ap-east-1.
                        Contact us (support@odyhpc.com) if you need to use a different region.\n  
                        </p>
                    </html>
               """
        label_text3 = QLabel(text3)
        label_text3.setWordWrap(True)
        label_text3.setFont(QFont('Verdana', 10))
        layout.addWidget(label_text3)
        
#___ Block 1: CREDENTIALS TEXT ___#
        block5 = QHBoxLayout()
        self.block1 = "            "
        self.BL1=QLabel(self.block1)                    
        self.BL1.setFont(QFont('Verdana', 14))
        self.BL1.setStyleSheet("font-weight: bold")
        block5.addWidget(self.BL1)
        self.BL2=QLabel(self.block1)                    
        self.BL2.setFont(QFont('Verdana', 14))
        self.BL2.setStyleSheet("font-weight: bold")
        block5.addWidget(self.BL2)
        self.documentum = "CREDENTIALS"
        self.documentorum=QLabel(self.documentum)                    
        self.documentorum.setFont(QFont('Verdana', 14))
        self.documentorum.setStyleSheet("font-weight: bold; border: 3px solid black;")
#        self.documentorum.setStyleSheet("border: 3px solid black;")
        self.documentorum.setAlignment(Qt.AlignCenter)
#        self.nuntisI.clicked.connect(self.input_credentials)
        block5.addWidget(self.documentorum)
        self.BL3=QLabel(self.block1)                    
        self.BL3.setFont(QFont('Verdana', 14))
        self.BL3.setStyleSheet("font-weight: bold")
        block5.addWidget(self.BL3)
        self.BL4=QLabel(self.block1)                    
        self.BL4.setFont(QFont('Verdana', 14))
        self.BL4.setStyleSheet("font-weight: bold")
        block5.addWidget(self.BL4)
        layout.addLayout(block5)
        
#___ Block 2: REGION - This should only be a ___#
        file_check00 = '/home/ubuntu/.aws/config'
        check00 = CheckPass.checking(file_check00)
        if (check00 == True):
            self.regio = S3_controller.chorda_meus(file_check00)
            print ("check00 ",self.regio)
        self.widget0 = QHBoxLayout()
        nuntiumR = QLabel("     REGION                 ")
        nuntiumR.setFont(QFont('Verdana', 12))
        self.widget0.addWidget(nuntiumR)
        self.selection = QComboBox()
        self.selection.addItems(self.terris)
        self.selection.setFont(QFont('Verdana', 12))
        aaa = S3_controller.autonomia(self)
        print ("AAA ",aaa)
        self.selection.setCurrentText(aaa)
        self.selection.currentTextChanged.connect(self.Area_changed)
        self.widget0.addWidget(self.selection)
        nuntiumR0 = QLabel("                                               ")
        nuntiumR0.setFont(QFont('Verdana', 12))
        self.widget0.addWidget(nuntiumR0)
        self.widget0.addWidget(nuntiumR0)
        self.widget0.addWidget(nuntiumR0)
        layout.addLayout(self.widget0)

#___ Block 3: Set credentials ___#
#        self.widget1 = Aws_credentials()
        self.widget1 = Aws_credentials(self, self.terris)
        layout.addWidget(self.widget1)

#___ Block 4: Create S3 bucket ___#
# New procedure
#        self.widget3 = S3_bucket_creation(self, self.regio)
#        self.widget3 = QHBoxLayout()
        hamam = "Create S3 bucket"
        self.widget3=QPushButton(hamam)                    
        self.widget3.setFont(QFont('Verdana', 14))
        self.widget3.clicked.connect(self.bucket_creation)
#        self.setLayout(layout)
        layout.addWidget(self.widget3)

#___ Block 5: Selection of bucket ___#
#        self.widget2 = S3_listing(self)
#        self.widget2.setFont(QFont('Verdana', 14))
#        layout.addWidget(self.widget2,2,0)
        self.widget2 = QHBoxLayout()
        wid2_nuntium = "     Choose S3 bucket"
        self.nuntis = QLabel(wid2_nuntium)                    
        self.nuntis.setFont(QFont('Verdana', 14))
        self.widget2.addWidget(self.nuntis)
        self.situla = QComboBox()
        self.situla.currentTextChanged.connect(self.bucket_changed)
#        self.bucket = self.situla.currentText()
        self.widget2.addWidget(self.situla)
        layout.addLayout(self.widget2)
  
#___ Block 6: S3 transfer ___#
        self.widget4 = Aws_transfer(self, self.regio, self.bucket)
        layout.addWidget(self.widget4)

        self.setLayout(layout)
#        self.layout().setAlignment(Qt.AlignTop) !This might not work with QVBoxLayout
        self.S3_toggling()
    
    def bucket_changed(self, s):
        self.bucket = s
        print ("Current bucket ",self.bucket)
        
    def bucket_return():
        print ("Calling bucket_return")
        aaa = S3_controller.bucket
        return aaa
                
    def S3_toggling(self):
        file_check01 = '/home/ubuntu/.aws/config'
        check1 = CheckPass.checking(file_check01)
        file_check02 = '/home/ubuntu/.aws/credentials'
        check2 = CheckPass.checking(file_check02)
        if (check1 == True and check2 == True):
            self.documentorum.setDisabled(False)
#            self.documentorum.setStyleSheet("background-color:#99FF33; color:black");
            self.documentorum.setStyleSheet("background-color:white; color:black");
            self.widget3.setDisabled(False)
            self.widget3.setStyleSheet("background-color:#fafad2; color:black");
            self.widget4.setDisabled(False)
            self.widget4.setStyleSheet("background-color:#99FF33; color:black");
            self.situla.setDisabled(False)
            self.situla.setStyleSheet("background-color:#99FF33; color:black");
#            with open(file_check01) as f:
#                self.chorda = f.readlines()[1]
            chorda_nomen = S3_controller.chorda_meus(file_check01)  
#            print ("CHORDA_NOMEN ",chorda_nomen)
#            # Check if chorda_nomen matches any of the regions at self.terris
#            for i in self.terris:
#                print ("CHECKING REGIONS ",i)
#                if i==chorda_nomen:
#                    print ("Matching region ")
#                    self.regio = chorda_nomen
#                else:
#                    error_dialog = QErrorMessage()
#                    error_dialog.setFont(QFont('Verdana', 14))
#                    error_dialog.showMessage('Region is not among those accepted')
            self.regio = chorda_nomen 
            response = s3.list_buckets()
#            print ("I'm at S3 toggling ",self.regio,self.chorda,self.chorda_meus,self.chorda_meus())
      
        if (check1 == True and check2 == True and response):
            self.situla.setDisabled(False)
            for bucket in response['Buckets']:
#                print(f'    {bucket["Name"]}')
#                stultus = bucket["Name"]
#                print (stultus)
                self.situla.addItem(bucket["Name"])
#            for bucket in s3.buckets.all():
#                self.situla.addItems(bucket.name)
            self.situla.setStyleSheet("background-color:#99FF33; color:black");
#            print ("THEY ARE TRUE ",self.situla)
#            if (self.situla == None):
#              print ("SITULA is empty ")
            print ("I'm at S3-1B toggling ",self.regio)
            
        else:
            self.documentorum.setDisabled(True)
            self.documentorum.setStyleSheet("background-color:#440000; color:white");
            self.widget3.setDisabled(True)
            self.widget3.setStyleSheet("background-color:#440000; color:white");
            self.widget4.setDisabled(True)
            self.widget4.setStyleSheet("background-color:#440000; color:white");
            self.situla.setDisabled(True)
            self.situla.setStyleSheet("background-color:#440000; color:white");
            print ("I'm at S3-2 toggling ",self.regio)
        
    def chorda_meus(filenameII):
#        print ("AT CHORDA MEUS ",filenameII)
        with open(filenameII) as f:
            chorda = f.readlines()[1]
        return chorda.partition("region = ")[2]
      
    def Area_changed(self):
        print ("Region_changed ",self.selection.currentText())
        self.regio = self.selection.currentText() 
        
    def autonomia(self):
        return self.regio

    def bucket_creation(self):         # I cannot include other variables so 'region' & 'bucket_name' must be predetermined
#        self.region = S3_controller.chorda_meus('/home/ubuntu/.aws/config')
#        try:
#            if self.region is None:
##                print ('Region by default ',bucket_name)
##                s3_client = boto3.client('s3')
##                s3_client.create_bucket(Bucket=bucket_name)
#                s3.create_bucket(Bucket='wrf_bucket')
#            else:
##                s3_client = boto3.client('s3', region_name=region)
##                location = {'LocationConstraint': region}
##                s3_client.create_bucket(Bucket=bucket_name,
##                                    CreateBucketConfiguration=location)
                self.nomen = QInputDialog.getText(self, 'Input_Dialog', 'Enter bucket name:')
                self.bucket_name = self.nomen[0]
                print ("NOMEN ",self.nomen,self.bucket_name)
                s3X = boto3.resource('s3')
                location = {'LocationConstraint': self.regio}
#$                if (self.regio[0] == 'u' and self.regio[1] == 's' and self.regio[3] == 'e' and self.regio[8] == '1'):
#                    print ("useast1")
                s3X.create_bucket(Bucket=self.bucket_name)
#$                else:
#$#                    print ("NONuseast1")
#$                    s3X.create_bucket(Bucket=self.bucket_name
#$                                        ,CreateBucketConfiguration=location)
                self.bucket = self.bucket_name
                print ("New bucket name ",self.bucket)
#                S3_controller.S3_toggling(self)
#        except ClientError as e:
#            logging.error(e)
#            return False
#        return True
        
