from ast import UAdd
from codecs import utf_16_be_decode
from socket import has_dualstack_ipv6
import pyautogui
import webbrowser as wb
import time


wb.open("https://web.whatsapp.com")
time.sleep(10)
for i in range(400):
    pyautogui.press("G")
    pyautogui.press("o")
    pyautogui.press("o")
    pyautogui.press("d")
    pyautogui.press(" ")
    pyautogui.press("M")
    pyautogui.press("o")
    pyautogui.press("r")
    pyautogui.press("n")
    pyautogui.press("i")
    pyautogui.press("n")
    pyautogui.press("g")
    pyautogui.press("enter")
