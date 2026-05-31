# Step 1: Define the array
arr = [10, 25, 7, 88, 32, 5]

# Step 2: Find the maximum element
max_element = arr[0]
for num in arr:
    if num > max_element:
        max_element = num

# Step 3: Reverse the array
reversed_array = arr[::-1]

# Step 4: Print the results
print("Original Array:", arr)
print("Maximum Element:", max_element)
print("Reversed Array:", reversed_array)
