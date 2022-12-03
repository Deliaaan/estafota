import time

from selenium import webdriver
from selenium.common.keys import keys

driver = webdriver.Firefox()
driver.get('https://www.estafeta.com/Herramientas/Rastreo')


driver.refresh()
time.sleep(5)