# A program that prints all numbers from 0 to 100 except numbers ending with 0
for i in range(101):
    if i % 10 != 0:
        print(i)