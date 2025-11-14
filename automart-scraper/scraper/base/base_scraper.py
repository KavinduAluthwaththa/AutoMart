class BaseScraper:
    def __init__(self, driver):
        self.driver = driver


    def scrape(self):
        raise NotImplementedError