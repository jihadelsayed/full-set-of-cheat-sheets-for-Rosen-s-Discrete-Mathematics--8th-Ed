def surjective_func(x):
    return x % 3

# Codomain: [0, 1, 2]
inputs = [0, 1, 2, 3, 4, 5]
outputs = [surjective_func(x) for x in inputs]
print(set(outputs))  # {0, 1, 2} — covers whole codomain
