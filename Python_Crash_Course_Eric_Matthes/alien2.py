alien_0 = {'color': 'zielony', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("Zdobyłeś " + str(new_points) + " punktów!")


alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}

alien_1[''] = 'zielony'
alien_1[''] = 5

print(alien_1)

alien_2 = {'color': 'zielony'}
print("Obcy ma kolor " + alien_2['color'] + ".")

alien_2['color'] = 'żółty'
print("Obcy ma teraz kolor " + alien_2['color'] + ".")



alien_0 = {'x_position' : 0, 'y_position': 25, 'speed': 'średnio'}
print("Początkowa wartość x-position: " + str(alien_0['x_position']))

#Przesunięcie obcego w prawo.
#Ustalenie odległości, jaką powinien pokonać obcy poruszający się z daną
#szybkością
if alien_0['speed'] == 'wolno':
	x_increment = 1
elif alien_0['speed'] == 'średnio':
	x_increment= 2
else:
	#To musi być szybki obcy.
	x_increment = 3
	
#Nowe położenie to suma dotychczasowego położenia i wartości x_increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("Nowa wartość x-position: " + str(alien_0['x_position']))
