item1 = float(input("Enter price of Item 1: "))
item2 = float(input("Enter price of Item 2: "))
item3 = float(input("Enter price of Item 3: "))

total = item1 + item2 + item3

discount = total * 10 / 100

final_bill = total - discount

print("Total Bill =", total)
print("Discount (10%) =", discount)
print("Bill After Discount =", final_bill)