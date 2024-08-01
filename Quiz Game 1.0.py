print("Welcome to our quiz game.")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit("Okay! See you later.")

print("Okay! Let's play.")
score = 0

answer = input("What does RAM stand for? ")
if answer.lower() == 'random access memory':
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print("The answer is 'Random Access Memory'")

answer = input("Which team was win 2024 euro cup? ")
if answer.lower() == 'spain':
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print("The answer is 'Spain'")

answer = input("What is the largest planet in our solar system? ")
if answer.lower() == 'jupiter':
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print("The answer is 'Jupiter'")

answer = input("What year did the Titanic sink? ")
if answer.lower() == '1912':
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print("The answer is '1912'")

answer = input("Witch element has the atomic number 1? ")
if answer.lower() == 'hydrogen':
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print("The answer is 'Hydrogen'")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5)*100) + "% marks")