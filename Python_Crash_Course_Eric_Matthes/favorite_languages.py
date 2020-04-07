favorite_languages = {
	'janek': 'python',
	'sara': 'c',
	'edward': 'ruby',
	'paweł': 'python',
	}
	
coders = ['janek', 'sara', 'edward', 'paweł', 'sarah', 'matt', 'danielle']
for coder in coders:
	if coder in favorite_languages.keys():
		print(coder.title() + " dzięki za wzięcie udziału")
	else:
		print(coder.title() + " wbijaj na ankiete")

print("Ulubiony język programowania Sary to " + 
	favorite_languages['sara'].title() + 
	".")

for name, lang in favorite_languages.items():
	print("Ulubiony język programowania użytkownika " + name.title() + " to " + lang.title() + ".")
	
for name in favorite_languages.keys():
	print(name.title())
	
friends = ['sara','paweł']
for name in favorite_languages.keys():
	print(name.title())
	
if name in friends:
	print(" Witaj, " + name.title() + "! Widzę, że Twoim ulubionym językiem programowania jest " +
	favorite_languages[name].title() + "!")


fav_lang = {
	'janek': ['python', 'ruby'],
	'sara': ['c'],
	'edward': ['go', 'ruby'],
	'paweł': ['python', 'haskell'],
}

for name, languages in fav_lang.items():
	print("Ulubione języki programowania uzytkownika " + name.title() +
	 " to:")
	 
for language in languages:
	print("\t" + language.title())
	
	
