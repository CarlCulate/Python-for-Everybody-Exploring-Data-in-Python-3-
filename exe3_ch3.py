grade = input("Please enter your grade: ")

try:
    to_float = float(grade)

    if to_float > 1.0 or to_float < 0:
        print("Out of range.")

    elif to_float >= 0.9:
        print("Grade: A")

    elif to_float >= 0.8 :
        print("Grade: B")

    elif to_float >= 0.7:
        print("Grade: C")

    elif to_float >= 0.6:
        print("Grade: D")

    elif to_float < 0.6:
        print("Grade: F")

except:
    print("Error, please enter a valid numeric grade")