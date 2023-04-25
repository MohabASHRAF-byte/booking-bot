from Booking.Booking import Booking
from time import sleep

with Booking() as bot:
    bot.get_land_page()
    bot.skip_sign_in()
    # bot.choose_currency(currency='EGP')
    bot.choose_destinations(destination="hurghada")
    bot.set_dates(checkIn='2023-04-25', checkOut='2023-04-27')
    # bot.list(2, 0, 1)
    bot.submit()
    bot.apply_filtrations()
    bot.get_data()
    sleep(10000)
