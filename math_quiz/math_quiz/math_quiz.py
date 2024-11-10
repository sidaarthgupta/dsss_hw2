import random

def random_integers(min, max): # function to select random integer
    return random.randint(min, max)


def random_operator(): # Adding a function to select a random operator among +. - and *
    return random.choice(['+', '-', '*'])


def problem_question(n1, n2, o): # Adding a function to create maths equations with the selected operator
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2 # if operator from function randon_operator() is +, add
    elif o == '-': a = n1 - n2  # if operator from function randon_operator() is -, subtract
    else: a = n1 * n2 # if operator from function randon_operator() is *, multiply
    return p, a 

def math_quiz():
    correct_answers = 0 # variable with initial score value = 0
    total_questions = 5 # Total number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(total_questions): # for loop to ask a different random maths question

        # calling randon_integers() function and storing values in n1 and n2, and random_operator() function and storing value in o
        n1 = random_integers(1, 10); n2 = random_integers(1, 10); o = random_operator() 

        # calling problem_question() function and storing the question and answer in two variables, Problem and Answer respectively
        PROBLEM, ANSWER = problem_question(n1, n2, o) 
        print(f"\nQuestion: {PROBLEM}") # print the question
        while True: # While loop to force the user to enter an integer for the answer to be considered
            useranswer = input("Your answer: ")
            # Try and except to show the error if input is not an integer
            try:
                useranswer = int(useranswer)
            except ValueError:
                print ('Please enter an integer')
                continue
            if useranswer == ANSWER:
                print("Correct! You earned a point.") # if useranswer is correct, increment the correct_answers variable by 1
                correct_answers += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.") # else print the correct answer
            break

    print(f"\nGame over! Your score is: {correct_answers}/{total_questions}") # After total_questions are asked, display the score.

if __name__ == "__main__":
    math_quiz()

