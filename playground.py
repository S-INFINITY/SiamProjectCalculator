import re

test = "2+2*2-2"

# in the case 2+2, length will be '2', '+', '2' = 3
# in the case 2+2+2, length will be '2', '+', '2', '+', '2' = 5
#in the case 2+2+22, length will be '2', '+', '2', '+', '22' = 5


def testingRE(string):
    output = re.split(f'(\D)', string)
    # if you assum the length of output is odd, you can do this:
    outputFirst = output[0]
    if float(outputFirst) > 0:
        outputFirst = ['+', outputFirst]
    else:
        outputFirst = ['-', outputFirst]
    outputPairs = []
    
    # start at position 1, and go to the end of the list, in steps of 2
    for i in range(1, len(output), 2):
        outputPairs.append((output[i], output[i+1]))
        
    finalOutput = outputFirst + outputPairs
    return finalOutput

print(testingRE(test))