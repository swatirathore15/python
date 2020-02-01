import sys

print(sys.getrecursionlimit())

def greet():
    print("hello developer")
    greet()
