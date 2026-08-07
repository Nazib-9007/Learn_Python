# Bill Split Calculator....
print("Bill Split Calculator")
bill_amount = float(input("Enter the bill amount: "))
tip_persentage = float(input("Enter the tip amount: "))
people_number = int(input("Enter the number of people: "))
tip_amount = (tip_persentage / 100) * bill_amount
total_amount = bill_amount + tip_amount
print(f"Total (including tip): ${total_amount}")
amount_perperson = total_amount / people_number
print(f"Each person pays: ${amount_perperson}")