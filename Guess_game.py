#no of guesses = 9
#print guesses
#game over
#and if he wins then print no of guesses he took to finish
print("||||||||||   ||    ||   ||||||||   ||||||||   |||||||")
print("||           ||    ||   |||        ||         ||     ")
print("||  ||||||   ||    ||   ||||||||   ||||||||   |||||||")
print("||   || ||   ||    ||   |||              ||        ||")
print("||||||| ||   ||||||||   ||||||||   ||||||||   |||||||\n")
print("                 Instructions For Playing Game")
print("     1)YOu Will get in all 8 Chances to guess the number")
print("     2)If your guessed number is Greater than the hidden number you will get a command to decrement your guess")
print("     2)If your guessed number is Smaller than the hidden number you will get a command to Increment your guess\n")
n=36
chance=8
guess=0
while(True):

    no=input("Guess a number \n")

    if str(no).isnumeric():
        no=int(no)
        chance -= 1
        guess += 1
    else:
        print("Invalid Input")
        continue

    if chance == 0:
        print(chance," Chance Left \n")
        print("!!!!  GAME OVER  !!!!\n")
        print("The number was ",n)
        break


    if no == n:
        print("You have Guessed the right number in ",guess," guesses \n")
        print("     Congratulations !!! You Win  \n")
        break
    elif no > n :
        print("Decrement your guess !!!")
        print("You have ",chance," Chance Left !\n")
    elif no < n:
        print("Incremenet Your guess !!!")
        print("You have ",chance," Chance Left !\n")
    else:
        print("Invalid Input")
