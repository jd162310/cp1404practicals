"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    score = user_score()
    grade(score)
    score_random = random_score()
    grade(score_random)
def user_score():
    return float(input("Enter score: "))

def grade(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
        print("you get a prize")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def random_score():
    score = random.randint(0, 100)
    print("random score is: ", score)
    return score
main()