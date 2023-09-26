print("lesson_8")
print("ex_03")

sample_dict = {
 "name": "Kelly",
 "age": 25,
 "salary": 8000,
 "city": "New york"}


key = ["name","salary"]


dict1 = dict((k , sample_dict[k])for k in key if k in sample_dict)
print(dict1)
