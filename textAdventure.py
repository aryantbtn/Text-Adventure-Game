import ast
import subprocess
from home import home


def textAdventure(Pid):
    out = False
    with open(f"Players\\playerRecord{Pid}.txt", 'r') as file:
        data = file.read()
        data = ast.literal_eval(data)
        progress = data[3]
        level = progress
        if isinstance(level, str):
            level = 0

    print(
        "-----------------------------------------------------------\n"
        "                  TEXT ADVENTURE GAME\n"
        "-----------------------------------------------------------\n"
        "NOTE: Your data automatically gets saved to the system.\n"
        "So the game will start from the last saved level you \n"
        "have completed.\n"
        "----------------------------------------------------------")
    np = input("Hit Enter to continue...\n"
               "----------------------------------------------------------")

    while True:
        subprocess.run('cls', shell=True)

        if level == 0:
            print("Start: \n"
                  "--------------------------------------------------------------------\n"
                  "You have been chosen by gods to be the son/daughter of a King. How\n"
                  "will you prove your people to be their next King/Queen?\n"
                  "--------------------------------------------------------------------\n"
                  "a. Explore around the world to find knowledge and strengthen yourself.\n"
                  "b. Defeat enemies to prove your worthy.\n"
                  "c. Bring wealth and gold to the kingdom by some means.\n"
                  "d. Let your luck choose your destination.\n"
                  "--------------------------------------------------------------------")

            ans = input("Select from options or q to quit: ")
            while True:
                if ans == "q":
                    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                        data[3] = level
                        file.write(str(data))
                    home(Pid)
                if ans == "a":
                    print("sent to Q1.")
                    level = 1
                    break
                elif ans == "b":
                    print("sent to enemy fight")
                    from bossFight import bossFight
                    level = bossFight( level, 17, 1, 120, 200, 6, 2)
                    break
                elif ans == "c":
                    print("sent to Q2.")
                    level = 2
                    break
                elif ans == "d":
                    print("sent to Q3.")
                    level = 3
                    break
                else:
                    print("Wrong input! Try again!")
                    break

        elif level == 1:
            subprocess.run('cls', shell=True)
            print("Level: 1\n"
                  "------------------------------------------------------------------------------\n"
                  "You are now brave enough to take big decisions for your kingdom and its people.\n"
                  "How will you protect them from a disaster heading towards the kingdom?\n"
                  "------------------------------------------------------------------------------\n"
                  "a. Use your bravery and strength and protect them all alone.\n"
                  "b. Follow the path of others.\n"
                  "------------------------------------------------------------------------------")
            ans = input("Select from options or q to quit: ")
            while True:
                if ans == "q":
                    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                        data[3] = level
                        file.write(str(data))
                    home(Pid)
                if ans == "a":
                    print("sent to Q5.")
                    level = 5
                    break
                elif ans == "b":
                    print("sent to Q4.")
                    level = 4
                    break
                else:
                    print("Wrong input! Try again!")
                    break

        elif level == 2:
            subprocess.run('cls', shell=True)
            print("Level: 2\n"
                  "----------------------------------------------------------------------------\n"
                  "You have came far from home where victory can be a reward and patience can\n"
                  "be a virtue. What would you choose then?\n"
                  "----------------------------------------------------------------------------\n"
                  "a. Have patience\n"
                  "b. Have great rewards.\n"
                  "----------------------------------------------------------------------------")
            ans = input("Select from options or q to quit: ")
            while True:
                if ans == "q":
                    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                        data[3] = level
                        file.write(str(data))
                    home(Pid)
                if ans == "a":
                    print("sent to Q1.")
                    level = 6
                    break
                elif ans == "b":
                    with open(f"Players\\playerRecord{Pid}.txt", 'r') as file:
                        data = file.read()
                        data = ast.literal_eval(data)
                        gold = data[2]

                    print("Play a game")
                    from Practice_Projects import _4randomCalculation
                    Gold = 0
                    if gold > 200:
                        level = 11
                    else:
                        level, Gold = _4randomCalculation.randomCalculation(level, gold)

                    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                        data[2] = Gold
                        file.write(str(data))

                    break
                else:
                    print("Wrong input! Try again!")
                    break

        elif level == 3:
            subprocess.run('cls', shell=True)
            print("Level: 3\n"
                  "----------------------------------------------------------------------------\n"
                  "You have been brought to the place where the prize is same again and again.\n"
                  "----------------------------------------------------------------------------\n"
                  "a. Luck is all what would suit you.\n"
                  "b. Ready to face whatever comes next.\n"
                  "-----------------------------------------------------------------------------")
            ans = input("Select from options or q to quit: ")
            while True:
                if ans == "q":
                    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                        data[3] = level
                        file.write(str(data))
                    home(Pid)
                if ans == "a":
                    print("sent to Q2.")
                    level = 2
                    break
                elif ans == "b":
                    print("sent to Q4.")
                    level = 4
                    break
                else:
                    print("Wrong input! Try again!")
                    break

        elif level == 4:
            subprocess.run('cls', shell=True)
            print("Level: 4\n"
                  "-------------------------------------------------------------------------------\n"
                  "King sends you a gift for your for healthy progress.\n"
                  "Would you like to ....\n"
                  "-------------------------------------------------------------------------------\n"
                  "a. open it.\n"
                  "b. go for a different game.\n"
                  "--------------------------------------------------------------------------------")
            ans = input("Select from options or q to quit: ")
            while True:
                if ans == "q":
                    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                        data[3] = level
                        file.write(str(data))
                    home(Pid)
                if ans == "a":
                    print("sent to Q7.")
                    level = 7
                    break
                elif ans == "b":
                    with open(f"Players\\playerRecord{Pid}.txt", 'r') as file:
                        data = file.read()
                        data = ast.literal_eval(data)
                        gold = data[2]

                    print("sent to a game")
                    Gold = 0
                    if gold > 200:
                        level = 11
                    else:
                        from Practice_Projects import _2numberGusser
                        level, Gold = _2numberGusser.numberGuess(level, gold)

                    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                        data[2] = Gold
                        file.write(str(data))
                    break
                else:
                    print("Wrong input! Try again!")
                    break
        elif level == 5:
            subprocess.run('cls', shell=True)
            print("Level: 5\n"
                  "---------------------------------------------------------------------------\n"
                  "Would you rather die for the kingdom or fight for the kingdom?\n"
                  "---------------------------------------------------------------------------\n"
                  "a. die\n"
                  "b. fight\n"
                  "---------------------------------------------------------------------------")
            ans = input("Select from options or q to quit: ")
            while True:
                if ans == "q":
                    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                        data[3] = level
                        file.write(str(data))
                    home(Pid)
                if ans == "a":
                    print("sent to Q0.")
                    level = 0
                    break
                elif ans == "b":
                    print("sent to Q8.")
                    level = 8
                    break
                else:
                    print("Wrong input! Try again!")
                    break

        elif level == 6:
            with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                data[3] = level
                file.write(str(data))

            subprocess.run('cls', shell=True)
            print("Level: 6\n"
                  "----------------------------------------------------------------------------\n"
                  "Life is nothing but an adventure. Win the reward of your choice.\n"
                  "----------------------------------------------------------------------------\n"
                  "a. By winning a game.\n"
                  "b. By defeating an enemy.\n"
                  "------------------------------------------------------------------------------")
            ans = input("Select from options or q to quit: ")
            while True:
                if ans == "q":
                    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                        data[3] = level
                        file.write(str(data))
                    home(Pid)
                if ans == "a":
                    with open(f"Players\\playerRecord{Pid}.txt", 'r') as file:
                        data = file.read()
                        data = ast.literal_eval(data)
                        gold = data[2]
                        level = data[3]

                    print("sent to a game")
                    Gold = 0
                    if gold > 200:
                        level = 11
                    else:
                        from Practice_Projects import _3rock_paper_scissors
                        level, Gold = _3rock_paper_scissors.rockpaper(level, gold)

                    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                        data[2] = Gold
                        file.write(str(data))

                    break
                elif ans == "b":
                    print("sent to an enemy fight")
                    from bossFight import bossFight
                    level = bossFight(level, 42, 2.7, 200, 500, 7, 3)

                    break
                else:
                    print("Wrong input! Try again!")
                    break

        elif level == 7:
            subprocess.run('cls', shell=True)
            print("Level: 7\n"
                  "--------------------------------------------------------------------------\n"
                  "Your destiny took you to a place where every thing is strange and \n"
                  "requests you to - Do not touch something or just touch and die.\n"
                  "--------------------------------------------------------------------------\n"
                  "a. Take a risk.\n"
                  "b. Make a safe journey.\n"
                  "---------------------------------------------------------------------------")
            ans = input("Select from options or q to quit: ")
            while True:
                if ans == "q":
                    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                        data[3] = level
                        file.write(str(data))
                    home(Pid)
                if ans == "a":
                    print("sent to Q5.")
                    level = 9
                    break
                elif ans == "b":
                    print("sent to Q4.")
                    level = 4
                    break
                else:
                    print("Wrong input! Try again!")
                    break

        elif level == 8:
            subprocess.run('cls', shell=True)
            print("Level: 8\n"
                  "-----------------------------------------------------------------------------\n"
                  "Life would never give you a chance again. Live for good or die in discretion.\n"
                  "-----------------------------------------------------------------------------\n"
                  "a. Fight an enemy and end the terror for all.\n"
                  "b. Save your life for a better future.\n"
                  "-----------------------------------------------------------------------------")
            ans = input("Select from options or q to quit: ")
            while True:
                if ans == "q":
                    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                        data[3] = level
                        file.write(str(data))
                    home(Pid)
                if ans == "a":
                    print("sent to an enemy")
                    from bossFight import bossFight
                    level = bossFight(level, 83, 3.9, 350, 1000, 11, 9)
                    break
                elif ans == "b":
                    print("sent to Q2.")
                    level = 2
                    break
                else:
                    print("Wrong input! Try again!")
                    break

        elif level == 9:
            subprocess.run('cls', shell=True)
            print("Level: 9\n"
                  "----------------------------------------------------------------------------\n"
                  "Gamble of life and death is not an easy choice.\n"
                  "----------------------------------------------------------------------------\n"
                  "a. Prove you are worthy enough to rule over the kingdom.\n"
                  "b. Have some time to be acknowledged.\n"
                  "----------------------------------------------------------------------------")
            ans = input("Select from options or q to quit: ")
            while True:
                if ans == "q":
                    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                        data[3] = level
                        file.write(str(data))
                    home(Pid)
                if ans == "a":
                    with open(f"Players\\playerRecord{Pid}.txt", 'r') as file:
                        data = file.read()
                        data = ast.literal_eval(data)
                        gold = data[2]

                    print("sent to a game")
                    Gold = 0
                    if gold > 200:
                        level = 11
                    else:
                        from Practice_Projects import _1betWet
                        level, Gold = _1betWet.betWet(level, gold)

                    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                        data[2] = Gold
                        file.write(str(data))

                    break
                elif ans == "b":
                    print("sent to Q10.")
                    level = 10
                    break
                else:
                    print("Wrong input! Try again!")
                    break

        elif level == 10:
            subprocess.run('cls', shell=True)
            print("Level: 10\n"
                  "--------------------------------------------------------------------------\n"
                  "Your kingdom is falling. Every one is saving their lives and protecting \n"
                  "themselves. You have less chance of any victory. Would you like to fight\n"
                  "till the end or begin a new journey.\n"
                  "---------------------------------------------------------------------------\n"
                  "a. Fight till the end.\n"
                  "b. Run away for better start.\n"
                  "-----------------------------------------------------------------------------")
            ans = input("Select from options or q to quit: ")

            if ans == "q":
                with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
                    data[3] = level
                    file.write(str(data))
                home(Pid)
            if ans == "a":
                subprocess.run('cls', shell=True)
                print("-------------------------------------------------------------------\n"
                      "                              You Lose!\n"
                      "-------------------------------------------------------------------\n"
                      "You fought bravely, but wasn't able to protect the kingdom and your\n"
                      "people. You could have defeated the enemy before it hit your\n"
                      "ground.\n"
                      "No worries, try your luck in another life, if you ever get one.\n"
                      "--------------------------------------------------------------------\n"
                      "                            The End..."
                      )
                level = "You Lose!"
                break
            elif ans == "b":
                print("sent to Q3.")
                level = 3
                break
            else:
                print("Wrong input! Try again!")
                break

        elif level == 11:
            print("----------------------------------------------------------\n"
                  "                        YOU WON\n"
                  "----------------------------------------------------------\n"
                  "Congratulations! You won the game. You will be the greatest\n"
                  "King/Queen for your kingdom.\n"
                  "----------------------------------------------------------\n"
                  "                         THE END"
                  )
            level = "You Won!"
            break

        if out:
            break

    with open(f"Players\\playerRecord{Pid}.txt", 'w') as file:
        data[3] = level
        file.write(str(data))
    home(Pid)