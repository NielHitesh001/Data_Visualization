# Scenario-Based Program: Online Shopping Company Order & Discount Processing

def online_shopping_system():
    print("=== Welcome to the Online Shopping System ===")
    
    # 1. Iterate through a list of product prices using a for loop
    product_prices = [299.0, 1499.0, 499.0, 5499.0, 199.0]
    print("\n--- Current Product Catalog Prices ---")
    for i, price in enumerate(product_prices, start=1):
        print(f"Product {i}: Rs. {price:.2f}")
        
    # 2. Continue accepting orders until the customer chooses to stop using a while loop
    while True:
        print("\n----------------------------------------")
        action = input("Do you want to calculate a discount / place an order? (yes/no): ").strip().lower()
        
        if action == 'no':
            print("Thank you for visiting! Exiting the system.")
            break
        elif action != 'yes':
            print("Invalid choice. Please type 'yes' or 'no'.")
            continue
            
        try:
            purchase_amount = float(input("Enter total purchase amount: Rs. "))
        except ValueError:
            print("Error: Please enter a valid numeric amount.")
            continue
            
        # 3. Categorize orders and determine discounts using if, elif, else
        if purchase_amount >= 5000:
            category = "Premium Order"
            discount_percentage = 20
        elif purchase_amount >= 2500:
            category = "Standard Order"
            discount_percentage = 10
        elif purchase_amount > 0:
            category = "Basic Order"
            discount_percentage = 5
        else:
            print("Purchase amount must be greater than zero.")
            continue
            
        # Calculate final bill
        discount_amount = (purchase_amount * discount_percentage) / 100
        final_payable = purchase_amount - discount_amount
        
        # Display summary
        print(f"\n--- Order Summary ---")
        print(f"Order Category   : {category}")
        print(f"Original Amount  : Rs. {purchase_amount:.2f}")
        print(f"Discount Applied : {discount_percentage}% (Rs. {discount_amount:.2f})")
        print(f"Final Payable    : Rs. {final_payable:.2f}")

if __name__ == "__main__":
    online_shopping_system()