hours = input("Enter your working hours: ")
rate = 10

try: 
    to_int = int(hours)
    if hours > 40:
        overtime_pay = (40 * rate) + ((to_int-40) * 10 * 1.5)       # 40 * 10 refers to the original pay without overtime
        print("Pay: " + str(overtime_pay))

    else: 
        original_pay = hours * rate
        print("Pay: " + str(original_pay))

except:
    print("Error , please enter a numeric input.")