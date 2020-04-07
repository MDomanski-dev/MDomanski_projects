panstwa = ['meksyk','polska','niemcy','czechy','wegry'] #3.10

print(panstwa)

print(panstwa[0])

print(panstwa[0].title())

print(panstwa[1])
print(panstwa[3])

print(panstwa[-1])

message = "Panstwem jest np. " + panstwa[0].title() +  "."
print(message)

panstwa[0] = 'norwegia'
print(panstwa)

panstwa.append('finlandia')
print(panstwa)

panstwa.insert(0, 'pakistan')
print(panstwa)

del panstwa[0]
print(panstwa)

del panstwa[1]
print(panstwa)

popped_panstwa = panstwa.pop()
print(panstwa)
print(popped_panstwa)

last_owned = panstwa.pop()
print(last_owned.title())

first_owned = panstwa.pop(0)
print(first_owned.title())

panstwa = ['meksyk','polska','niemcy','czechy','wegry']
panstwa.remove('wegry')
print(panstwa)

too_expensive = 'polska'
panstwa.remove(too_expensive)
print(too_expensive.title())

panstwa = ['meksyk','polska','niemcy','czechy','wegry']

panstwa.sort()
print(panstwa)

panstwa.sort(reverse=True)
print(panstwa)

print(panstwa)

print(sorted(panstwa))

print(panstwa)

panstwa.reverse()
print(panstwa)

panstwa = ['meksyk','polska','niemcy','czechy','wegry']
print(panstwa[0])

