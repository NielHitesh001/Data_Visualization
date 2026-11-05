# Input the order amount from the user
order_amount = float(input("Enter the order amount: ₹"))

# Check if the order amount is ₹1,000 or more
if order_amount >= 1000:
    delivery_charge = 0
    print("Free delivery applied.")
else:
    # Otherwise, charge ₹50 for delivery
    delivery_charge = 50
    print("Delivery charge: ₹50")

# Calculate and display the final total amount
total_amount = order_amount + delivery_charge
print(f"Total amount to pay: ₹{total_amount}")