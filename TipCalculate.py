print("====Welcome to the tip Calculator====")
bill=input("What was the total bill? $")
tip=input("How would much you like to give? 10 ,12, 15?")
people = input("How many people to split the bill?")
b=float(bill)
t=float(tip)
pp=int(people)
tip_amount=b * t /100
total=b+tip_amount
each_pay=total/pp
print(f'Each person should pay{each_pay}$')