print("Welcome to the quiz")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
     quit()
else:
     print("okay let us play :)")
point=0

answer = input("Who was the first person to step on the moon? ")
if answer.title() == "Neil Arm Strong":
    print("correct")
    point += 1
else:
    print ("incorrect")

answer = input("Which animal is known as the ship of the desert ")
if answer.title() == "Camel":
    print("correct")
    point +=1
else:
    print ("incorrect")

answer = input(" Who gave the universal law of gravitation? ")
if answer.title()== "Issac Newton":
    print("correct")
    point += 1
else:
    print ("incorrect")

print(f"your total score is {point}/3 :)")
print("thank you for playing")

