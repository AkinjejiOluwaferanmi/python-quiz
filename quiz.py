def quiz():
    score = 0

    print("Welcome to the Python Quiz!")
    print("Answer the following questions:\n")

    # Question 1
    print("1. What is the capital of France?")
    print("a) Berlin\nb) Madrid\nc) Paris\nd) Rome")
    answer = input("Your answer: ").lower()
    if answer == "c":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is c) Paris.\n")

    # Question 2
    print("2. Python is a statically typed language. (True/False)")
    answer = input("Your answer: ").lower()
    if answer == "false":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is False.\n")

    # Question 3
    print("3. Which data type is used to store True or False?")
    print("a) int\nb) str\nc) bool\nd) float")
    answer = input("Your answer: ").lower()
    if answer == "c":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is c) bool.\n")

    # Question 4
    print("4. What keyword is used to define a function in Python?")
    print("a) def\nb) func\nc) function\nd) define")
    answer = input("Your answer: ").lower()
    if answer == "a":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is a) def.\n")

    # Question 5
    print("5. Python was created by Guido van Rossum. (True/False)")
    answer = input("Your answer: ").lower()
    if answer == "true":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong. The correct answer is True.\n")

    # Final Score
    print(f"Quiz Completed! Your final score is {score}/5.")

quiz()

