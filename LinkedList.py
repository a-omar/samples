class Empty:
    def __init__(self):
        self.IsEmpty = True

    def Length(self):
        return 0

    def Filter(self,p):
        return Empty()

class Node:
    def __init__(self, value, tail):
        self.IsEmpty = False
        self.Value = value
        self.Tail = tail

    def Length(self):
        return 1 + self.Tail.Length()

    def Filter(self,p):
        if p(self.Value):
            return Node(self.Value, self.Tail.Filter(p))
        else:
            return self.Tail.Filter(p)


class Employee:
    def __init__(self,name, age, salary):
        self.Name = name
        self.Age = age
        self.Salary = salary

class Product:
    def __init__(self,name, num):
        self.Name = name
        self.Num = num


e1 = Employee("Tim Jakobson",23,2000);
e2 = Employee("Bob Jakobson",24,2300);
e3 = Employee("Tom Jakobson",25,2400);
e4 = Employee("Sjors Jakobson",26,2500);
e5 = Employee("Jack Jakobson",40,3600);

l = Node(e1, Node(e2,Node(e3,Node(e4,Node(e5,Empty())))))
print(l.Length())
fl1 = l.Filter(lambda x: x.Salary > 2300 )
fl2 = l.Filter(lambda x: x.Age > 26 )
fl3 = l.Filter(lambda x: x.Name == "Sjors Jakobson" )
print(fl3.Length())

p1 = Product("PS4", 4)
p2 = Product("XBOX", 10)
p3 = Product("Nintendo Switch", 30)

ll = Node(p1, Node(p2,Node(p3,Empty())))
fll = ll.Filter(lambda x: x.Num > 11 )
print(fll.Length())



