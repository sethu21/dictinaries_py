print("lesson_8")
print("ex_08")
foods = {
 "Milk": 110,
 "Tea": 50,
 "Candy": 90,
 "Juice": 150,
 "Coffee": 70
 }

print("welcome to the vending machine")

for k,v in foods.items():
  print(f'{k:8}{v:8}')

print()

total = input("Enter the foods you want to get==>")

if total in foods:
  
  print(f'Great, {total} cost you {((foods[total])/100):.2f}')
else:
  print("Invalid Input")
    
def vend():
    
    inserted = 0
    while inserted < foods[total]:
        inserted += int(input("Enter a coins(5,10,20,50): "))
        print(f'you paid {inserted} still pay {foods[total] - inserted}')
    if inserted == foods[total]:
        print("you paid")

vend()