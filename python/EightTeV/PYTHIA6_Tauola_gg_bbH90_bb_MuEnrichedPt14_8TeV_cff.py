# General Import
import FWCore.ParameterSet.Config as cms
# Define the source (empty for Multipurpose Generators)
source = cms.Source("EmptySource")

# Import settings for modules
from Configuration.Generator.PythiaUEZ2Settings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *

# Define the generator module
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(1.1),
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            TauolaPolar, # tau polarisation switch on
            TauolaDefaultInputCards #set default TAUOLA input card
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    UseExternalGenerators = cms.untracked.bool(True),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=0         ! User defined processes',
            'MSUB(186)= 1   ! gg->QQbarH (MSSM)', 
            'KFPR(186,2)= 5 ! Q = b Registered by Alexandre.Nikitenko@cern.ch', 
            # MSSM settings
            'IMSS(1)= 1     ! MSSM with parameters',
            'RMSS(5)= 30.   ! tan beta', 
            'RMSS(19)= 90. ! m_A', 
            'RMSS(1)= 100.  ! M1',   
            'RMSS(2)= 200.  ! M2',   
            'RMSS(3)= 800.  ! Mg',   
            'RMSS(4)= 200.  ! mu',   
            'RMSS(6)= 1000.  ! MS',
            'RMSS(7)= 1000.  ! MS',
            'RMSS(8)= 1000.  ! MS',
            'RMSS(9)= 1000.  ! MS',
            'RMSS(10)= 1000.  ! MS',
            'RMSS(11)= 1000.  ! MS',
            'RMSS(12)= 1000.  ! MS',
            'RMSS(13)= 1000.  ! MS',
            'RMSS(14)= 1000.  ! MS',
            'RMSS(15)= 2000.  ! Ab',
            'RMSS(16)= 2000.  ! At',
            'RMSS(17)= 2000.  ! Atau',
            # Switch off / on desirable channels for A
            'MDME(420,1)=0  ! Higgs(H) decay into d              dbar', 
            'MDME(421,1)=0  ! Higgs(H) decay into u              ubar', 
            'MDME(422,1)=0  ! Higgs(H) decay into s              sbar', 
            'MDME(423,1)=0  ! Higgs(H) decay into c              cbar', 
            'MDME(424,1)=1  ! Higgs(H) decay into b              bbar', 
            'MDME(425,1)=0  ! Higgs(H) decay into t              tbar', 
            'MDME(426,1)=0  ! Higgs(H) decay into b              bbar', 
            'MDME(427,1)=0  ! Higgs(H) decay into t              tbar', 
            'MDME(428,1)=0  ! Higgs(H) decay into e-             e+', 
            'MDME(429,1)=0  ! Higgs(H) decay into mu-            mu+', 
            'MDME(430,1)=0  ! Higgs(H) decay into tau-           tau+', 
            'MDME(431,1)=0  ! Higgs(H) decay into tau-           tau+', 
            'MDME(432,1)=0  ! Higgs(H) decay into g              g', 
            'MDME(433,1)=0  ! Higgs(H) decay into gamma          gamma', 
            'MDME(434,1)=0  ! Higgs(H) decay into gamma          Z0', 
            'MDME(435,1)=0  ! Higgs(H) decay into Z0             Z0', 
            'MDME(436,1)=0  ! Higgs(H) decay into W+             W-', 
            'MDME(437,1)=0  ! Higgs(H) decay into Z0             h0', 
            'MDME(438,1)=0  ! Higgs(H) decay into h0             h0', 
            'MDME(439,1)=0  ! Higgs(H) decay into W+             H-', 
            'MDME(440,1)=0  ! Higgs(H) decay into H+             W-', 
            'MDME(441,1)=0  ! Higgs(H) decay into Z0             A0', 
            'MDME(442,1)=0  ! Higgs(H) decay into h0             A0', 
            'MDME(443,1)=0  ! Higgs(H) decay into A0             A0', 
            'MDME(444,1)=0  ! Higgs(H) decay into ~chi_10        ~chi_10', 
            'MDME(445,1)=0  ! Higgs(H) decay into ~chi_20        ~chi_10', 
            'MDME(446,1)=0  ! Higgs(H) decay into ~chi_20        ~chi_20', 
            'MDME(447,1)=0  ! Higgs(H) decay into ~chi_30        ~chi_10', 
            'MDME(448,1)=0  ! Higgs(H) decay into ~chi_30        ~chi_20', 
            'MDME(449,1)=0  ! Higgs(H) decay into ~chi_30        ~chi_30', 
            'MDME(450,1)=0  ! Higgs(H) decay into ~chi_40        ~chi_10', 
            'MDME(451,1)=0  ! Higgs(H) decay into ~chi_40        ~chi_20', 
            'MDME(452,1)=0  ! Higgs(H) decay into ~chi_40        ~chi_30', 
            'MDME(453,1)=0  ! Higgs(H) decay into ~chi_40        ~chi_40', 
            'MDME(454,1)=0  ! Higgs(H) decay into ~chi_1+        ~chi_1-', 
            'MDME(455,1)=0  ! Higgs(H) decay into ~chi_1+        ~chi_2-', 
            'MDME(456,1)=0  ! Higgs(H) decay into ~chi_2+        ~chi_1-', 
            'MDME(457,1)=0  ! Higgs(H) decay into ~chi_2+        ~chi_2-', 
            'MDME(458,1)=0  ! Higgs(H) decay into ~d_L           ~d_Lbar', 
            'MDME(459,1)=0  ! Higgs(H) decay into ~d_R           ~d_Rbar', 
            'MDME(460,1)=0  ! Higgs(H) decay into ~d_L           ~d_Rbar', 
            'MDME(461,1)=0  ! Higgs(H) decay into ~d_Lbar        ~d_R', 
            'MDME(462,1)=0  ! Higgs(H) decay into ~u_L           ~u_Lbar', 
            'MDME(463,1)=0  ! Higgs(H) decay into ~u_R           ~u_Rbar', 
            'MDME(464,1)=0  ! Higgs(H) decay into ~u_L           ~u_Rbar', 
            'MDME(465,1)=0  ! Higgs(H) decay into ~u_Lbar        ~u_R', 
            'MDME(466,1)=0  ! Higgs(H) decay into ~s_L           ~s_Lbar', 
            'MDME(467,1)=0  ! Higgs(H) decay into ~s_R           ~s_Rbar', 
            'MDME(468,1)=0  ! Higgs(H) decay into ~s_L           ~s_Rbar', 
            'MDME(469,1)=0  ! Higgs(H) decay into ~s_Lbar        ~s_R', 
            'MDME(470,1)=0  ! Higgs(H) decay into ~c_L           ~c_Lbar', 
            'MDME(471,1)=0  ! Higgs(H) decay into ~c_R           ~c_Rbar', 
            'MDME(472,1)=0  ! Higgs(H) decay into ~c_L           ~c_Rbar', 
            'MDME(473,1)=0  ! Higgs(H) decay into ~c_Lbar        ~c_R', 
            'MDME(474,1)=0  ! Higgs(H) decay into ~b_1           ~b_1bar', 
            'MDME(475,1)=0  ! Higgs(H) decay into ~b_2           ~b_2bar', 
            'MDME(476,1)=0  ! Higgs(H) decay into ~b_1           ~b_2bar', 
            'MDME(477,1)=0  ! Higgs(H) decay into ~b_1bar        ~b_2', 
            'MDME(478,1)=0  ! Higgs(H) decay into ~t_1           ~t_1bar', 
            'MDME(479,1)=0  ! Higgs(H) decay into ~t_2           ~t_2bar', 
            'MDME(480,1)=0  ! Higgs(H) decay into ~t_1           ~t_2bar', 
            'MDME(481,1)=0  ! Higgs(H) decay into ~t_1bar        ~t_2', 
            'MDME(482,1)=0  ! Higgs(H) decay into ~e_L-          ~e_L+', 
            'MDME(483,1)=0  ! Higgs(H) decay into ~e_R-          ~e_R+', 
            'MDME(484,1)=0  ! Higgs(H) decay into ~e_L-          ~e_R+', 
            'MDME(485,1)=0  ! Higgs(H) decay into ~e_L+          ~e_R-', 
            'MDME(486,1)=0  ! Higgs(H) decay into ~nu_eL         ~nu_eLbar', 
            'MDME(487,1)=0  ! Higgs(H) decay into ~nu_eR         ~nu_eRbar', 
            'MDME(488,1)=0  ! Higgs(H) decay into ~nu_eL         ~nu_eRbar', 
            'MDME(489,1)=0  ! Higgs(H) decay into ~nu_eLbar      ~nu_eR', 
            'MDME(490,1)=0  ! Higgs(H) decay into ~mu_L-         ~mu_L+', 
            'MDME(491,1)=0  ! Higgs(H) decay into ~mu_R-         ~mu_R+', 
            'MDME(492,1)=0  ! Higgs(H) decay into ~mu_L-         ~mu_R+', 
            'MDME(493,1)=0  ! Higgs(H) decay into ~mu_L+         ~mu_R-', 
            'MDME(494,1)=0  ! Higgs(H) decay into ~nu_muL        ~nu_muLbar', 
            'MDME(495,1)=0  ! Higgs(H) decay into ~nu_muR        ~nu_muRbar', 
            'MDME(496,1)=0  ! Higgs(H) decay into ~nu_muL        ~nu_muRbar', 
            'MDME(497,1)=0  ! Higgs(H) decay into ~nu_muLbar     ~nu_muR', 
            'MDME(498,1)=0  ! Higgs(H) decay into ~tau_1-        ~tau_1+', 
            'MDME(499,1)=0  ! Higgs(H) decay into ~tau_1-        ~tau_1+', 
            'MDME(500,1)=0  ! Higgs(H) decay into ~tau_1-        ~tau_1+', 
            'MDME(501,1)=0  ! Higgs(H) decay into ~tau_1-        ~tau_1+', 
            'MDME(502,1)=0  ! Higgs(H) decay into ~tau_2-        ~tau_2+'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)

#####################################
#####   filter mu from b-decay  #####
#####################################
mugenfilter = cms.EDFilter("MCSmartSingleParticleFilter",
    MinPt       = cms.untracked.vdouble(14., 14.),
    MinEta      = cms.untracked.vdouble(-2.5, -2.5),
    MaxEta      = cms.untracked.vdouble(2.5, 2.5),
    ParticleID  = cms.untracked.vint32(13, -13),
    Status      = cms.untracked.vint32(1, 1)
)


ProductionFilterSequence = cms.Sequence(generator * mugenfilter)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: /local/reps/CMSSW/CMSSW/Configuration/GenProduction/python/SevenTeV/PYTHIA6_Tauola_gg_bbH90_bb_MuEnrichedPt14_8TeV_cff.py,v $'),
    annotation = cms.untracked.string('PYTHIA6 - SUSY gg->bbH(90)->bb MuEnriched w/ pT>=14. |eta|<=2.5, with Tauola at 8TeV')
    )

