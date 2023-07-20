import random


def play():
    welcome_game()
    secret_word = get_secret_word()

    right_letters = ["_" for letter in secret_word]
    print(right_letters)

    right = False
    hanged = False
    mistakes = 0


    while(not hanged and not right):

        kick = capture_kick()

        if(kick in secret_word):
            mark_correct_kick(kick, right_letters, secret_word)
        else:
            mistakes += 1
            print("Ops, you made a mistake! {} attempts left.".format(6 - mistakes))
            draw_gallows(mistakes)

        hanged = mistakes == 7
        right = "_" not in right_letters
        print(right_letters)

    if(right):
        print_message_won()
    else:
        print_message_lost(secret_word)



def draw_gallows(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
def print_message_lost(secret_word):
    print("You lost :(")
    print("The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def print_message_won():
    print("You won :)")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mark_correct_kick(kick, right_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (kick == letter):
            print("Found the letter {} in position {}".format(letter, index))
            right_letters[index] = letter
            print(right_letters)
        index += 1


def capture_kick():
    kick = input("Say a letter: ")
    kick = kick.strip().upper()
    return kick


def get_secret_word():
    file = open("words.txt", "r")
    words = []
    for line in file:
        line = line.strip()
        words.append(line)
    file.close()
    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def welcome_game():
    print("*******************************")
    print("Welcome to the gallows game!")
    print("*******************************")

if (__name__ == "__main__"):
    play()
