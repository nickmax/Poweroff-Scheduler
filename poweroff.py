#!/usr/bin/python3

import progress
from progress.bar import Bar
from functions import *

optionlist = ["1","2"]


def poweroff():
    logo()
    start()
    n = 0
    while  n == 0:
        option = input("-->")
        if option not in optionlist:
            False
            n += 0
            print("Please try again")
        elif option in optionlist and option == "1":
            timer()
            n +=1
            quit()
            
        elif option in optionlist and option == "2":
            power_off()
            n += 2
            quit()
            
            
poweroff()