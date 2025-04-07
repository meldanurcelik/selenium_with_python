from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("./chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
driver.maximize_window()
seckin_madde_alani = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "mp-tfa"))
)
seckin_madde_metni = seckin_madde_alani.text
print(seckin_madde_metni.split(",")[0])

kaliteli_madde_alani = driver.find_element(By.ID, "mf-tfp")
kaliteli_madde_metni = kaliteli_madde_alani.text
print(kaliteli_madde_metni.split(",")[0])

driver.quit()
