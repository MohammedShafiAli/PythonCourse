contacts = {
    "number": 4,
    "students": 
        [
            {"name": "Ali Khan", "email": "khan@gmail.com"},
            {"name": "Hamza Ibrahim", "email": "ibrahim@gmail.com"},
            {"name": "Jon Doe", "email": "doe@gmail.com"},
            {"name": "Chen Patel", "email": "patel@gmail.com"}
        ]
}

print("Student emails:")
for student in contacts["students"]:
    print(student["email"])

input("Press any key to continue")