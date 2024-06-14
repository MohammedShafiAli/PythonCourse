
message = input("Enter message: \n")
backwards = ""
for i in range(len(message) - 1, -1, -1):
    backwards += message[i]

print(backwards)