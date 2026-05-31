# Step 1: Create a dictionary
student_marks = {
    "Ansh": 85,
    "Dipanshu": 92,
    "Aryan": 78,
    "Sally": 90
}

# Step 2: Input the key to search for
search_name = input("Enter the student's name to find their marks: ")

# Step 3: Search for the key
if search_name in student_marks:
    print(f"{search_name}'s marks: {student_marks[search_name]}")
else:
    print(f"{search_name} is not found in the dictionary.")
