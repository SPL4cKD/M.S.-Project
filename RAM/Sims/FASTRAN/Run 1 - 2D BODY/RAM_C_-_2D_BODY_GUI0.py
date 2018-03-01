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
GuiVersion.RecordVersion("2017.0.0.11893")

GuiFILE.SetMode("FASTRAN")
GuiFILE.Open("C:/Users/spl4ckd/Documents/Aerospace.Courses/AE.295.A_B/Plasma Blackout/CFD/RAM/Sims/FASTRAN/Run 1 - 2D BODY/RAM_C_-_2D_BODY.DTF")
GuiPT.Set("Chem", 1)
GuiMO.Set("Shared/Polar", "Axisymmetric")
GuiMO.Set("Chem/ThermalMode", "Two Temp. Non-Equilibrium")
GuiMO.Set("Chem/SpeciesDatabase", "Molecular")
GuiMO.Set("Chem/ChemistryModel", "Reacting (Finite Rate)")
GuiDBM.Import("C:/Users/spl4ckd/Desktop/Reactions/Mixture1.sdb", GuiDBM.MODEL, "RAM_C_-_2D_BODY")
GuiDBM.Import("C:/Users/spl4ckd/Desktop/Reactions/Reactions.sdb", GuiDBM.MODEL, "RAM_C_-_2D_BODY")
GuiDBM.Import("C:/Users/spl4ckd/Desktop/Reactions/EBU.sdb", GuiDBM.MODEL, "RAM_C_-_2D_BODY")
GuiMO.Set("Chem/BulkReaction", "Reactions")
GuiMO.Set("Chem/ThermalMode", "Two Temp. Non-Equilibrium")
GuiBC.Set([14], "Flow/Sub_Type", "Extrapolated")
GuiBC.Set([13], "Flow/u", 7000)
GuiBC.Set([13], "Flow/p", 5.25)
GuiBC.Set([13], "Flow/T", 219.7)
GuiBC.Set([13], "Chem/InternalT", 219.7)
GuiBC.Set([13], "Chem/Mixture", "Mixture1")
GuiIC.Set([17], "Flow/u", 7000)
GuiIC.Set([17], "Flow/p", 5.25)
GuiIC.Set([17], "Flow/T", 219.7)
GuiIC.Set([17], "Chem/InternalT", 219.7)
GuiIC.Set([17], "Chem/Mixture", "Mixture1")
GuiSC.Set("Shared/Transient_eval_method", "Transient")
GuiSC.Set("Iter/Cycles", 130000)
GuiSC.Set("Shared/EndTime", 1)
GuiSC.Set("Shared/StartTime", 0)
GuiSC.Set("Relax/RampingIterations", 2000)
GuiSC.Set("Spatial/LinearWaves", 0.30000001192)
GuiSC.Set("Spatial/NonLinearWaves", 0.30000001192)
GuiOut.Set("Output/OutputFrequency", "Specified Interval")
GuiOut.Set("Output/Output_Interval", 100)
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Submit()
GuiFILE.SaveAs("C:/Users/spl4ckd/Documents/Aerospace.Courses/AE.295.A_B/Plasma Blackout/CFD/RAM/Sims/FASTRAN/Run 2 - 2D BODY/RAM_C_-_2D_BODY.DTF")
GuiSC.Set("Relax/RampingIterations", 127000)
GuiOut.Set("Output/Output_Interval", 2600)
GuiFILE.Save()
GuiRun.Submit()
GuiFILE.CloseCurrentSim()
