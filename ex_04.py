print("lesson_8")
print("ex_04")

sample_dict = {
 "name": "Kelly",
 "age": 25,
 "salary": 8000,
 "city": "New york"}


 
# initializing Remove keys
remove_keys = ['name', 'salary']
 
# printing original dictionary
print(sample_dict)
 
# Remove multiple keys from dictionary
for key in remove_keys:
  if key in sample_dict:
    del sample_dict[key]
 
# printing result
print( str(sample_dict))
