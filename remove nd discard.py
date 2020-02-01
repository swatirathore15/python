Months = set(["January", "February", "March", "April", "May", "June"])
print("\nprinting the original set ... ")  
print(Months)  
print("\nRemoving items through discard() method...")
Months.discard("aug")
print("\nprinting the modified set...")  
print(Months)  
print("\nRemoving items through remove() method...")
Months.remove("aug")
print("\nPrinting the modified set...")  
print(Months)

#remove will give error if element is not present ,but discard not.