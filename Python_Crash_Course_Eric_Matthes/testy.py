requested_topping = 'marynata'

if requested_topping != 'coś':
	print("Proszę o coś!")
	
else:
	print("źle")

answer = 20

if answer != 42:
	print("Zła odpowiedź. Try again bicz")
	
else:
	print("To jest prawidłowa odpowiedź, gratuluję")

banned_users = ['tak','mam','na','imie','fajnie']
user = 'nic'

if user not in banned_users:
	print(user.title() + ",dawaj tą odpowiedź jeśli chcesz")
	

car = 'subaru'
print("Czy car == 'subaru'? Przewiduję wartość True.")
print(car == 'subaru')

print("\nCzy car == 'audi'? Przewiduję wartość False.")
print(car == 'audi')

food = 'marchewka'
print("Czy food == 'marchewka'? Przewiduję wartość True.")
print(food == 'marchewka')

print("\nCzy food == 'jabłko'? Przewiduję wartość False.")
print(food == 'jabłko')
