current_users = ['admin','laszlo','member','useless','one']

new_users = ['sergiej','laszlo','mydlo','golder','one', 'LASZLO']

for new_user in new_users:
	if new_user.lower() in current_users:
		print("Wybrana nazwa użytkownika " + new_user + 
							" jest zajęta. Proszę zmienić")
	else:
		print("Nazwa użytkownika dozwolona. Witaj "
							+ new_user + ".")
		
