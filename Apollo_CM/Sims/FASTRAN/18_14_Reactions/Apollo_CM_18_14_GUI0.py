import GuiVersion
import GuiDBM
import GuiFILE
import GuiML
import GuiPT
import GuiMO
import GuiVC
import GuiBC
import GuiIC
import GuiPC
import GuiFan
import GuiMacP
import GuiMR
import GuiMRF
import GuiSC
import GuiOut
import GuiRun

#The following line is for backwards-compatibility, DO NOT DELETE IT.
GuiVersion.RecordVersion("2014.0.0.11217")

GuiFILE.SetMode("FASTRAN")
GuiFILE.Open("C:/Users/spl4ckd/Documents/Aerospace.Courses/Spring.2017/AE.295A/Plasma Blackout/CFD/Apollo_CM/18_14_Reactions/Apollo_CM_18_14.DTF")
GuiPT.Set("Chem", 1)
GuiMO.Set("Shared/Polar", "Axisymmetric")
GuiMO.Set("Chem/SolverFor", "Mixture Fractions")
GuiMO.Set("Chem/SolverFor", "Species Mass Fractions")
GuiMO.Set("Chem/ChemistryModel", "Reacting (Finite Rate)")
GuiMO.Set("Chem/ChemistryModel", "Mixing")
GuiDBM.Import("C:/Users/spl4ckd/Desktop/Mixture1.sdb", GuiDBM.MODEL, "Apollo_CM_18_14")
GuiDBM.Import("C:/Users/spl4ckd/Desktop/EBU.sdb", GuiDBM.MODEL, "Apollo_CM_18_14")
GuiMO.Set("Chem/SolverFor", "Mixture Fractions")
GuiMO.Set("Chem/SpeciesDatabase", "Molecular")
GuiMO.Set("Chem/SolverFor", "Species Mass Fractions")
GuiMO.Set("Chem/ChemistryModel", "Reacting (Finite Rate)")
GuiMO.Set("Chem/BulkReaction", "EBU")
GuiBC.Set([14], "Flow/u", 4000)
GuiBC.Set([14], "Flow/p", 0.0)
GuiBC.Set([14], "Flow/T", 300)
GuiBC.Set([14], "Chem/Mixture", "Mixture1")
GuiBC.Set([16], "Flow/Sub_Type", "Extrapolated")
GuiIC.Set([18], "Flow/T", 300)
GuiIC.Set([18], "Flow/u", 4000)
GuiIC.Set([18], "Chem/Mixture", "Mixture1")
GuiSC.Set("Shared/Transient_eval_method", "Transient")
GuiSC.Set("Iter/Cycles", 5000)
GuiSC.Set("Shared/EndTime", 1)
GuiSC.Set("Relax/RampingIterations", 2000)
GuiSC.Set("Spatial/SpatialAccuracyOrder", "Higher Order")
GuiSC.Set("Spatial/SpatialAccuracyOrder", "First Order")
GuiSC.Set("Spatial/LinearWaves", 0.3)
GuiSC.Set("Spatial/NonLinearWaves", 0.3)
GuiOut.Set("Output/OutputFrequency", "Specified Interval")
GuiOut.Set("Output/Output_Interval", 100)
GuiFILE.Save()
GuiRun.Submit()
GuiIC.Set([18], "Flow/p", 81.646)
GuiFILE.Save()
GuiRun.Submit()
GuiBC.Set([14], "Flow/Method_BC", "Profile from File")
GuiBC.Set([14], "Flow/Method_BC", "Constant")
GuiBC.Set([14], "Flow/p", 81.646)
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Submit()
GuiRun.Submit()
GuiRun.Submit()
GuiRun.Submit()
GuiRun.Submit()
GuiMO.Set("Chem/ThermalMode", "Two Temp. Non-Equilibrium")
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Submit()
GuiRun.Submit()
GuiFILE.CloseCurrentSim()
