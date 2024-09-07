'''A subset of.'''

ls_1 = [1, 2, 3, 4, 5]
ls_2 = [2, 3, 4]

is_subset = True
for i in ls_1:
    if i not in ls_2:
        is_subset = False

print(is_subset)

# Либо через множество
set_1 = set(ls_1)
set_2 = set(ls_2)
is_sub = set_1.issubset(set_2)
print(is_sub)