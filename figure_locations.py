import fnmatch
import os


# Partial list of original paths of figure
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

def FindFigures(figure_list):
	possible_paths = []
	possible_paths.append("/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/figures/")
	possible_paths.append("/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/figures/")
	possible_paths.append("/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/ML2012InternalNote/paper/figures")
	possible_paths.append("/Users/dryu/Documents/Physics/ATLAS/Multilepton/Documents/TypeIIISeesaw8TeV/paper/figures")

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
		#print command
		os.system(command)

if __name__ == "__main__":
	#FindFigures(sorted(model_independent_figures.keys()))
	CopyFigures(model_independent_figures)

