order = input("Закажите блюдо(шаурма, самса, пирожок): ")

filling = ''
waiting = ''

if order == "шаурма":
    filling = input("Выберите начинку(мясо, курица): ")
elif order == "самса":
    filling = input("Выберите начинку(мясо, курица, сыр): ")
    if filling == "сыр":
        print("Самсы с сыром закончилсь, свежие будут готовы через 15 минут")
        waiting = input("Вы будете ждать(да, нет): ")

elif order == "пирожок":
    filling = input("Выберите начинку(картошка, капуста): ")

print(waiting)


def onExit(waiting):
    if waiting == "нет":
        return
    else:
        print('as;ldkfj')


onExit(waiting)
