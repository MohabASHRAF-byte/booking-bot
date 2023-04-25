from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Scrap:
    def __init__(self, driver: WebDriver):

        self.driver = driver
        self.page_values = []
        self.cnt = 0

    def get_boxes(self):
        return (
            self.driver.find_element(
                By.CLASS_NAME, "d4924c9e74"
            ).find_elements(
                By.CSS_SELECTOR, 'div[data-testid="property-card"]'
            )
        )

    def go_next(self):
        try:
            btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR, 'button[aria-label="Next page"]'
                ))
            )
            btn.click()
            sleep(3)
            return True
        except:
            return False

    def get_box_values(self, box):
        # getting price of the hotel
        try:
            hotel_price = box.find_element(
                By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]'
            ).text
        except:
            hotel_price = -1
        # getting hotel name
        try:
            hotel_name = box.find_element(
                By.CSS_SELECTOR, 'div[data-testid="title"]'
            ).text
        except:
            hotel_name = -1
        # getting rate
        try:
            rate_box = box.find_element(
                By.CSS_SELECTOR, 'div[data-testid="review-score"]'
            )
            hotel_rate = rate_box.find_element(
                By.CLASS_NAME, 'b5cd09854e'
            ).text
        except Exception as e:
            hotel_rate = " NO SCORE"
        return [self.cnt, hotel_name, hotel_price, hotel_rate]

    def get_values(self):
        while True:
            for box in self.get_boxes():
                self.cnt += 1
                self.page_values.append(self.get_box_values(box))
            if not self.go_next():
                break
        return self.page_values, self.cnt
