from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class DriverManager:
    def __init__(self, headless=True):
        opts = Options()
        if headless:
            opts.add_argument('--headless=new')
            opts.add_argument('--no-sandbox')
            opts.add_argument('--disable-dev-shm-usage')
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)


    def get(self):
        return self.driver

    def quit(self):
        try:
            self.driver.quit()
        except Exception:
            pass