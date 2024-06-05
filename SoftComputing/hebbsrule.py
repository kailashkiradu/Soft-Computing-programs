def hebb_rule(w, x, lr):
    w_updated = []
    for i in range(len(w)):
        row_updated = []
        for j in range(len(w[0])):
            new_weight = w[i][j] + lr * x[i] * x[j]
            row_updated.append(new_weight)
        w_updated.append(row_updated)
    return w_updated

w = [[0, 0], [0, 0]]
x = [1, 0.5]
lr = 0.1
w_updated = hebb_rule(w, x, lr)

print("Original weight matrix:")
for row in w:
    print(row)

print("\nUpdated weight matrix:")
for row in w_updated:
    print(row)
