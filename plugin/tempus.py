import datetime
from datetime import timedelta, date
import subprocess, multiprocessing
import psutil

class Tempus:
    def __init__(self):
        self.satus_dies = date.today() + timedelta(days = -7)
        self.finis_dies = date.today()
        self.satus_hora = 0
        self.finis_hora = 0
        self.interval = 21600
        self.hist_int = 60
        self.time_delta = 45
        self.vertical_points = 35
        
class Cpu:
    def __init__(self):
#        pCPU = psutil.cpu_count(logical=FALSE)
        pCPU = multiprocessing.cpu_count()
        self.cores = pCPU
        
    def ncores(self):
        return self.cores
    
