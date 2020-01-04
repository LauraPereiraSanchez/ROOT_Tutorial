
#!/usr/bin/python                                                                                                                 
from ROOT import TFile,TCanvas,TH1F
from src.Dict import *

def canvas(name):
    mycanvas = TCanvas(name, name, 800, 800)
    return mycanvas

def histo(name, var):
    h = TH1F(name, name, VarDict[var]["bin"],VarDict[var]["beg"],VarDict[var]["end"])
    return h

    
