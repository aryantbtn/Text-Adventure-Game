import os
import ast
import subprocess


def newPlayer():
    from profile import profile # type: ignore
    subprocess.run('cls', shell=True)
    print("---------------------------------------\n"
          "             Sign-up\n"
          "---------------------------------------")
    name = input("Enter your name: ")
    n = profile(name)
    return n


def existingPlayer():
    while True:
        try:
            subprocess.run('cls', shell=True)
            print("---------------------------------------\n"
                  "             Sign-in\n"
                  "---------------------------------------")
            id1 = int(input("Enter your id: "))

            path = (f"E:\\Python Codes\\PROJECTS\\"
                    f"Text_Adventure_Game\\Players"
                    f"\\playerRecord{id1}.txt")
            if os.path.exists(path):
                with open(f"Players\\playerRecord{id1}.txt", 'r') as file:
                    data = file.read()
                    data = ast.literal_eval(data)
                    password = data[4]
                    Pass = input("Enter password: ")
                    if password == Pass:
                        return id1
                    else:
                        jkl = input("----------------------------------------------\n"
                                    "Wrong Password!\n"
                                    "----------------------------------------------\n"
                                    "Click \"Enter\" : to Try Again...\n"
                                    "\"q\": to go back...\n"
                                    "----------------------------------------------\n"
                                    "Response here: ")
                        if jkl == "q":
                            n = login()
                            return n
                        else:
                            pass
            else:
                print("-----------------------------------------------------\n"
                      "Player does not exists!")
                np = input("--------------------------------------------------\n"
                           "\"Enter\": to try again...\n"
                           "\"q\": to go back...\n"
                           "--------------------------------------------------\n"
                           "Response here: ")
                if np == "q":
                    pid = login()
                    return pid
                else:
                    pass
                subprocess.run('cls', shell=True)

        except ValueError:
            subprocess.run('cls', shell=True)
            ikl = input("--------------------------------------\n"
                        "Wrong Input! Try again...\n"
                        "Enter Integer number only..\n"
                        "---------------------------------------\n"
                        "              Hit Enter\n"
                        "---------------------------------------")


def login():
    option2 = 0
    while True:
        while True:
            try:
                subprocess.run('cls', shell=True)
                print("-----------------------------------------------")
                print("               Welcome User!!")
                print("-----------------------------------------------")
                option2 = int(input("Please...\n1. Sign-in\n2. Sign-up\n3. Exit\n"
                                    "---------------------------\n"
                                    "Choose option: "))
                break
            except ValueError:
                msg = input("----------------------------\n"
                            "Wrong Input! Try Again...\n"
                            "----------------------------")

        if option2 == 1 or option2 == 2 or option2 == 3:
            match option2:
                case 1:
                    subprocess.run('cls', shell=True)
                    n = existingPlayer()
                    return n

                case 2:
                    n = newPlayer()
                    return n
                case 3:
                    subprocess.run('cls', shell=True)
                    quit()
        else:
            msg = input("---------------------------\n"
                        "Wrong input! Try again...\n"
                        "---------------------------")