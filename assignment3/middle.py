def middle():
    enter = input("Input a string: ")
    length = len(enter)
    mid = length // 2

    if length % 2 == 0:
        return enter[mid - 1] + enter[mid]

    else:
        return enter[mid]

print(middle())
