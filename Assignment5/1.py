numbers = []
while True:
    number = input("Enter a number: ")
    if number == "":
        break
    numbers.append(int(number))

numbers.sort(reverse=True)
print("5 biggest num : ",numbers[:5])

