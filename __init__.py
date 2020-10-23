from __future__ import print_function, division
import numpy as np
import mraw_reader
from matplotlib import pyplot as plt
import os,sys,glob

class Log:

    def __init__(self,log_directory):
        self.logdir = log_directory
        self.flist = glob.glob(os.path.join(self.logdir,'*.txt'))
        self.flist.sort()
        self.kinds = []
        for f in self.flist:
            g = os.path.split(f)[1]

    def fn_time(self,fn):
        """Given a CIAO log file, return the time in the filename."""
        return float(os.path.split(fn)[1].split('_')[-1].replace('.txt',''))
