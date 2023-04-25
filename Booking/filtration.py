from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Filters:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def star_rating(self, *values):
        star_box = self.driver.find_element(By.ID, "filter_group_class_:R14q:")
        inputs = star_box.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')

        for i in values:
            if -1 < i < 6:
                inputs[i - 1].click()

    def lower_price_first(self):
        menu_button = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]'
        )
        menu_button.click()
        set_price_sort = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-id="price"]'
        )
        set_price_sort.click()
