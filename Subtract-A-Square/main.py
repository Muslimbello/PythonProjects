import math
from random import randint


def check_sqr(player):
    while True:
        user_input = input(f"Player {player} pick a squared number: ")
        try:
            user_number = int(user_input)
            if math.sqrt(user_number) % 1 == 0:
                return user_number
            else:
                print("Make sure you picked a squared number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def sqr_subtract():
    num = randint(1, 100)
    print(num)

    while True:
        user1 = check_sqr(1)
        num -= user1
        print(num)

        if num == 0:
            print("Player 1 wins!")
            break
        elif num < 0:
            print("It's a tie!")
            break

        user2 = check_sqr(2)
        num -= user2
        print(num)

        if num == 0:
            print("Player 2 wins!")
            break
        elif num < 0:
            print("It's a tie!")
            break


sqr_subtract()
