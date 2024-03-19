family = {'sarvesh': 19, 'sathish': 50, 'tarunesh': 15, 'eswari': 45}

# Get keys in a dictionary 
keys = family.keys() # returns a list of keys
print('keys:', keys) #! O(N) 

# Get Values in a dictionary
values = family.values() # returns a list of values
print('values: ', values) #! O(N)

# Get item in a dictionary
myAge = family.get('sarvesh')
print('My Age: ', myAge) #! O(N)

# Set item in a dictionary

