# Sample student marks list
marks = [85, 90, 78, 92, 88]

# 1. Using the built-in function max() to find the highest mark[cite: 96]
highest_mark = max(marks)

# 2. Creating a user-defined function calculate_average(marks) to calculate the average[cite: 96]
def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)

average_mark = calculate_average(marks)

# Displaying the results
print(f"Marks List: {marks}")
print(f"Highest Mark (Built-in max()): {highest_mark}")[cite: 96]
print(f"Average Mark (User-defined calculate_average()): {average_mark:.2f}")[cite: 96]