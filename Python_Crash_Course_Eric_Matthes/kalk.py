# importujemy przez nas utworzoną bibliotekę / moduł
# "*" gwiazdka oznacza, że importujemy wszystko z modułu
# nazwę modułu importujemy bez rozszerzenia ".py"
from modulkalk import *
# możemy również zaimportować tylko interesujące nas funkcje, robimy to jak poniżej
# from modulKalkulator import dodawanie, odejmowanie, mnozenie, dzielenie
 
# tworzymy dwie zmienne pobierające liczby do działania z klawiatury
# tworzymy zmienną, która będzie pobierała liczbę z klawiatury, reprezentującą dane działanie
pierwszaLiczba = int(input("Wpisz pierwszą liczbę: "))
drugaLiczba = int(input("Wpisz drugą liczbę: "))
rodzajDzilania = int(input("Wybierz rodzaj działania:\n1 - dodawanie\n2 - odejmowanie\n3 - mnożenie\n4 - dzielenie\nWpisz cyfrę działania: "))
 
# tworzymy instrukcję warunkową, która będzie sprawdzała wprowadzoną liczbę reprezentującą dane działanie
# oraz przypisywała do tej liczby odpowiednią funkcję wraz z parametrami
if (rodzajDzilania == 1):
    wynikDzialania = dodawanie(pierwszaLiczba, drugaLiczba)
elif (rodzajDzilania == 2):
    wynikDzialania = odejmowanie(pierwszaLiczba, drugaLiczba)
elif (rodzajDzilania == 3):
    wynikDzialania = mnozenie(pierwszaLiczba, drugaLiczba)
elif (rodzajDzilania == 4):
    wynikDzialania = dzielenie(pierwszaLiczba, drugaLiczba)
 
# wyświetlamy wynik działania wybranej funkcji, który został przypisany do zmiennej "wynikDzialania"
print("\nWynik działania: ", wynikDzialania)
