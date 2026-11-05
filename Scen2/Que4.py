# A billing system allowing entry of maximum three order quantities
# Using a while loop to display the numbers from 1 to 3 representing order entries processed

entry_count = 1
max_orders = 3

print("--- Processing Order Entries ---")
while entry_count <= max_orders:
    print(f"Order entry processed: {entry_count}")
    entry_count += 1