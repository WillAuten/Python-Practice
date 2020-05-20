hourlyWage = float(input("Input your hourly wage: "))
regHours = int(input("Input your total regular hours worked: "))
overHours = int(input("Input your total over time hours worked: "))

totalRegHours = hourlyWage * regHours
print ("You earned", totalRegHours, "working regular hours")

totalOver = 1.5 * hourlyWage * overHours
print ("You earned", totalOver, "working overtime hours")                

totalWeeklyPay = totalRegHours + totalOver
print ("In total this week your earned", totalWeeklyPay)
