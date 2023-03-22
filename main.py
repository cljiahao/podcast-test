import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class spotifyUpload():
    def __init__(self):

        load_dotenv()
        user = os.getenv("USER")
        pwd = os.getenv("PASS")

        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--remote-debugging-port=9222')
        chrome_options.binary_location = '/usr/bin/google-chrome'
        chrome_options.headless = True
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
        self.wait = WebDriverWait(self.driver, 300)
        self.login(user,pwd)
        self.uploadFiles(os.path.join(os.getcwd(),"spotify","Eng"),"test.mp3")
        print("Published")

    def login(self,user,pwd):
        
        self.driver.get("https://podcasters.spotify.com/pod/login")

        username = self.wait.until(EC.presence_of_element_located((By.NAME,"email")))
        password = self.driver.find_element(By.NAME,"password")

        username.send_keys(user)
        password.send_keys(pwd)
        username.submit()        # Submit Login

    def uploadFiles(self,spotPath,fileName):
        
        uploadepisode = self.wait.until(EC.presence_of_element_located((By.XPATH,'//input[@type="file"]')))
        uploadepisode.send_keys(os.path.join(spotPath,fileName))
        self.driver.save_screenshot("image.png")
        print(uploadepisode)

spotifyUpload()