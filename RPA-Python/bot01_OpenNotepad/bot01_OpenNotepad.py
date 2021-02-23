# Script capaz de abrir a janela "executar", digitar o comando "notepad", digitar uma frase, renomear o arquivo e salva-lo automaticamente no Desktop.

import pyautogui as p

p.hotkey('win', 'r')
p.sleep(1)
p.typewrite('notepad')
p.sleep(1)
p.press('enter')
p.sleep(1)
p.typewrite("Hello, world! I'm a bot able to control your mouse e keyboard!")
p.sleep(3)
close_window = p.getActiveWindow()
close_window.close()
p.press('enter')
p.sleep(1)
p.press('enter')
p.typewrite('bot_notepad.txt')
p.press('enter')
