def sum_numbers(text):
    total = 0
    number = ""

    for char in text:
        if char.isdigit():
            number += char
        else:
            if number != "":
                total += int(number)
                number = ""


    if number != "":
        total += int(number)

    return total


text = "Today is January 16, 2025. The temperature is 11 degrees Celsius."
print(sum_numbers(text))