#-------------------------------
# REGIONS DEFINITIONS
#-------------------------------                                                                                                                                                                                    
hardlepton_presel = "stxe_trigger==1 && lep_pt[0]>25e3 && n_jet>3 && jet_pt[0]>25e3 && jet_pt[1]>25e3 && jet_pt[2]>25e3 && jet_pt[3]>25e3 && met>230e3 && dphi_jet0_ptmiss>0.4 && dphi_jet1_ptmiss>0.4 && mt>30e3 && (mT2tauLooseTau_GeV>80||mT2tauLooseTau_GeV<0)  && n_lep ==1"
ttV_basic = "(mu_trigger||el_trigger) && (n_jet>=4) && (n_lep==3) && (dilep_m>81e3&&dilep_m<101e3) && (n_mu==3||Sum$(el_idTight)>0) && (lep_pt[0]>25e3)&&(lep_pt[1]>15e3)&&(lep_pt[2]>15e3)"
#ttV_basic = "(mu_trigger||el_trigger) && (n_jet>=4) && (n_lep==4) && (dilep_m>60e3&&dilep_m<130e3)"
tn_med_jetpt = "jet_pt[0]>100.0e3 && jet_pt[1]>90.0e3 && jet_pt[2]>70.0e3 && jet_pt[3]>50.0e3"
tn_high_jetpt = " jet_pt[0]>120.0e3 && jet_pt[2]>50.0e3 && jet_pt[3]>25.0e3"
dm_jetpt = " (jet_pt[0]>80000) && (jet_pt[1]>60000) && (jet_pt[2]>30000) && (jet_pt[3]>25000)"

#-------------                                                                                                   
# DM
#-------------                                                                                                                                                                                                      
dm_sr = "n_bjet >=2 && (mt>180000) && (ht_sig>15) && (topness>8) && (hadtop_cand_m[0]>150000) && dphi_min_ptmiss>0.9 && (bjet_pt[0]>80000)"
dm_onebin = "dphi_met_lep>1.1"
dm_1 = "dphi_met_lep>1.1 && dphi_met_lep<1.5"
dm_2 = "dphi_met_lep>1.5 && dphi_met_lep<2.0"
dm_3 = "dphi_met_lep>2.0 && dphi_met_lep<2.5"
dm_4 = "dphi_met_lep>2.5"

dm_t2l = "mt>180.0e3 && n_bjet>=2 && topness<8.0 && dphi_met_lep>1.1 && bjet_pt[0]>80000 && dphi_min_ptmiss>0.6"
dm_t2lcr  = "ht_sig>13 && (n_hadtop_cand==0 || Alt$(hadtop_cand_m[0],0)<150000)"
dm_t2lvr = "ht_sig>15 && (hadtop_cand_m[0]>150000)"
dm_ttzcr = "(zll_met > 230e3) && n_bjet>=2 && (bjet_pt[0]>80000)" 
dm_ttzvr = "n_bjet>=2 && (bjet_pt[0]>80000) && (zll_met > 230e3)" 
dm_dbcr = " n_bjet==0"

#----------- 
# tN_med
#-----------

tn_sr = "ht_sig>16.0 && mt>220.0e3 && met_perp>400.0e3 && n_bjet>0.5 && topness>9.0 && dr_bjet_lep<2.8 && hadtop_cand_m[0]>150e3"
tn1 = "met<400e3"
tn2 = "met>400e3 && met<500e3"
tn3 = "met>500e3 && met<600e3 && mt<380e3"
tn4 = "met>500e3 && met<600e3 && mt>380e3"
tn5 = "met>600e3 && mt<380e3"
tn6 = "met>600e3 && mt>380e3"

tn_med_t1lvr = "ht_sig>10.0 && mt>90.0e3 && mt<120e3 && met_perp>350.0e3 && n_bjet>0.5 && topness<9.0 && hadtop_cand_m[0]>150e3"
tn_med_t2lvr = "ht_sig>10.0 && mt>120.0e3 && met_perp>300.0e3 && n_bjet>0.5 && topness<9.0 && hadtop_cand_m[0]>150e3"
tn_med_wvr = "ht_sig>10.0 && mt>30.0e3 && mt<90e3 && met_perp>300.0e3 && n_bjet>0.5 && topness>9.0 && hadtop_cand_m[0]>150e3 && deltaRbb_orderpt<1.4 && lep_charge[0]==1"

tn_med_t1lcr = "mt>30.0e3 && mt<90e3 && met_perp>350.0e3 && n_bjet>0.5 && topness < 9.0 && Alt$(hadtop_cand_m[0],0)>150e3 && ht_sig>10.0"
tn_med_t2lcr = "mt>120.0e3 && met_perp>300.0e3 && n_bjet>0.5 && topness<9.0 && Alt$(hadtop_cand_m[0], 0)< 150e3 && ht_sig>10.0"
tn_med_wcr   = "mt>30.0e3 && mt< 90e3 && met_perp>300.0e3 && n_bjet>0.5 && topness>9.0 && Alt$(hadtop_cand_m[0], 0) < 150e3 && deltaRbb_orderpt<1.4 && lep_charge[0]==1 && ht_sig>10.0"
tn_med_stcr  = "mt>30.0e3 && mt<120e3 && met_perp>350.0e3 && n_bjet>1.5 && topness>10.0 && Alt$(hadtop_cand_m[0], 0) < 150e3 && deltaRbb_orderpt>1.4 && ht_sig>10.0"
tn_ttzcr = "zll_met>230e3 && n_bjet>=1"
tn_ttzvr = "n_bjet>=1 && zll_met>230e3" 
tn_dbcr = "n_bjet==0"

#----------- 
# tN_high 
#---------- 

tn_high_sr = "topness>8.0 && met>520.0e3 && mt>380.0e3 && ht_sig>25.0 && dr_bjet_lep<2.6 && n_bjet>0.5 && hadtop_cand_m[0]>150e3"

tn_high_t1lvr = "topness<8.0 && met>450.0e3 && mt>90.0e3 && mt<120.0e3 && ht_sig>10.0 && n_bjet>0.5 && hadtop_cand_m[0]>150e3"
tn_high_t2lvr = "topness<8.0 && met>450.0e3 && mt>120.0e3&& ht_sig>10.0 && n_bjet>0.5 && hadtop_cand_m[0]>150e3"
tn_high_wvr = "topness>8.0 && met>450.0e3 && mt>30.0e3 && mt<90.0e3 && ht_sig>10.0 && n_bjet>0.5 && hadtop_cand_m[0]>150e3 && deltaRbb_orderpt<1.4 && lep_charge[0]==1"

tn_high_t1lcr = "topness<8.0 && met>450.0e3 && mt>30.0e3 && mt<90.0e3 && ht_sig>10.0 && n_bjet>0.5 && hadtop_cand_m[0]>150e3"
tn_high_t2lcr = "topness<8.0 && met>450.0e3 && mt>120.0e3&& ht_sig>10.0 && n_bjet>0.5 && Alt$(hadtop_cand_m[0], 0)< 150e3"
tn_high_wcr = "topness>8.0 && met>450.0e3 && mt>30.0e3 && mt<90.0e3 && ht_sig>10.0 && n_bjet>0.5 && Alt$(hadtop_cand_m[0], 0)< 150e3 && deltaRbb_orderpt<1.4 && lep_charge[0]==1"
tn_high_stcr = "topness>10.0 && met>450.0e3 && mt>30.0e3 && mt<120.0e3 && ht_sig>10.0 && n_bjet>1.5 && Alt$(hadtop_cand_m[0], 0)< 150e3 && deltaRbb_orderpt>1.4"

