from jupyterthemes import jtplot
from IPython import display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def setup_theme(theme='monokai'):
    jtplot.style(theme=theme)
    # set "context" (paper, notebook, talk, poster)
    jtplot.style(context='talk', fscale=1.4, spines=True, gridlines='--')
    jtplot.style(ticks=True, grid=True, figsize=(6, 4.5))
    
def reset_theme():
    jtplot.reset()


# from ipywidgets import interact
# import ipywidgets as widgets
# def f(x):
#     return x**2
# # Generate a slider 
# interact(f, x=10,);