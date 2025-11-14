from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)


    def find(self, by, selector):
        return self.wait.until(EC.presence_of_element_located((by, selector)))

    def finds(self, by, selector):
        return self.wait.until(EC.presence_of_all_elements_located((by, selector)))