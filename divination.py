import random

# while (rounded <= total_attempts):
#     print("Attempts: {} of {}".format(rounded, total_attempts))
#     kick = input("Enter a number: ")
#     print("You typed: ", kick)
#
#     kick = int(kick)
#
#     hit = secret_number == kick
#     bigger = kick > secret_number
#     smaller = kick < secret_number
#
#     if (hit):
#         print("You're right :)")
#     else:
#         print("You're wrong :(")
#         if(bigger):
#             print("Your kick was bigger than the secret number.")
#         elif(smaller):
#             print("Your kick was smaller than the secret number.")
#
#     rounded += 1
def play():
    print("*******************************")
    print("Welcome to the divination game!")
    print("*******************************")

    secret_number = random.randrange(1, 101)
    total_attempts = 0
    rounded = 1
    points = 1000
    print(secret_number)

    print("Choose difficulty level")
    print("(1) Easy (2) Medium (3) Difficult")

    level = int(input("Set the level:"))

    if (level == 1):
        total_attempts = 20
    elif (level == 2):
        total_attempts = 10
    else:
        total_attempts = 5

    for rounded in range(1, total_attempts + 1):
        print("Attempts: {} of {}".format(rounded, total_attempts))
        kick = input("Enter a number between 1 and 100: ")
        print("You typed: ", kick)

        kick = int(kick)

        if (kick < 1 or kick > 100):
            print("You must enter a number between 1 and 100!")
            continue

        hit = secret_number == kick
        bigger = kick > secret_number
        smaller = kick < secret_number

        if (hit):
            print("You're right :)")
            print("Your score was {} points".format(points))
            break
        else:
            print("You're wrong :(")
            if(bigger):
                print("Your kick was bigger than the secret number.")
            elif(smaller):
                print("Your kick was smaller than the secret number.")
            lost_points = abs(secret_number - kick)
            points = points - lost_points

    print("End the game...")

if (__name__ == "__main__"):
    play()