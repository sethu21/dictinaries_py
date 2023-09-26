import runpy

print("Lesson 8")
exercise = 0

while exercise != -1:
  exercise = int(input("input number of exercise ==> "))
  if exercise == 1:
    runpy.run_module("ex_01")
  elif exercise == 2:
    runpy.run_module("ex_02")
  elif exercise == 3:
    runpy.run_module("ex_03")
  elif exercise == 4:
    runpy.run_module("ex_04")
  elif exercise == 5:
    runpy.run_module("ex_05") 
  elif exercise == 6:
    runpy.run_module("ex_06") 
  elif exercise == 7:
    runpy.run_module("ex_07")
  elif exercise == 8:
    runpy.run_module("ex_08")
  elif exercise == 9:
    runpy.run_module("ex_09")