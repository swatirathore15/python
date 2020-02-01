class Calculation1:
    def summation(self, a, b):
        return a+b

class Calculation2:
    def multiplication(self, a, b):
        return a*b


class Derived(Calculation1, Calculation2):
    def divide(self, a, b):
        return a/b
d = Derived()
print(issubclass(Derived, Calculation2))
print(issubclass(Calculation2, Calculation2))
