print("Welcome to the Car Quiz")

playing = input("Do you want to play?(Yes or No): ")

if playing.upper() != "YES":
    quit()

print("Okay! Let's start the quiz :) ")
score = 0

#Question1
answer = input("Which car brand has a logo with four interlocking rings? ")
if answer.lower() == "audi":
    print("Correct!")
    score += 5
else:
    print("Incorrect!")
#Question2
answer = input("Which company makes the Mustang? ")
if answer.lower() == "ford":
    print("Correct!")
    score += 5
else:
    print("Incorrect!")
#Question3
answer = input("Toyota is a car brand from which country? ")
if answer.lower() == "japan":
    print("Correct!")
    score += 5
else:
    print("Incorrect!")
#Question4
answer = input("Which brand is known for the luxury 3 Series and 5 Series models? ")
if answer.lower() == "bmw":
    print("Correct!")
    score += 5
else:
    print("Incorrect!")
#Question5
answer = input("Tata is a car brand from which country? ")
if answer.lower() == "india":
    print("Correct!")
    score += 5
else:
    print("Incorrect!")


print("You got " + str(int(score/5)) + " out of 5 questions correct!")
print("You got " + str((score/25)*100) + "%")




