import random
import subprocess
from time import sleep


def randomCalculation(level, Gold):
    level = level
    gold = Gold
    subprocess.run('cls', shell=True)
    print("-------------------------------------------------\n"
          "           Welcome to maths IQ test.\n"
          "-------------------------------------------------\n"
          "Answer the 10 mathematical questions for an\n"
          "easy win! Double your gold for perfect answer!\n"
          "10 % increment or decrement of gold for every \n"
          "single answer. Once game starts you can't quit.\n"
          "-------------------------------------------------")
    start = input("Hit Enter to continue...")
    Amount = 0
    while True:
        while True:
            Amount = 0
            try:
                subprocess.run('cls', shell=True)
                print(f"---------------------------\n"
                      f"You have {gold} gold.\n"
                      f"---------------------------")
                Amount = input("Enter any bet amount between 5 to 50 or \"q\" to quit: ")
                if Amount == "q":
                    break
                else:
                    Amount = int(Amount)

                if gold <= 0:
                    print("Not Enough gold!")
                    l = input("Hit enter to continue...")

                elif Amount <= gold:
                    if 5 <= Amount <= 50:
                        print(f"Bet amount is: {Amount}"
                              f"\n----------------------------")
                        st = input("Hit Enter to continue...")
                        break
                    else:
                        print("This amount cannot be accepted!")
                        st = input("Hit Enter to try again...")
                else:
                    print("This amount cannot be accepted!")
                    st = input("Hit Enter to try again...")
            except ValueError:
                jkl = input("Wrong Input! Hit Enter... ")
                continue

        score = 0
        t = 10
        while t != 0:
            if Amount == "q":
                break
            elif isinstance(Amount, str):
                break
            sleep(1)
            subprocess.run('cls', shell=True)
            print(f"----------------------------\n"
                  f"Questions left: {t}")
            calc = 0
            operators = ['+', '-', '*']
            i = random.randint(0, 2)
            num1 = random.randint(3, 35)
            num2 = random.randint(3, 35)
            if operators[i] == '+':
                while True:
                    try:
                        calc = int(input(f"-------------------------------------\n"
                                         f"Calculate: {num1} + {num2} = "))
                    except ValueError:
                        print("Enter integer value next time!")
                        break
                    if calc == num1 + num2:
                        print("Correct!")
                        score += 1
                        t -= 1
                        break
                    else:
                        print("Wrong!")
                        t -= 1
                        break

            elif operators[i] == '-':
                while True:
                    try:
                        calc = int(input(f"-------------------------------------\n"
                                         f"Calculate: {num1} - {num2} = "))
                    except ValueError:
                        print("Enter integer value next time!")
                        break
                    if calc == num1 - num2:
                        print("Correct!")
                        score += 1
                        t -= 1
                        break
                    else:
                        print("Wrong!")
                        t -= 1
                        break

            elif operators[i] == '*':
                while True:
                    try:
                        calc = int(input(f"--------------------------------------\n"
                                         f"Calculate: {num1} * {num2} = "))
                    except ValueError:
                        print("Enter integer value next time!")
                        break
                    if calc == num1 * num2:
                        print("Correct!")
                        score += 1
                        t -= 1
                        break
                    else:
                        print("Wrong!")
                        t -= 1
                        break
        if Amount == "q":
            break

        play = input("Would you like to play again!(y/n): ")
        if play == "y":
            continue
        else:
            break

    if Amount == "q":
        pass
    else:
        st = input("Game finished! Hit Enter to see result...")
        percent = 10 * score
        profit = int(Amount * (percent / 100))
        gold = gold + profit
        subprocess.run('cls', shell=True)
        print(f"--------------------------------------\n"
              f"Your score is {score}.\n"
              f"Bet Amount : {Amount}\n"
              f"Profit made : {profit}\n"
              f"Gold is : {gold}\n"
              f"---------------------------------------")
        jkl = input("Hit Enter to continue...")
        if gold < 200:
            level = 3
        elif gold > 500:
            level = 11
        else:
            level = 6
    return level, gold