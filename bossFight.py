import random
import subprocess

subprocess.run('cls', shell=True)


def bossFight(level, Pattack, Battack, Phealth, Ehealth, W, L):
    Life = 3
    level = level
    EnemyAttack = Battack

    while Life != 0:
        Player_attack = Pattack
        Player_health = Phealth
        Boss_health = Ehealth
        Bbattle = ['a', 's', 's', 'd', 's', 's', 'a', 'd', 'a', 's', 'a', 'd', 'a', 's', 'a', 's']
        subprocess.run('cls', shell=True)
        a = input(f"-----------------------------------------------\n"
                  f"Defeat an enemy to move ahead. Best of luck.\n"
                  f"-----------------------------------------------\n"
                  f"You have {Life} life left. Defeat the enemy!\n"
                  f"-----------------------------------------------\n"
                  f"Hit "'Enter'" to continue or q to quit : ")
        subprocess.run('cls', shell=True)
        if a == 'q':
            break

        while Boss_health != 0 or Player_health != 0:
            print("***************************************************************")
            array1 = [25, 15, 15, 10, 35, 30, 50, 40]
            bdmg = random.randint(0, len(array1) - 1)
            Boss_attack = array1[bdmg]
            Boss_attack = int(Boss_attack * EnemyAttack)

            if bdmg >= 4:
                print("-----------------------\n"
                      "{Critical Section}\n"
                      "-----------------------")
            else:
                print("-----------------------\n"
                      "{Vital Section}\n"
                      "-----------------------")

            print(f"Enemy Health : {Boss_health} \t Player Health : {Player_health}")
            b = random.randint(0, len(Bbattle) - 1)

            a = input("Enter a/d to attack/defence : ")
            subprocess.run('cls', shell=True)
            if a == 'q':
                quit()
            if a == 'a' and Bbattle[b] == 's':
                Boss_health -= Player_attack
                if Boss_health <= 0:
                    Boss_health = 0
                    break
                subprocess.run('cls', shell=True)
                print("***************************************************************\n"
                      "Player damage :", Player_attack, "\t Enemy Stun!")

            elif a == 'a' and Bbattle[b] == 'a':
                print("***************************************************************\n"
                      "Player damage :", Player_attack, f"\t Enemy damage:{Boss_attack}")
                Player_health -= Boss_attack
                Boss_health -= Player_attack
                if Player_health <= 0 and Boss_health <= 0:
                    Player_health = 0
                    Boss_health = 0
                    break
                elif Player_health <= 0:
                    Player_health = 0
                    break
                elif Boss_health <= 0:
                    Boss_health = 0
                    break

                subprocess.run('cls', shell=True)
                print("***************************************************************\n"
                      f"Player damage : {Player_attack} \t Enemy damage : {Boss_attack} ")
            else:
                subprocess.run('cls', shell=True)
                if a == 'd':
                    if Bbattle[b] == 's':
                        print("***************************************************************\n"
                              "Player Defence! \t Enemy Stun!")
                    elif Bbattle[b] == 'a':
                        print("***************************************************************\n"
                              "Player Defence! \t Enemy Attack :", Boss_attack)
                    else:
                        print("***************************************************************\n"
                              "Player Defence! \t Enemy Defence!")
                else:
                    print("***************************************************************\n"
                          "Player damage :", Player_attack, "\t Enemy Defence!")

        if Player_health == 0 and Boss_health == 0:
            print("***************************************************************")
            print("                  Tie! No one wins!\n Player Health : 0 \t Enemy Health : 0")
            print("***************************************************************")
            n = input("Hit Enter to continue...")
        elif Boss_health == 0:
            print("***************************************************************")
            print(f"                    You Win! \nEnemy Health : 0 \t Player Health : {Player_health} ")
            print("***************************************************************")
            n = input("Hit Enter to continue...")
            level = W
            break
        elif Player_health == 0:
            print("***************************************************************")
            print(f"                    You lost! \nEnemy Health : {Boss_health} \t Player Health : 0")
            print("***************************************************************")
            n = input("Hit Enter to continue...")
            Life -= 1
            if Life == 0:
                level = L

    return level