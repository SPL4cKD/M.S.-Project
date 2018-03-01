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
GuiSC.Set("Relax/InitialCFL", 0.001)
GuiFILE.Save()
GuiSC.Set("Relax/RampingIterations", 250)
GuiFILE.Save()
GuiSC.Set("Spatial/SpatialAccuracyOrder", "Higher Order")
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Submit()
GuiDBM.Copy(GuiDBM.SPECIES, "C", GuiDBM.LOCAL, "C", GuiDBM.MODEL, "", "RAM_C_II_2D", True)
GuiDBM.SetList(GuiDBM.SPECIES, "C", "Physical-Chemical/Characteristic Vibration Modes/No. of Degeneracies Per Mode", [], GuiDBM.MODEL)
GuiDBM.SetList(GuiDBM.SPECIES, "C", "Physical-Chemical/Characteristic Vibration Modes/Characteristic Wave Number", [], GuiDBM.MODEL)
GuiDBM.AddToComposition(GuiDBM.SPECIES, "NO+", "E", -1, GuiDBM.MODEL)
GuiDBM.AddToComposition(GuiDBM.MIXTURE, "Candler_MacCormack", "C", 0.000000, GuiDBM.MODEL)
GuiDBM.Set(GuiDBM.BULKREACTION, "Candler_MacCormack", "Units", "cgs", GuiDBM.MODEL)
GuiDBM.Set(GuiDBM.BULKREACTION, "Candler_MacCormack", "Units", "SI", GuiDBM.MODEL)
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Submit()
GuiFILE.CloseAllSim()
