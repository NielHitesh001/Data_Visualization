# Store the prices of five products in a list
product_prices = [250.0, 450.50, 100.0, 1250.25, 75.0]

total_price = 0

# Use a for loop to calculate the total price of all products
for price in product_prices:
    total_price += price

# Display the total price
print(f"Product Prices: {product_prices}")
print(f"Total Price of all products: ₹{total_price:.2f}")