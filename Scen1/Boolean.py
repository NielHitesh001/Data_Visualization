price = float(input("Enter unit price: "))
quantity = int(input("Enter quantity: "))

total_bill = price * quantity

is_premium_input = input("Is the customer a premium member? (yes/no): ").strip().lower()
is_premium = is_premium_input == "yes"

eligible_for_discount = (total_bill > 10000) and is_premium

print("\n--- Bill Details ---")
print("Total Bill Amount: ₹", total_bill)
print("Eligible for Discount:", eligible_for_discount)

if eligible_for_discount:
    discount = total_bill * 0.10
    final_bill = total_bill - discount
    print("Discount Applied (10%): ₹", discount)
    print("Final Payable Amount: ₹", final_bill)
else:
    print("Final Payable Amount: ₹", total_bill)