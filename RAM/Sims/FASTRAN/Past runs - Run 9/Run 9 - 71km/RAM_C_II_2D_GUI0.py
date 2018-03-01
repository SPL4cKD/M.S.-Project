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
GuiMO.Set("Flow/ViscousModel", "Inviscid (Euler)")
GuiMO.Set("Flow/ViscousModel", "Laminar (Navier-Stokes)")
GuiBC.Set([13], "Flow/Sub_Type", "Extrapolated")
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Submit()
GuiRun.Submit()
GuiDBM.AddToComposition(GuiDBM.SPECIES, "NO+", "E", -1, GuiDBM.MODEL)
GuiDBM.Copy(GuiDBM.SPECIES, "C", GuiDBM.LOCAL, "C", GuiDBM.MODEL, "", "RAM_C_II_2D", True)
GuiDBM.SetList(GuiDBM.SPECIES, "C", "Physical-Chemical/Characteristic Vibration Modes/No. of Degeneracies Per Mode", [], GuiDBM.MODEL)
GuiDBM.SetList(GuiDBM.SPECIES, "C", "Physical-Chemical/Characteristic Vibration Modes/Characteristic Wave Number", [], GuiDBM.MODEL)
GuiFILE.Save()
GuiRun.Stop()
GuiRun.Submit()
GuiRun.Submit()
GuiFILE.Save()
GuiRun.Submit()
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Submit()
