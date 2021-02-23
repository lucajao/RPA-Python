import pyautogui as p

p.hotkey('win', 'r')
p.sleep(1)
p.write('C:\RPA.pbix') # Deixar o arquivo direto no C:/
p.sleep(1)
p.press('enter')
p.sleep(20)
p.getActiveWindow().maximize()
p.moveTo(x=879, y=112)
p.click()
p.sleep(7)
p.moveTo(x=1889, y=19)
p.sleep(2)
p.click()
p.moveTo(x=980, y=561)
p.sleep(1)
p.click()

# # Descobrir a localização de X e Y:
# p.sleep(3)
# print(p.position())
