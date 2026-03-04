from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from webdriver_manager.chrome import ChromeDriverManager
import time


class SeleniumHomeTest(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_homepage_load(self):
        self.driver.get(self.live_server_url)

        body = self.driver.find_element(By.TAG_NAME, "body")
        self.assertIn("Online Exams System", body.text)

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
