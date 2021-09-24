import random

left = 1
right = 100


def command_exit():
    exit("Goodbye!")


commands = {
    'exit': command_exit
}


command = input(
    'Добро пожаловать!\nДля игры с компьютером введите (play)\nДля отгадывания числа введите (guess)\nДля выхода введите (exit) > ')

number = int(random.uniform(1, 100))

counter = 0


while True:
    if command == 'play':
        counter += 1
        current = (left + right) // 2
        is_right = input(
            'Ваше число: {}? (yes, greater, less) > '.format(current))
        if is_right.lower() == 'yes':
            print('Число было отгадано за %s ходов!' % counter)
            break
        elif is_right.lower() == 'greater':
            left = current + 1
        elif is_right.lower() == 'less':
            right = current - 1
        elif is_right == 'exit':
            break
    elif command == 'guess':
        counter += 1
        answer = int(input("Угадайте число от 1 до 100 > "))
        if answer == 'exit':
            break
        elif answer > int(number):
            print("меньше")
        elif answer < int(number):
            print('больше')
        else:
            print("Поздравляю! Вы угадали число за %s ходов!" % counter)
            break
    elif command == 'exit':
        exit()
