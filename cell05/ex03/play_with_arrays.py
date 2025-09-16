original = [2, 8, 9, 48, 8, 22, -12, 2]
new_duplicated = list(set(original))
new = []
for i in range(len(new_duplicated)):
    if new_duplicated[i] not in [2,-12]:
        new.append(new_duplicated[i]+2)
print(original)
print(set(new))