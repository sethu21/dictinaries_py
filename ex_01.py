print("lesson_8")
print("ex_01")
cities = [('London', 'UK'), 
          ('New York', 'US'), 
          ('Tokyo', 'Japan')]


dict_cities = dict(cities)
print(dict_cities)

cities_2 = ['Ventspils', 'Riga', 'Liepaja']



cities_3 = ['London', 'New York', 'Tokyo']
countries = ['UK', 'US', 'Japan']

dict_cities_3 = dict(zip(countries, cities_3))
print(dict_cities_3)
list1 = ['Ten', 'Twenty', 'Thirty']
list2 = [10, 20, 30]

dict_number = dict(zip(list1,list2))
print(dict_number)
dict_number1 = dict(zip(list2,list1))
print(dict_number1)
