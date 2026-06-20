"""
Project 04: Multiplication Table Generator
Author: Rushika Patel

This program generates the multiplication table
of a number entered by the user.
"""

number = int(input("Enter a number: "))

print(f"\n===== Multiplication Table of {number} =====")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("===================================")
