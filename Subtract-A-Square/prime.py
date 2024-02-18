import math


def sqr(n):
    usr1 = int(input("pick a number "))
    if usr1 % (math.sqrt(usr1)) == 0:
        n = n - usr1
        print(n)
    else:
        print("invalid input")


sqr(10)
