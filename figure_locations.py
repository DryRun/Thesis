import fnmatch
import os


# Partial list of original paths of figure
luminosity_figures = {}
luminosity_figures["figures/luminosity/c_dz_NTrk5_BCID81.pdf"]     = "/Users/dryu/Documents/Physics/ATLAS/Luminosity/Papers/VdMVertexAnalysis/trunk/note/figures/Masking/data_7TeV_17.2_default/c_dz_NTrk5_BCID81.pdf"
luminosity_figures["figures/luminosity/c_pmask_dz_NTrk5_Data.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Luminosity/Papers/VdMVertexAnalysis/trunk/note/figures/Masking/data_7TeV_17.2_default/c_pmask_dz_NTrk5.pdf"
luminosity_figures["figures/luminosity/c_dz_NTrk5_MC.pdf"]          = "/Users/dryu/Documents/Physics/ATLAS/Luminosity/Papers/VdMVertexAnalysis/trunk/note/figures/Masking/mc_7TeV_17.2_default_pythia8_pu_bs55/c_dz_NTrk5.pdf"
luminosity_figures["figures/luminosity/c_pmask_dz_NTrk5_MC.pdf"]    = "/Users/dryu/Documents/Physics/ATLAS/Luminosity/Papers/VdMVertexAnalysis/trunk/note/figures/Masking/mc_7TeV_17.2_default_pythia8_pu_bs55/c_pmask_dz_NTrk5.pdf"
 
model_independent_figures = {}
model_independent_figures["figures/modelindependent/DYOSee_cut_3f_AllLeptonMass.pdf"]                          = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/DYOSee_cut_3f_AllLeptonMass.pdf"
model_independent_figures["figures/modelindependent/DYOSmm_cut_3f_AllLeptonMass.pdf"]                          = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/DYOSmm_cut_3f_AllLeptonMass.pdf"
model_independent_figures["figures/modelindependent/OSZ_LeadingEta.eps"]                                       = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/OSZ_LeadingEta.eps"
model_independent_figures["figures/modelindependent/OSZ_LeadingEta.pdf"]                                       = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/OSZ_LeadingEta.pdf"
model_independent_figures["figures/modelindependent/OSZ_LeadingPt.eps"]                                        = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/OSZ_LeadingPt.eps"
model_independent_figures["figures/modelindependent/OSZ_LeadingPt.pdf"]                                        = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/OSZ_LeadingPt.pdf"
model_independent_figures["figures/modelindependent/OSZ_SubleadEta.eps"]                                       = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/OSZ_SubleadEta.eps"
model_independent_figures["figures/modelindependent/OSZ_SubleadEta.pdf"]                                       = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/OSZ_SubleadEta.pdf"
model_independent_figures["figures/modelindependent/OSZ_SubleadPt.eps"]                                        = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/paper/figures/OSZ_SubleadPt.eps"
model_independent_figures["figures/modelindependent/OSZ_SubleadPt.pdf"]                                        = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/paper/figures/OSZ_SubleadPt.pdf"
model_independent_figures["figures/modelindependent/Z_emu_Zee_offZmu_intmuon_MET.pdf"]                         = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/intmuon/Z_emu_Zee_offZmu_intmuon_MET.pdf"
model_independent_figures["figures/modelindependent/Z_emu_Zee_offZmu_intmuon_OffZEta.pdf"]                     = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/intmuon/Z_emu_Zee_offZmu_intmuon_OffZEta.pdf"
model_independent_figures["figures/modelindependent/Z_emu_Zee_offZmu_intmuon_OffZMT.eps"]                      = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/paper/figures/Z_emu_Zee_offZmu_intmuon_OffZMT.eps"
model_independent_figures["figures/modelindependent/Z_emu_Zee_offZmu_intmuon_OffZMT.pdf"]                      = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/paper/figures/Z_emu_Zee_offZmu_intmuon_OffZMT.pdf"
model_independent_figures["figures/modelindependent/Z_emu_Zee_offZmu_intmuon_OffZPt.pdf"]                      = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/intmuon/Z_emu_Zee_offZmu_intmuon_OffZPt.pdf"
model_independent_figures["figures/modelindependent/Z_emu_Zee_offZmu_intmuon_ST.pdf"]                          = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/intmuon/Z_emu_Zee_offZmu_intmuon_ST.pdf"
model_independent_figures["figures/modelindependent/Z_emu_Zee_offZmu_intmuon_Simple3LEventClassification.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/intmuon/Z_emu_Zee_offZmu_intmuon_Simple3LEventClassification.pdf"
model_independent_figures["figures/modelindependent/Z_emu_Zmm_offZe_intelec_MET.pdf"]                          = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/intelec/Z_emu_Zmm_offZe_intelec_MET.pdf"
model_independent_figures["figures/modelindependent/Z_emu_Zmm_offZe_intelec_OffZEta.pdf"]                      = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/intelec/Z_emu_Zmm_offZe_intelec_OffZEta.pdf"
model_independent_figures["figures/modelindependent/Z_emu_Zmm_offZe_intelec_OffZMT.pdf"]                       = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/intelec/Z_emu_Zmm_offZe_intelec_OffZMT.pdf"
model_independent_figures["figures/modelindependent/Z_emu_Zmm_offZe_intelec_OffZPt.pdf"]                       = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/intelec/Z_emu_Zmm_offZe_intelec_OffZPt.pdf"
model_independent_figures["figures/modelindependent/Z_emu_Zmm_offZe_intelec_ST.pdf"]                           = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/intelec/Z_emu_Zmm_offZe_intelec_ST.pdf"
model_independent_figures["figures/modelindependent/Z_emu_Zmm_offZe_intelec_Simple3LEventClassification.pdf"]  = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/intelec/Z_emu_Zmm_offZe_intelec_Simple3LEventClassification.pdf"
model_independent_figures["figures/modelindependent/c_e_eta_allSF.pdf"]                                        = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/c_e_eta_allSF.pdf"
model_independent_figures["figures/modelindependent/c_e_pt_allSF.pdf"]                                         = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/c_e_pt_allSF.pdf"
model_independent_figures["figures/modelindependent/c_m_eta_allSF.pdf"]                                        = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/c_m_eta_allSF.pdf"
model_independent_figures["figures/modelindependent/c_m_pt_allSF.pdf"]                                         = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/c_m_pt_allSF.pdf"
model_independent_figures["figures/modelindependent/semileptop_emu_mue_LeadEta.pdf"]                           = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/CR_ttbar/semileptop_emu_mue_LeadEta.pdf"
model_independent_figures["figures/modelindependent/semileptop_emu_mue_LeadPt.pdf"]                            = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/CR_ttbar/semileptop_emu_mue_LeadPt.pdf"
model_independent_figures["figures/modelindependent/semileptop_emu_mue_MET.eps"]                               = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/paper/figures/semileptop_emu_mue_MET.eps"
model_independent_figures["figures/modelindependent/semileptop_emu_mue_MET.pdf"]                               = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/paper/figures/semileptop_emu_mue_MET.pdf"
model_independent_figures["figures/modelindependent/semileptop_emu_mue_ST.pdf"]                                = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/CR_ttbar/semileptop_emu_mue_ST.pdf"
model_independent_figures["figures/modelindependent/semileptop_emu_mue_SubleadEta.pdf"]                        = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/CR_ttbar/semileptop_emu_mue_SubleadEta.pdf"
model_independent_figures["figures/modelindependent/semileptop_emu_mue_SubleadPt.pdf"]                         = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/CR_ttbar/semileptop_emu_mue_SubleadPt.pdf"

model_independent_figures["figures/modelindependent/inttau_offZ_OSSF_DY_TauEta.pdf"]  = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/offZ_OSSF/DY_TauEta.pdf"
model_independent_figures["figures/modelindependent/inttau_offZ_OSSF_DY_TauEta.eps"]  = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/offZ_OSSF/DY_TauEta.eps"
model_independent_figures["figures/modelindependent/inttau_offZ_OSSF_DY_TauPt.pdf"]   = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/offZ_OSSF/DY_TauPt.pdf"
model_independent_figures["figures/modelindependent/inttau_offZ_OSSF_DY_TauPt.eps"]   = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/offZ_OSSF/DY_TauPt.eps"
model_independent_figures["figures/modelindependent/inttau_offZ_mixed_DY_TauEta.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/offZ_mixed/DY_TauEta.pdf"
model_independent_figures["figures/modelindependent/inttau_offZ_mixed_DY_TauEta.eps"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/offZ_mixed/DY_TauEta.eps"
model_independent_figures["figures/modelindependent/inttau_offZ_mixed_DY_TauPt.pdf"]  = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/offZ_mixed/DY_TauPt.pdf"
model_independent_figures["figures/modelindependent/inttau_offZ_mixed_DY_TauPt.eps"]  = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/offZ_mixed/DY_TauPt.eps"
model_independent_figures["figures/modelindependent/inttau_onZ_DY_TauEta.pdf"]        = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/onZ/DY_TauEta.pdf"
model_independent_figures["figures/modelindependent/inttau_onZ_DY_TauEta.eps"]        = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/onZ/DY_TauEta.eps"
model_independent_figures["figures/modelindependent/inttau_onZ_DY_TauPt.pdf"]         = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/onZ/DY_TauPt.pdf"
model_independent_figures["figures/modelindependent/inttau_onZ_DY_TauPt.eps"]         = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/TauCR/onZ/DY_TauPt.eps"

model_independent_figures["figures/modelindependent/DCH_L_emutau_3_HTLepComb_combined.eps"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/DCH_L_emutau_3_HTLepComb_combined.eps"
model_independent_figures["figures/modelindependent/DCH_L_emutau_4_HTLepComb_combined.eps"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/DCH_L_emutau_4_HTLepComb_combined.eps"

resonance_figures = {}
resonance_figures["figures/resonance/c_output_ETMiss_Ze_ElseNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/ElseNoM3L/c_output_ETMiss_Ze_ElseNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_ETMiss_Ze_FourLNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/FourLNoM3L/c_output_ETMiss_Ze_FourLNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_ETMiss_Ze_InclusiveNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/InclusiveNoM3L/c_output_ETMiss_Ze_InclusiveNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_ETMiss_Ze_ThreeLDijetNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/ThreeLDijetNoM3L/c_output_ETMiss_Ze_ThreeLDijetNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_ETMiss_Zmu_ElseNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/ElseNoM3L/c_output_ETMiss_Zmu_ElseNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_ETMiss_Zmu_FourLNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/FourLNoM3L/c_output_ETMiss_Zmu_FourLNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_ETMiss_Zmu_InclusiveNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/InclusiveNoM3L/c_output_ETMiss_Zmu_InclusiveNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_ETMiss_Zmu_ThreeLDijetNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/ThreeLDijetNoM3L/c_output_ETMiss_Zmu_ThreeLDijetNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_dR_Ze_ElseNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/ElseNoM3L/c_output_dR_Ze_ElseNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_dR_Ze_FourLNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/FourLNoM3L/c_output_dR_Ze_FourLNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_dR_Ze_InclusiveNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/InclusiveNoM3L/c_output_dR_Ze_InclusiveNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_dR_Ze_ThreeLDijetNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/ThreeLDijetNoM3L/c_output_dR_Ze_ThreeLDijetNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_dR_Zmu_ElseNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/ElseNoM3L/c_output_dR_Zmu_ElseNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_dR_Zmu_FourLNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/FourLNoM3L/c_output_dR_Zmu_FourLNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_dR_Zmu_InclusiveNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/InclusiveNoM3L/c_output_dR_Zmu_InclusiveNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_dR_Zmu_ThreeLDijetNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/ThreeLDijetNoM3L/c_output_dR_Zmu_ThreeLDijetNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_m3l_Ze_ElseNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/ElseNoM3L/c_output_m3l_Ze_ElseNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_m3l_Ze_FourLNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/FourLNoM3L/c_output_m3l_Ze_FourLNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_m3l_Ze_InclusiveNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/InclusiveNoM3L/c_output_m3l_Ze_InclusiveNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_m3l_Ze_ThreeLDijetNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/ThreeLDijetNoM3L/c_output_m3l_Ze_ThreeLDijetNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_m3l_Zmu_ElseNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/ElseNoM3L/c_output_m3l_Zmu_ElseNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_m3l_Zmu_FourLNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/FourLNoM3L/c_output_m3l_Zmu_FourLNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_m3l_Zmu_InclusiveNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/InclusiveNoM3L/c_output_m3l_Zmu_InclusiveNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_m3l_Zmu_ThreeLDijetNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/ThreeLDijetNoM3L/c_output_m3l_Zmu_ThreeLDijetNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_mTW_Ze_ElseNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/ElseNoM3L/c_output_mTW_Ze_ElseNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_mTW_Ze_FourLNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/FourLNoM3L/c_output_mTW_Ze_FourLNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_mTW_Ze_InclusiveNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/InclusiveNoM3L/c_output_mTW_Ze_InclusiveNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_mTW_Ze_ThreeLDijetNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Ze/ThreeLDijetNoM3L/c_output_mTW_Ze_ThreeLDijetNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_mTW_Zmu_ElseNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/ElseNoM3L/c_output_mTW_Zmu_ElseNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_mTW_Zmu_FourLNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/FourLNoM3L/c_output_mTW_Zmu_FourLNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_mTW_Zmu_InclusiveNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/InclusiveNoM3L/c_output_mTW_Zmu_InclusiveNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/c_output_mTW_Zmu_ThreeLDijetNoM3L_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel/Control/Zmu/ThreeLDijetNoM3L/c_output_mTW_Zmu_ThreeLDijetNoM3L_300GeV.pdf"
resonance_figures["figures/resonance/sigVLL_Ze_InclusiveNoM3L_300_Fit.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/sigVLL_Ze_InclusiveNoM3L_300_Fit.pdf"
resonance_figures["figures/resonance/sigVLL_Zmu_InclusiveNoM3L_300_Fit.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/sigVLL_Zmu_InclusiveNoM3L_300_Fit.pdf"
resonance_figures["figures/resonance/c_output_DeltaM_Ze_HighDeltaR_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_output_DeltaM_Ze_HighDeltaR_300GeV.pdf"
resonance_figures["figures/resonance/c_output_DeltaM_Zmu_HighDeltaR_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_output_DeltaM_Zmu_HighDeltaR_300GeV.pdf"
resonance_figures["figures/resonance/c_output_DeltaM_Ze_TwoZ_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_output_DeltaM_Ze_TwoZ_300GeV.pdf"
resonance_figures["figures/resonance/c_output_DeltaM_Zmu_TwoZ_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_output_DeltaM_Zmu_TwoZ_300GeV.pdf"
resonance_figures["figures/resonance/c_output_DeltaM_Ze_OffZ_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_output_DeltaM_Ze_OffZ_300GeV.pdf"
resonance_figures["figures/resonance/c_output_DeltaM_Zmu_OffZ_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_output_DeltaM_Zmu_OffZ_300GeV.pdf"
resonance_figures["figures/resonance/c_output_DeltaM_Ze_WZ_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_output_DeltaM_Ze_WZ_300GeV.pdf"
resonance_figures["figures/resonance/c_output_DeltaM_Zmu_WZ_300GeV.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_output_DeltaM_Zmu_WZ_300GeV.pdf"
resonance_figures["figures/resonance/c_output_DeltaM_Ze_FourLNoM3L_300GeV_hide_ratio.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_output_DeltaM_Ze_FourLNoM3L_300GeV_hide_ratio.pdf"
resonance_figures["figures/resonance/c_output_DeltaM_Zmu_FourLNoM3L_300GeV_hide_ratio.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_output_DeltaM_Zmu_FourLNoM3L_300GeV_hide_ratio.pdf"
resonance_figures["figures/resonance/c_output_DeltaM_Ze_ThreeLDijetNoM3L_300GeV_hide_ratio.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_output_DeltaM_Ze_ThreeLDijetNoM3L_300GeV_hide_ratio.pdf"
resonance_figures["figures/resonance/c_output_DeltaM_Zmu_ThreeLDijetNoM3L_300GeV_hide_ratio.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_output_DeltaM_Zmu_ThreeLDijetNoM3L_300GeV_hide_ratio.pdf"
resonance_figures["figures/resonance/c_output_DeltaM_Ze_ElseNoM3L_300GeV_log.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_output_DeltaM_Ze_ElseNoM3L_300GeV_log.pdf"
resonance_figures["figures/resonance/c_output_DeltaM_Zmu_ElseNoM3L_300GeV_log.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_output_DeltaM_Zmu_ElseNoM3L_300GeV_log.pdf"
resonance_figures["figures/resonance/Fit_BGOnly_Ze_ErrorBand.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/Fit_BGOnly_Ze_ErrorBand.pdf"
resonance_figures["figures/resonance/Fit_BGOnly_Zmu_ErrorBand.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/Fit_BGOnly_Zmu_ErrorBand.pdf"
resonance_figures["figures/resonance/p0Ze_plot.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/p0Ze_plot.pdf"
resonance_figures["figures/resonance/p0Zmu_plot.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/p0Zmu_plot.pdf"
resonance_figures["figures/resonance/LimitVLL_Ze_NP.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/LimitVLL_Ze_NP.pdf"
resonance_figures["figures/resonance/LimitVLL_Zmu_NP.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/LimitVLL_Zmu_NP.pdf"
resonance_figures["figures/resonance/SeesawZe_ShapeInterpol_xsectot_plot.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/SeesawZe_ShapeInterpol_xsectot_plot.pdf"
resonance_figures["figures/resonance/SeesawZmu_ShapeInterpol_xsectot_plot.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/SeesawZmu_ShapeInterpol_xsectot_plot.pdf"
resonance_figures["figures/resonance/SeesawZe_N95_Inclusive.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/SeesawZe_N95_Inclusive.pdf"
resonance_figures["figures/resonance/SeesawZmu_N95_Inclusive.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/SeesawZmu_N95_Inclusive.pdf"
resonance_figures["figures/resonance/c_fid_eff_vs_mass_Ze_InclusiveNoM3L_Seesaw_minimal.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_fid_eff_vs_mass_Ze_InclusiveNoM3L_Seesaw_minimal.pdf"
resonance_figures["figures/resonance/c_fid_eff_vs_mass_Zmu_InclusiveNoM3L_Seesaw_minimal.pdf"] = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/c_fid_eff_vs_mass_Zmu_InclusiveNoM3L_Seesaw_minimal.pdf"

def FindFigures(figure_list):
	possible_paths = []
	possible_paths.append("/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/")
	#possible_paths.append("/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/figures/")
	possible_paths.append("/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/paper/figures")
	#possible_paths.append("/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures")
	possible_paths.append("/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/LimitSetting/figures_NoLabel")

	for thesis_figure_path in figure_list:
		matches = []
		figure_basename = os.path.basename(thesis_figure_path)
		for possible_path in possible_paths:
			for root, dirnames, filenames in os.walk(possible_path):
				for filename in fnmatch.filter(filenames, '*' + figure_basename + '*'):
					matches.append(os.path.join(root, filename))

		if len(matches) == 0:
			print "model_independent_figures[\"" + thesis_figure_path + "\"] = \"\""
		if len(matches) >= 2:
			print "Multiple matches found for " + thesis_figure_path

		for match in matches:
			print "model_independent_figures[\"" + thesis_figure_path + "\"] = \"" + match + "\""

def CopyFigures(figures_list):
	for key, value in figures_list.iteritems():
		command = "cp " + value + " " + key
		print command
		#os.system(command)

if __name__ == "__main__":
	#FindFigures(sorted(resonance_figures.keys()))
	CopyFigures(resonance_figures)

