from random import randint


def user_interface(options):
    """
    Дает пользователю выбрать камень ножницы или бумагу
    """

    for index, weapon in enumerate(options):
        print(f'{index} = {weapon}')
    try:
        user_input = int(input("What do you choose?\n"
                               "========================>"))
        return user_input
    except ValueError:
        print("              !ERROR!\n"
              "Please use numbers to select weapon"), main()


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
    print("==========================\n "
          "+++Welcome to my Game!+++ \n"
          " +Please pick your weapon+\n "
          "+++++++Good luck+++++++++\n"
          "==========================\n")
    # Объявили список возможных вариантов для выбора
    options_list = ['Rock', 'Paper', 'Scissors']
    user_result = user_interface(options_list)
    computer_result = computer_choise(options_list)

    # Показываем выбор игрока и компьютера
    try:
        print(f'Player choose:{options_list[user_result]}')
        print(f'Computer chooser:{options_list[computer_result]}')

        result = check_result(options_list, user_result, computer_result)
        print(f'\n{result}')
    except IndexError:
        print("              !ERROR!\n"
              "Please choose from the proposed values")
        play()


def main():
    flag = ''
    while flag.lower() != 'n':
        play()
        print('Do you want to try again?')
        flag = input('Press Enter to continue or N to stop the game:')


main()


