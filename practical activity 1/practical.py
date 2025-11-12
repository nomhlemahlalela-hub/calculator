def check_age_and_print():
    # Decision making
    # accepts user's age (input) and check if user is adult or minor

    name = input("enter your name: ")
    surname = input("enter your surname: ")
    age = int(input("enter your age: "))

    if age >= 18: 
        print(name, surname, "you are an adult.")
    else:
        print(name, surname, "you are a minor.")
        print("You are not eligible to vote.")

    # Loops (Repetition)
    for i in range(3):
        print(name, surname, i)

# Call the functionif __name__ == "__main__":
if __name__ == "__main__":
    check_age_and_print()
