//root -l Tree_edit.C'("play.root")' 

void Tree_edit(const TString Name){

  TString path = "Ntuples/";

  TFile *f0 = TFile::Open(path+Name); //Open File
  if (!f0) std::cout << "ERROR  opening file" << std::endl;
  TTree *t0 = (TTree*)f0->Get("ttV_Nom"); //Get Tree by name
  if (!t0) std::cout << "ERROR reading  tree"  << std::endl;
  
  //If you want to copy only some branches:
  t0->SetBranchStatus("*", 0);   // Deactivate all branches                                                                                                                                                                     
  for (auto activeBranchName : {"event_number", "met", "dphi_met_lep", "mt","stxe_trigger","lep_pt","jet_pt","n_jet","n_bjet","dphi_jet0_ptmiss","dphi_jet1_ptmiss","mT2tauLooseTau_GeV","n_lep","mu_trigger","el_trigger","lumi_weight","dilep_m","el_idTight","n_mu","n_el", "ht_sig","topness","hadtop_cand_m","dphi_min_ptmiss","bjet_pt","mc_channel_number","n_dilep","mt3L","zll_met","xs_weight","n_dilep","sf_total","weight","amt2"})   // Activate only the branches you want to keep
    t0->SetBranchStatus(activeBranchName, 1);
  
  //dilep_m, zll_met
  TFile *f1 = TFile::Open("NewFiles/"+Name+".root","RECREATE"); //Create new file
  auto *t1 = t0->CloneTree();
  //  t1->SetName("tree"); //Change the tree name if you need to

  t1->Print(); //Print the new tree
  f1->Write(); //Save the new file

}
