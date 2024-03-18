import os

dirStr = 'problems-solved'
dir = os.listdir(dirStr)

numFiles = 0
problems = []

for path in dir:
    if os.path.isfile(os.path.join(dirStr, path)):
        # print('fileName: ', path) # path is the filename
        problemName = path.split('.')[0]
        problems.append(problemName)
        numFiles += 1
        
print('You have solved ', numFiles, ' problems.')
for problem in problems:
    print('\t- ', problem)
