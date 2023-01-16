#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Nov 2022
# This program sees if you guess the right number using while true

import random


def main():
    # This program sees if you guess the right number using while true

    # Input, Process and Output
    while True:
        guess_as_string = input("\nEnter a whole number between 0-9: ")

        try:
            guess_as_int = int(guess_as_string)
            random_number = random.randint(0, 9)
            if guess_as_int == random_number:
                print("\nYou guessed right.")
                break
            else:
                print("\nYou guessed wrong, please try again.")

        except ValueError:
            print("\nPlease enter a valid number.")

    print("\nDone.")


if __name__ == "__main__":
    main()
