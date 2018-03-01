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
GuiFILE.Open("C:/Users/spl4ckd/Documents/Aerospace.Courses/AE.295.A_B/Plasma Blackout/CFD/RAM/Sims/FASTRAN/Run 9 - 2D Body/RAM_C_II_2D.DTF")
GuiDBM.Import("C:/Users/spl4ckd/Desktop/Reactions/RAM_C_-_2D_BODY_1.sdb", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "O2(1)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "O(1)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "NO+(1)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "NO(1)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "N2(1)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "N(1)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "M(1)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.Delete(GuiDBM.SPECIES, "E(1)", GuiDBM.MODEL, "RAM_C_II_2D")
GuiDBM.AddToComposition(GuiDBM.SPECIES, "NO+", "E", -1, GuiDBM.MODEL)
GuiMO.Set("Flow/ViscousModel", "Inviscid (Euler)")
GuiSC.Set("Spatial/SpatialAccuracyOrder", "First Order")
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Stop()
GuiMO.Set("Chem/BulkReaction", "Reactions_1")
GuiDBM.AddItem(GuiDBM.MIXTURE, "New_Mixture", GuiDBM.MODEL)
GuiDBM.AddToComposition(GuiDBM.MIXTURE, "New_Mixture", "N2", 0.770000, GuiDBM.MODEL)
GuiDBM.AddToComposition(GuiDBM.MIXTURE, "New_Mixture", "O2", 0.230000, GuiDBM.MODEL)
GuiDBM.Rename(GuiDBM.MIXTURE, "New_Mixture", "Mixture_2", GuiDBM.MODEL)
GuiBC.Set([11], "Chem/Mixture", "Mixture_2")
GuiBC.Set([11], "Flow/T", 300)
GuiBC.Set([11], "Flow/p", 0.0001)
GuiFILE.Save()
GuiBC.Set([11], "Flow/p", 0.0001)
GuiBC.Set([11], "Flow/u", 4000)
GuiBC.Set([11], "Chem/InternalT", 300)
GuiIC.Set([15], "Flow/u", 4000)
GuiIC.Set([15], "Flow/p", 0.0001)
GuiIC.Set([15], "Flow/T", 300)
GuiIC.Set([15], "Chem/InternalT", 300)
GuiIC.Set([15], "Chem/Mixture", "Mixture_2")
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Stop()
GuiIC.Set([15], "Flow/u", 7650)
GuiIC.Set([15], "Flow/p", 4.5)
GuiIC.Set([15], "Flow/T", 176.9716)
GuiIC.Set([15], "Chem/InternalT", 176.9716)
GuiBC.Set([11], "Chem/InternalT", 176.9716)
GuiBC.Set([11], "Flow/u", 7650)
GuiBC.Set([11], "Flow/p", 4.5)
GuiBC.Set([11], "Flow/T", 176.9716)
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Stop()
GuiSC.Set("Relax/InitialCFL", 0.1)
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Stop()
GuiIC.Set([15], "Chem/Mixture", "Mixture_1")
GuiIC.Set([15], "Chem/Mixture", "Mixture_1")
GuiBC.Set([11], "Chem/Mixture", "Mixture_1")
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Stop()
GuiSC.Set("Relax/InitialCFL", 0.001)
GuiFILE.Save()
GuiMO.Set("Chem/BulkReaction", "Candler_MacCormack")
GuiMO.Set("Shared/Polar", "Axisymmetric")
GuiBC.Set([11], "Chem/Mixture", "Candler_MacCormack")
GuiIC.Set([15], "Chem/Mixture", "Candler_MacCormack")
GuiSC.Set("Spatial/SpatialAccuracyOrder", "Higher Order")
GuiSC.Set("Solvers/TimeAccuracyScheme", "Second-Order Backward")
GuiSC.Set("Solvers/TimeAccuracyScheme", "Backward Euler")
GuiFILE.Save()
GuiRun.Submit()
GuiSC.Set("Spatial/FluxLimiter", "Osher-C(L)")
GuiFILE.Save()
GuiSC.Set("Solvers/TimeAccuracyScheme", "Second-Order Backward")
GuiSC.Set("Spatial/SpatialAccuracyOrder", "First Order")
GuiSC.Set("Relax/InitialCFL", 0.01)
GuiFILE.Save()
GuiSC.Set("Shared/Transient_eval_method", "Steady")
GuiSC.Set("Shared/Transient_eval_method", "Transient")
GuiFILE.Save()
