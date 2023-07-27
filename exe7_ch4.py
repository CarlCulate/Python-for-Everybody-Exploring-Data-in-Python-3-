'''Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.'''

# Score Grade
# > 0.9 A
# > 0.8 B
# > 0.7 C
# > 0.6 D
# <= 0.6 F

# Begin the program by defining the function
def computegrade(grade):

    try:
        if grade > 1 or grade <0:
            print("Grade: Bad score")
        elif grade > 0.9:
            print('Grade: A')
        elif grade > 0.8:
            print('Grade: B')
        elif grade > 0.7:
            print('Grade: C')
        elif grade > 0.6:
            print('Grade: D')
        elif grade <= 0.6:
            print('Grade: F')

    except:
        print("Bad score")

computegrade(0.9)