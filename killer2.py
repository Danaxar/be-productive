import win32console
import win32gui
import time

ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana, 0)  # No muestres la ventana pero no la cierres

while True:
    print("Hola mundo")
    time.sleep(2)