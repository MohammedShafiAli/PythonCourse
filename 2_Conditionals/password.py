saved_password = "monkey"
input_password = input("Enter you password:\n")

if input_password == saved_password:
    print("Access granted")
else:
    print("Access denied")

input("Press any key to exit")