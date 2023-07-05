print("*******************************")
print("Welcome to the divination game!")
print("*******************************")

secret_number = 47
total_attempts = 3
round = 1

while (round <= total_attempts):
    print("Attempts: {} of {}".format(round, total_attempts))
    kick = input("Enter a number: ")
    print("You typed: ", kick)

    kick = int(kick)

    hit = secret_number == kick
    bigger = kick > secret_number
    smaller = kick < secret_number

    if (hit):
        print("You're right :)")
    else:
        print("You're wrong :(")
        if(bigger):
            print("Your kick was bigger than the secret number.")
        elif(smaller):
            print("Your kick was smaller than the secret number.")

    round += 1

for round in range(1, total_attempts + 1):
    print("Attempts: {} of {}".format(round, total_attempts))
    kick = input("Enter a number: ")
    print("You typed: ", kick)

    kick = int(kick)

    hit = secret_number == kick
    bigger = kick > secret_number
    smaller = kick < secret_number

    if (hit):
        print("You're right :)")
    else:
        print("You're wrong :(")
        if(bigger):
            print("Your kick was bigger than the secret number.")
        elif(smaller):
            print("Your kick was smaller than the secret number.")

print("End the game...")