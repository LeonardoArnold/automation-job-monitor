from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WebBot:
    def __init__(self):
        self.chrome_options = Options()
        # Rodar em modo headless (opcional) ajuda a economizar tempo e CPU
        # self.chrome_options.add_argument("--headless") 
        self.chrome_options.add_argument("--start-maximized")

    def run_automation(self):
        start_time = time.time()
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=self.chrome_options)
        
        try:
            driver.get("https://sicredi.gupy.io/")
            wait = WebDriverWait(driver, 15) # Espera até 15 segundos
            
            # Tentando um seletor mais genérico que a Gupy usa para títulos de vagas
            vagas_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/jobs/')]")))
            
            # Pega o texto e limpa espaços extras
            lista_vagas = [v.text.strip().split('\n')[0] for v in vagas_elements if v.text.strip()][:3]
            
            duration = time.time() - start_time
            return {
                "status": "success", 
                "msg": f"Vagas: {', '.join(lista_vagas)}",
                "duration": round(duration, 2)
            }
            
        except Exception as e:
            # Isso vai nos dizer exatamente onde o robô travou
            return {"status": "failed", "error": str(e)[:50], "duration": round(time.time() - start_time, 2)}
        finally:
            driver.quit()