"""
Wordle
Daniel Martinez
CS 1210
"""

import random
from colorama import Fore, Back, Style, init


def replay():
    x_ = ""
    while True:
        x_ = input(Style.RESET_ALL + "\nPress y to play again or press q to quit: ")
        if x_.lower() == "y" or x_.lower() == "q":
            break
    if x_ == "q":
        return False
    else:
        print()
        return True


if __name__ == "__main__":
    with open("word_list.txt") as fh:  # picks random word from list
        lst = []
        for line in fh:
            lst.append(line.strip())

    init()  # initializes colorama

    print(Style.BRIGHT + "\nWordle!\n")
    print(Style.RESET_ALL + "Guess the five letter word within six attempts.\n")

    flag = True

    while flag:
        wrong_letters = []  # letter not in word
        word = random.choice(lst)

        for attempts in range(6):
            correct_letters = 0
            guessed_letters = ["_", "_", "_", "_", "_"]  # letter in correct spot
            in_letters = ["_", "_", "_", "_", "_"]  # letter in wrong spot

            while True:
                x = input(Style.RESET_ALL + "Guess a five letter word: ")
                x = x.lower()

                if len(x) == 5 and x in lst:  # input validation
                    break
                elif len(x) == 5 and x not in lst:
                    print(Fore.RED + "Try a different word.")
                elif len(x) < 5:
                    print(Fore.RED + "Too Short.")
                else:
                    print(Fore.RED + "Too Long.")

            for n, e in enumerate(word):  # guessed letters appended to respective lists
                for i, j in enumerate(x):
                    if i == n and e == j:
                        guessed_letters[n] = j
                        correct_letters += 1
                    elif i != n and e == j:
                        in_letters[i] = j

            for n, i in enumerate(in_letters):  # prevents multiples appearing as yellow
                if (in_letters.count(i) + guessed_letters.count(i)) > word.count(i):
                    in_letters[n] = "_"

            for letter in range(5):  # prints guessed word with respective colors
                if guessed_letters[letter] == x[letter]:
                    print(Back.GREEN + Fore.BLACK + x[letter], end="")
                elif in_letters[letter] == x[letter]:
                    print(Back.YELLOW + Fore.BLACK + x[letter], end="")
                else:
                    print(Back.WHITE + Fore.BLACK + x[letter], end="")
                    if (  # so green or yellow multiples don't appear in wrong letters
                        x[letter] not in wrong_letters
                        and x[letter] not in in_letters
                        and x[letter] not in guessed_letters
                    ):
                        wrong_letters.append(x[letter])
                if letter == 4:  # formatting
                    print(Style.RESET_ALL + "")
            wrong_letters.sort()

            if correct_letters == 5 and attempts > 0:  # winning
                print(f"You guessed the correct word within {attempts + 1} attempts!")
                break
            elif correct_letters == 5 and attempts == 0:
                print("Lucky Guess!")
                break
            elif correct_letters != 5 and attempts == 5:  # losing
                print(f"You failed to guess the correct word, {Fore.RED + word}")
                break  # so wrong letters doesn't display at game over
            print(f"Incorrect letters: {wrong_letters}\n")
        flag = replay()
