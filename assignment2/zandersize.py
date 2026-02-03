def  checkzandersize():

    zander_size = float(input("Please enter the length of your zander(cm): "))
    sizelimit = 42

    if zander_size < sizelimit:
        print("Release the fish back into the lake!")
        print(f"Your zander size is {sizelimit - zander_size} (cm) below the size limit")
    else:
        print("Your zander is big enough to bring home")

checkzandersize()


