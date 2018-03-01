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
GuiFILE.Open("C:/Users/spl4ckd/Documents/Aerospace.Courses/AE.295.A_B/Plasma Blackout/CFD/RAM/Sims/FASTRAN/Run 7 - 2D Body/RAM_C_II_2D.DTF")
GuiPT.Set("Chem", 1)
GuiMO.Set("Chem/ChemistryModel", "Reacting (Finite Rate)")
GuiMO.Set("Chem/ThermalMode", "Two Temp. Non-Equilibrium")
GuiMO.Set("Chem/SpeciesDatabase", "Molecular")
GuiDBM.Import("C:/Users/spl4ckd/Desktop/Reactions/Candler_MacCormack_Mix.sdb", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Import("C:/Users/spl4ckd/Desktop/Reactions/Mixture1.sdb", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Import("C:/Users/spl4ckd/Desktop/Reactions/forebody_reactions.sdb", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "O2(2)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "O2(1)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "O(2)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "O(1)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "NO(2)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "NO(1)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "N2(2)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "N2(1)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "N(1)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiMO.Set("Chem/BulkReaction", "forebody_Reactions")
GuiBC.Set([15], "Flow/u", 7650)
GuiBC.Set([15], "Flow/p", 19)
GuiBC.Set([15], "Flow/T", 300)
GuiBC.Set([15], "Chem/Mixture", "Mixture1")
GuiIC.Set([19], "Flow/u", 7650)
GuiIC.Set([19], "Flow/p", 19)
GuiIC.Set([19], "Flow/T", 300)
GuiIC.Set([19], "Chem/Mixture", "Mixture1")
GuiBC.Set([17], "Flow/Sub_Type", "Extrapolated")
GuiSC.Set("Shared/Transient_eval_method", "Transient")
GuiSC.Set("Shared/StartTime", 10)
GuiSC.Set("Shared/StartTime", 0)
GuiSC.Set("Shared/EndTime", 1)
GuiSC.Set("Iter/Cycles", 5000)
GuiSC.Set("Relax/RampingIterations", 2000)
GuiSC.Set("Spatial/LinearWaves", 0.30000001192)
GuiSC.Set("Spatial/NonLinearWaves", 0.30000001192)
GuiOut.Set("Output/OutputFrequency", "Specified Interval")
GuiOut.Set("Output/Output_Interval", 100)
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Stop()
