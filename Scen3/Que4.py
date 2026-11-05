# Assuming the user-defined function is already defined as:
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function call for the second student
student2_marks = [75, 80, 85]
average_result = calculate_average(student2_marks)

print(f"Second Student Average: {average_result:.2f}")