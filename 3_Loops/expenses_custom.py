total = 0
expenses = []
num_expenses = int(input("How many expenses would you like to enter? "))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)

print('You spent £', total, sep='')

input("Press any key to exit.")