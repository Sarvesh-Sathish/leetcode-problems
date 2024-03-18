import os

dirStr = 'problems-solved'
dir = os.listdir(dirStr)

# Number of files in directory
numFiles = 0
# Dictionary of problems with fileName as a key and extension as it's respective value
problems = {}
# Number of java files
numJavaFiles = 0
# Number of python files
numPythonFiles = 0




for path in dir:
    if os.path.isfile(os.path.join(dirStr, path)):
        # print('fileName: ', path) # path is the filename
        problemName = path.split('.')[0]
        ext = path.split('.')[1]
        if ext == 'py' or ext == 'java' or ext == 'c' or ext == 'cpp' or ext == 'js':
            if problemName not in problems:
                problems[problemName] = ext
                numFiles += 1
 
# Display Results    
print('You have solved ', numFiles, ' problems.')
for problemName, ext in problems.items():
    if ext == 'py':
        numPythonFiles += 1
    elif ext == 'java':
        numJavaFiles += 1
    print('\t- ', problemName, ' (', ext, ')')

print('You have solved ', numPythonFiles, ' problems in Python.')
print('You have solved ', numJavaFiles, ' problems in Java.')
