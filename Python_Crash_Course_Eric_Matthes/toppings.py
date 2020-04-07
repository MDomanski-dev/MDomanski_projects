requested_toppings = ['boczek','pieczarki','podwójny ser']

if 'pieczarki' in requested_toppings:
    print("Dodaje pieczarki")
    
if 'pepperoni' in requested_toppings:
    print("Dodaje pepperoni")  
    
if 'podwójny ser' in requested_toppings:
    print("Dodaje podwójny ser")

print("\nTwoja pizza jest już gotowa!")

if 'pieczarki' in requested_toppings:
    print("Dodaje pieczarki")
elif 'pepperoni' in requested_toppings:
	print("Dodaje pepperoni")

elif 'podwójny ser' in requested_toppings:
	print("Dodaje podwójny ser")
	
print("\nTwoja pizza jest juz gotowa!")

requested_toppingss = ['boczek','pieczarki','podwójny ser']

for requested_topping in requested_toppingss:
	if requested_topping == 'boczek':
		print("Niestety, nie posiadamy boczku")
else:
	print("Dodaję " + requested_topping + ".")
	
print("\nTwoja pizza jest już gotowa!")


requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print("Dodaję " + requested_topping + '.')
	print("\nTwoja pizza jest juz gotowa!")
else:
	print("Czy jesteś pewien że chcesz pizze bez dodatków?")
	
available_toppings = ['pieczarki','oliwki','boczek',
						'pepperoni','ananas','podwójny ser']
						
requested_toppingss = ['frytki','pieczarki','podwójny ser']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Dodaję " + requested_topping + '.')
	else:
		print("Przepraszamy,ale obecnienie mamy dodatku" + 
		requested_topping + '.')
		
print("\nTwoja pizza jest już gotowa")
	
	

