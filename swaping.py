a = 5
b = 6
#temp = a  # swap the twp value without asign third variable
# a = b
#b = temp
#a = a + b #THIS MATHOED WASTE THE BIT, WE CAN ALSO USE (XOR) OPRATOR
#b = a - b
#a = a - b

a = a ^ b
b = a ^ b
a = a ^ b
print(a)
print(b)