import numpy as np

def max_min_composition(rel1, rel2):
    rows_rel1, cols_rel1 = rel1.shape
    rows_rel2, cols_rel2 = rel2.shape

    if cols_rel1 != rows_rel2:
        raise ValueError("Number of columns in rel1 must match number of rows in rel2 for composition.")

    composed_relation = np.zeros((rows_rel1, cols_rel2))

    for i in range(rows_rel1):
        for j in range(cols_rel2):
            max_min = max(min(rel1[i, k], rel2[k, j]) for k in range(cols_rel1))
            composed_relation[i, j] = max_min

    return composed_relation

# User input for fuzzy relations A and B
rows_relA = int(input("Enter the number of rows for fuzzy relation A: "))
cols_relA = int(input("Enter the number of columns for fuzzy relation A: "))
rows_relB = int(input("Enter the number of rows for fuzzy relation B: "))
cols_relB = int(input("Enter the number of columns for fuzzy relation B: "))

print("\nEnter values for fuzzy relation A (separate values by spaces):")
relA_values = [float(val) for val in input().split()]
relA = np.array(relA_values).reshape(rows_relA, cols_relA)

print("\nEnter values for fuzzy relation B (separate values by spaces):")
relB_values = [float(val) for val in input().split()]
relB = np.array(relB_values).reshape(rows_relB, cols_relB)

# Perform Max-Min Composition
try:
    composition = max_min_composition(relA, relB)
    print("\nOutput:")
    print("Fuzzy relation C (result of Max-Min composition):")
    print(composition)
except ValueError as e:
    print("Error:", e)
