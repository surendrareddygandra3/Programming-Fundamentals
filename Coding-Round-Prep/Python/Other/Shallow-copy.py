import copy

original = [[1,2],[3,4]]

copied = copy.copy(original)

copied[0][0] = 100

print(original)

print(copied)