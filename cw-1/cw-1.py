import random

dragon = {
    'hp': 2000,       # жизненная энергия, запас здоровья
    'defence': 120,   # защита
    'str': 250,       # сила
    'weapon': 0       # оружие
}

hero = {
    'hp': 1000,
    'defence': 100,
    'str': 120,
    'weapon': 250,
    'shield': 150     # щит
}

print()
print('Битва героя и дракона')
print()


commands = {
    'attack': None,
    'pass': None,
    'defence': None
}

while True:

    def display_dragon_info():
        if dragon['hp'] > 0:
            print('У дракона осталось %s hp' % (dragon['hp']))
        else:
            print('Дракон мёртв')

    def display_hero_info():
        if hero['hp'] > 0:
            print('У героя осталось %s hp' % hero['hp'])
        else:
            print('Герой мертв')

    def hero_attack():
        damage = hero['str'] + hero['weapon'] - dragon['defence']
        return damage

    def dragon_attack():
        damage = dragon['str'] + dragon['weapon'] - hero['defence']
        return damage

    def modify_health(person, modify_hp):
        person['hp'] += modify_hp
        if person['hp'] <= 0:
            person['hp'] = 0
        return person['hp']

    def hero_move():
        hero_damage = hero_attack()
        modify_health(dragon, (hero_damage * -1))
        print("Герой попал по дракону и нанёс %s урона" % hero_damage)
        display_dragon_info()

    def dragon_move():
        dragon_damage = dragon_attack()
        modify_health(hero, (dragon_damage * -1))
        print("Дракон ударил героя и нанёс %s урона" % dragon_damage)
        display_hero_info()

    if dragon['hp'] > 0 and hero['hp'] > 0:
        command = input('Введите attack для атаки, defence для защиты или pass для пропуска хода > ')
        print()
        if command == 'pass':
            pass
        if command == 'attack':
            if random.randint(1, 100) <= 75:
                hero_move()
            else:
                print("Герой промахнулся")
                display_dragon_info()
        if command == 'defence':
            print('Герой выставил щит')
    else:
        if hero['hp'] > 0:
            print('Герой победил!')

        if dragon['hp'] > 0:
            print('Дракон победил')
        break

    if dragon['hp'] > 0 and hero['hp'] > 0:
        if random.randint(1, 100) <= 50:
            dragon_move()
            print()
            print('========================================')
            print()
        else:
            print('Дракон проспал ход')
            display_hero_info()
            print()
            print('========================================')
            print()
