import schedule
import time
from bot_Scheduler import Bot01

# Escolher umas das funções e substituir "job" pelo nome da função importada.

# schedule.every(10).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
schedule.every().day.at("10:41").do(Bot01)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)