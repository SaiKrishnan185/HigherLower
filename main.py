import os
from followers import data
import art 
import random

def screen():
    print(art.logo)

def clear():
    os.system('cls')

clear()
screen()
score = 0
game = 0
# Generate random Question
def randomQuestion():
    question = random.choice(data)
    A = question["follower_count"]
    print(f'Compare A : {question["name"]} ,a {question["description"]} ,from {question["country"]}')
    
    print(art.vs)
    
    question = random.choice(data)
    B = question["follower_count"]
    print(f'Compare B : {question["name"]} ,a {question["description"]} ,from {question["country"]}')
    print(A,B) 
    return A,B

while game == 0:
    A,B = randomQuestion()

# Generate solution
    if A>B:
        solution = "A"
    else:
       solution = "B"

# Get user answer
    print("\n")
    answer = input("Enter who has more followers\nType 'A' or 'B'\n")

# Compare answer
    if answer.upper() == solution:
        score = score + 1
        game = 0
        clear()
        screen()
        print(f"You're right. Current Score = {score}")
    else:
        game = 1
        clear()
        screen()
        print(f"\nSorry ,that's wrong. Final score : {score}")