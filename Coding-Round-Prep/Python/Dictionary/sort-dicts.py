# Input dictionary
d = {
    'a':3,
    'b':1,
    'c':2
}

# Sort by value
sorted_dict = dict(
    sorted(d.items(), key=lambda item: item[1])
)

# Print result
print(sorted_dict)


# Sort by key
d = {
    'c':3,
    'a':1,
    'b':2
}

sorted_dict = dict(sorted(d.items()))

print(sorted_dict)