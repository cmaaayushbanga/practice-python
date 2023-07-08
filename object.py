# class Dog(object):
#     def __init__(self, name, age,fred):
#         self.name = name
#         self.age = age
#         self.li = [1,2,3]
        
#     def speak(self):
#         print("hi i am", self.name, 'and i am',self.age, 'year old' )
    
#     def chane_age(self, age):
#         self.age = age
    
#     def add_weight(self, weight):
#         self.weight = weight


# fred = Dog('fred', 65)
# tim.chane_age(5)
# tim.add_weight(60)
# tim.speak()
# fred.speak()

# print(fred.weight)

class _private:
    def _init_(self, name):
        self.name = name

class Notprivate:
    def _init_(self, name):
        self.name = name
        self.priv = _private(name)
    
    def display(self):
        print("hello")
    def display(self):
        print("hi")
    
