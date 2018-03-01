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
GuiFILE.Open("C:/Users/spl4ckd/Documents/Aerospace.Courses/AE.295.A_B/Plasma Blackout/CFD/RAM/Sims/FASTRAN/Run 8 - 2D Body/RAM_C_II_2D.DTF")
GuiRun.Submit()
GuiSC.Set("Relax/InitialCFL", 0.001)
GuiSC.Set("Relax/FinalCFL", 0.1)
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Submit()
GuiSC.Set("Shared/TimeStep_eval_method", "Direct Specification of dt")
GuiSC.Set("Relax/RampingIterations", 2000)
GuiFILE.Save()
GuiRun.Submit()
GuiSC.Set("Solvers/TimeIntegration_eval_method", "Implicit Iterative")
GuiSC.Set("Solvers/TimeIntegration_eval_method", "Implicit Non-Iterative")
GuiFILE.Save()
GuiRun.Stop()
GuiSC.Set("Solvers/Sub-iterations", 40)
GuiFILE.Save()
GuiSC.Set("Relax/Initialdt", 1e-8)
GuiSC.Set("Relax/Finaldt", 1e-7)
GuiFILE.Save()
GuiRun.Submit()
GuiRun.Stop()
GuiFILE.CloseCurrentSim()
