input = [5,2,1,3,4]

"""
O(n * log2(n))

"""
for x in range(len(input) - 1, 0, -1):

.... fordi vi mutater input, vi skal "recurse" i  vores upper / lower...

    target = input[x]

    upper = []
    same = []
    lower = []

    for y in range(x):
        if input[y] < target:
            lower.append(input[y])
        elif input[y] > target:
            upper.append(input[y])
        else:
            same.append(input[y])

    input = lower + same + [target] + upper

    print(input, same, lower)
    
print(input)