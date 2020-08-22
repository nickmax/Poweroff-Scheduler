import colored
import time
from time import sleep
import progress
from progress.bar import Bar
from colored import fg, attr

import os


blink = colored.attr("blink")


blue = fg("light_cyan")
green = fg("light_green")
magenta = fg("magenta")
yellow = fg("light_yellow")
reset = colored.attr("reset")


def logo():
    print(blue + " ____     ___   __        __  _____   ____             ___    _____   _____ " + reset)
    print(green + "|  _ \   / _ \  \ \      / / | ____| |  _ \           / _ \  |  ___| |  ___|" + reset)
    print(blue + "| |_) | | | | |  \ \ /\ / /  |  _|   | |_) |  _____  | | | | | |_    | |_   " + reset)
    print(green + "|  __/  | |_| |   \ V  V /   | |___  |  _ <  |_____| | |_| | |  _|   |  _| " + reset)
    print(blue + "|_|      \___/     \_/\_/    |_____| |_| \_\          \___/  |_|     |_|   " + reset)


def start():
    print("Choose option!")
    print(yellow + "1.Timer"+reset)
    print(magenta + "2.Set a time when the computer will automatically poweroff!"+reset)

def bar_():
    with Bar(max=1000) as bar:
        for i in range(1000):
            bar.next()
            sleep(0.001)
        bar.finish


def stop():
    bar_()
    print(magenta + "Powering Off!"+reset)
    
def timer():
    timer_time = int(input("Input time in Minutes:"))
    print("The computer will shutdown after "+ magenta(str(timer_time))+reset+" Minutes")
    os.system("shutdown -P " +str(timer_time))
    
def power_off():
        user_time = input("Input time (In 24hr clock system:"+(blue +"eg. 12:00" + reset)+ " --> ")
        bar_()
        os.system("shutdown -P "+ str(user_time))
    
    
    
