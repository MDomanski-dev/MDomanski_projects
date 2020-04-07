favourite_lang = {
'janek': 'python',
'sara': 'c',
'edward': 'ruby',
'paweł': 'python',
}

friends = ['edward','sara']
for imie in favourite_lang.keys():
	print(imie.title())
	
	if imie in friends:
		print("Witaj, " + imie.title() + "! Widzę, że twoim ulubiony"
		" językiem programowania jest "
		+ favourite_lang[imie].title() + "!")
		
	if 'malgorzata' not in favourite_lang.keys():
		print("Malgorzata, weź udział w ankiecie")

for imie in sorted(favourite_lang.keys()):
	print(imie.title() + " dziękuje za udział w ankiecie")
