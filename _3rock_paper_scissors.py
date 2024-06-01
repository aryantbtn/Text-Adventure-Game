# Checked and works ... no change needed in this game
import random
import subprocess


def rockpaper(level, Gold):
    level = level
    profit = 0
    n = False
    gold = Gold
    subprocess.run('cls', shell=True)
    print("-----------------------------------------------------\n"
          "            WELCOME TO GAME OF\n"
          "        >> ROCK PAPER AND SCISSOR <<\n"
          "-----------------------------------------------------\n"
          "Please note: Any bet amount will not be returned if\n"
          "you quit the game. You get 10 chance per bet.\n"
          "-----------------------------------------------------")
    st = input("Hit Enter to start...")
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

        user_wins = 0
        computer_wins = 0
        chance = 1
        options = ["r", "p", "s"]
        # score = 0
        while chance <= 10:
            if Amount == "q":
                break
            print(f"-------------------------------------------------------------\n"
                  f"You have {11 - chance} chances left !\n"
                  "--------------------------------------------------------------")
            chance += 1
            user_input = input(f"{chance - 1})Type \"r\"=Rock_\"p\"=Paper_\"s\"=Scissor : ").lower()
            print()

            if user_input not in options:
                print("Wrong input! Try again...")
                chance -= 1

            random_number = random.randint(0, 2)
            # rock: 0, paper: 1, scissor: 2
            if user_input == "r":
                print("You picked Rock.")
            elif user_input == "p":
                print("You picked Paper.")
            elif user_input == "s":
                print("You picked Scissor.")

            computer_pick = options[random_number]

            if computer_pick == "r":
                print("Player 2 picked Rock.")
            elif computer_pick == "p":
                print("Player 2 picked Paper.")
            else:
                print("Player 2 picked Scissor.")

            if user_input == computer_pick:
                print("----->Tie! No score <-----\n")

            elif user_input == "r" and computer_pick == "s":
                print("------>You win!<------\n")
                user_wins += 1

            elif user_input == "p" and computer_pick == "r":
                print("------>You win!<------\n")
                user_wins += 1

            elif user_input == "s" and computer_pick == "p":
                print("------>You win!<------\n")
                user_wins += 1

            else:
                print("------>You lost!<------\n")
                computer_wins += 1
        if Amount == "q":
            break
        msg = input("Hit \"Enter\" to continue...")
        score = 0
        if user_wins > computer_wins:
            score = user_wins - computer_wins
        elif user_wins == computer_wins:
            score = 0
        else:
            score = user_wins - computer_wins

        percent = 10 * (score*2)
        profit = int(Amount * (percent / 100))
        gold = gold + profit
        while True:
            subprocess.run('cls', shell=True)
            print("------------------------------------------\n"
                  "You won", user_wins, "times.")
            print("Player 2 won", computer_wins, "times.\n"
                  "------------------------------------------")

            print(f"--------------------------------------\n"
                  f"Bet Amount : {Amount}\n"
                  f"Profit made : {profit}\n"
                  f"Gold is : {gold}\n"
                  f"---------------------------------------")
            st1 = input("Would you like to bet again? (y/n): ")
            if st1 == "y":
                break
            elif st1 == "n":
                n = True
                break
            else:
                print("Wrong input! Try Again...")
        if n:
            n = True
            break
        elif Amount == "q":
            break
    if gold <= 200:
        level = 1
    elif gold > 500:
        level = 11
    else:
        level = 8

    return level, gold