print("lesson_8")
print("ex_07")

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

d1 ={
 "physics": 70,
 "history": 80
 }
  
print(students["student1"]['name'])
for key,val in d1.items():
  print(key,val)

average1 = sum(d1.values())/len(d1)

print("average grade " + "%.2f" %average1 )
print("---------")
d2 ={
 "physics": 65,
 "history": 90
 }
print(students["student2"]['name'])
for key,val in d2.items():
  print(key,val)

average2 = sum(d2.values())/len(d2)

print("average grade " + "%.2f" %average2 )
print("----------")
d3 ={
 "physics": 90,
 "history": 85,
 "mathematics": 88
 }
print(students["student3"]['name'])
for key,val in d3.items():
  print(key,val)

average3 = sum(d3.values())/len(d3)

print("average grade " +"%.2f" %average3 )
print("----------")
d4 ={
 "physics": 75,
 "mathematics": 85
 }
print(students["student4"]['name'])
for key,val in d4.items():
  print(key,val)

average4 = sum(d4.values())/len(d4)

print("average grade " +  "%.2f" %average4 )
print("----------")
print("pogram_2")
dict ={'physics': [300, 4], 'history': [255, 3], 'mathematics': [173, 2]}
out =  {k : ("%.2f" %(i/j)) for k,(i,j) in dict.items()}

for key,val in out.items():
  print(key,val)
