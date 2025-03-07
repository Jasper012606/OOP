# A program that asks the user to input 10 numbers and prints the how many are the odd numbers
odd = 0
for i in range(10):
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        odd += 1
print("Number of odd numbers:", odd)