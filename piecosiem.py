# -*- coding: utf-8 -*-

users = ['admin','laszlo','member','useless','one']

if users:
	for user in users:
		if user == 'admin':
			print(
			"Witaj, admin! Czy chcesz przejrzeć dzisiejszy raport?")
		else:
			print("Witaj " + user + "."
			" Dziękujemy, ze ponownie się zalogowałeś") 
			
else:
	print("Musimy jakoś znaleźć jakiś użytkowników")
