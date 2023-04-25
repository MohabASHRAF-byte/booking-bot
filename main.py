from Booking.Booking import Booking
from Applicatoin.GUI import *


currency = get_currency()
destination = get_destination()
check_in_date = get_check_in_date()
check_out_date = get_check_out_date()
list_args = get_children_number()
stars = get_stars()

with Booking() as bot:
    bot.get_land_page()
    bot.skip_sign_in()
    bot.choose_currency(currency=currency)
    bot.choose_destinations(destination=destination)
    bot.set_dates(
        checkIn=check_in_date,
        checkOut=check_out_date
    )
    bot.list(list_args)
    bot.submit()
    bot.apply_filtrations(stars)
    bot.get_data()
