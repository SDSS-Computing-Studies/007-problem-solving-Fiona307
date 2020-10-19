# !python3

import pyautogui as p
import time as t

doLoop = True
count = 0
while doLoop:
    p.click(1118,470)
    count = count + 1
    if p.pixelMatchesColor(1691,896,(102,255,102)) == True:
        p.click(1691,896)
    if count == 50:
        count = 0
        p.click()
        doLoop = False