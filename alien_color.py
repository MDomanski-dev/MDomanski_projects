#5.3
alien_color = ['zółty']
#1
if 'zielony' in alien_color:
	print("Jest zielony.Zdobyłeś 5 pkt")
#2	
if 'zółty' in alien_color:
	print("Jest zółty.Zdobyłeś 5 pkt")
	
if 'czerwony' in alien_color:
	print("Jest czerwony.Zdobyłeś 5 pkt")


#5.4
alien_color = ['zielony']
#wariant 1
if 'czerwony' in alien_color:
	print("\nZdobyłeś 5 pkt.")
else:
	print("Zdobyłeś 10 pkt.")
	
#wariant 2
if 'zielony' in alien_color:
	print("\nZdobyłeś 5 pkt.")
else:
	print("Zdobyłeś 10 pkt.")
	
#5.5
# wariant_1
alien_color = 'zielony'
if 'zielony' in alien_color:
	print("Zdobyłeś 5 pkt za zielonego")
	
elif 'zółty' in alien_color:
	print("Zdobyłeś 10 pkt za żółtego")
	
elif 'czerwony' in alien_color:
	print("Zdobyłeś 15 pkt za czerwonego")
	
#wariant_2
alien_color = 'zółty'
if 'zielony' in alien_color:
	print("Zdobyłeś 5 pkt za zielonego")
	
elif 'zółty' in alien_color:
	print("Zdobyłeś 10 pkt za żółtego")
	
elif 'czerwony' in alien_color:
	print("Zdobyłeś 15 pkt za czerwonego")

#wariant_3	
alien_color = 'czerwony'
if 'zielony' in alien_color:
	print("Zdobyłeś 5 pkt za zielonego")
	
elif 'zółty' in alien_color:
	print("Zdobyłeś 10 pkt za żółtego")
	
elif 'czerwony' in alien_color:
	print("Zdobyłeś 15 pkt za czerwonego")

#5.6

age = 27
if age < 2:
	print("Niemowle")
	
elif age >= 2 and age < 4:
	print("Dziecko uczące się chodzić")
	
elif age >= 4 and age < 13:
	print("Dziecko")
	
elif age >= 13 and age < 20:
	print("Nastolatek")
	
elif age >= 20 and age < 65:
	print("Dorosły")
	
elif age > 65:
	print("Senior")

favourite_fruits = ['jabłko','gruszka','banan']

if 'jabłko' in favourite_fruits:
	print("Naprawdę lubisz jabłka")
	
if 'mango' in favourite_fruits:
	print("Naprawdę lubisz mango")
	
if 'ananas' in favourite_fruits:
	print("Naprawdę lubisz ananas")
	
if 'gruszka' in favourite_fruits:
	print("Naprawdę lubisz gruszki")
	
if 'banan' in favourite_fruits:
	print("Naprawdę lubisz banany")
	
