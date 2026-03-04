from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class SeleniumHomePageTest(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_homepage_load(self):
        self.driver.get(self.live_server_url)

        body = self.driver.find_element(By.TAG_NAME, "body")

        self.assertIn("Online Exams", body.text)

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
# Create your tests here.
