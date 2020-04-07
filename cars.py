cars = ['bmw', 'audi','toyota','subaru']

print("Oto lista początkowa")
print(cars)

print("\nOto lista posortowana:")
print(sorted(cars))

print("\nOto ponownie lista początkowa:")
print(cars)

cars2 = ['bmw', 'audi','toyota','subaru']
print(cars2)

cars2.reverse()
print(cars2)

cars2.reverse()
print(cars2)
len(cars2)

#3.8

miejsca = ['lizbona','tokyo','londyn','wenecja','shanghai']
print(miejsca)

print(sorted(miejsca))

print(miejsca)

print(sorted(miejsca, reverse=True))

print(miejsca)

miejsca.reverse()
print(miejsca)

miejsca.reverse()
print(miejsca)

miejsca.sort()
print(miejsca)

miejsca.sort(reverse=True)
print(miejsca)

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
