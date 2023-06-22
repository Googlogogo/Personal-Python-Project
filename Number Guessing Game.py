import random
import time

print("Number Guessing Game---A Fantastic Way to Improve Calculating Skills".center(150))
print("Welcome to Number Guessing Game!")
time.sleep(0.5)
print("Ready?")
time.sleep(0.5)
print("Set?")
time.sleep(0.5)
print("Go!\n")

points = 0

while True:
    counts = 13
    answer = random.randint(1, 10000)

    while counts > 0:
        g = input("Pick a whole number from 1 to 10000: ")
        if g.count(".") == 1 and not g.startswith(".") and not g.endswith("."):
            print("ONLY WHOLE NUMBERS PLEASE!")
            # counts -= 1
            print("You have", counts, "guess(es) left. Keep trying!")
            continue
        else:
            guess = int(g)
            # a = 0
            # b = int(5)
            # print("DRUMROLL PLEASE: ")
            # while a < b:
            #     m = b - a
            #     print(m, end=" ")
            #     time.sleep(1)
            #     a += 1

            if guess == answer:
                print("\nCORRECT!")
                print("Wonderful job! You earned 10 points! \n")
                points += 10
                break

            else:
                if guess < answer:
                    print("\nToo SMALL!")
                else:
                    print("\nToo BIG!")
                counts -= 1
                if bool(counts <= 0):
                    print("The correct answer is: " + str(answer))
                    print("You lost 10 points! \n")
                    points -= 10
                else:
                    print("You have", counts, "guess(es) left. Keep trying!\n")

    once_more = input('Play Again (Type "Y" or "N") ? ')
    if once_more != "Y":
        print("Thank you for playing! Your total points: " + str(points))
        break
    else:
        continue
