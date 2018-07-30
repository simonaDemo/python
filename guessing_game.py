import random
A = random.randint (1,9)
counter = 0
while True:
    B = int (input("Guess the number from 1 to 9: "))
    if A == B:
        counter += 1
        print ("Yes, your guess was right. And it took you " + str(counter) + " tries ")
        break
    elif A > B:
        counter += 1
        print("The secret number is bigger. Try another one.")
    elif A < B:
        counter += 1
        print("The secret number is smaller. Try another one.")
