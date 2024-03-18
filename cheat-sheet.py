# This is a list of fruits
fruits = ['orange', 'apple', 'banana', 'kiwi', 'grape']

# Copy Operation 
fruitsCopy = fruits.copy()
print('fruitsCopy: ',fruitsCopy) #! O(N) because it has to iterate through a loop and copy each element (which takes n times)

# Append Operation
fruits.append('mango') # Added a mango to the end of the list
print('fruitsAppended: ',fruits) #! O(1)* because we are added at end of array but doubling the size of the backing array if it is full

# Pop Operation
fruits.pop() # Removed the last element from the list
print('fruitsPopped: ',fruits) #! O(1) because we are simply setting the internal size of the array to be one less than it was

# Pop Intermediate Operation
fruits.pop(3) # Removed the element at whatever index is given as a parameter
print('fruitsPopped: ', fruits) #! O(N) because of the shifting of elements to fill up the gap

# Insert Operation
fruits.insert(0, 'passionfruit') # Insert a passionfruit into the start of the array
print('fruitsInserted: ', fruits) #! O(N) because of the shifting of elements to make up space

# Get Operation
selectedFruit = fruits[0] # Pretty intuitive 
print('fruitsGet: ', selectedFruit) #! O(1) because it is simply returning the element at the given index

