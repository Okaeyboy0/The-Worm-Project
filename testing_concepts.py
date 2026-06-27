import random as r
class Organism:
    def __init__(self, name, energy, age, position, alive = True):
        self.name = name
        self.energy = energy
        self.age = age
        self.position = position
        self.alive = alive
    
    def move(self, ):
        self.position += 1
        self.energy -= 20
        print(f"{self.name} has moved {self.position} positions while energy has decreased by 20 leaving {self.energy} left")

    def eat(self, food_amount):
        
        self.energy += food_amount
        print(f"{self.name} has eaten {food_amount} therefore having {self.energy} energy left")

    def sleep(self):
        self.energy += 5
        print(f"sleep added 5 energy, so energy is now {self.energy}")

    def age_up(self):
        self.age += 1
        print(f"{self.name} is now {self.age} days old")
    
    def alive_TRACK(self):
        if self.energy <= 0:
            self.alive = False
            print(f"{self.name} energy has reached 0 therefore worm has died")

class worm(Organism):
    
    def move(self, ):
        self.position += 2
        self.energy -= 20
        print(f"{self.name} has slithered {self.position} positions while energy has decreased by 20 leaving {self.energy} left")

class Predator(Organism):
    
    def hunt(self, worms):
        target = r.choice(worms)

        if target.alive == False:
            print(f"{target.name} is already dead")
            return

        success = r.randint(1, 100)
        if success <= 50:
            damage = r.randint(10, 30)
            target.energy -= damage
            self.energy += 10
            print(f"{self.name} attacked {target.name} for {damage} damage")

            if target.energy <= 0:
                target.alive = False
                print(f"{target.name} died")
        
        else:
            self.energy -= 10
            print(f"{target.name} escaped. {self.name} lost 10 energy")
                
            
            
            
            
    def move(self, ):
        self.position += 4
        self.energy -= 20
        print(f"{self.name} Sprinted {self.position} positions while energy has decreased by 20 leaving {self.energy} left")


worm0 = worm("Worm0", 75, 0, 0)
worm1 = worm("Worm1", 75, 0, 0)
Predator1 = Predator("Predator0", 75, 0, 0)



organisms = [worm0, worm1, Predator1]
for day in range(1, 11):
    print(f"DAY {day}")
    
    for organism in organisms:
        if organism.alive:
            action = r.randint(1, 4)

            if action == 1:
                organism.move()
            elif action == 2:
                organism.eat(r.randint(0, 5))
            elif action == 3:
                organism.sleep()
            elif action == 4:
                if isinstance(organism, Predator):
                    organism.hunt([worm0, worm1])

            organism.age_up()
            organism.alive_TRACK()
            
            
        else:
                    print(f"{organism.name} is dead")

print("===== FINAL RESULTS =====")

for organism in organisms:
    print(f"Name: {organism.name}")
    print(f"Energy: {organism.energy}")
    print(f"Age: {organism.age}")
    print(f"Position: {organism.position}")
    print(f"Alive: {organism.alive}")
    print()
