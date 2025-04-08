from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("./chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Doğru kullanıcı adı ve hatalı şifre
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()
message2 = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "flash"))
).text
if "Your password is invalid!" in message2:
    print("Şifre hatalı.")

# Hatalı kullanıcı adı ve doğru şifre
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("tom")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()
message2 = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "flash"))
).text
if "Your username is invalid!" in message2:
    print("Kullanıcı adı hatalı.")

# Başarılı giriş
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()
message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "flash"))
).text
if "You logged into a secure area!" in message:
    print("Başarılı giriş yapıldı.")

link = driver.current_url
if "secure" in link:
    print("Link secure içeriyor.")
else:
    print("HATA! Link secure içermiyor.")

baslik = driver.find_element(By.CSS_SELECTOR, "h2").text
if "Secure Area" in baslik:
    print("Sayfa başlığı Secure Area içeriyor.")
else:
    print("HATA! Sayfa başlığı Secure Area içermiyor.")

driver.find_element(By.XPATH, "//i[contains(text(),'Logout')]").click()
baslik2 = driver.find_element(By.CSS_SELECTOR, "h2").text
if "Login Page" in baslik2:
    print("Sayfa başlığı Login Page içeriyor.")
else:
    print("HATA! Sayfa başlığı Login Page içermiyor.")

link2 = driver.current_url
if "login" in link2:
    print("Link login içeriyor.")
else:
    print("HATA! Link login içermiyor.")

driver.quit()
