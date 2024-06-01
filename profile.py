import os
import subprocess


def profile(name):
    gold = 100
    progress = 0
    id1 = 0
    password = input("Enter Password: ")

    while True:
        try:
            id1 += 1
            path = (f"E:\\Python Codes\\PROJECTS\\"
                    f"Text_Adventure_Game\\Players"
                    f"\\playerRecord{id1}.txt")

            list1 = [name, id1, gold, progress, password]
            data = str(list1)

            if os.path.exists(path):
                pass
            else:
                subprocess.run('cls', shell=True)
                print(f"-------------------------------------------------\n"
                      f"Welcome to Text Adventure Game!\nYour id is: {id1}"
                      f"\n------------------------------------------------\n"
                      f"Please do not forget your id. Can be used for")
                print(f"Log-in again.")
                with open(f'Players/playerRecord{id1}.txt', 'w') as file:
                    file.write(data)
                break

        except Exception as e:
            print(e)
    return id1