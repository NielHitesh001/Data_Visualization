product_1_info = (101, "Laptop", "Electronics")
product_2_info = (102, "Mouse", "Electronics")
product_3_info = (103, "Notebook", "Stationery")

price_laptop = 800.00
price_mouse = 25.50
price_notebook = 4.00

qty_laptop = 1
qty_mouse = 2
qty_notebook = 5

in_stock_items = {"Laptop", "Mouse", "Notebook", "Keyboard"}
categories_available = {"Electronics", "Stationery", "Groceries"}

laptop_available = product_1_info[1] in in_stock_items
mouse_available = product_2_info[1] in in_stock_items

cart = [product_1_info[1], product_2_info[1], product_3_info[1]]

subtotal_laptop = price_laptop * qty_laptop
subtotal_mouse = price_mouse * qty_mouse
subtotal_notebook = price_notebook * qty_notebook

total_bill = subtotal_laptop + subtotal_mouse + subtotal_notebook
total_items = qty_laptop + qty_mouse + qty_notebook

is_premium_member = False
qualifies_for_discount = (total_bill > 500 and total_items >= 3) or is_premium_member

discount_amount = 0.0
if qualifies_for_discount:
    discount_amount = total_bill * 0.10

final_bill = total_bill - discount_amount

print("--- RETAIL STORE RECEIPT ---")
print("Items in Cart (List):", cart)
print("Subtotal: $", round(total_bill, 2))
print("Discount Applied: $", round(discount_amount, 2))
print("Final Total: $", round(final_bill, 2))
print("Discount Eligibility Status (Boolean):", qualifies_for_discount)
print("\n--- INVENTORY INFO ---")
print("Available Categories (Set):", categories_available)