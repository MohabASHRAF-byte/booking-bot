import Booking.constants as const
from Booking.filtration import Filters
from Booking.scraping import Scrap
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import datetime
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    teardown = False

    def __int__(self, driver_path=const.chrome_path,
                teardown=False):
        os.environ['PATH'] += const.chrome_path
        self.driver_path = driver_path
        super(Booking, self).__init__()
        self.maximize_window()
        self.implicitly_wait(15)
        self.teardown = teardown

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def get_land_page(self):
        self.get(const.BASE_URL)

    def skip_sign_in(self):
        try:

            close_btn = WebDriverWait(self, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]'))
            )
            close_btn.click()
        except Exception:
            pass

    def choose_currency(self, currency=None):
        menu_btn = WebDriverWait(self, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]'))
        )
        menu_btn.click()
        currencies = self.find_elements(By.CLASS_NAME, 'ea1163d21f')
        currency_btn = None
        for button in currencies:
            if button.text == currency:
                currency_btn = button
                break
        if currency_btn is None:
            exit(1)
        currency_btn.click()

    def choose_destinations(self, destination="New York"):
        input_txt = self.find_element(By.ID, ':Ra9:')
        input_txt.send_keys(destination)
        sleep(3)
        select_btn = self.find_element(By.CLASS_NAME, 'cd1e09fdfe')
        select_btn.click()

    def set_dates(self, checkIn, checkOut):
        sleep(1)
        # store checkin && check out date in variables
        checkIn_set = checkIn
        checkOut_set = checkOut
        # checkIn = str(checkIn)
        # checkOut = str(checkOut)
        # create list contain dates as a numbers
        checkIn = [int(ii) for ii in checkIn.split('-')]
        checkOut = [int(ii) for ii in checkOut.split('-')]
        # get current month and year
        current_month = datetime.datetime.now().month
        current_year = datetime.datetime.now().year
        # calculate how many months between now and check in
        checkIn_page_number = ((12 * checkIn[0] + checkIn[1]) - (12 * current_year + current_month))
        # calculate how many months between check in  and check out
        checkOut_page_number = ((12 * checkOut[0] + checkOut[1]) - (
                12 * current_year + current_month)) - checkIn_page_number
        # get next button position
        nxt_btn = self.find_elements(
            By.CLASS_NAME, 'b9def0936d'
        )[1]
        #  get next page until get check in page
        for _ in range(checkIn_page_number):
            sleep(.5)
            nxt_btn.click()
        sleep(1)
        #    choose the check in date
        check_in_elements = self.find_elements(By.CSS_SELECTOR, f'span[role="checkbox"]')
        for _ in check_in_elements:
            if _.get_attribute('data-date') == checkIn_set:
                _.click()
                break
        sleep(1)
        #  get next page until get check out page
        for _ in range(checkOut_page_number):
            sleep(.5)
            nxt_btn.click()
        sleep(1)
        # set for check out
        check_in_elements = self.find_elements(By.CSS_SELECTOR, f'span[role="checkbox"]')
        for _ in check_in_elements:
            if _.get_attribute('data-date') == checkOut_set:
                _.click()
                break
        sleep(1)

    def set_adults(self, num):
        buttons = self.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
        buttons[6].click()
        for i in range(int(num) - 1):
            buttons[7].click()
            sleep(.5)

    def set_children(self, num):
        buttons = self.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
        for _ in range(num[2]):
            buttons[9].click()
        select = self.find_elements(By.CSS_SELECTOR, 'select[name="age"]')
        for i in range(len(select)):
            select[i].click()
            sleep(1)
            choose_age = self.find_elements(By.CSS_SELECTOR, f'option[value="{num[i + 3]}"]')
            choose_age[i].click()
            sleep(1)

    def set_rooms(self, num):
        buttons = self.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
        for _ in range(int(num) - 1):
            buttons[11].click()
            sleep(.5)

    def close_list(self):
        buttons = self.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
        buttons[12].click()

    # 11
    def list(self, args):
        menu = self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
        menu.click()
        sleep(2)
        self.set_adults(num=args[0])
        self.set_children(args)
        self.set_rooms(num=args[1])
        self.close_list()

    def submit(self):
        btn = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        btn.click()

    def apply_filtrations(self, stars):
        ob = Filters(self)
        ob.star_rating(values=stars)
        sleep(10)
        ob.lower_price_first()

    def get_data(self):
        self.refresh()
        ob = Scrap(driver=self)
        res_table, cnt = ob.get_values()
        table = PrettyTable(field_names=["index", "Hotel Name", "Price", "Score"])
        table.add_rows(res_table)
        print(f'{cnt} results')
        print(table)
