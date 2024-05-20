from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pag

def main():
    network_url = "https://linkedin.com/mynetwork/"
    driver = webdriver.Chrome()
    driver.get(network_url)
    
    try:
        # Realizar login
        driver.find_element(By.ID, "username").send_keys("@gmail.com")
        driver.find_element(By.ID, "password").send_keys("PASSWORD.")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Clica no botão de login

        # Verificar se o login foi bem-sucedido
        WebDriverWait(driver, 10).until(EC.url_contains("mynetwork"))
        send_requests(driver)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

def send_requests(driver):
    n = int(input("Número de solicitações: "))  # Número de solicitações que você deseja enviar

    for _ in range(n):
        try:
            # Esperar até que o botão de conexão esteja presente
            connect_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.artdeco-button--2.artdeco-button--secondary.ember-view.full-width"))
            )

            # Clicar em cada botão de conexão encontrado
            for button in connect_buttons:
                button.click()
                pag.sleep(1)  # Pausa para evitar problemas de sincronização
                
                # Esperar o botão de confirmação desaparecer (ou qualquer outro indicador de que a solicitação foi enviada)
                WebDriverWait(driver, 10).until(
                    EC.staleness_of(button)
                )
                
        except Exception as e:
            print(f"An error occurred while sending requests: {e}")
            break

if __name__ == "__main__":
    main()
    print("Feito!")
