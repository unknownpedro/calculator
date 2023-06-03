import math
print('Welcome to this calculator')
soma: float
sub: float
mult: float
div: float

nmr1 = float(input('Digite um numero: '))
nmr2 = float(input('Digite outro: '))
soma = nmr1 + nmr2
sub = nmr1 - nmr2
mult = nmr1 * nmr2
div = nmr1 / nmr2

select = int(input('Selecione a operação: + (1) / - (2) / * (3) / : (4) '))

if select == 1: (
    print('A soma é:', soma)
)

if  select == 2: (
    print('A subtração é:', sub)
)

if select == 3: (
    print('A multiplicação é:', mult)
)

if select == 4: (
    print('A divisão é:', div)
)

if select > 4:  (
    print('Opção inválida!')
)
    
if select < 1:  (
    print('Opção inválida!')
)
