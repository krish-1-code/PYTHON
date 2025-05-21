item = input("WHAT ITEM WILL YOU BE BUYING: ")
num = int(input(f"HOW MANY {item} WILL YOU BE BUYING: "))
total = 5.99 * num
print(f"COST OF ONE {item} IS $5.99")
print(f"YOUR TOTAL BILL IS ${round(total,2)}")