def playAgain():
    print("Do you want to play again? (YES or NO)")

    answer = input("").upper()

    if answer == "YES":
        start()

    else:
        exit()

def gameOver(reason):
    print(reason)
    print("Game Over!")
    playAgain()

def newCareer():
    print("\nYou have been working really hard learning to code. You are offered a new career as a developer.")
    print("\nWhat do you do?")
    print("1). Take the offer.")
    print("2). Continue being a teacher. It's all for the kids.")

    answer = input()

    if answer == "1":
        print("You win!")

    elif answer == "2":
        gameOver("FTK. You lose!")

    else:
        print("Wrong input. Choose a number")
        newCareer()

def sponsor():
    print("\nYou love working with students but you begin realize the education system is flawed and teaching will never pay well.")
    print("\nWhat do you do?")
    print("1). Look into learning a different skill so you can change careers.")
    print("2). Continue being a teacher. Maybe it will get better.")

    answer = input()

    if answer == "1":
        newCareer()
    
    elif answer == "2":
        gameOver("You lied to yourself. It will never get better. You lose!")
        
    else:
        print("Wrong input. Choose a number")
        sponsor()

def earlyCollege():
    print("\nYou are a great teacher and go above and beyond for the students.")
    print("\nYour boss notices this and asks you to become a sponsor for the early college after school program.")
    print("What do you do?")
    print("A). Accept Do it for the students!")
    print("B). Decline. I don't have time for this.")

    answer = input("").lower()

    if answer == "A":
        sponsor()

    elif answer == "B":
        gameOver("You are selfish for declining. You lose!")

    else:
        print("Wrong input.Choose a letter.")
        earlyCollege()
        

def evaluation():
    print("\nYou did so good in your yearly evaluation and get asked to be an Early College Teacher.")
    print("\nWhat do you do?")
    print("1). Accept.")
    print("2). Decline.")

    answer = input("")

    if answer == "1":
        earlyCollege()

    elif answer == "2":
        gameOver("You are ungrateful! You lose!")

    else:
        print("Wrong input. Choose a number.")
        evaluation()
        

def software():
    print("Congrats you win!")
    playAgain()

def teacher():
    print("Congrats! You are now a teacher.")
    print("\nYou will have your yearly evaluation soon.")
    print("\nWhat do you do?")
    print("1). Rock it! Teaching is the best!")
    print("2). Sit at your desk and be lazy.")

    answer = input("")

    if answer == "1":
        evaluation()
        
    elif answer == "2":
        gameOver("You can't sit at your desk all day! You are fired!")

    else: 
        print("Wrong input. Choose a number.")
        teacher()
        

def start():
    print("You have just graduated college")
    print("\nYou have two career choices")
    print("\nDo you choose to become a teacher or a software developer?")
    print("A). Teacher")
    print("B). Software Developer")

    answer = input("").upper()

    if answer == "A":
        teacher()

    elif answer == "B":
        software()

    else:
        print("Wrong input. Choose a letter.")
        start()
        
start()