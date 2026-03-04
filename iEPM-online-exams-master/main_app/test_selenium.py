from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumHomeTest(LiveServerTestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")   # required for Jenkins
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def test_homepage_load(self):
        self.driver.get(self.live_server_url)

        body = self.driver.find_element(By.TAG_NAME, "body")
        self.assertIn("Online Exams", body.text)

    def tearDown(self):
        self.driver.quit()
