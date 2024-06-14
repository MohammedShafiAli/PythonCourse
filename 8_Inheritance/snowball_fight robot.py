import random

class Fighter(object):
    def __init__(self, name):
        self.__name = name
        self.__health = 3
        self.__ammo = 3

    @property
    def name(self):
        return self.__name
    
    @property
    def health(self):
        return self.__health
    
    def take_turn(self, distance, other_fighter):
        self.__display_menu()
        valid_move = False
        quit_game = False
        while(not valid_move):
            choice = input("Choice: ")
            if choice == "1":
                valid_move, distance = self.__move_forward(distance)
            elif choice == "2":
                valid_move, distance = self.__move_backward(distance)
            elif choice == "3":
                valid_move = self.__make_snowball()
            elif choice == "4":
                valid_move = self.__throw_snowball(distance, other_fighter)
            elif choice == "5":
                print("Exiting game")
                quit_game = True
                break
            else:
                print("Invalid choice.")
        return distance, quit_game
 
    def __move_forward(self, distance):
        if distance == 1:
            print("Invalid move. Distance must be between 1-10.")
            return False, distance
        
        print(self.__name, "moved forward.")
        distance -= 1
        return True, distance            

    def __move_backward(self, distance):  
        if distance == 10:
            print("Invalid move. Distance must be between 1-10.")
            return False, distance
        
        print(self.__name, "moved backwards.")
        distance += 1
        return True, distance            

    def __make_snowball(self):
        if self.__ammo == 5:
            print("Invalid move. Maximum of 5 snowballs allowed.")
            return False
        
        print(self.__name, "made a snowball.")
        self.__ammo += 1
        return True            
        
    def __throw_snowball(self, distance, other_fighter):
        if self.__ammo == 0:
            print("Invalid move. No snowballs available.")
            return False
        
        print(self.__name, "threw snowball.")
        if self.__is_hit(distance):
            print("That's a hit!")
            other_fighter.__deplete_health()
        else:
            print("That's a miss!")

        self.__ammo -= 1
        return True

    def __deplete_health(self):
        self.__health -= 1

    def __display_menu(self):
        print("""
                1. Move forward
                2. Move backward
                3. Make snowball
                4. Throw snowball
                5. Exit game
            """)

    def __is_hit(self, distance):
         hit_chance = 11 - distance #chance of being hit out of 10
         num = random.randint(1,10) 
         if num in range(1, hit_chance + 1): # +1 because range() is not inclusive 
             return True
         else:
             return False
         
    def __str__(self):
        return "Fighter: " + self.__name + ", Health: " + str(self.__health) + ", Ammo: " + str(self.__ammo)

class RobotFighter(Fighter):
    def take_turn(self, distance, other_fighter):

        moves_available = [1, 2, 3, 4]
        valid_move = False
        while(not valid_move):
            choice = random.choice(moves_available)
            if choice == 1:
                valid_move, distance = self.__move_forward(distance)
            elif choice == 2:
                valid_move, distance = self.__move_backward(distance)
            elif choice == 3:
                valid_move = self.__make_snowball()
            elif choice == 4:
                valid_move = self.__throw_snowball(distance, other_fighter)
            
            if not valid_move:
                moves_available.remove(choice)

        return distance, False

class GameManager(object):
    def __init__(self, fighter1, fighter2):
        self.distance = 5
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.active_fighter = self.fighter1
        self.other_fighter = self.fighter2 

    def start_game(self):
        while(True):
            print("\n", self.active_fighter.name, "'s turn!", sep="")
            
            self.distance, self.quit_game = self.active_fighter.take_turn(self.distance, self.other_fighter)
            
            if self.quit_game:
                break
            
            self.__display_summary()

            if self.__have_winner():
                break

            self.__swith_turn()
    
    def __have_winner(self):
        if self.other_fighter.health == 0:
            print("\n", self.active_fighter.name, " WINS!!!", sep="")
            return True
        else:
            return False

    def __display_summary(self):
        print("---------------")
        print("Summary")
        print("Distance: ", self.distance)    
        print(str(self.fighter1))
        print(str(self.fighter2))
        print("---------------")

    def __swith_turn(self):
        if self.active_fighter == self.fighter1:
            self.active_fighter = self.fighter2
            self.other_fighter = self.fighter1
        else:
            self.active_fighter = self.fighter1
            self.other_fighter = self.fighter2

def main():
    print("\nWelcome to Snowball Fighter\n")

    print("""
        Game Options:
          1. Play Human
          2. Play Computer
    """)

    while True:
        choice = input("Enter choice: ")
        if choice == "1":
            name1 = input("Enter player 1 name: ")
            name2 = input("Enter player 2 name: ")
            fighter1 = Fighter(name1)
            fighter2 = Fighter(name2)
            break
        elif choice == "2":
            name1 = input("Enter player name: ")
            fighter1 = Fighter(name1)
            fighter2 = RobotFighter("Robot")
            break
        else:
            print("Invalid choice")
        
    game = GameManager(fighter1, fighter2)
    game.start_game()

main()
print("\nGame Finished\n")