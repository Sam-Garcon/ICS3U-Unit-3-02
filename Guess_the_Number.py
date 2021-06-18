#!/usr/bin/env python3

# Created by: Sam. Garcon
# Created on: June 2021
# This program do Number Guessing 

import constants

def main():
    # this function do Number Guessing 
    
    #input
    number = random.randrange (1,10)
    guess =int("Enter number between 1 and 10")
    whille guess != Number:
        if guess < number:
            print("You guessed wrong")
            guess =int("\nEnter number between 1 and 10"))
            
            print("you guessed correct")