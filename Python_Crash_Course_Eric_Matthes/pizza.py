#4.1
pizzas=['la_mafia','kolejorz','margarita']

for pizza in pizzas:
	print(pizza.title() + " jest moją ulubioną pizzą")

print("\nNaprawdę uwielbiam pizze!")

#4.2
animals=['kaczki','kury','gęsi']

for animal in animals:
	print(animal.title() + "lubią jeść")
	
print("\nUWIELBIAM JE XD")

#4.11
friend_pizzas = pizzas[:]
friend_pizzas.append('spoko')
pizzas.append('chill')
print("Moje ulubione rodzaje pizzy to:")
for friend_pizza in friend_pizzas[:]:
	print(friend_pizza.title())
	
print("Ulubione rodzaje pizzy mojego ziomka to:")
for pizza in pizzas[:]:
	print(pizza.title())

#Przechowywanie informacji o pizzy zamawianej przez klienta.
pizza_2 = {
	'crust': 'grubym',
	'toppings': ['pieczarki', 'podwojny ser'],
	}
#Podsumowanie zamówienia.
print("Zamówiłeś pizzę na " + pizza_2['crust'] + " cieście " +
	"wraz z następującymi dodatkami:")
	
for topping in pizza_2['toppings']:
	print("\t" + topping)
