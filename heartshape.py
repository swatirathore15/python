num = int(input("enter a name: "))
msg = input("enter any message:")
l = len(msg)
n = num//2
for i in range(n):
    print(" "*(n-i-1) + "* "*(i+1), end="")

    if num % 2 == 0:
        for j in range(2*(n-i-1)):
            print(" ", end="")
    else:
        for j in range(2*(n-i-1)+1):
            print(" ", end="")
    for j in range(i+1):
        print("* ", end="")

    print()
print("*"*((num-1)//2) + " ".join(msg) + "*"*((num-1)//2))
for i in range(num, 0, -1):
    print(" "*(num-i) + "* " * (i))
