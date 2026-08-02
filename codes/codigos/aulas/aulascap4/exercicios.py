for value in range(1,21,2):
    print(value)
print('\n')

um_milhao = [value for value in range(1,1_000_001)]
print(max(um_milhao))
print(min(um_milhao))
print(sum(um_milhao))

mu3 = [value for value in range(3,31,3)]
print(mu3)

cube = [value**3 for value in range(1,11)]
print(cube)