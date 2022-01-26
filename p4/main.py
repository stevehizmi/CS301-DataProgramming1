# project: p4
# submitter-netid: shizmi
# partner-netid: modonnell7

tries = input("How many tries do you want for each question: ")
initTries = tries
right = 0

def askQuestion(question="", answer="" , hint = "Check the textbook"):
    global tries
    global initTries
    global right
    print("\n"+question)
    user = input("Your answer: ")
    while int(tries) > 0:

        if user.strip().lower() == answer:
            right = right + 1
            print("\nCongratulations! You got it right.")
            break

        else:
            tries = int(tries) - 1
            if int(tries)==1:
                print("\n"+hint)
                print("You have this many remaining tries: "+ str(tries))
                user = input("Your answer: ")
            else:
                print("\nYou answered '" + user + "'. The correct answer is '"+answer+"'.")
                print("You have this many remaining tries: "+ str(tries))
                if int(tries)>=1:
                    user = input("Your answer: ")

            
    tries = initTries


            
askQuestion("What is the type of the following? "+ '"1.0" + "2.0"\na) int \nb) float \nc) str \nd) bool\ne) NoneType\n', 'c')
askQuestion("What is the type of the following? "+'"1" * 2', 'str', "notice the quotes!") 
askQuestion("What does this expression evaluate to?\n True != (3 < 2)", 'true',"Calcuate the right side first. Don't forget != means not equal to.")

print("You tried 3 questions and got " + str(right) + " right.")
