from datetime import datetime


birth_day = input("Введите дату своего дня рождения в формате ДД/ММ/ГГГГ: ")


date_arr = birth_day.split('/')
date_str = '-'.join(date_arr)
date_obj = datetime.strptime(date_str, "%d-%m-%Y")


def get_month(month):
    my_month = ''
    if (month == 1):
        my_month = 'января'
    elif (month == 2):
        my_month = 'февраля'
    elif (month == 3):
        my_month = 'марта'
    elif (month == 4):
        my_month = 'апреля'
    elif (month == 5):
        my_month = 'мая'
    elif (month == 6):
        my_month = 'июня'
    elif (month == 7):
        my_month = 'июля'
    elif (month == 8):
        my_month = 'августа'
    elif (month == 9):
        my_month = 'сентября'
    elif (month == 10):
        my_month = 'октября'
    elif (month == 11):
        my_month = 'ноября'
    elif (month == 12):
        my_month = 'декабря'
    return my_month


year = date_obj.year
day = date_obj.day
month = get_month(date_obj.month)


print("Вы родились в %s году, %s %s" % (year, day, month))
