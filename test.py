from __future__ import print_function, division
import numpy as np
import mraw_reader
from matplotlib import pyplot as plt
import ciao_tools


mraw = mraw_reader.MRAW('/home/rjonnal/Share/flood_and_ao_data/paper_with_structure_800_875_nm_500_fps_C001H001S0001.mraw',
                        256,256,4000,fps=500.0,t0=0.97)

log = ciao_tools.Log('/home/rjonnal/Share/flood_and_ao_data/log')
