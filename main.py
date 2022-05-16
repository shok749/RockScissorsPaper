from random import randint


def user_interface(options):
    """
    Дает пользователю выбрать камень ножницы или бумагу
    """
    for index, weapon in enumerate(options):
        print(f'{index} = {weapon}')

    user_input = int(input("What do you choose?"))
    return user_input


def computer_choise(content):
    comp_choise = randint(0, len(content) - 1)
    return comp_choise


def check_result(choises, player, comp):
    if player == comp:
        return ("It's a draw!")
    elif (player == 0 and comp == len(choises) - 1) or (
            player > comp and not (player == len(choises) - 1 and comp == 0)):
        return ('Player won!')
    return "WASTED!"


def play():
    print("=========================\n "
          "Welcome my Game! \n"
          "Please pick your weapon!\n ")
    # Объявили список возможных вариантов для выбора
    options_list = ['Rock', 'Paper', 'Scissors']
    user_result = user_interface(options_list)
    computer_result = computer_choise(options_list)

    # Показываем выбор игрока и компьютера
    print(f'player choose:{options_list[user_result]}')
    print(f'computer chooser:{options_list[computer_result]}')

    result = check_result(options_list, user_result, computer_result)
    print(f'\n{result}')


def main():
    flag = ''
    while flag.lower() != 'n':
        play()
        print('do you want to try again?')
        flag = input('type y to continue or n to stop the game:')


main()
