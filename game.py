# !python3

import pyautogui as p
import time as t

doLoop = True
count = 0
cursor = 0

while doLoop:
    p.click(1118,470)
    count = count + 1
    if count == 100:
        count = 0
        while p.pixelMatchesColor(1650,533,(16,40,54),tolerance=8):
            p.click(1650,533)
            #upgrade
        while p.pixelMatchesColor(1674,999,(255,255,255),tolerance = 10):
            p.click(1674,999)
        while p.pixelMatchesColor(1674,939,(255,255,255),tolerance = 10):
            p.click(1674,939)
        while p.pixelMatchesColor(1674,872,(255,255,255),tolerance = 10):
            p.click(1674,872)
        while p.pixelMatchesColor(1674,811,(255,255,255),tolerance = 10):
            p.click(1674,811)
        while p.pixelMatchesColor(1674,745,(255,255,255),tolerance = 10):
            p.click(1674,745)
        while p.pixelMatchesColor(1672,681,(255,255,255),tolerance = 10):
            p.click(1672,681)
        while p.pixelMatchesColor(1673,620,(255,255,255),tolerance = 10):
            p.click(1673,620)
            cursor = cursor +1
            if cursor == 50:
                break
        