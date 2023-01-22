class A():
    def primera(self):
        return "Clase A"

class B():
    def segunda(self):
        return "Clase B"

class C(A , B):
    pass

c = C()

print(c.primera())
print(c.segunda())