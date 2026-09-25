"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
score = float(input("Enter score: "))
if 100 >= score >= 90:
    print("excellent")
elif 90 > score >= 50:
    print("passable")
elif 50 > score >= 0:
    print("bad")
else:
    print("invalid score")
