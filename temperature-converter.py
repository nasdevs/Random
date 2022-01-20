'''
@name : Temperature Conversion
@version : 0.2.0
'''

menu = {
    1: 'Celcius (C)',
    2: 'Reamur (R)',
    3: 'Fahrenheit (F)',
    4: 'Kelvin (K)'
}

# output menu
print('----------MENU----------')
for i in menu:
    print(f'{i}. {menu[i]}')

A = int(input('Input : ')) 

if A not in menu:
    print('Tidak ada dalam menu')
    exit()

N = int(input(f'Input {menu[A]} : '))

# Pertama mencari Celcius yang nantinya akan dikonversikan ke R K dan F
# Celcius
if A == 1:
    C = N

# Reamur
elif A == 2:
    C = 5/4 * N

# Fahrenheit
elif A == 3:
    C = 5/9 * (N - 32)

# Kelvin
elif A == 4:
    C = 5/5 * (N  - 273.15)

# proses konversi dari Celcius ke R K F
R = 4/5 * C 
K = (5/5 * C) + 273.15
F = (9/5 * C) + 32

# output hasil
print('\n------------------------')
print(f'Konversi {menu[A]} ke:\n')

if A != 1:
    print('Celcius (C)    : ', round(C, 2))
if A != 2:
    print('Reamur (R)     : ', round(R, 2))
if A != 3:
    print('Fahrenheit (F) : ', round(F, 2))
if A != 4:
    print('Kelvin (K)     : ', round(K, 2))
