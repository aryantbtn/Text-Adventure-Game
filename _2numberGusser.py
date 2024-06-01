import random
import subprocess


def numberGuess(level, Gold):
    subprocess.run('cls', shell=True)
    level = level
    gold = Gold
    print("-------------------------------------------\n"
          "           NUMBER GUESSING GAME\n"
          "-------------------------------------------\n"
          "Guess the number in less than 5 step to have\n"
          "greater reward!\n"
          "-------------------------------------------")
    st = input("Hit Enter to start...")
    inst = False
    while True:
        while True:
            Amount = 0
            try:
                subprocess.run('cls', shell=True)
                print(f"---------------------------\n"
                      f"You have {gold} gold.\n"
                      f"---------------------------")
                Amount = input("Enter any bet amount between 5 to 100 or \"q\" to quit: ")
                if Amount == "q":
                    break
                else:
                    Amount = int(Amount)

                if gold <= 0:
                    print("Not Enough gold!")
                    l = input("Hit enter to continue...")

                elif Amount <= gold:
                    if 5 <= Amount <= 100:
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

        random_number = random.randrange(1, 101)
        step = 0
        subprocess.run('cls', shell=True)
        while True:
            if Amount == "q":
                break

            print(f"Step : {step + 1}")
            top_of_range = input("Guess a number between 1 to 100 : ")
            if top_of_range.isdigit():
                top_of_range = int(top_of_range)
                if top_of_range <= 0:
                    print('Please type a number greater than 0!')
            else:
                print("Please type a number!")
                continue
            if random_number < top_of_range:
                if random_number < top_of_range - 3:
                    print("Too High!")
                    step += 1
                else:
                    print("Too Close!")
                    step += 1

            elif random_number > top_of_range:
                if random_number > top_of_range + 3:
                    print("Too Low!")
                    step += 1

                else:
                    print("Too Close!")
                    step += 1

            else:
                print("\n\nYou got this! Correct number was ", random_number)
                jkl = input("\n\nFinished! Hit Enter to continue...")
                subprocess.run('cls', shell=True)
                step += 1
                break
        if Amount == "q":
            break
        else:
            print("You took", step, "steps to find!")
            profit = 5 - step
            profit = 40 * profit
            profit = int(Amount * (profit / 100))
            gold = gold+profit
            print(f"--------------------------------------\n"
                  f"Your score is {step} out of 10.\n"
                  f"Bet Amount : {Amount}\n"
                  f"Profit made : {profit}\n"
                  f"Gold is : {gold}\n"
                  f"---------------------------------------")
            st = input("Hit enter to continue...")
            if gold < 200:
                level = 3
            elif gold > 500:
                level = 11
            else:
                level = 6

    return level, gold