import json

def makeOperationOnList(numbers, pathOfFile):

    output = map(lambda x:x**2, numbers)
    dictOutput = dict(zip(numbers,output))

    with open(pathOfFile, 'w') as file:
        json.dump(dictOutput, file)
        print(f"the dictionary created successfully")

makeOperationOnList([1,2,3,4,5], "./result.txt")
