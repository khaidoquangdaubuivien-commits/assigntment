while True:
    inches = float(input("Enter inches: "))

    if inches < 0 :
        break

    else:
        print(f"Centimeters: {inches * 2.54}")


