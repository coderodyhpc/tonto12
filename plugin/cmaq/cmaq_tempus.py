import datetime
from datetime import timedelta, date
import subprocess, multiprocessing

class CTempus:
    def __init__(self):
        self.satus_dies = date.today() + timedelta (days = -1)
        self.finis_dies = date.today()
        self.horas = 24
        self.minuta = 0
        self.secundo = 0
        self.hist_int = 1
        
class CCpu:
    def __init__(self):
        pCPU = multiprocessing.cpu_count()
        self.coros = pCPU
        if self.coros == 1:
            self.ordines = 1
            self.columnae = 1
        elif self.coros == 2:
            self.ordines = 2
            self.columnae = 1
        elif self.coros == 4:
            self.ordines = 2
            self.columnae = 2
        elif self.coros == 8:
            self.ordines = 4
            self.columnae = 2
        elif self.coros == 16:
            self.ordines = 4
            self.columnae = 4
        elif self.coros == 32:
            self.ordines = 8
            self.columnae = 4
        elif self.coros == 48:
            self.ordines = 8
            self.columnae = 6
        elif self.coros == 64:
            self.ordines = 8
            self.columnae = 8
    
    def ncoros(self):
        return self.coros

    def nordines(self):
        return self.ordines

    def ncolumnae(self):
        return self.columnae
    
