def remove_odd(numbers):

    even_numbers = []

    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)

    return even_numbers


def main():

    numbers = [1,2,3,4,5,6,7,8,9,10]

    new_list = remove_odd(numbers)

    print("Original list:", numbers)
    print("Without odd numbers:", new_list)


main()