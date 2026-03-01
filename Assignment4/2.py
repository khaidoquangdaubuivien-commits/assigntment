def colorcheck():
    color = input("Enter your color: ")
    validchars = "0123456789ABCDEFabcdef"
    if color.startswith("#") and len(color) == 7 and all(c in validchars for c in color[1:]):
        print("True")
    else:
        print("False")

colorcheck()
