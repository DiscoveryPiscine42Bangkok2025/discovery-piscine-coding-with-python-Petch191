original = [2, 8, 9, 48, 8, 22, -12, 2]
new = []
for i in range(len(original)):
    if original[i] not in [2,-12,2]:
        new.append(original[i]+2)
print(original)
print(new)