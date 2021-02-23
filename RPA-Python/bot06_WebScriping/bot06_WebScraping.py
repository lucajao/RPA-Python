import rpa as r
import pyautogui as p
import psutil
import pandas as pd
import os as o

process_tee = "tee.exe"

for proc in psutil.process_iter():
    if proc.name() == process_tee:
        proc.kill()

r.init()
r.url('https://rpachallengeocr.azurewebsites.net/')
window = p.getActiveWindow().maximize()
p.sleep(2)

countPage = 1
while countPage <= 3:
    if countPage == 1:
        r.table('//*[@id="tableSandbox"]', 'Temp.csv')
        dados = pd.read_csv('Temp.csv')
        dados.to_csv(r'WebTable.csv', mode='a', index=None, header=True)
        p.moveTo(x=1861, y=584)
        p.click()
        countPage += 1
    else:
        r.table('//*[@id="tableSandbox"]', 'Temp.csv')
        dados = pd.read_csv('Temp.csv')
        dados.to_csv(r'WebTable.csv', mode='a', index=None, header=False)
        p.moveTo(x=1861, y=584)
        p.click()
        countPage += 1
p.moveTo(x=1890, y=16)
p.click()
o.remove('Temp.csv')
csv_xlsx = pd.read_csv(r'WebTable.csv')
csv_xlsx.to_excel(r'WebTable02.xlsx')


process_phantomjs = "phantomjs.exe"

for proc in psutil.process_iter():
    if proc.name() == process_phantomjs:
        proc.kill()


