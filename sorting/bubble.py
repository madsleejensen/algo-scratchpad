input = [3,2,5,1,4]

"""
O(n^2)

1: [3,2,5,1,4]
2: [2,3,5,1,4]
3: [2,3,1,5,4]
4: [2,3,1,4,5]
5: [2,1,3,4,5]
6: [1,2,3,4,5]
"""
for x in range(len(input)):
    for y in range(1, len(input)):
        if input[y - 1] > input[y]:
            temp = input[y]
            input[y] = input[y - 1]
            input[y-1] = temp