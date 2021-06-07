import time, colorama
from playsound import playsound
from colorama import Fore, Back, Style
colorama.init()

def work():

    print('\x1b[2J' + Fore.RED + "Time to work - next twenty-five minutes")
    playsound('./sfx/Metal_Gong.mp3')
    time.sleep(25 * 60)

def shortBreak():

    print('\x1b[2J' + Fore.YELLOW + "Time for a break - next five minutes")
    playsound('./sfx/tibetan-bell-sound.mp3')
    time.sleep(5 * 60)

def longBreak():

    print('\x1b[2J' + Fore.GREEN + "Time for a long break - next thirty minutes")
    playsound('./sfx/Gong.mp3')
    time.sleep(30 * 60)

def cycle():
    try:
        cycles = 0
        while True:
            work()
            cycles = cycles + 1
            if cycles == 4:
                longBreak()
                cycles = 0
            else:
                shortBreak()
    except:
        pass
cycle()
