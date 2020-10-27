# !python3

import pyautogui as p
import time as t


# Only works when the cookie cliker game is on the right half side of the screen
doLoop = True
count = 0
a = 0
while doLoop:
    p.click(1118,470)
    count = count + 1
    a = a + 1
    if count == 150:
        count = 0
        while p.pixelMatchesColor(1650,533,(16,40,54),tolerance= 0.9):
            p.click(1650,533)
            #upgrade
        while p.pixelMatchesColor(1674,995,(255,255,255),tolerance = 0.9):
            p.click(1674,995)
        while p.pixelMatchesColor(1674,939,(255,255,255),tolerance = 0.9):
            p.click(1674,939)
        while p.pixelMatchesColor(1674,872,(255,255,255),tolerance = 0.9):
            p.click(1674,872)
        while p.pixelMatchesColor(1674,811,(255,255,255),tolerance = 0.9):
            p.click(1674,811)
        while p.pixelMatchesColor(1674,745,(255,255,255),tolerance = 0.9):
            p.click(1674,745)
        while p.pixelMatchesColor(1672,681,(255,255,255),tolerance = 0.9):
            p.click(1672,681)
        while p.pixelMatchesColor(1673,620,(255,255,255),tolerance = 0.9):
            p.click(1673,620)
    if a == 600:
        a = 0
        if p.confirm(text='Stop the program?',title='',buttons=['Stop','Continue']) == 'Stop':
            doLoop = False
