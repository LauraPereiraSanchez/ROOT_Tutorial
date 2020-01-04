# Remember to source /usr/local/Cellar/root/6.18.04_1/bin/thisroot.sh

#!/usr/bin/python
from ROOT import TFile,TCanvas,TH1F,TLegend
from src.RegionsDef_tN_DM import *
from src.definitions import *
#from src.Dict import *    
import os

Lumi = "139500"
Variables = ["mt"]#"jet_pt[0]","jet_pt[1]","jet_pt[2]","jet_pt[3]","lep_pt[0]","n_lep","n_jet","n_bjet","dphi_met_lep","dphi_jet0_ptmiss","dphi_jet1_ptmiss","jet_pt[0]","ht_sig"]

# Regions from RegionsDef_tN_DM.py
cut = '('+hardlepton_presel+'&&'+dm_jetpt+ '&&'+dm_sr+'&&'+dm_onebin+')'
weights = "xs_weight*sf_total*lumi_weight*weight*139500"

######### Open the different files ###########
bkgFile = TFile.Open("Files/mc16_ttZnunu.root")
sigFile = TFile.Open("Files/mc16_DM_scalar_p20_c1.root")
otherbkgFile = TFile.Open("Files/mc16_other_ttZ.root")

######## Read trees #############
bkgTree = bkgFile.Get("ttV_Nom")
sigTree = sigFile.Get("DM_scalar_p20_c1_Nom")
otherbkgTree = otherbkgFile.Get("ttV_Nom")

c = canvas("c")

for var in Variables:
    #Create histogram
    h_mc = histo("h_mc",var)
    h_sig = histo("h_sig",var)
    h_other = histo("h_other",var)

    #Draw tree branch (var) in histogram applying the necessary weights and cuts.
    bkgTree.Draw(var+">>h_mc", weights+"*("+cut+")","goff")
    sigTree.Draw(var+">>h_sig",weights+"*("+cut+")","goff")
    otherbkgTree.Draw(var+">>h_other", weights+"*("+cut+")","goff")

    # Make it pretty
    h_sig.SetStats(False)
    h_sig.SetFillColor(2)
    h_sig.SetTitle("DM vs ttZnunu")
    h_sig.GetXaxis().SetTitle(var)
    h_mc.SetFillColor(4)
    h_other.SetFillColor(7)

    legend = TLegend(0.75,0.8,0.95,0.95) #(0.1,0.8,0.35,0.9)
    legend.AddEntry(h_sig,"DM scalar m(20,1)","f")
    legend.AddEntry(h_mc,"ttZnunu","f")
    legend.AddEntry(h_other,"other ttZ","f")

    # Only for the first variable, calculate yields and S/B ratio.
    if var == Variables[0]:
        SigEv = h_sig.Integral()
        BkgEv = h_mc.Integral()
        OtherEv = h_other.Integral()
        Ratio = SigEv/BkgEv
        
        print ("S/B = "+str(Ratio))
        print ("signal events = "+str(SigEv))
        print ("ttZnunu events = "+str(BkgEv))
        print ("Other ttZ events = "+str(OtherEv))
        
    # Make canvas with 
    c.cd()
    h_sig.Draw("hist")
    h_mc.Draw("hist SAME")
    h_other.Draw("hist SAME")
    legend.Draw()

    # To stack the different backgrounds make a THStack, add the different histograms and draw the stack afterwards.

    c.SaveAs("Plots/"+var+".png")

    os.system("open Plots/"+var+".png")

    del h_sig
    del h_mc
    del h_other
