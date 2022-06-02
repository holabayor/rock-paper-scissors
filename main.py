#!/usr/bin/python3
import random

options = ["R", "P", "S"]


def getUser():
    user = input("\nWhat is your choice?\n'R' for 'Rock', 'P' for 'Paper', 'S' for 'Scissors'\t").upper()
    if user not in options:
        print("Invalid Choice")
        getUser()
    return user


def getCpu():
    return random.choice(options)


def play():
    cpu = getCpu()
    user = getUser()
    if user == cpu:
        print("\nIt is a tie")
        play()

    # r > s, s > p, p > r

    if is_win(user, cpu):
        return "\nYou have chosen {} and the computer has chosen {}. You won!".format(user, cpu)
    else:
        return "\nYou have chosen {} and the computer has chosen {}. Computer won!".format(user, cpu)


def is_win(p1, p2):
    if (p1 == 'R' and p2 == 'S') or (p1 == 'S' and p2 == 'P') or (p1 == 'P' and p2 == 'R'):
        return True

if __name__ == '__main__':
   print(play())
