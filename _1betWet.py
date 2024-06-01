import random
import subprocess


def betWet(level, Gold):
    level = level
    subprocess.run('cls', shell=True)
    m = False
    gold = Gold
    Amount = 0
    print("----------------------------------------------\n"
          "              ROLLING LUCK\n"
          "----------------------------------------------\n"
          "Bet an amount to 2x double or 3x triple it on\n"
          "your given luck. \"Be the richest in no time.\n"
          "----------------------------------------------")
    st = input("Hit Enter to start...")
    while True:
        while True:
            Amount = 0
            try:
                subprocess.run('cls', shell=True)
                print(f"---------------------------\n"
                      f"You have {gold} gold.\n"
                      f"---------------------------")
                Amount = input("Enter any bet amount or \"q\" to quit: ")
                if Amount == "q":
                    break
                else:
                    Amount = int(Amount)

                if gold < 0:
                    print("Not Enough gold!")
                    l = input("Hit enter to continue...")
                elif Amount <= gold:
                    print(f"Bet amount is: {Amount}"
                          f"\n----------------------------")
                    break
                else:
                    print("This amount cannot be accepted!")
                    st = input("Hit Enter to try again...")
            except ValueError:
                jkl = input("Wrong Input! Hit Enter... ")
                continue
        if Amount == "q":
            break
        else:
            gold = gold - Amount
            rollRandom = [0, 1.2, 3, 0, 2, 1, 0, 2, 1.2, 0, 3, 0, 1.2, 0, 0, 2, 0, 1, 0, 1.2, 0, 1.5]
            num = len(rollRandom)
            num = random.randint(0, num-1)
            print(f"It is {rollRandom[num]}x")
            mult = 0
            if rollRandom[num] == 1.2 and Amount <=5:
                if Amount == 0:
                    pass
                else:
                    mult = Amount + 1
            else:
                mult = Amount * rollRandom[num]
            print(f"Profit Made: {int(mult)}")
            gold = int(gold + mult)
            print("Gold left: ", gold)
            while True:
                n = input("----------------------------------------------\n"
                          "Hit Enter to play again! \"q\" to quit:  ")
                if n == "":
                    break
                if n == "q":
                    m = True
                    break
                else:
                    print("Wrong input! Try again...")
        if m:
            break
        elif Amount == "q":
            break
    if gold >= 200:
        level = 8
    elif gold > 500:
        level = 11
    else:
        level = 3

    return level, gold