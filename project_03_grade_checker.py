"""
Project 03: Grade Checker
Author: Rushika Patel

This program takes marks as input
and displays the grade.
"""

marks = int(input("Enter your marks: "))

print("\n===== GRADE REPORT =====")

if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Result: Fail")

print("========================")
