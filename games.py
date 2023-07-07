import divination
import gallows

print("*******************************")
print("Choose your game!")
print("*******************************")

print("(1) Divination (2) Gallows")

game = int(input("Wich game?"))

if (game == 1):
    print("Playing Divination")
    divination.play()
elif (game == 2):
    print("Playing Gallows")
    gallows.play()