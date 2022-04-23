class Person:
  def __init__(self, fn, ln):
    self.firstname = fn
    self.lastname = ln

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Ashly", "Ochwada")
x.printname()