def  hemoglobinvalue():

    biologicalsex = input("Please enter your biological sex(male/female): ")
    hemoglobinvalue = float(input("Please enter your hemoglobin value: "))
    if biologicalsex == "male" and hemoglobinvalue > 167:
        print("Your hemoglobin value is high")
    elif biologicalsex == "female" and hemoglobinvalue > 155:
        print("Your hemoglobin value is high")
    elif biologicalsex == "male" and hemoglobinvalue  < 134:
        print("Your hemoglobin value is low")
    elif biologicalsex == "female" and hemoglobinvalue < 117:
        print("Your hemoglobin value is low")
    elif biologicalsex == "male" and 134< hemoglobinvalue < 167:
        print("Your hemoglobin value is normal")
    elif biologicalsex == "female" and 117 < hemoglobinvalue < 155:
        print("Your hemoglobin value is normal")

hemoglobinvalue()