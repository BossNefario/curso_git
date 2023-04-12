from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

servico = Service(GeckoDriverManager().install())

navegador = webdriver.Firefox(service=servico)
navegador.get('http://publicazo.insprak.com/sign_in')
navegador.find_element('xpath','//*[@id="user_email"]').send_keys('tobio@tobio.com')
navegador.find_element('xpath','//*[@id="user_password"]').send_keys('marmota')
navegador.find_element('xpath','/html/body/div/div/div/form/div[4]/input').click()