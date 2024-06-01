import subprocess

from login import login

if __name__ == '__main__':
    while True:
        subprocess.run('cls', shell=True)
        input("----------------------------------------\n"
              "         TEXT ADVENTURE GAME\n"
              "----------------------------------------\n"
              "Hit enter to continue...")
        subprocess.run('cls', shell=True)
        from home import home
        home(login())