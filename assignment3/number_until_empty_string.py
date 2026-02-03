print("Enter an empty string to quit")

smallest = None
largest = None

while True:
    Numbers = (input("Enter a number: "))
    if Numbers == "":
        break

    Numbers = float(Numbers)

    if largest is None or Numbers > largest:
        largest = Numbers

    if smallest is None or Numbers < smallest:
        smallest = Numbers

print(smallest)
print(largest)