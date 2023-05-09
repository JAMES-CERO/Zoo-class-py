class Person:
  def __init__(self,in_name,in_age):
    self.name = in_name
    self.age = in_age
      
  def get_name(self):
    return self.name
  
class Customer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.has_ticket = False
        self.in_Zoo = False

    def buy_ticket(self):
      if self.age < 18:
        print('Welcome younghood')
      else:
        print('Welcome to the zoo, take care of the kids an animals')
        self.has_ticket == True

    def enter_zoo(self, zoo):
      if self.has_ticket:
           Zoo.add_customer(self.name)
           self.has_ticket = False
           self.in_Zoo = True
      else: 
          print('You need to purchase a ticket ')
          
    def exit_zoo(self):
      if self.in_Zoo == True:
          self.in_Zoo = False
          Zoo.remove_customer(self.name)
      else: print('You are not inside of the Zoo')
    
    

class Zoo:
  def __init__(self,name="Local Zoo"):
    self.name = name
    self.animals = []
    self.customers = []

  def add_animal(self, animal):
    self.animals.append(animal)
    print(f"{self.name} has a(n) {animal}")
  
  def add_animals(self, animals):
    self.animals.extend(animals)
    print(f"{self.name} has many animals")
  
  def add_customer(self, name):
    self.customers.append(name)
    print(f"{name} has entered {self.name}")

  def remove_customer(self, name):
    self.customers.remove(name)
    print(f"{name} has left {self.name}")
  
  def visit_animals(self):
    for a in self.animals:
      print(f"visiting {a.get_name()}")
      a.make_noise()
      a.eat_food()

class Animal:
  def __init__(self,name):
    self.name = name
  def get_name(self):
    return self.name
  

class Fish(Animal):
  def __init__(self, name):
      super().__init__(name)

  def make_noise(self):
      print(f'{self.name} doesnt make sound')

  def eat_food(self):
      print('Giving seafood to the fishy')

class Bird(Animal):
  def __init__(self, name):
      super().__init__(name)

  def make_noise(self):
      print(f'{self.name} tweeeet tweeet')

  def eat_food(self):
      print(f'Giving seeds to {self.name}')  

class Chimp(Animal):
  def __init__(self, name):
      super().__init__(name)

  def make_noise(self):
      print(f'{self.name} uhhhaa uhaaa')

  def eat_food(self):
      print(f'Giving fruits to {self.name}')  

nycZoo = Zoo("NYC Zoo")

salmon = Fish("salmon")
robin = Bird("robin")
bonobo = Chimp("bonobo")
nycZoo.add_animals([salmon, robin, bonobo])

alice = Customer("Alice",25)
bob = Customer("Bob",20)
charlie = Customer("Charlie",10)
dave = Customer("Dave",30)
for c in [alice, bob, charlie, dave]:
  c.buy_ticket()
  c.enter_zoo(nycZoo)
nycZoo.visit_animals()
for c in [alice, bob, charlie, dave]:
  c.exit_zoo(nycZoo)