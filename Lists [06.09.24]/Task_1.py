'''Nested lists'''

nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = []
for i in nested_lists:
    for j in i:
        new_list.append(j)

print(new_list)