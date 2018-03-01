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
GuiFILE.Open("C:/Users/spl4ckd/Documents/Aerospace.Courses/AE.295.A_B/Plasma Blackout/CFD/RAM/Sims/FASTRAN/Past runs - Run 9/Run 9 - 81km - Laminar/RAM_C_II_2D.DTF")
GuiRun.Submit()
GuiFILE.CloseAllSim()
