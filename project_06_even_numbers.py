number = int(input("Enter a number: "))

print("Even Numbers:")

for i in range(1, number + 1):
    if i % 2 == 0:
        print(i)
