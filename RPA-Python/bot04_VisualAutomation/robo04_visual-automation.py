import pyautogui as p

p.doubleClick(x=49, y=688)
p.sleep(3)
p.getActiveWindow().maximize()
p.write('http://udemy.com')
p.press('enter')
p.sleep(3)

localPesq = p.locateOnScreen('Pesquisa.PNG', confidence=0.9)
localPesquisa = p.center(localPesq)
xPesq, yPesq = localPesquisa
p.moveTo(xPesq, yPesq, duration=1)
p.click(xPesq, yPesq)
p.sleep(1)
p.write('RPA')
p.press('enter')
p.sleep(1)
p.screenshot('Cursos RPA.png')
p.sleep(1)

localClose = p.locateOnScreen('Close.PNG', confidence=0.9)
localExit = p.center(localClose)
xClose, yExit = localExit
p.moveTo(xClose, yExit, duration=1)
p.click(xClose, yExit)