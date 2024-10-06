from datetime import datetime


def get_employees(name, lastname):
    names = name
    lastnames = lastname
    times_is_now = datetime.now()
    print(f'{lastnames} {names}, пришел на работу {times_is_now}')

