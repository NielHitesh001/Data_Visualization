# 1. Variables and Data Types
product_name = "Laptop"
price = 50000.0
quantity = 2
stock_available = True

print("Product:", product_name)
print("Price:", price)
print("Quantity:", quantity)
print("Stock Available:", stock_available)

# 2. Arithmetic Operators
total_bill = price * quantity
print("Total Bill:", total_bill)

# 3. Comparison and Boolean Operators
discount_eligible = total_bill >= 50000 and quantity >= 2
print("Discount Eligible:", discount_eligible)

if discount_eligible:
    discount = total_bill * 0.10
else:
    discount = 0

final_bill = total_bill - discount
print("Discount:", discount)
print("Final Bill:", final_bill)

# 4. Lists: Product names
products = ["Laptop", "Mouse", "Keyboard"]
products.append("Monitor")
print("Products:", products)

# 5. Tuples: Product prices
prices = (50000, 800, 1500)
print("Product Prices:", prices)

# 6. Sets: Unique product categories
categories = {"Electronics", "Accessories", "Electronics"}
print("Unique Categories:", categories)