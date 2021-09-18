from datetime import date, datetime

name = input("Введите ваше имя: ")
surename = input("Введите вашу фамилию: ")
born_year = int(input("Введите год вашего рождения: "))
location = input("Введите место вашего проживания: ")

current_year = int(datetime.now().year)

def takeYear(born_year, current_year):
    return current_year - born_year

age = takeYear(born_year, current_year)

print("Привет, %s %s. Твой возраст %s лет. Твоё место жительства %s. " % (name.capitalize(), surename.capitalize(), age, location.capitalize()))