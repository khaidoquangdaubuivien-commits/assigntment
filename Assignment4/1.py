def coursecheck():
    course = input("Enter course name : ")
    if course[:3].isupper() and  course[:3].isalpha() and course[3:].isdigit():
        print("True")
    else:
        print("False")

coursecheck()
