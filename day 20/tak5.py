num = int(input("enter number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("your number is not prime number")
            break
        else:
            print("your number is prime number")