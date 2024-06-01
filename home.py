import ast
import os
import subprocess


def home(n):
    from time import sleep
    bn = input("----------------------------------------\n"
               "Hit Enter to continue...")
    print("----------------------------------------\n"
          "              Loading", end="")
    for i in range(3):
        print(".", end="", flush=True)
        sleep(0.5)

    sleep(0.2)
    global option1
    while True:
        while True:
            try:
                subprocess.run('cls', shell=True)
                print("---------------------------------------------------")
                print("         WELCOME TO TEXT ADVENTURE GAME")
                print("---------------------------------------------------")
                option1 = int(input("1. Start Game"
                                    "\n2. Profile"
                                    "\n3. Logout"
                                    "\n4. How to play?"
                                    "\n5. Quit"
                                    "\nChoose options from 1 to 5: "))
                if isinstance(option1, int):
                    break
                else:
                    continue
            except ValueError:
                subprocess.run('cls', shell=True)
                print("Wrong Input! Try again...1")
                continue
        if 1 <= option1 <= 5:
            match option1:
                case 1:
                    subprocess.run('cls', shell=True)
                    from textAdventure import textAdventure
                    textAdventure(n)
                case 2:
                    path = (f"E:\\Python Codes\\PROJECTS\\"
                            f"Text_Adventure_Game\\Players"
                            f"\\playerRecord{n}.txt")
                    if os.path.exists(path):
                        with open(f"Players\\playerRecord{n}.txt", 'r') as file:
                            data = file.read()
                            data = ast.literal_eval(data)
                            name = data[0]
                            id = data[1]
                            gold = data[2]
                            progress = data[3]

                    subprocess.run('cls', shell=True)
                    print("--------------------------------------\n"
                          "                Profile\n"
                          "--------------------------------------\n"
                          f"Player id: {id}\n"
                          f"Player name: {name}\n"
                          f"Gold: {gold}\n"
                          f"Progress: {progress}\n"
                          f"-------------------------------------")
                    np = input("Hit Enter to go back...\n"
                               "-------------------------------------")
                case 3:
                    subprocess.run('cls', shell=True)
                    from login import login
                    home(login())
                case 4:
                    subprocess.run('cls', shell=True)
                    print("--------------------------------------------"
                          "\n              How to play?\n"
                          "--------------------------------------------\n"
                          "1. Choose the options you like and move on.\n"
                          "2. Defeat enemies for an easy win.\n"
                          "3. Or Bring home the worth of gold that could\n"
                          "   also be a victory. 5 times of what you get.\n"
                          "4. You get 100 gold at the start of the game\n"
                          "   use it carefully when betting in mini games.\n"
                          "5. Smart choices can be a fast win.\n "
                          "--------------------------------------------")

                    n1 = input("Hit Enter to go back...")
                case 5:
                    quit()
        else:
            subprocess.run('cls', shell=True)
            print("Wrong input! Try again...2")
            home(n)