//root -l TreeTutorial.cxx 

void TreeTutorial(){

  TString Name = "mc16_ttZnunu.root"; //Original file name
  TString path = "Files/";

  TFile *f0 = TFile::Open(path+Name, "UPDATE"); //Open File
  if (!f0) std::cout << "ERROR  opening file" << std::endl;
  TTree *t0 = (TTree*)f0->Get("ttV_Nom"); //Get Tree by name
  if (!t0) std::cout << "ERROR reading  tree"  << std::endl;
  
  // ###############################################################################
  // If you want to copy only some branches when cloning/copying tree (opts A or B):
  // ###############################################################################
  
  std::cout << "Copying only selected branches from original file"  << std::endl;
  t0->SetBranchStatus("*", 0);   // Deactivate all branches             
  //for (auto activeBranchName : {"event_number","n_jet","n_bjet","sf_total","weight"})   // Activate only the branches you want to keep
  for (auto activeBranchName : {"event_number", "met", "dphi_met_lep", "mt", "stxe_trigger","lep_pt","jet_pt","n_jet","n_bjet","dphi_jet0_ptmiss","dphi_jet1_ptmiss","mT2tauLooseTau_GeV", "n_lep", "mu_trigger", "el_trigger", "lumi_weight", "el_idTight", "n_mu","n_el", "ht_sig","topness","hadtop_cand_m","dphi_min_ptmiss","bjet_pt","mc_channel_number","sf_total","weight", "amt2"})   // Activate only the branches you want to keep
    t0->SetBranchStatus(activeBranchName, 1);
  

  //#########################################
  // Clone and save original tree in new file:  (The new file and tree  will be used for all future steps)
  //#########################################
  //This is mandatory
  std::cout << "Creating file New_"+Name << std::endl;
  TFile *f1 = TFile::Open("Files/New_"+Name,"RECREATE"); //Create new file                                                                                                                                               
  //You must uncomment one between  A,B,C
  // A
  auto t1 = t0->CloneTree(t0->GetEntries()); // Clone the full original tree (only branches with BranchStatus = 1)
  // B
  //TTree *t1 = t0->CopyTree("n_bjet == 1"); // To get only a subset of events;
  // C
  //TTree *t1 = new TTree("t1","");  //define tree name here
  
  // ########################################################################################
  //  If you want to add a new branch (ex: n_non_bjet = n_jet-n_bjet) or you chose option C:
  //  #######################################################################################

  std::cout << "Adding new branch to tree" << std::endl;

  //First you need to find out the types of the original branches to define them properly.
  /*
  TString n_jet_type = t0->GetLeaf("n_jet")->GetTypeName();
  TString n_bjet_type =  t0->GetLeaf("n_bjet")->GetTypeName();
  std::cout << n_jet_type << std::endl;
  std::cout << n_bjet_type << std::endl;
  */

  Int_t  n_non_bjet = -99; //default value
  TBranch* newBranch = t1->Branch("n_non_bjet", &n_non_bjet); //Attention: the new branch needs too be  added to the original tree, If you add it later to the cloned tree it will not work.

  Int_t n_jet; Int_t n_bjet; //First you need to define the needed variables
  t0->SetBranchAddress("n_jet",&n_jet); //Remember to set the branch addrresses to read the trree content
  t0->SetBranchAddress("n_bjet",&n_bjet);

  //If you chose C (did not clone/copy the original tree) you can add new variables in the following way (remember to seet all the branch addresses properly beforer hand)
  //t1->Branch("n_jet",&n_jet);
  //t1->Branch("n_bjet",&n_bjet);
 
  int n_events = t0->GetEntries();
  std::cout << n_events << std::endl;

  for (int i=0;i<n_events;i++) {
    t0->GetEntry(i);
    n_non_bjet = n_jet + n_bjet;
    std::cout << "n_non_bjet = " << n_jet << " + " << n_bjet << " = " << n_non_bjet << std::endl;
    t1->Fill();
  }

  t1->SetName("tree"); //Change the tree name if you need to

  t1->Print(); //Print the new tree
  f1->Write(); //Save the new file

  f0->Close();
  //exit(1); //Use this to exit root inteface when the program finishes.
}
