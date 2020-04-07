alien_0 = {'color': 'zielony', 'points': 5}
alien_1 = {'color': 'żółty', 'points': 10}
alien_2 = {'color': 'czerwony', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

#utworzenie pustej listy przeznaczonej do przechowywania obcych	
aliens_more = []

#utworzenie 40 zielonych obcych
for alien_number in range(40):
	new_alien = {'color': 'zielony', 'points': 5, 'speed': 'fast'}
	aliens_more.append(new_alien)
#Utworzenie zależności dla 3 pierwszych przykładów
for alienn in aliens_more[0:3]:
	if alienn['color'] == 'zielony':
		alienn['color'] = 'żołty'
		alienn['points'] = 10
		alienn['speed'] = 'medium'	
#Wyświetlanie pierwszych pięciu obcych
for alienn in aliens_more[:5]:
	print(alienn)
print("...")


		
#Wyświetlanie całkowitej liczby utworzonych obcych
print("Całkowita liczba obcych: " + str(len(aliens_more)))
