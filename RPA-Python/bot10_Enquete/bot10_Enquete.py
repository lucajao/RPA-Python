from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time as t

nav = Chrome()
nav.get('https://ferendum.com/pt/')
nav.maximize_window()
t.sleep(3)
nav.find_element_by_name('titulo').send_keys('A automação é algo bom? (João Lucas)')
nav.find_element_by_name('descripcion').send_keys('Os robôs estão cada vez mais frequentes em nossas vidas..')
nav.find_element_by_name('creador').send_keys('João Lucas Curso RPA com Python')
nav.find_element_by_css_selector('input[type="email"]').send_keys('joaolucas.mdk@outlook.com.br')
nav.find_element_by_id('op1').send_keys('Sim! Ela me ajuda muito.')
nav.find_element_by_id('op2').send_keys('Não! Temo perder o emprego!')
nav.find_element_by_name('config_anonimo').click()
nav.find_element_by_name('config_priv_pub').click()
nav.find_element_by_name('config_un_solo_voto').click()
nav.find_element_by_name('accept_terms_checkbox').click()
t.sleep(0.5)
nav.find_element_by_css_selector('input[value="Criar enquete"]').click()
nav.find_element_by_id('crear_votacion').click()
t.sleep(3)
link = nav.find_element_by_id('textoACopiar').click()
