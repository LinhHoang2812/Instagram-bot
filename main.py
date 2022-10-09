import selenium
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

INSTA_EMAIL = os.environ["EMAIL"]
INSTA_PASS = os.environ["PASSWORD"]
SIMILAR_ACCOUNT_EN = "data.science.beginners"
SIMILAR_ACCOUNT_VI = "thepresentwriter"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

class InstaFollower():
    def __init__(self):
        self.driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

    def log_in(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        cookies = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div/button[1]')
        cookies.click()
        time.sleep(5)

        user_name = self.driver.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
        user_name.send_keys(INSTA_EMAIL)

        password = self.driver.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
        password.send_keys(INSTA_PASS)

        log_in = self.driver.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div')
        log_in.click()

        time.sleep(10)
        no_save = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button')
        no_save.click()

        time.sleep(5)
        no_notif = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        no_notif.click()
    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT_VI}/")
        main_page = self.driver.current_window_handle
        time.sleep(10)
        followers = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        for handle in self.driver.window_handles:
            if handle!= main_page:
                popup = handle
                self.driver.switch_to.window(popup)
        time.sleep(5)
        ## scroll from the top to the element height and load all the followers
        for _ in range(25):
            time.sleep(2)
            scroll = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)


    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR,"._acas")
        for button in follow_buttons:
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", button)


bot = InstaFollower()
bot.log_in()
bot.find_followers()
bot.follow()
