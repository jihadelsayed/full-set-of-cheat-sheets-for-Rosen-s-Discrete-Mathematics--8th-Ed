def bijective_func(x):
    return x * 2 + 1

# If domain = [0, 1, 2], codomain = [1, 3, 5]
inputs = [0, 1, 2]
outputs = [bijective_func(x) for x in inputs]
print(outputs)  # [1, 3, 5]
