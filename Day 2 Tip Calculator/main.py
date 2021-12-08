# Tip Calculator
# 12/08/2021
# Jeff Kern

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? "))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15 "))
numberSplit = int(input("How many people to split the bill? "))
totalPercent = float(round(percent/100 * bill, 2))
totalBill = float(round(bill + totalPercent, 2))

# Using "{:.2f}".format makes sure to show two decimal places, even with ending zeros

math = "{:.2f}".format(totalBill / numberSplit)

print(f"Each person should pay: ${math}")