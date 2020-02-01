from functools import reduce
num = [2, 3, 4, 5, 6, 7, 8, 9]
even = list(filter(lambda n: n % 2 == 0, num))
print("even no is: ", even)
odd = list(filter(lambda n: n % 2 != 0, num))
print("odd no. is: ", odd)
double = list(map(lambda n: n*2, even))
print("double of even no is: ", double)
sum = reduce(lambda a, b: a + b, double)

print(sum)
