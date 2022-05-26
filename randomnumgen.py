import random
number = random.randint (1,30)

number_of_guesses = 0

while number_of_guesses<5:
    guess = int(input("enter the number"))

    number_of_guesses += 1
    if guess<number:
        print ("too low")
    if guess>number:
        print ("too high")
    if guess == number:
        break
if guess == number:
    print ("you guessed the number in" +str(number_of_guesses) +'tries')
else:
    print ("the number was" +str(number))