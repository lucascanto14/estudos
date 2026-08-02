convidados = ['tereza','abel','olga','sergia']

print(f'opa {convidados[0].title()}, venha pra meu aniversario')
print(f'opa {convidados[1].title()}, venha pra meu aniversario')
print(f'opa {convidados[2].title()}, venha pra meu aniversario')
print(f'opa {convidados[3].title()}, venha pra meu aniversario')
print('\n')

nao_vai = convidados.pop(1)
convidados.insert(1, 'areza')

print(f'opa {convidados[0].title()}, venha pra meu aniversario')
print(f'opa {convidados[1].title()}, venha pra meu aniversario')
print(f'opa {convidados[2].title()}, venha pra meu aniversario')
print(f'opa {convidados[3].title()}, venha pra meu aniversario')
print(f'{nao_vai.title()} nao vem')
print('\n')

convidados.insert(0, 'adriana')
convidados.insert(2, 'fabio')
convidados.append('eduardo')
print('achei uma mesa com mais lugares')
print('\n')


print(f'opa {convidados[0].title()}, venha pra meu aniversario')
print(f'opa {convidados[1].title()}, venha pra meu aniversario')
print(f'opa {convidados[2].title()}, venha pra meu aniversario')
print(f'opa {convidados[3].title()}, venha pra meu aniversario')
print(f'opa {convidados[4].title()}, venha pra meu aniversario')
print(f'opa {convidados[5].title()}, venha pra meu aniversario')
print(f'opa {convidados[6].title()}, venha pra meu aniversario')

print('a mesa nao vai chegar a tempo so posso convidar duas pessoas')

desconvidados = []
desconvidados.append(convidados.pop(4))
desconvidados.append(convidados.pop(3))
desconvidados.append(convidados.pop(2))
desconvidados.append(convidados.pop(1))
desconvidados.append(convidados.pop(0))

print(f'{desconvidados[0].title()}, nao venha pra meu aniversario')
print(f'{desconvidados[1].title()}, nao venha pra meu aniversario')
print(f'{desconvidados[2].title()}, nao venha pra meu aniversario')
print(f'{desconvidados[3].title()}, nao venha pra meu aniversario')
print(f'{desconvidados[4].title()}, nao venha pra meu aniversario')
print('\n')
print(f'opa {convidados[0].title()}, venha pra meu aniversario')
print(f'opa {convidados[1].title()}, venha pra meu aniversario')

del convidados[0:2]

print(convidados)
print(f'vem {len(convidados)} convidados')