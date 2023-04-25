def get_currency():
    x = input("Enter the currency :\t")
    return x.upper()


def get_destination():
    x = input("Enter the destination :\t")
    return x


def get_check_in_date():
    day = int(input("Enter the check in day :\t"))
    month = int(input("Enter the check in month :\t"))
    year = int(input("Enter the check in year :\t"))
    day = str(f"{day:02d}")
    month = str(f"{month:02d}")
    year = str(year)
    return year + '-' + month + '-' + day


def get_check_out_date():
    day = int(input("Enter the check out day :\t"))
    month = int(input("Enter the check out month :\t"))
    year = int(input("Enter the check out year :\t"))
    day = str(f"{day:02d}")
    month = str(f"{month:02d}")
    year = str(year)
    return year + '-' + month + '-' + day


def get_number_of_adults():
    x = int(input("Enter the number of the adults : \t"))
    return x


def get_number_of_rooms():
    x = int(input("Enter the number of the rooms : \t"))
    return x


def get_children_number():
    li = [get_number_of_adults(), get_number_of_rooms()]
    x = int(input("Enter the number of children :\t"))
    li.append(x)
    for i in range(x):
        xx = int(input(f"Enter child number {i + 1} age :\t"))
        li.append(xx)
    return li


def get_stars():
    li = []
    x = int(input("Enter the number of stars\t"))
    print(
        'choose option\n'
        f'1- {x} stars or higher \n'
        f'2- {x} stars or lower \n'
        f'3- {x} stars exact\n'
    )
    xx = int(input())
    if xx == 1:
        for i in range(x, 6):
            li.append(i)
    elif xx == 2:
        for i in range(1, x + 1):
            li.append(i)
    else:
        li.append(x)
    return li

# '2023-04-25'
