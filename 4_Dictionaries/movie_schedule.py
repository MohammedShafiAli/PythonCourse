current_movies = {"Shrek": "11:00am",
                  "Spiderman": "1:00pm",
                  "Xmen": "3:00pm",
                  "Batman": "5:00pm"}

print("Where showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, "is showing at", showtime)

input("Press any key to exit")