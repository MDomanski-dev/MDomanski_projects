glosariusz = {}

glosariusz['pętla'] = '''Pętla:
						Jedna z trzech podstawowych konstrukcji 
						programowania strukturalnego 
						(obok instrukcji warunkowej i
						instrukcji wyboru). Umożliwia cykliczne wykonywanie 
						ciągu instrukcji określoną liczbę razy, do momentu 
						zajścia pewnych warunków, dla każdego elementu 
						kolekcji lub w nieskończoność.'''

glosariusz['string'] = '''String:
						jest sekwencją znaków, a zazwyczaj 
						przechowują słowa, zdania. Nie ma skryptu, 
						w którym nie użyjecie stringów,'''

glosariusz['krotka'] = '''Krotka: 
						struktura danych będąca 
						odzwierciedleniem matematycznej n-ki, tj. 
						uporządkowanego ciągu wartości. Krotki 
						przechowują stałe wartości o różnych typach 
						danych – nie można zmodyfikować żadnego 
						elementu, odczyt natomiast wymaga podania 
						indeksu liczbowego żądanego elementu.'''
						
glosariusz['lista'] = '''Lista: 
						To zmienna zawierająca zbiór elementów. 
						Elementami listy mogą być wszystkie dostępne w 
						Python typy danych. Listy są jednym z 
						najczęściej używanych typów danych. Można je 
						porównać z tablicami (PHP, Perl) 
						lub matrycami.'''

glosariusz['słownik'] = '''Słownik: 
						jest strukturą danych podobną do 
						tablicy, ale pracuje się na nim w oparciu o 
						klucze (zwane też hasłami),a nie indeksy. 
						Klucze mogą być obiektem dowolnego typu 
						(napisy, liczby, tablice itp.).'''
glosariusz['test'] = "ss"

glosariusz['xd'] = "ss"

glosariusz['xs'] = "ss"					

for name, lang in glosariusz.items():
	print(name.title() + lang.title())
