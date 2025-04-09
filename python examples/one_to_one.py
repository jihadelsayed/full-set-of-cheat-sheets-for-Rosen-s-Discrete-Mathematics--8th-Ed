def injective_func(x):
    return x + 3

# Test
inputs = [1, 2, 3]
outputs = [injective_func(x) for x in inputs]
print(outputs)  # [4, 5, 6] — all unique
