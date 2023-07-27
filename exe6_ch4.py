'''Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).'''

# For this exercise, we will use the equation: total_pay = (number of hours*rate) + (hours-40 * 15)

hours = int(input("Enter your working hours: "))
def countepay(hours, rate):
    if hours > 40:
        overtime_pay = (40 * rate) + ((hours - 40) * 10 * 1.5)  # 40 * 10 refers to the original pay without overtime
        print("Pay: " + str(overtime_pay))

    else:
        original_pay = hours * rate
        print("Pay: " + str(original_pay))

countepay(45, 10)