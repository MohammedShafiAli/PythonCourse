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

    def move_forward(self, distance):
        if distance == 1:
            print("Invalid move. Distance must be between 1-10.")
            return False, distance
        
        print(self.__name, "moved forward.")
        distance -= 1
        return True, distance            

    def move_backward(self, distance):  
        if distance == 10:
            print("Invalid move. Distance must be between 1-10.")
            return False, distance
        
        print(self.__name, "moved backwards.")
        distance += 1
        return True, distance            

    def make_snowball(self):
        if self.__ammo == 5:
            print("Invalid move. Maximum of 5 snowballs allowed.")
            return False
        
        print(self.__name, "made a snowball.")
        self.__ammo += 1
        return True            
        
    def throw_snowball(self, distance, other_fighter):
        if self.__ammo == 0:
            print("Invalid move. No snowballs available.")
            return False
        
        if self.__is_hit(distance):
            print("That's a hit!")
            other_fighter.deplete_health()
        else:
            print("That's a miss!")

        self.__ammo -= 1
        return True

    def deplete_health(self):
        self.__health -= 1

    def __is_hit(self, distance):
         hit_chance = 11 - distance #chance of being hit out of 10
         num = random.randint(1,10) 
         if num in range(1, hit_chance + 1): # +1 because range() is not inclusive 
             return True
         else:
             return False
         
    def __str__(self):
        return "Fighter: " + self.__name + ", Health:" + str(self.__health) + ", Ammo:" + str(self.__ammo)

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
            self.__display_menu()
            
            choice = input("Choice: ")
            if choice == "1":
                valid_move, self.distance = self.active_fighter.move_forward(self.distance)
            elif choice == "2":
                valid_move, self.distance = self.active_fighter.move_backward(self.distance)
            elif choice == "3":
                valid_move = self.active_fighter.make_snowball()
            elif choice == "4":
                valid_move = self.active_fighter.throw_snowball(self.distance, self.other_fighter)
            elif choice == "5":
                print("Exiting game")
                break

            if not valid_move:
                    continue 
    
            self.__display_summary()
            
            #check for winner
            if self.other_fighter.health == 0:
                print( self.active_fighter.name, "WINS!!!")
                break

            self.__swith_turn()

    def __display_menu(self):
        print("""
                1. Move forward
                2. Move backward
                3. Make snowball
                4. Throw snowball
                5. Exit game
            """)
        
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
    name1 = input("Enter player 1 name: ")
    name2 = input("Enter player 2 name: ")

    fighter1 = Fighter(name1)
    fighter2 = Fighter(name2)
    game = GameManager(fighter1, fighter2)
    game.start_game()

main()
print("Game Finished")