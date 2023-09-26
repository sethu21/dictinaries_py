print("lesson_8")
print("ex_06")
students = {
 "student1": {
 "name": "Mike",
 "marks": {
 "physics": 70,
 "history": 80
 }
 },
 "student2": {
 "name": "Ana",
 "marks": {
 "physics": 65,
 "history": 90
 }
 },
 "student3": {
 "name": "Bob",
 "marks": {
 "physics": 90,
 "history": 85,
 "mathematics": 88
 }
 },
 "student4": {
 "name": "Alex",
 "marks": {
 "physics": 75,
 "mathematics": 85
 }
 }
}

  
print(students["student1"]['marks']['history'])
print(students["student2"]['marks']['history'])
print(students["student3"]['marks']['history'])
if students.get("history") is not None:
  print(history)
else:
  print("0")
  
  
