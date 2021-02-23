import rpa as r
import pyautogui as p
import pandas as pd
import psutil


process_tee = "tee.exe"

for proc in psutil.process_iter():
    if proc.name() == process_tee:
        proc.kill()


r.init()
r.url('http://rpachallenge.com')
window = p.getActiveWindow().maximize()
p.sleep(5)

r.download('http://rpachallenge.com/assets/downloadFiles/challenge.xlsx', 'challenge.xlsx')
p.sleep(1)

dados = pd.read_excel('challenge.xlsx', sheet_name='Sheet1')

df = pd.DataFrame(dados, columns=["First Name", "Last Name ", "Company Name", "Role in Company", "Address", "Email", "Phone Number"])

r.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')

for row in df.itertuples():
    r.type('//*[@ng-reflect-name="labelFirstName"]', row[1])
    r.type('//*[@ng-reflect-name="labelLastName"]', row[2])
    r.type('//*[@ng-reflect-name="labelCompanyName"]', row[3])
    r.type('//*[@ng-reflect-name="labelRole"]', row[4])
    r.type('//*[@ng-reflect-name="labelAddress"]', row[5])
    r.type('//*[@ng-reflect-name="labelEmail"]', row[6])
    r.type('//*[@ng-reflect-name="labelPhone"]', str(row[7]))
    r.click('/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')

p.sleep(3)
p.screenshot('score.png')
window = p.getActiveWindow().close()

process_phantomjs = "phantomjs.exe"

for proc in psutil.process_iter():
    if proc.name() == process_phantomjs:
        proc.kill()
