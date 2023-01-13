from tkinter import image_types
import pyautogui
import time 

time.sleep(10)

def mesaj():
    pyautogui.write("AMI PATLAMIS OHH")
    pyautogui.press('enter')

sayac=0

while sayac<75: #göndermek istediğiniz adeti girin
    mesaj()
    time.sleep(0)
    sayac=sayac+1

