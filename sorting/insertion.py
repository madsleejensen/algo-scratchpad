input = [3,2,4,1,5]

"""
O(n^2)

1: [3,2,4,1,5]
2: [2,3,4,1,5]
3: [2,3,4,1,5]
4: [1,2,3,4,5]
"""
for x in range(len(input)):
    for y in range(x, 0, -1):
        # keep moving the smallest number back till an item with lower value is found.
        if input[y - 1] > input[y]:
            # swap
            temp = input[y - 1]
            input[y - 1] = input[y]
            input[y] = temp
        else: 
            break

print(input)