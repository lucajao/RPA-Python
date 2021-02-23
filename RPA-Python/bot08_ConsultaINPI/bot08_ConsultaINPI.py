from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time as t
import pyautogui as p

nav = Chrome()
nav.get('https://gru.inpi.gov.br/pePI/servlet/LoginController?action=login')
nav.maximize_window()
t.sleep(1)
avancar = nav.find_element_by_id('details-button').click()
t.sleep(1)
nav.find_element_by_id('proceed-link').click()
t.sleep(3)
nav.find_element_by_xpath('//map/area[2]').click()
t.sleep(3)
nav.find_element_by_name('ExpressaoPesquisa').send_keys('03768202000176')
t.sleep(0.5)
nav.find_element_by_xpath('//select[2]/option[4]').click()
t.sleep(1)
nav.find_element_by_css_selector('input[type="submit"]').click()






