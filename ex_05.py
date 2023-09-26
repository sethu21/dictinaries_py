print("lesson_8")
print("ex_05")

d1 = {'a': 4, 'b': 5, 'd': 8}
d2 = {'a': 1, 'd': 10, 'e': 9}
merged_d = {key:d1.get(key,0)+d2.get(key,0) for key in set(d2) | set(d1)}
print(f'merged_d = {merged_d}')
