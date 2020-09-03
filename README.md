# Tutorial_ROOT

This repository contains different example files to master ROOT.

### Setup

git clone ssh://git@gitlab.cern.ch:7999/lapereir/Tutorial_ROOT.git

cd Tutorial_ROOT

mkdir Files; cd Files; cp /afs/cern.ch/user/l/lapereir/public/TutorialNuples/* .

### Make plots:
```
python PlotTutorial.py
```
### Read and modifiy trees:
```
root -l TreeTutorial.cxx
```
### Further information

You can read a root file as:
```
root -l Files/mc16_ttZnunu.root
```
This will initiate a root session. To see the file content write:
```
.ls 
```
You should see that the file contains a tree called ttV_Nom. To see the variables (branches) inside the tree type:
```
ttV_Nom->Print()
```
You can draw a histogram of a selected variable (e.g. n_bjets) by typing:
```
ttV_Nom->Draw("n_bjets")
```
If you prefer to see the event by event values for a variable type:
```
ttV_Nom->Scan("n_bjets")
```
NOTE: The plot tutorial is written in python and the tree tutorial in cpp, but the other language could have also been used instead.