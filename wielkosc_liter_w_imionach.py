# -*- coding: utf-8 -*-

first_name = "Marcin"  

print("Witaj, " + first_name.title() + "! " + "Czy chcesz dzisiaj poznać Pythona?") 

#testowanie formatowania znakow w przypisanej zmiennej
print(first_name.lower())
print(first_name.upper())
print(first_name.title())

imie = "Albert"
nazwisko = "Einstein"

pelne = imie + " " + nazwisko

message = pelne.title()  + ' ' +  'powiedział kiedyś:"Osoba, która nigdy nie popełniła błędu, \njest kimś, \tkto nigdy nie probował niczego nowego".'

print(message)  

famous_person = "Albert Einstein"

message = famous_person.title() + ' ' + 'powiedział kiedyś:"Osoba, która nigdy nie popełniła błędu, \njest kimś, kto nigdy nie probował niczego nowego".'
print(message)

first_name = " Marcin "
print(first_name.lstrip())
print(first_name.rstrip())
print(first_name.strip())

