# Factorial of a given number 

num = int(input("enter a number here : "))
fact = 1
if num < 0:
    print("Factorial of 0 does not exist")
if num == 0:
    print("Factorial of 0 is ",1)
if num > 0:
    for i in range (1, num+1):
        fact = fact*i
print("Factorial of th given number is ",fact)
        