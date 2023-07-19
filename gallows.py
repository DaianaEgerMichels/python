import random


def play():
    print("*******************************")
    print("Welcome to the gallows game!")
    print("*******************************")

    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    right_letters = ["_" for letter in secret_word]

    right = False
    hanged = False
    mistakes = 0

    print(right_letters)

    while(not hanged and not right):

        kick = input("Say a letter: ")
        kick = kick.strip().upper()


        if(kick in secret_word):
            index = 0
            for letter in secret_word:
                if(kick == letter):
                    print("Found the letter {} in position {}".format(letter, index))
                    right_letters[index] = letter
                    print(right_letters)
                index += 1
        else:
            mistakes += 1
            print("Ops, you made a mistake! {} attempts left.".format(6 - mistakes))

        hanged = mistakes == 6
        right = "_" not in right_letters
        print(right_letters)

    if(right):
        print("You won :)")
    else:
        print("You lost :(")
    print("End the game...")

if (__name__ == "__main__"):
    play()