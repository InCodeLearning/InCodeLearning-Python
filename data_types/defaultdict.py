# usage of defaultdict and & in sets

from collections import defaultdict

a = [[1, 2], [3, 4], [3, 6]]
b = [[1, 2], [2, 3], [3, 5]]

dict_a = defaultdict(list)
dict_b = defaultdict(list)

print(dict_a)
print(dict_b)

for item in a:
    dict_a[item[0]].append(item)

for item in b:
    dict_b[item[0]].append(item)

# get common first element in each list
common_keys = set(dict_a.keys()) & set(dict_b.keys())

for key in common_keys:
    print("key: {0}, dict a: {1}, dict b: {2} \n".
          format(key, dict_a[key], dict_b[key]))