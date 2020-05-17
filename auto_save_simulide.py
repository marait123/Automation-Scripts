#@author Mohammed Ibrahim Gaballah
#requirements
#pip install pynput


from pynput.keyboard import Key, Controller
import time
import win32gui as w
keyboard = Controller()
timeInSeconds = 20
windowName = 'simulide'
##
##time.sleep(10)
##print(w.GetWindowText (w.GetForegroundWindow()))
##'SimulIDE'
print("auto save started")
while(True):    
    x = w.GetWindowText (w.GetForegroundWindow())
    time.sleep(timeInSeconds)
    if x[0:len(windowName)].lower() == windowName:
        print('saving')        
        keyboard.press(Key.ctrl);
        keyboard.press('s')
        keyboard.release('s')
        keyboard.release(Key.ctrl);

