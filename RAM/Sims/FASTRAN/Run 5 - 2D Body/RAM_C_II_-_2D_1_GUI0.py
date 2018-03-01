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
GuiFILE.Open("C:/Users/spl4ckd/Documents/Aerospace.Courses/AE.295.A_B/Plasma Blackout/CFD/RAM/Sims/FASTRAN/Run 5 - 2D Body/RAM C II - 2D_1.DTF")
GuiPT.Set("Chem", 1)
GuiMO.Set("Chem/ChemistryModel", "Reacting (Finite Rate)")
GuiDBM.Import("C:/Users/spl4ckd/Desktop/Reactions/Candler_MacCormack.sdb", GuiDBM.MODEL, "RAM_C_II_-_2D_1")
GuiDBM.Import("C:/Users/spl4ckd/Desktop/Reactions/Candler_MacCormack_Mix.sdb", GuiDBM.MODEL, "RAM_C_II_-_2D_1")
GuiDBM.Delete(GuiDBM.SPECIES, "O2(1)", GuiDBM.MODEL, "RAM_C_II_-_2D_1")
GuiDBM.Delete(GuiDBM.SPECIES, "O(1)", GuiDBM.MODEL, "RAM_C_II_-_2D_1")
GuiDBM.Delete(GuiDBM.SPECIES, "NO(1)", GuiDBM.MODEL, "RAM_C_II_-_2D_1")
GuiDBM.Delete(GuiDBM.SPECIES, "N2(1)", GuiDBM.MODEL, "RAM_C_II_-_2D_1")
GuiDBM.SetList(GuiDBM.SPECIES, "E", "Physical-Chemical/Characteristic Vibration Modes/No. of Degeneracies Per Mode", [], GuiDBM.MODEL)
GuiDBM.SetList(GuiDBM.SPECIES, "E", "Physical-Chemical/Characteristic Vibration Modes/Characteristic Wave Number", [], GuiDBM.MODEL)
GuiMO.Set("Chem/SpeciesDatabase", "Molecular")
GuiMO.Set("Chem/BulkReaction", "Candler_MacCormack")
GuiBC.Set([15], "Flow/u", 7650)
GuiBC.Set([15], "Flow/p", 19)
GuiBC.Set([15], "Flow/T", 300)
GuiBC.Set([15], "Chem/Mixture", "Candler_MacCormack")
GuiBC.Set([18], "Flow/Sub_Type", "Extrapolated")
GuiIC.Set([19], "Flow/u", 7650)
GuiIC.Set([19], "Flow/p", 19)
GuiIC.Set([19], "Flow/T", 300)
GuiIC.Set([19], "Chem/Mixture", "Candler_MacCormack")
GuiSC.Set("Shared/Transient_eval_method", "Transient")
GuiSC.Set("Iter/Cycles", 5000)
GuiSC.Set("Shared/EndTime", 1)
GuiSC.Set("Shared/StartTime", 0)
GuiSC.Set("Relax/InitialCFL", 0.001)
GuiSC.Set("Relax/RampingIterations", 2000)
GuiFILE.Save()
GuiSC.Set("Spatial/SpatialAccuracyOrder", "Higher Order")
GuiOut.Set("Output/OutputFrequency", "Specified Interval")
GuiOut.Set("Output/Output_Interval", 100)
GuiFILE.Save()
GuiRun.Submit()
GuiSC.Set("Solvers/Sub-iterations", 50)
GuiSC.Set("Relax/InitialCFL", 0.0001)
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Stop()
GuiDBM.SetListWithIndex(GuiDBM.BULKREACTION, "Candler_MacCormack", "ReactStep/Equation", 3, "NO+M<->N+O+M", GuiDBM.MODEL)
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Submit()
GuiRun.Submit()
GuiSC.Set("Spatial/SpatialAccuracyOrder", "First Order")
GuiFILE.Save()
GuiSC.Set("Spatial/LinearWaves", 0.3)
GuiSC.Set("Spatial/NonLinearWaves", 0.3)
GuiFILE.Save()
GuiDBM.SetListWithIndex(GuiDBM.BULKREACTION, "Candler_MacCormack", "ReactStep/Equation", 1, "N2+M<->2N+M", GuiDBM.MODEL)
GuiDBM.SetListWithIndex(GuiDBM.BULKREACTION, "Candler_MacCormack", "ReactStep/Equation", 2, "O2+M<->2O+M", GuiDBM.MODEL)
GuiDBM.SetListWithIndex(GuiDBM.BULKREACTION, "Candler_MacCormack", "ReactStep/Forward_Ap", 1, 7E+018, GuiDBM.MODEL)
GuiDBM.SetListWithIndex(GuiDBM.BULKREACTION, "Candler_MacCormack", "ReactStep/Forward_Ap", 2, 2E+018, GuiDBM.MODEL)
GuiDBM.SetListWithIndex(GuiDBM.BULKREACTION, "Candler_MacCormack", "ReactStep/Forward_Ap", 3, 5E+012, GuiDBM.MODEL)
GuiDBM.SetListWithIndex(GuiDBM.BULKREACTION, "Candler_MacCormack", "ReactStep/Forward_n", 2, -1.5, GuiDBM.MODEL)
GuiDBM.SetListWithIndex(GuiDBM.BULKREACTION, "Candler_MacCormack", "ReactStep/Forward_n", 3, 0, GuiDBM.MODEL)
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Submit()
GuiRun.Submit()
GuiRun.Stop()
GuiFILE.CloseCurrentSim()
