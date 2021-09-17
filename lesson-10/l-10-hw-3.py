order = input("Закажите блюдо(шаурма, самса, пирожок): ")

shawarma_filling = ''
samsa_filling = ''
pie_filling = ''
waiting = ''
shawarma_quantity = 0
samsa_quantity = 0
pie_quantity = 0
warm_up = ''

if order == "шаурма":
    shawarma_filling = input("Выберите начинку (мясо, курица): ")
    shawarma_quantity = input("Сколько шаурма вы будете? ")
    warm_up = input("Подогреть? ")
elif order == "самса":
    samsa_filling = input("Выберите начинку(мясо, курица, сыр): ")
    if samsa_filling == "сыр":
        print("Самсы с сыром закончилсь, свежие будут готовы через 15 минут")
        waiting = input("Вы будете ждать? (да, нет): ")
        if waiting == "да":
            samsa_quantity = int(input("Сколько самс вы будете? "))
            warm_up = input("Подогреть? ")
    else:
        warm_up = input("Подогреть? ")

elif order == "пирожок":
    pie_filling = input("Выберите начинку(картошка, капуста): ")
    pie_quantity = input("Сколько пирожков вы будете? ")
    warm_up = input("Подогреть? ")

def onExit(waiting):
    if waiting == "нет":
        print("До свидания")
        return

if warm_up == "да":
    warm_up = "подогреть"
else:
    warm_up = "греть не нужно"

def orderInput(quantity, order, filling, warming):
    print("Ваш заказ: %s %s с начинкой %s %s"  % (quantity, order, filling, warming))




onExit(waiting)

if order == "шаурма":
    orderInput(shawarma_quantity, order, shawarma_filling)
elif order == "самса" and waiting == "да":
    orderInput(samsa_quantity, order, samsa_filling, warm_up)
elif order == "пирожок":
    orderInput(order, pie_filling)
