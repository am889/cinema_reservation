# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import logging
# from selenium.webdriver.remote.remote_connection import LOGGER
# LOGGER.setLevel(logging.INFO)
# # Path to the Chrome WebDriver executable
# webdriver_path = 'C:\\Users\\Thndr\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

# service = Service(webdriver_path)
# options=webdriver.ChromeOptions()
# # options.add_argument("disable-infobar")
# # options.add_argument("--disable-blink-features=AutomationControlled")
# # options.add_argument("start-maximized")
# # options.add_argument("disable-dev-shm-usage")
# # options.add_argument("no-sandbox")
# # options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors
# # options.add_argument("--allow-insecure-localhost")  # Allow insecure connections

# driver = webdriver.Chrome(service=service, options=options)

# url=("https://dashboard.stripe.com/dashboard")
# # link_home = driver.find_element(By.TAG_NAME,'body')
# driver.get(url)
# print(driver.title)
# # try:
# #     # Navigate to the URL with retries
# #     for attempt in range(3):  # Retry up to 3 times
# #         try:
# #             driver.get(url)
# #             # Wait for an element identified by its XPath to be present
# #             # element_xpath = '/html/body/form/table/tbody/tr[2]/td/center/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/a' 
# #             # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, tag)))
# #             # Print the page source
# #             print(driver.page_source)
# #             break  # If successful, break out of the loop
# #         except Exception as e:
# #             print(f"Attempt {attempt + 1} failed: {e}")
# #             time.sleep(5)  # Wait before retrying
# #     else:
# #         print("Failed to load the page after multiple attempts")

# # except Exception as e:
# #     print(f"An error occurred: {e}")

# # finally:
    
# #     driver.quit()


# # import requests 
# # import certifi
# # from bs4 import BeautifulSoup 

# # # cert = ("C:\\Users\\Thndr\\Downloads\\egx-cert.pem", "C:\\Users\\Thndr\\Downloads\\egx-key.pem")

# # URL = "http://egx.com.eg/ar/BulletinNews.aspx" 
# # r = requests.get(URL)

# # print(r.text)
# # # soup = BeautifulSoup(r.content, 'html5lib') 
# # # print(soup.prettify())
name = input("Your Name").strip().title().rstrip()
print(name)