from Booking.Booking import Booking
from time import sleep

with Booking() as bot:
    bot.get_land_page()
    bot.skip_sign_in()
    bot.choose_currency(currency='EGP')
    bot.choose_destinations(destination="hurghada")
    bot.set_dates(checkIn='2024-01-20', checkOut='2024-01-26')
    bot.list(5, 1, 2)
    bot.submit()
    sleep(10000)
