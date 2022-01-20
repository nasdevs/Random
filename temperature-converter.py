'''
@name : Temperature Converter
@version : 0.1.0
'''

menu = {
    1: 'Celcius (C)',
    2: 'Reamur (R)',
    3: 'Fahrenheit (F)',
    4: 'Kelvin (K)'
}

print('----------MENU----------')
for i in menu:
    print(f'{i}. {menu[i]}')

A = int(input('Input : ')) 

if A not in menu:
    print('Tidak ada dalam menu')
    exit()

N = int(input(f'Input {menu[A]} : '))

# Celcius
if A == 1:
    R =  4/5 * N 
    K = (5/5 * N) + 273.15
    F = (9/5 * N) + 32

# Reamur
elif A == 2:
    C = 5/4 * N
    K = (5/4 * N) + 273.15
    F = (9/4 * N) + 32

# Fahrenheit
elif A == 3:
    C = 5/9 * (N - 32)
    K = 5/9 * (N + 459.67)
    R = 4/9 * (N - 32)

# Kelvin
elif A == 4:
    C = 5/5 * (N  - 273.15)
    R = 4/5 * (N - 273.15)
    F = (9/5 * N) - 459.67

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
