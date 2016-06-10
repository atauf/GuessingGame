from random import randint

print ("Let's play a guessing game...You'll get 5 tries to pick a number between\
 a range of numbers that you give me.  Good Luck!")
print ("You tell me what range you want to have to pick a number from...")
lwrBound = input("Lower bound: ")
upprBound = input("Upper bound: ")
num = randint(int(lwrBound), int(upprBound))
print (num)  #For Testing...comment this line out if you're actually playing the game.
count = 0

while count < 5:
    print ("Attempt #%d" % (count + 1))
    guess = input("Enter a number between %s and %s: " % (lwrBound, upprBound))
    # print ("Guess: %s" % (guess))
    # print ("Num: %d" % (num))
    if guess == str(num):
        print ("You win")
        break
    else:
        if count == 4:
            print ("GAME OVER\n")
            playAgain = input("Do you want to play again? [y/n]  ")
            if playAgain[0].lower() == "y":
                print ("Ok, here we go again!\n5 more tries!\n")
                count = 0
                num = randint(int(lwrBound), int(upprBound))
                print ("New number to guess is: %d" % (num)) #For Testing...comment this line out if you're actually playing the game.
                continue
            elif playAgain[0].lower() == "n":
                print ("Alright, catch you on the flip side!")
                break
        print ("Nope, try again")
        count += 1
input("Press 'ENTER' to end.")