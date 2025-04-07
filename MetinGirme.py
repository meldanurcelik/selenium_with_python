from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("./chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://duckduckgo.com/")
driver.maximize_window()
aramakutusu = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "searchbox_input"))
)
aramakutusu.send_keys("selenium")
# aramakutusu.send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, ".iconButton_button__A_Uiu.searchbox_searchButton__LxebD").click()
driver.find_element(By.ID, "r1-2").click()

driver.quit()
