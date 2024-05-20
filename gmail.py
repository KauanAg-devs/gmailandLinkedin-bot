import time  # Importe a biblioteca de tempo

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pag

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Edge(options=options)

def main():
    driver.get("https://mail.google.com/mail/u/0/#inbox")
    driver.find_element(By.ID, 'identifierId').send_keys('@gmail.com')

    time.sleep(2)  # Adiciona um atraso de 2 segundos

    pag.press('enter')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))

main()
