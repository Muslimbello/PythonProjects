list = []
for i in range(1, 10):
    list.append(i)
print(list)


def scrabble(list):
    total = sum(list)
    if len(list) >= 3 and total == 15:
        return True
    return False


usr1_list = []
usr2_list = []

while list != []:
    user1 = int(input("pick a number from 1 -9: "))
    list.remove(user1)
    usr1_list.append(user1)
    print(list)
    print(usr1_list)
    if scrabble(usr1_list):
        print("Player 1 wins! The numbers add up to 15.")
        break

    # user2
    user2 = int(input("pick a number from 1 -9: "))
    list.remove(user2)
    usr2_list.append(user2)
    print(list)
    print(usr2_list)
    if scrabble(usr2_list):
        print("Player 2 wins! The numbers add up to 15.")
        break
    if len(list) == 0:
        print("its a tie")
        break
