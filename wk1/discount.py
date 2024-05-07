import random


day = random.choice(["MO", "TU", "WE", "TH", "FR", "SA", "SU"])
subtotal = float(input("Please enter the subtotal: "))

#sta = sales tax amount
sta = subtotal * 0.06

total = subtotal + sta

if day == "TU" or "WE":
     if subtotal > 50:
        discount = subtotal / 0.1
        new_subtotal = subtotal + discount

print(f"Sales tax amount: {sta}")
print(f"Total: {total}")
    
