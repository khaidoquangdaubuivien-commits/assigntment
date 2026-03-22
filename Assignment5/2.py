number =int(input("Enter the number : "))
if number < 2:
    print("Number is not prime")
else :
    for i in range(2,number):
        if number % i == 0:
            print("Number is not prime")
            break
    print("Number is prime")