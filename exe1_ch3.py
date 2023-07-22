#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = int(input("Enter your working hours: "))
rate = 10

if hours > 40:
  overtime_pay = (40 * rate) + ((hours-40) * 10 * 1.5)       # 40 * 10 refers to the original pay without overtime
  print("Pay: " + str(overtime_pay))

else: 
  original_pay = hours * rate
  print("Pay: " + str(original_pay))
