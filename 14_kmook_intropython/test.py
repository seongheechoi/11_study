import numpy as np

class Cal1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

class Cal2:
    def __init__(self, c, d):
        self.c = c
        self.d = d
    def add(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

aa = Cal(10,10)
print(aa.add())
print(aa.a)


