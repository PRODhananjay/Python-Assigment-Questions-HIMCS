# Python program to check whether the given number is prime or not 

num = int(input("enter a number here : "))
if num == 1:
    print("It is not a Prime Number")
if num > 1:
    for i in range (2,num):
        if num % i == 0:
            print("It is not a prime number")
            break
    else:
         print("It is prime number")