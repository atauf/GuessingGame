from random import randint

num = randint(1, 101)
print (num)
print ("Let's play a guessing game...You'll get 5 tries to pick a number between 1 and 100!  Good Luck!")
count = 0

while count < 5:
    print ("Attempt #%d" % (count + 1))
    guess = input("Enter a number between 1 and 100: ")
    # print ("Guess: %s" % (guess))
    # print ("Num: %d" % (num))
    if guess == str(num):
        print ("You win")
        break;
    else:
        if count == 4:
            print ("GAME OVER\n")
            playAgain = input("Do you want to play again? [y/n]  ")
            if playAgain[0].lower() == "y":
                print ("Ok, here we go again!\n5 more tries!\n")
                count = 0
                num = randint(1, 100)
                print ("New number to guess is: %d" % (num))
                continue
            elif playAgain[0].lower() == "n":
                print ("Alright, catch you on the flip side!")
                break
        print ("Nope, try again")
        count += 1
input("Press 'ENTER' to end.")