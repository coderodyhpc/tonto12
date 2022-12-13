# Gv3GEWRF 
# Copyright (c) Odycloud.

from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap, QFont

from Gv3GEWRF.plugin.ui.S3.widget_S3I import S3_controller

class S3Tab(QWidget):
    """Class for creating the Home tab"""
    def __init__(self, iface, ancilla) -> None:
        super().__init__()
        layout = QGridLayout()
        add_S3 = S3_controller(iface)
        layout.addWidget(add_S3)
        self.setLayout(layout)
        self.layout().setAlignment(Qt.AlignTop)
        
        
