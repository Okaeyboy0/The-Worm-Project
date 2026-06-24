import random as r
class Worm:
    def __init__(self, name, energy, age, position, alive = True):
        self.name = name
        self.energy = energy
        self.age = age
        self.position = position
        self.alive = alive
    
    def move(self, ):
        self.position += 1
        self.energy -= 20
        print(f"worm has moved {self.position} positions while energy has decreased by 20 leaving {self.energy} left")

    def eat(self, food_amount):
        
        self.energy += food_amount
        print(f"worm has eaten {food_amount} therefore having {self.energy} energy left")


    def sleep(self):
        self.energy += 5
        print(f"sleep added 5 energy, so energy is now {self.energy}")

    def age_up(self):
        self.age += 1
        print(f"worm is now {self.age} days old")
    
    def alive_TRACK(self):
        if self.energy <= 0:
            self.alive = False
            print(f"{self.name} energy has reached 0 therefore worm has died")
            

          

 
      


worm0 = Worm("Alpha0", 75, 0, 0)
worm1 = Worm ("Alpha01", 75, 0, 0)
worm2 = Worm("Alpha02", 75, 0, 0)

worms = [worm0, worm1, worm2]
for day in range(1, 11):
    print(f"DAY {day}")
    

    for worm in worms:
        if worm.alive == True:
        
        
            action = r.randint(1, 3)

            if action == 1:
                worm.move()
            elif action == 2:
                worm.eat(r.randint(0, 5))
            elif action == 3:
                worm.sleep()
            worm.age_up()
            worm.alive_TRACK()
            
        else:
            print(f"{worm.name} has died")
            
print("===== FINAL RESULTS =====")

for worm in worms:
    print(f"Name: {worm.name}")
    print(f"Energy: {worm.energy}")
    print(f"Age: {worm.age}")
    print(f"Position: {worm.position}")
    print(f"Alive: {worm.alive}")
    print()