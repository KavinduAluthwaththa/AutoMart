from ..base.base_scraper import BaseScraper
from ..base.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import json


class autolanka_scraper(BaseScraper):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = BasePage(driver)

    def _get_detail(self, field_class):
        try:
            return self.driver.find_element(By.XPATH, f"//div[@id='{field_class}']//div[@class='value']").text
        except Exception:
            return None

    def scrape(self):
        self.driver.get("https://www.autolanka.com/cars.html")
        time.sleep(1)
        
        print(f"Page title: {self.driver.title}")
        print(f"Current URL: {self.driver.current_url}")

        try:
            listings_container = self.page.find(By.ID, "listings")
            print(f"Found listings container")
        except Exception as e:
            print(f"Could not find listings container with ID 'listings': {e}")
            # Try alternative selectors
            try:
                listings_container = self.driver.find_element(By.TAG_NAME, "body")
                print("Using body as fallback")
            except:
                print("Failed to find any container")
                return []

        # Find all car listing items
        cars = listings_container.find_elements(By.CSS_SELECTOR, "article.item")
        print(f"Found {len(cars)} cars with article.item selector")
        
        if len(cars) == 0:
            print("No car listings found!")
            return []
        
        results = []
        print(f"Starting to scrape {len(cars)} cars...")

        for idx, car in enumerate(cars, 1):
            try:
                # Find the link-large anchor tag
                link_element = car.find_element(By.CLASS_NAME, "link-large")
                link = link_element.get_attribute("href")
                
                if not link:
                    print(f"Car {idx}: No href found")
                    continue
                
                print(f"\nCar {idx}/{len(cars)}: Navigating to {link}")
                
                # Navigate to detail page
                self.driver.get(link)

                # Extract details from the detail page
                try:
                    title = self.driver.find_element(By.TAG_NAME, "h1").text
                except:
                    title = "Unknown Title"
                
                print(f"  Title: {title}")
                
                try:
                    price = self.driver.find_element(By.CSS_SELECTOR, ".price-tag, [class*='price']").text
                except:
                    price = "N/A"
                
                try:
                    details = self.driver.find_element(By.CSS_SELECTOR, ".card-info, .listing-details")
                except:
                    details = self.driver.find_element(By.TAG_NAME, "body")

                body_style = self._get_detail("df_field_body_style")
                model_year = self._get_detail("df_field_built")
                condition = self._get_detail("df_field_condition")
                reference_no = self._get_detail("df_field_ref_number")
                transmission = self._get_detail("df_field_transmission")
                engine_cylinders = self._get_detail("df_field_engine_cylinders")
                fuel = self._get_detail("df_field_fuel")
                mileage = self._get_detail("df_field_mileage")
                doors = self._get_detail("df_field_doors")
                exterior_color = self._get_detail("df_field_exterior_color")
                interior_color = self._get_detail("df_field_interior_color")

                try:
                    additional_info = self.page.find(By.XPATH, "//div[contains(text(), 'Additional Information:')]/following-sibling::div").text
                except Exception:
                    additional_info = None

                car_data = {
                    "title": title,
                    "price": price,
                    "body_style": body_style,
                    "model_year": model_year,
                    "condition": condition,
                    "reference_no": reference_no,
                    "transmission": transmission,
                    "engine_cylinders": engine_cylinders,
                    "fuel": fuel,
                    "mileage": mileage,
                    "doors": doors,
                    "exterior_color": exterior_color,
                    "interior_color": interior_color,
                    "additional_info": additional_info,
                    "link": link,
                }

                print(f"  Extracted data: {car_data}")

                results.append(car_data)
                print(f"  ✓ Successfully scraped")
                
                # Go back to listings page
                self.driver.back()
                time.sleep(2)
                
                # Re-find the listings container after going back
                listings_container = self.driver.find_element(By.ID, "listings")
                cars = listings_container.find_elements(By.CSS_SELECTOR, "article.item")
                
            except Exception as e:
                print(f"  ✗ Error scraping car: {e}")
                # Try to go back to listings page
                try:
                    self.driver.get("https://www.autolanka.com/cars.html")
                    time.sleep(2)
                    listings_container = self.driver.find_element(By.ID, "listings")
                    cars = listings_container.find_elements(By.CSS_SELECTOR, "article.item")
                except:
                    pass
                continue

        if results:
            print("=== Scraped Cars (raw) ===")
            print(json.dumps(results, indent=2, ensure_ascii=False))

        else:
            print("No cars were scraped.")

        return results


if __name__ == "__main__":
    from selenium import webdriver

    driver = webdriver.Chrome()
    scraper = autolanka_scraper(driver)
    try:
        scraper.scrape()
    finally:
        driver.quit()