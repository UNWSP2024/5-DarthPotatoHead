#Program Written By: Ainsley Bellamy
#Date Written: 02/14/2025
#Program Title: Math_Quiz


# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

#I found this cool thing that lets me generate random numbers.
import random
#Create an empty list to add scores to (basically just hold 1's and 0's so that
# I can caluclate how many the user gets right).
scores = []
#Function that acutally gives the quiz.
def math_quiz():
    for i in range(number_of_problems):
        rando1 = random.randrange(1,100)
        rando2 = random.randrange(1,100)
        print(f"What is the sum of {rando1} and {rando2}?")
        user_answer = int(input("Enter Answer: "))
        answer = rando1 + rando2
        if user_answer == answer:
            print(f"Correct; The answer is {answer}.")
            scores.append(1)
        else:
            print(f"Incorect; The answer is {answer}.")
            scores.append(0)
        print("---------------------")
#Function that adds the sum of answer the user gets right, divides it by the total number of questions,
#and multiplies by 100 for a %.
def percentage_calculator():
    added_total = sum(scores)
    percent = (added_total / number_of_problems) * 100
    return percent
#This user input determines how many times the loop in the math_quiz() function runs.
number_of_problems = int(input("How many problems would you like to answer? "))
#Call above function.
math_quiz()
user_results = percentage_calculator()
#Display final percentage.
print(f"You got {user_results:.1f}%.")