amount = float(input("Insert the cash amount."))
VAT = float(input("Insert VAT.")) / 100

total = amount + amount * VAT

print("The sum is:", total) 