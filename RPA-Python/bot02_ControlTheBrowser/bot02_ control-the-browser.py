import rpa as r
import psutil
import pyautogui as p


process_tee = "tee.exe"

for proc in psutil.process_iter():
    if proc.name() == process_tee:
        proc.kill()


r.init(visual_automation=False, chrome_browser=True)
r.url('http://www.google.com.br')
window = p.getActiveWindow()
window.maximize()
r.wait(2.0)
r.type('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input', 'RPA[enter]')
r.wait(2.0)
r.snap('page', 'rpa_page2.png')
r.wait(1)
window.close()




