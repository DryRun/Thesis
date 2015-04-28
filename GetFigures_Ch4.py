import os
import sys

figures = {}

vertexing_paper_figure_directory = "/Users/dryu/Documents/Physics/ATLAS/Luminosity/Papers/VdMVertexAnalysis/trunk/note/figures/"

figures[vertexing_paper_figure_directory + "/Masking/data_7TeV_17.2_default/c_dz_NTrk5_BCID81.pdf"] = "c_dz_NTrk5_BCID81.pdf"
figures[vertexing_paper_figure_directory + "/Masking/data_7TeV_17.2_default/c_pmask_dz_NTrk5.pdf"] = "c_pmask_dz_NTrk5.pdf"
figures[vertexing_paper_figure_directory + "/Masking/data_7TeV_17.2_default/c_dz_NTrk7_BCID81.pdf"] = "c_dz_NTrk7_BCID81.pdf"
figures[vertexing_paper_figure_directory + "/Masking/data_7TeV_17.2_default/c_pmask_dz_NTrk7.pdf"] = "c_pmask_dz_NTrk7.pdf"
figures[vertexing_paper_figure_directory + "/Masking/data_7TeV_17.2_default/c_dz_NTrk10_BCID81.pdf"] = "c_dz_NTrk10_BCID81.pdf"
figures[vertexing_paper_figure_directory + "/Masking/data_7TeV_17.2_default/c_pmask_dz_NTrk10.pdf"] = "c_pmask_dz_NTrk10.pdf"
figures[vertexing_paper_figure_directory + "/Masking/mc_7TeV_17.2_default_pythia8_pu_bs55/c_dz_NTrk5.pdf"] = "c_dz_NTrk5.pdf"
figures[vertexing_paper_figure_directory + "/Masking/mc_7TeV_17.2_default_pythia8_pu_bs55/c_pmask_dz_NTrk5.pdf"] = "c_pmask_dz_NTrk5.pdf"
figures[vertexing_paper_figure_directory + "/Masking/mc_7TeV_17.2_default_pythia8_pu_bs55/c_dz_NTrk7.pdf"] = "c_dz_NTrk7.pdf"
figures[vertexing_paper_figure_directory + "/Masking/mc_7TeV_17.2_default_pythia8_pu_bs55/c_pmask_dz_NTrk7.pdf"] = "c_pmask_dz_NTrk7.pdf"
figures[vertexing_paper_figure_directory + "/Masking/mc_7TeV_17.2_default_pythia8_pu_bs55/c_dz_NTrk10.pdf"] = "c_dz_NTrk10.pdf"
figures[vertexing_paper_figure_directory + "/Masking/mc_7TeV_17.2_default_pythia8_pu_bs55/c_pmask_dz_NTrk10.pdf"] = "c_pmask_dz_NTrk10.pdf"
figures[vertexing_paper_figure_directory + "/PileupCorrections/c_truefakemu_NGenInt.pdf"] = "c_truefakemu_NGenInt.pdf"
figures[vertexing_paper_figure_directory + "/PileupCorrections/c_mu_fake_NGenInt.png"] = "c_mu_fake_NGenInt.png"
figures[vertexing_paper_figure_directory + "/PileupCorrections/c_mu_fake_mu.png"] = "c_mu_fake_mu.png"
figures[vertexing_paper_figure_directory + "/PileupCorrections/c_mu_fake_MuReconMC.png"] = "c_mu_fake_MuReconMC.png"
figures[vertexing_paper_figure_directory + "/PileupCorrections/c_fake_fraction_MuReconMC.png"] = "c_fake_fraction_MuReconMC.png"
figures[vertexing_paper_figure_directory + "/VdM/musp/c_musp_x_BCID81_NTrkCut5.pdf"] = "c_musp_x_BCID81_NTrkCut5.pdf"
figures[vertexing_paper_figure_directory + "/VdM/musp/c_musp_y_BCID81_NTrkCut5.pdf"] = "c_musp_y_BCID81_NTrkCut5.pdf"
figures[vertexing_paper_figure_directory + "/VdM/musp/c_musp_x_BCID867_NTrkCut5.pdf"] = "c_musp_x_BCID867_NTrkCut5.pdf"
figures[vertexing_paper_figure_directory + "/VdM/musp/c_musp_y_BCID867_NTrkCut5.pdf"] = "c_musp_y_BCID867_NTrkCut5.pdf"
figures[vertexing_paper_figure_directory + "/VdM/musp/c_musp_x_BCID2752_NTrkCut5.pdf"] = "c_musp_x_BCID2752_NTrkCut5.pdf"
figures[vertexing_paper_figure_directory + "/VdM/musp/c_musp_y_BCID2752_NTrkCut5.pdf"] = "c_musp_y_BCID2752_NTrkCut5.pdf"
figures["/Users/dryu/Documents/Physics/ATLAS/Luminosity/Data/LumiVtx/191373/17.2_normal_bs_55mm/ATLAS/c_lumi_combined_191373.pdf"] = "c_lumi_combined_191373.pdf"
figures[vertexing_paper_figure_directory + "/MuScan/c_pileup_corrections_NVtx_BCID200.pdf"] = "c_pileup_corrections_NVtx_BCID200.pdf"
figures[vertexing_paper_figure_directory + "/MuScan/c_pileup_corrections_NVtx_BCID999.pdf"] = "c_pileup_corrections_NVtx_BCID999.pdf"
figures[vertexing_paper_figure_directory + "/MuScan/systematics/c_muscan.pdf"] = "c_muscan.pdf"

for original_figure, thesis_figure in figures.iteritems():
	command = "cp " + original_figure + " figures/ch4-reconstruction/" + thesis_figure
	#print command
	os.system(command)
