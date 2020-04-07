my_foods = ['pizza','chipsy','pasta']
friend_foods = my_foods[:]
#friend_foods = my_foods - dodatek robiący dwie takie same listy
my_foods.append('burger')
friend_foods.append('sos')
print("Moje ulubiony potrawy to:")
print(my_foods)
print("A ulubionymi potrafami mojego ziomka są")
print(friend_foods)

print("Moje ulubiony potrawy to:")
for my_food in my_foods[:]:
	print(my_food.title())
	
print("A ulubionymi potrafami mojego ziomka są")
for friend_food in friend_foods[:]:
	print(friend_food.title())


