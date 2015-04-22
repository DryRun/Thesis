import os
import sys

figures = {}

paper_figure_directory = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures/"
intnote_figure_directory = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/figures/"
data_directory = "/Users/dryu/Documents/Physics/ATLAS/Multilepton/Data/VectorLeptons/AnaVLL/Jobset_MLv5.2Central/"

figures[paper_figure_directory + "fd_cc2.eps"]                = "fd_cc2.eps"
figures[paper_figure_directory + "fd_cn2.eps"]                = "fd_cn2.eps"
figures[intnote_figure_directory + "/david/c_xsec_t3ss.png"]  = "c_xsec_t3ss.png"
figures[intnote_figure_directory + "/david/vll_xsec.png"]     = "vll_xsec.png"
figures[intnote_figure_directory + "/david/c_br_charged.pdf"] = "c_br_charged.pdf"
figures[intnote_figure_directory + "/david/c_br_neutral.pdf"] = "c_br_neutral.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Ze/InclusiveNoM3LDeltaR/c_output_dR_Ze_InclusiveNoM3LDeltaR_300GeV_log.pdf"] = "c_output_dR_Ze_InclusiveNoM3LDeltaR_300GeV_log.pdf"
figures[intnote_figure_directory + "/david/CutOptimization/DeltaR/c_limits_dRVariation_VLL_Combined_BRe1.0_BRmu0.0.pdf"]     = "c_limits_dRVariation_VLL_Combined_BRe1.0_BRmu0.0.pdf"
figures[intnote_figure_directory + "/david/CutOptimization/DeltaR/c_limits_dRVariation_Seesaw_Combined_BRe1.0_BRmu0.0.pdf"]  = "c_limits_dRVariation_Seesaw_Combined_BRe1.0_BRmu0.0.pdf"
figures[intnote_figure_directory + "/david/c_oppositeside_charged.pdf"] = "c_oppositesideactivity_charged.pdf"
figures[intnote_figure_directory + "/david/c_oppositeside_neutral.pdf"] = "c_oppositesideactivity_neutral.pdf"
figures[intnote_figure_directory + "/david/CutOptimization/c_eff_fid_Ze_Seesaw.pdf"]  = "c_eff_fid_Ze_Seesaw.pdf"
figures[intnote_figure_directory + "/david/CutOptimization/c_eff_fid_Ze_VLL.pdf"]     = "c_eff_fid_Ze_VLL.pdf"
figures[intnote_figure_directory + "/david/CutOptimization/c_eff_fid_Zmu_Seesaw.pdf"] = "c_eff_fid_Zmu_Seesaw.pdf"
figures[intnote_figure_directory + "/david/CutOptimization/c_eff_fid_Zmu_VLL.pdf"]    = "c_eff_fid_Zmu_VLL.pdf"
figures[intnote_figure_directory + "/david/Systematics/WZShape/c_Ze_InclusiveNoM3L_WZ.pdf"]                   = "c_systematics_WZShape_Ze_InclusiveNoM3L_WZ.pdf"
figures[intnote_figure_directory + "/david/Systematics/WZShape/c_Ze_ThreeLDijetNoM3L_WZ.pdf"]                 = "c_systematics_WZShape_Ze_ThreeLDijetNoM3L_WZ.pdf"
figures[intnote_figure_directory + "/david/Systematics/WZShape/c_Zmu_InclusiveNoM3L_WZ.pdf"]                  = "c_systematics_WZShape_Zmu_InclusiveNoM3L_WZ.pdf"
figures[intnote_figure_directory + "/david/Systematics/WZShape/c_Zmu_ThreeLDijetNoM3L_WZ.pdf"]                = "c_systematics_WZShape_Zmu_ThreeLDijetNoM3L_WZ.pdf"
figures[intnote_figure_directory + "/david/Systematics/ZZShape/c_ZZ_DeltaM_Ze_InclusiveNoM3L.pdf"]            = "c_systematics_ZZShape_DeltaM_Ze_InclusiveNoM3L.pdf"
figures[intnote_figure_directory + "/david/Systematics/ZZShape/c_ZZ_DeltaM_Ze_ThreeLDijetNoM3L.pdf"]          = "c_systematics_ZZShape_DeltaM_Ze_ThreeLDijetNoM3L.pdf"
figures[intnote_figure_directory + "/david/Systematics/ZZShape/c_ZZ_DeltaM_Zmu_InclusiveNoM3L.pdf"]           = "c_systematics_ZZShape_DeltaM_Zmu_InclusiveNoM3L.pdf"
figures[intnote_figure_directory + "/david/Systematics/ZZShape/c_ZZ_DeltaM_Zmu_ThreeLDijetNoM3L.pdf"]         = "c_systematics_ZZShape_DeltaM_Zmu_ThreeLDijetNoM3L.pdf"
figures[intnote_figure_directory + "/david/Systematics/ZZShape/c_ZZShapeSyst_Ze_InclusiveNoM3L.pdf"]          = "c_systematics_ZZShapeSyst_Ze_InclusiveNoM3L.pdf"
figures[intnote_figure_directory + "/david/Systematics/ZZShape/c_ZZShapeSyst_Ze_ThreeLDijetNoM3L.pdf"]        = "c_systematics_ZZShapeSyst_Ze_ThreeLDijetNoM3L.pdf"
figures[intnote_figure_directory + "/david/Systematics/ZZShape/c_ZZShapeSyst_Zmu_InclusiveNoM3L.pdf"]         = "c_systematics_ZZShapeSyst_Zmu_InclusiveNoM3L.pdf"
figures[intnote_figure_directory + "/david/Systematics/ZZShape/c_ZZShapeSyst_Zmu_ThreeLDijetNoM3L.pdf"]       = "c_systematics_ZZShapeSyst_Zmu_ThreeLDijetNoM3L.pdf"
figures[intnote_figure_directory + "/david/Systematics/c_systematics_DeltaM_Ze_InclusiveNoM3L_300GeV.pdf"]    = "c_systematics_DeltaM_Ze_InclusiveNoM3L_300GeV.pdf"
figures[intnote_figure_directory + "/david/Systematics/c_systematics_DeltaM_Ze_FourLNoM3L_300GeV.pdf"]        = "c_systematics_DeltaM_Ze_FourLNoM3L_300GeV.pdf"
figures[intnote_figure_directory + "/david/Systematics/c_systematics_DeltaM_Ze_ThreeLDijetNoM3L_300GeV.pdf"]  = "c_systematics_DeltaM_Ze_ThreeLDijetNoM3L_300GeV.pdf"
figures[intnote_figure_directory + "/david/Systematics/c_systematics_DeltaM_Ze_ElseNoM3L_300GeV.pdf"]         = "c_systematics_DeltaM_Ze_ElseNoM3L_300GeV.pdf"
figures[intnote_figure_directory + "/david/Systematics/c_systematics_DeltaM_Zmu_InclusiveNoM3L_300GeV.pdf"]   = "c_systematics_DeltaM_Zmu_InclusiveNoM3L_300GeV.pdf"
figures[intnote_figure_directory + "/david/Systematics/c_systematics_DeltaM_Zmu_FourLNoM3L_300GeV.pdf"]       = "c_systematics_DeltaM_Zmu_FourLNoM3L_300GeV.pdf"
figures[intnote_figure_directory + "/david/Systematics/c_systematics_DeltaM_Zmu_ThreeLDijetNoM3L_300GeV.pdf"] = "c_systematics_DeltaM_Zmu_ThreeLDijetNoM3L_300GeV.pdf"
figures[intnote_figure_directory + "/david/Systematics/c_systematics_DeltaM_Zmu_ElseNoM3L_300GeV.pdf"]        = "c_systematics_DeltaM_Zmu_ElseNoM3L_300GeV.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Ze/HighDeltaR/c_output_DeltaM_Ze_HighDeltaR_300GeV.pdf"]   = "c_output_DeltaM_Ze_HighDeltaR_300GeV.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Zmu/HighDeltaR/c_output_DeltaM_Zmu_HighDeltaR_300GeV.pdf"] = "c_output_DeltaM_Zmu_HighDeltaR_300GeV.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Ze/TwoZ/c_output_DeltaM_Ze_TwoZ_300GeV.pdf"]               = "c_output_DeltaM_Ze_TwoZ_300GeV.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Zmu/TwoZ/c_output_DeltaM_Zmu_TwoZ_300GeV.pdf"]             = "c_output_DeltaM_Zmu_TwoZ_300GeV.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Ze/OffZ/c_output_DeltaM_Ze_OffZ_300GeV.pdf"]               = "c_output_DeltaM_Ze_OffZ_300GeV.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Zmu/OffZ/c_output_DeltaM_Zmu_OffZ_300GeV.pdf"]             = "c_output_DeltaM_Zmu_OffZ_300GeV.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Ze/WZ/c_output_DeltaM_Ze_WZ_300GeV.pdf"]                   = "c_output_DeltaM_Ze_WZ_300GeV.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Zmu/WZ/c_output_DeltaM_Zmu_WZ_300GeV.pdf"]                 = "c_output_DeltaM_Zmu_WZ_300GeV.pdf"

figures[intnote_figure_directory + "/Liv/Fit/sig120_Fit.pdf"]                      = "Fit_sig120_Fit.pdf"
figures[intnote_figure_directory + "/Liv/Seesaw_inclusive/sig120_Fit.pdf"]         = "Seesaw_inclusive_sig120_Fit.pdf"
figures[intnote_figure_directory + "/Liv/Fit/sig120_Pull.pdf"]                     = "Fit_sig120_Pull.pdf"
figures[intnote_figure_directory + "/Liv/Seesaw_inclusive/sig120_Pull.pdf"]        = "Seesaw_inclusive_sig120_Pull.pdf"
figures[intnote_figure_directory + "/Liv/Fit/sig120_Resid.pdf"]                    = "Fit_sig120_Resid.pdf"
figures[intnote_figure_directory + "/Liv/Seesaw_inclusive/sig120_Resid.pdf"]       = "Seesaw_inclusive_sig120_Resid.pdf"
figures[intnote_figure_directory + "/Liv/Fit/Central/corr_fit_sigp_xp__WZ_hS.pdf"] = "corr_fit_sigp_xp__WZ_hS.pdf"
figures[intnote_figure_directory + "/Liv/Fit/Central/corr_fit_xi_xp__WZ_hS.pdf"]   = "corr_fit_xi_xp__WZ_hS.pdf"
figures[intnote_figure_directory + "/Liv/Fit/Central/corr_fit_sigp_xp__ZZ_hS.pdf"] = "corr_fit_sigp_xp__ZZ_hS.pdf"
figures[intnote_figure_directory + "/Liv/Fit/Central/corr_fit_xi_xp__ZZ_hS.pdf"]   = "corr_fit_xi_xp__ZZ_hS.pdf"
figures[intnote_figure_directory + "/david/Fits/c_FitVariations_ZZ_Sherpa_Bukin3Par_InclusiveNoM3L_Ze_DeltaM_InclusiveNoM3L.pdf"] = "c_FitVariations_ZZ_Sherpa_Bukin3Par_InclusiveNoM3L_Ze_DeltaM_InclusiveNoM3L.pdf"
figures[intnote_figure_directory + "/david/Fits/c_FitVariations_ZZ_Sherpa_Bukin3Par_InclusiveNoM3L_Zmu_DeltaM_InclusiveNoM3L.pdf"] = "c_FitVariations_ZZ_Sherpa_Bukin3Par_InclusiveNoM3L_Zmu_DeltaM_InclusiveNoM3L.pdf"
figures[intnote_figure_directory + "/david/Fits/c_FitVariations_ZZ_Sherpa_Bukin3Par_FourLNoM3L_Ze_DeltaM_FourLNoM3L.pdf"] = "c_FitVariations_ZZ_Sherpa_Bukin3Par_FourLNoM3L_Ze_DeltaM_FourLNoM3L.pdf"
figures[intnote_figure_directory + "/david/Fits/c_FitVariations_ZZ_Sherpa_Bukin3Par_FourLNoM3L_Zmu_DeltaM_FourLNoM3L.pdf"] = "c_FitVariations_ZZ_Sherpa_Bukin3Par_FourLNoM3L_Zmu_DeltaM_FourLNoM3L.pdf"
figures[intnote_figure_directory + "/david/Fits/c_FitVariations_ZZ_Sherpa_Bukin3Par_ThreeLDijetNoM3L_Ze_DeltaM_ThreeLDijetNoM3L.pdf"] = "c_FitVariations_ZZ_Sherpa_Bukin3Par_ThreeLDijetNoM3L_Ze_DeltaM_ThreeLDijetNoM3L.pdf"
figures[intnote_figure_directory + "/david/Fits/c_FitVariations_ZZ_Sherpa_Bukin3Par_ThreeLDijetNoM3L_Zmu_DeltaM_ThreeLDijetNoM3L.pdf"] = "c_FitVariations_ZZ_Sherpa_Bukin3Par_ThreeLDijetNoM3L_Zmu_DeltaM_ThreeLDijetNoM3L.pdf"
figures[intnote_figure_directory + "/david/Fits/c_FitVariations_ZZ_Sherpa_Bukin3Par_ElseNoM3L_Ze_DeltaM_ElseNoM3L.pdf"] = "c_FitVariations_ZZ_Sherpa_Bukin3Par_ElseNoM3L_Ze_DeltaM_ElseNoM3L.pdf"
figures[intnote_figure_directory + "/david/Fits/c_FitVariations_ZZ_Sherpa_Bukin3Par_ElseNoM3L_Zmu_DeltaM_ElseNoM3L.pdf"] = "c_FitVariations_ZZ_Sherpa_Bukin3Par_ElseNoM3L_Zmu_DeltaM_ElseNoM3L.pdf"
figures[intnote_figure_directory + "/david/Fits/c_FitVariations_WZ_Sherpa_Bukin3Par_InclusiveNoM3L_Ze_DeltaM_InclusiveNoM3L.pdf"] = "c_FitVariations_WZ_Sherpa_Bukin3Par_InclusiveNoM3L_Ze_DeltaM_InclusiveNoM3L.pdf"
figures[intnote_figure_directory + "/david/Fits/c_FitVariations_WZ_Sherpa_Bukin3Par_InclusiveNoM3L_Zmu_DeltaM_InclusiveNoM3L.pdf"] = "c_FitVariations_WZ_Sherpa_Bukin3Par_InclusiveNoM3L_Zmu_DeltaM_InclusiveNoM3L.pdf"
figures[intnote_figure_directory + "/david/Fits/c_FitVariations_WZ_Sherpa_Bukin3Par_ThreeLDijetNoM3L_Ze_DeltaM_ThreeLDijetNoM3L.pdf"] = "c_FitVariations_WZ_Sherpa_Bukin3Par_ThreeLDijetNoM3L_Ze_DeltaM_ThreeLDijetNoM3L.pdf"
figures[intnote_figure_directory + "/david/Fits/c_FitVariations_WZ_Sherpa_Bukin3Par_ThreeLDijetNoM3L_Zmu_DeltaM_ThreeLDijetNoM3L.pdf"] = "c_FitVariations_WZ_Sherpa_Bukin3Par_ThreeLDijetNoM3L_Zmu_DeltaM_ThreeLDijetNoM3L.pdf"
figures[intnote_figure_directory + "/david/Fits/c_FitVariations_WZ_Sherpa_Bukin3Par_ElseNoM3L_Ze_DeltaM_ElseNoM3L.pdf"] = "c_FitVariations_WZ_Sherpa_Bukin3Par_ElseNoM3L_Ze_DeltaM_ElseNoM3L.pdf"
figures[intnote_figure_directory + "/david/Fits/c_FitVariations_WZ_Sherpa_Bukin3Par_ElseNoM3L_Zmu_DeltaM_ElseNoM3L.pdf"] = "c_FitVariations_WZ_Sherpa_Bukin3Par_ElseNoM3L_Zmu_DeltaM_ElseNoM3L.pdf"
figures[intnote_figure_directory + "/david/KSTests/c_ZZ_Sherpa_FourLNoM3L_Ze.pdf"]        = "c_KSTests_ZZ_Sherpa_FourLNoM3L_Ze.pdf"
figures[intnote_figure_directory + "/david/KSTests/c_ZZ_Sherpa_ThreeLDijetNoM3L_Ze.pdf"]  = "c_KSTests_ZZ_Sherpa_ThreeLDijetNoM3L_Ze.pdf"
figures[intnote_figure_directory + "/david/KSTests/c_ZZ_Sherpa_ElseNoM3L_Ze.pdf"]         = "c_KSTests_ZZ_Sherpa_ElseNoM3L_Ze.pdf"
figures[intnote_figure_directory + "/david/KSTests/c_ZZ_Sherpa_FourLNoM3L_Zmu.pdf"]       = "c_KSTests_ZZ_Sherpa_FourLNoM3L_Zmu.pdf"
figures[intnote_figure_directory + "/david/KSTests/c_ZZ_Sherpa_ThreeLDijetNoM3L_Zmu.pdf"] = "c_KSTests_ZZ_Sherpa_ThreeLDijetNoM3L_Zmu.pdf"
figures[intnote_figure_directory + "/david/KSTests/c_ZZ_Sherpa_ElseNoM3L_Zmu.pdf"]        = "c_KSTests_ZZ_Sherpa_ElseNoM3L_Zmu.pdf"
figures[intnote_figure_directory + "/david/KSTests/c_WZ_Sherpa_ThreeLDijetNoM3L_Ze.pdf"]  = "c_KSTests_WZ_Sherpa_ThreeLDijetNoM3L_Ze.pdf"
figures[intnote_figure_directory + "/david/KSTests/c_WZ_Sherpa_ElseNoM3L_Ze.pdf"]         = "c_KSTests_WZ_Sherpa_ElseNoM3L_Ze.pdf"
figures[intnote_figure_directory + "/david/KSTests/c_WZ_Sherpa_ThreeLDijetNoM3L_Zmu.pdf"] = "c_KSTests_WZ_Sherpa_ThreeLDijetNoM3L_Zmu.pdf"
figures[intnote_figure_directory + "/david/KSTests/c_WZ_Sherpa_ElseNoM3L_Zmu.pdf"]        = "c_KSTests_WZ_Sherpa_ElseNoM3L_Zmu.pdf"
figures[intnote_figure_directory + "/Liv/Fit/Central/fit_WZ_hS.pdf"]         = "fit_WZ_hS.pdf"
figures[intnote_figure_directory + "/Liv/Fit/Central/fit_WZ_3Ljj_hS.pdf"]    = "fit_WZ_3Ljj_hS.pdf"
figures[intnote_figure_directory + "/Liv/Fit/Central/fit_ZZ_hS.pdf"]         = "fit_ZZ_hS.pdf"
figures[intnote_figure_directory + "/Liv/Fit/Central/fit_ZZ_3Ljj_hS.pdf"]    = "fit_ZZ_3Ljj_hS.pdf"
figures[intnote_figure_directory + "/Liv/Fit/Central/fit_reducible_Ze.pdf"]  = "fit_reducible_Ze.pdf"
figures[intnote_figure_directory + "/Liv/Fit/Central/fit_reducible_Zmu.pdf"] = "fit_reducible_Zmu.pdf"
figures[intnote_figure_directory + "/liv/Fit/Central/fit_llgamma_Ze.pdf"]    = "fit_llgamma_Ze.pdf"
figures[intnote_figure_directory + "/liv/Fit/Central/fit_ttV_VVV.pdf"]       = "fit_ttV_VVV.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Ze/FourLNoM3L/c_output_DeltaM_Ze_FourLNoM3L_300GeV_hide_ratio.pdf"]               = "c_output_DeltaM_Ze_FourLNoM3L_300GeV_hide_ratio.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Zmu/FourLNoM3L/c_output_DeltaM_Zmu_FourLNoM3L_300GeV_hide_ratio.pdf"]             = "c_output_DeltaM_Zmu_FourLNoM3L_300GeV_hide_ratio.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Ze/ThreeLDijetNoM3L/c_output_DeltaM_Ze_ThreeLDijetNoM3L_300GeV_hide_ratio.pdf"]   = "c_output_DeltaM_Ze_ThreeLDijetNoM3L_300GeV_hide_ratio.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Zmu/ThreeLDijetNoM3L/c_output_DeltaM_Zmu_ThreeLDijetNoM3L_300GeV_hide_ratio.pdf"] = "c_output_DeltaM_Zmu_ThreeLDijetNoM3L_300GeV_hide_ratio.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Ze/ElseNoM3L/c_output_DeltaM_Ze_ElseNoM3L_300GeV_log.pdf"]                        = "c_output_DeltaM_Ze_ElseNoM3L_300GeV_log.pdf"
figures[data_directory + "/LimitSetting/figures/Control/Zmu/ElseNoM3L/c_output_DeltaM_Zmu_ElseNoM3L_300GeV_log.pdf"]                      = "c_output_DeltaM_Zmu_ElseNoM3L_300GeV_log.pdf"
figures[paper_figure_directory + "/Fit_BGOnly_Ze_ErrorBand.pdf"]              = "Fit_BGOnly_Ze_ErrorBand.pdf"
figures[paper_figure_directory + "/Fit_BGOnly_Zmu_ErrorBand.pdf"]             = "Fit_BGOnly_Zmu_ErrorBand.pdf"
figures[paper_figure_directory + "/LimitVLL_Ze_NP.pdf"]                       = "LimitVLL_Ze_NP.pdf"
figures[paper_figure_directory + "/LimitVLL_Zmu_NP.pdf"]                      = "LimitVLL_Zmu_NP.pdf"
figures[paper_figure_directory + "/SeesawZe_ShapeInterpol_xsectot_plot.pdf"]  = "SeesawZe_ShapeInterpol_xsectot_plot.pdf"
figures[paper_figure_directory + "/SeesawZmu_ShapeInterpol_xsectot_plot.pdf"] = "SeesawZmu_ShapeInterpol_xsectot_plot.pdf"
figures[paper_figure_directory + "/SeesawZe_N95_Inclusive.pdf"]               = "SeesawZe_N95_Inclusive.pdf"
figures[paper_figure_directory + "/SeesawZmu_N95_Inclusive.pdf"]              = "SeesawZmu_N95_Inclusive.pdf"
figures[data_directory + "Fiducial/Matched/c_fid_eff_vs_mass_Ze_InclusiveNoM3L_Seesaw_minimal.pdf"] = "c_fid_eff_vs_mass_Ze_InclusiveNoM3L_Seesaw_minimal"
figures[data_directory + "Fiducial/Matched/c_fid_eff_vs_mass_Zmu_InclusiveNoM3L_Seesaw_minimal.pdf"] = "c_fid_eff_vs_mass_Zmu_InclusiveNoM3L_Seesaw_minimal"

for original_figure, thesis_figure in figures.iteritems():
	command = "cp " + original_figure + " figures/ch6-resonance/" + thesis_figure
	#print command
	os.system(command)