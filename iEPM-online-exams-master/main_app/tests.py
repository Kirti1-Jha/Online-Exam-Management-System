from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


class SeleniumHomePageTest(LiveServerTestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

    def test_homepage_load(self):
        self.driver.get(self.live_server_url)

        body = self.driver.find_element(By.TAG_NAME, "body")
        self.assertIn("Online Exams", body.text)

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
