from tkinter import image_types
import pyautogui
import time 

time.sleep(10)

def mesaj():
    pyautogui.write("Bu alana göndermek isteğiniz mesajı yazınız")
    pyautogui.press('enter')

sayac=0

while sayac<50: #göndermek istediğiniz adeti girin
    mesaj()
    time.sleep(0)
    sayac=sayac+1

