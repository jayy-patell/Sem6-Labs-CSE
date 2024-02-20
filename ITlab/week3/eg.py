list = [1,2,4,3]
print(list[::-1])

word = "my name is"
print(word[::-2])

# # The start index is included, the end index is not # (It's a 
# # closed/open range for you mathy types.) \
# li[1:3] # Return list from index 1 to 3 => [2, 4]
# li[2:] # Return list starting from index 2 => [4, 3] 
# li[:3] # Return list from beginning until index 3 => [1, 2, 4] 
# li[::2] # Return list selecting every second entry => [1, 4] 
# li[::-1] # Return list in reverse order

# Use any combination of these to make advanced slices
# li[start:end:step]