moradores = ['palestra', 'vicky', 'coisa', 'katahas']
print(moradores)

moradores[0] = 'favela'
print(moradores)

moradores.append('borbo')
print(moradores)

moradores2 = []
moradores2.append('palestra')
moradores2.append('vicky')
moradores2.append('coisa')
print(moradores2)

moradores2.insert(0, 'borbo')
print(moradores2)

del moradores2[0]
print(moradores2)

ex =  moradores2.pop(0)

print(f'o proximo morador que vai sair da casa e o {ex.title()}')

moradores2.remove('coisa')

print(moradores2)

