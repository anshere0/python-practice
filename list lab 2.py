# Input: Define a list
my_list = [3, 15, 8, 23, 42, 4]

# Step 1: Find the maximum element
max_element = my_list[0]
for item in my_list:
    if item > max_element:
        max_element = item

# Step 2: Reverse the list
reversed_list = my_list[::-1]

# Step 3: Display the result
print("Original List:", my_list)
print("Maximum Element in the List:", max_element)
print("Reversed List:", reversed_list)
    