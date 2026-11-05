# Input the total purchase amount from the user
purchase_amount = float(input("Enter the total purchase amount: ₹"))

# Determine the discount percentage using if, elif, and else[cite: 90]
if purchase_amount >= 10000:
    discount_percentage = 20
elif purchase_amount >= 5000:
    discount_percentage = 10
elif purchase_amount >= 2000:
    discount_percentage = 5
else:
    discount_percentage = 0  # No discount for amounts below ₹2,000

# Calculate the discount amount and final bill
discount_amount = (purchase_amount * discount_percentage) / 100
final_bill = purchase_amount - discount_amount

# Display the results
print("\n--- Bill Summary ---")
print(f"Purchase Amount : ₹{purchase_amount:.2f}")
print(f"Discount Applied: {discount_percentage}% (₹{discount_amount:.2f})")
print(f"Final Bill Amount: ₹{final_bill:.2f}")