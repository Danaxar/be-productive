import Config as cfg
import time
import psutil
import win32console
import win32gui

print("Starting the killer...")
myConfig = cfg.Config()
print("Programs to close:", myConfig.programsToClose)

ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana, 0)  # No muestres la ventana pero no la cierres

while True:
    time.sleep(1.0)
    for programName in myConfig.programsToClose:  # Recorrer cerrables
        for process in psutil.process_iter():     # Recorrer procesos
            if programName == process.name():     # Comparar
                process.kill()                    # Matar
                print(programName, " closed.")    # Notificar
