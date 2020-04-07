# -*- coding: utf-8 -*-


lista_gosci = ['Hendrix', 'Cobain', 'Hauer', 'Tesla'] #3.4

print("\nZapraszam Cię na obiad, drogi "  + lista_gosci[0].title() + ".")
print("\nZapraszam Cię na obiad, drogi "  + lista_gosci[1].title() + ".")
print("\nZapraszam Cię na obiad, drogi "  + lista_gosci[2].title() + ".")
print("\nZapraszam Cię na obiad, drogi "  + lista_gosci[3].title() + ".")

print("\n Na obiad nie będzie mógł przyjść " + lista_gosci[0] + ".") # 3.5

del lista_gosci[0]

lista_gosci.append('Marlon')
print(lista_gosci)

print("\nZapraszam Cię na obiad, drogi "  + lista_gosci[0].title() + ".")
print("\nZapraszam Cię na obiad, drogi "  + lista_gosci[1].title() + ".")
print("\nZapraszam Cię na obiad, drogi "  + lista_gosci[2].title() + ".")
print("\nZapraszam Cię na obiad, drogi "  + lista_gosci[3].title() + ".")

#3.6

print("\nMam większy stół więc będzie więcej gości")

lista_gosci.insert(0, 'mama')
lista_gosci.insert(2, 'tata')
lista_gosci.insert(5, 'ja')

print("\nZapraszam Cię na obiad, drogi "  + lista_gosci[0].title() + ".")
print("\nZapraszam Cię na obiad, drogi "  + lista_gosci[1].title() + ".")
print("\nZapraszam Cię na obiad, drogi "  + lista_gosci[2].title() + ".")
print("\nZapraszam Cię na obiad, drogi "  + lista_gosci[3].title() + ".")
print("\nZapraszam Cię na obiad, drogi "  + lista_gosci[4].title() + ".")
print("\nZapraszam Cię na obiad, drogi "  + lista_gosci[5].title() + ".")

print(lista_gosci)
#3.6

print("\nJednak moge zaprosic tylko dwie osoby")

pierwszy_gosc = lista_gosci.pop(0)
print("\nNiestety nie będzie możliwości spotkania, przepraszam Cię " + pierwszy_gosc.title() + ".")

drugi_gosc = lista_gosci.pop(0)
print("\nNiestety nie będzie możliwości spotkania, przepraszam Cię " + drugi_gosc.title() + ".")

trzeci_gosc = lista_gosci.pop(0)
print("\nNiestety nie będzie możliwości spotkania, przepraszam Cię " + trzeci_gosc.title() + ".")

czwarty_gosc = lista_gosci.pop(0)
print("\nNiestety nie będzie możliwości spotkania, przepraszam Cię " + czwarty_gosc.title() + ".")

piaty_gosc = lista_gosci.pop(0)
print("\nNiestety nie będzie możliwości spotkania, przepraszam Cię " + piaty_gosc.title() + ".")
print("\nWidzimy się na obiedzie ," + lista_gosci[0] + ".")
print("\nWidzimy się na obiedzie ," + lista_gosci[1] + ".")


del lista_gosci[1]
del lista_gosci[0]

print(lista_gosci)






