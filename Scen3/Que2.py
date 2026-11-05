# User-defined function to calculate total and average marks[cite: 93]
def calculate_total_and_average(marks):
    total = sum(marks)
    count = len(marks)
    
    if count > 0:
        average = total / count
    else:
        average = 0.0
        
    return total, average

# Example usage:
student_marks = [85, 90, 78, 92, 88]

# Calling the user-defined function
total_marks, average_marks = calculate_total_and_average(student_marks)

# Displaying the results
print(f"Student Marks: {student_marks}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")