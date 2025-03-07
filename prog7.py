# A program that asks the user to enter 10 numbers and print the sum of all the numbers
sum = 0
for i in range(10):
    num = int(input("Enter a number: "))
    sum += num
print("Sum of all the numbers:", sum)