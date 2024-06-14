
class Critter(object): #base class on object type
    #A virtual pet
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food = 4):
        print("Brupp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def __str__(self):
        return "Hunger: " + str(self.hunger) + ", Boredom: " + str(self.boredom)
    

def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    while True:
        print("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
        choice = input("Choice: ")

        if choice == "0":
            print("Thanks for playing")
            break
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            feed = int(input("How much would you like to feed the critter? 1 - 10: "))
            crit.eat(feed)
        elif choice == "3":
            play = int(input("How long would you like to play with the critter? 1 - 10: "))
            crit.play(play)
        elif choice == "4":
            print(str(crit))
        else:
            print("Invalid choice.")

main()
input("Press any key to exit")

