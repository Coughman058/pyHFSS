#%%
import sys;  IMP_PATH = r'D:\\HFSS\\pyHFSS';
if ~(IMP_PATH in sys.path): sys.path.append(IMP_PATH);
    
import hfss;   #import bbqNumericalDiagonalization; 
import pandas as pd
from hfss import CalcObject, ureg
from hfss import load_HFSS_project
import bbq, matplotlib.pyplot as plt, numpy as np
from bbq import print_color, divide_diagonal_by_2, print_matrix
from IPython.display import display # test change


proj_name    = r'3DTransmons' 
project_path = 'D:\\HFSSpyHFSS_Examples\\'
app, desktop, project = load_HFSS_project(proj_name, project_path)
design       = project.get_active_design()

bbq_exp = bbq.Bbq(project, design, append_analysis=False, calculate_H=True)

bbq_exp.do_eBBQ(calculate_H = True,  plot_fig = True, LJvariablename="$LJ")
bbq_exp.bbq_analysis.plot_Hparams("_$LJ")