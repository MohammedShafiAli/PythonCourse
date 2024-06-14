gender = input("Are you male or female?\n")
age = int(input("What is your age?\n"))

if gender == "male" and age >= 50:
    print("Golf")
elif gender == "male" and age < 50:
    print("Football")
elif gender == "female" and age >= 50:
    print("Swimming")
elif gender == "female" and age < 50:
    print("Netball")

input("Press any key to exit")
