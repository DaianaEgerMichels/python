print("*******************************")
print("Welcome to the divination game!")
print("*******************************")

secret_number = 47

kick = input("Enter a number: ")

print("You typed: ", kick)

kick = int(kick)

if secret_number == kick:
    print("You're right :)")
else:
    print("You're wrong :(")