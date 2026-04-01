questions = (   "Lu jelek gak : ",
                "Lu bau gak : ", 
                "Pendek gak : ", 
                "Autis gak : ", 
                "Pinter gak : ")
options = ( ("A : Iya", "B : Gak", "C : Gak tau", "D: Lu kali", "E: Bodo ah"), 
            ("A : Iya", "B : Gak", "C : Gak tau", "D: Lu kali", "E: Bodo ahb"), 
            ("A : Iya", "B : Gak", "C : Gak tau", "D: Lu kali", "E: Bodo ahc"), 
            ("A : Iya", "B : Gak", "C : Gak tau", "D: Lu kali", "E: Bodo ahd"), 
            ("A : Iya", "B : Gak", "C : Gak tau", "D: Lu kali", "E: Bodo ahe"))
answers = ("A", "A", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Youre answer is right")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print(f"You're score is {score}")