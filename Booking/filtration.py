from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Filters:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def star_rating(self, values):
        star_box = self.driver.find_element(By.ID, "filter_group_class_:R14q:")
        star_child_elements = star_box.find_elements(By.CSS_SELECTOR, '*')
        for star_value in values:
            for star_element in star_child_elements:
                if star_value == 1:
                    if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} star':
                        star_element.click()
                        break
                elif str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()
                    break

    def lower_price_first(self):
        menu_button = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]'
        )
        menu_button.click()
        set_price_sort = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-id="price"]'
        )
        set_price_sort.click()
