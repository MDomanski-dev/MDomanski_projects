# -*- coding: utf-8 -*-

motocykle = ['Kawaski', 'Honda', 'Ducati', 'Yamaha']
print(motocykle[0])

print(motocykle)

motocykle[0] = 'Donald'

print(motocykle[0])

print(motocykle)

motocykle.append('suka')
print(motocykle)

motorcycles = []

motorcycles.append('ducati')
motorcycles.append('yamaha')
motorcycles.append('honda')
motorcycles.append('triumph')

print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motocykle = ['Kawaski', 'Honda', 'Ducati', 'Yamaha']
popped_motocykle = motocykle.pop()
print(motocykle)
print(popped_motocykle)

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("Ostatni zakupiony przeze mnie motocykl to " + last_owned.title() + ".")

pierwszy_zakup = motorcycles.pop(0)
print("Pierwszy zakupiony przeze mnie motocykl to " + pierwszy_zakup.title() + ".")

motorcycles = ['Kawaski', 'Honda', 'Ducati', 'Yamaha']
print(motorcycles)

motorcycles.remove('Honda')
print(motorcycles)

motorcycles = ['Kawaski', 'Honda', 'Ducati', 'Yamaha']
print(motorcycles)

za_drogi = 'Ducati'
motorcycles.remove(za_drogi)
print(motorcycles)
print("\nMotocykl " + za_drogi.title() + "jest zbyt drogi dla mnie.")
