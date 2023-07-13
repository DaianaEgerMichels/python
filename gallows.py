def play():
    print("*******************************")
    print("Welcome to the gallows game!")
    print("*******************************")

    secret_word = "flower"

    right = False
    hanged = False

    while(not hanged and not right):

        kick = input("Say a letter: ")
        kick = kick.strip()
        index = 0

        for letter in secret_word:
            if(kick.lower() == letter.lower()):
                print("Found the letter {} in position {}".format(letter, index))
            index = index + 1

        print("playing...")

    print("End the game...")

if (__name__ == "__main__"):
    play()