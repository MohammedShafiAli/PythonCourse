base_price = float(input("What is the base price of the car?\n"))

tax_percentage = 0.2
license_percentage = 0.15

tax = base_price * tax_percentage
license = base_price * license_percentage
dealer_prep = 150
destination_charge = 50

total = base_price + tax + license + dealer_prep + destination_charge
print("The total price is £" + str(total))

input("Press any key to exit")