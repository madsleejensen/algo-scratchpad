input = [4,1,2,5,3]
output = []

size = len(input)

"""
O(n^2)

1: 
    input: [4,1,2,5,3]
    output: []

2: 
    input: [4,2,5,3]
    output: [1]

3: 
    input: [4,5,3]
    output: [1,2]

4: 
    input: [4,5]
    output: [1,2,3]


5: 
    input: [5]
    output: [1,2,3,4]

6: 
    input: []
    output: [1,2,3,4,5]
"""
for x in range(size):
    minimum_index = 0
    for y in range(1, len(input)):
        if input[y] < input[minimum_index]: 
            minimum_index = y
    
    output.append(input[minimum_index])

    del input[minimum_index]

print(output)