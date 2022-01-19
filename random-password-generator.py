'''
@name : random password generator
@version : 0.1.0
'''

import random

password = []
alnum = 'abcdefghijklmnopqrstuvwxyz0123456789'

loop_alpha = 0
loop_num = 0

print('Random password generator')

while True:
    alpha = int(input('Berapa alphabet : '))
    num = int(input('Berapa nomor : '))
    
    if (num+alpha) not in range(8, 17):
        print('Minimal password terdiri dari 8 - 16 character')

    else:
        break

while True:
    index = random.randint(0, len(alnum) - 1)
    rd_selection = random.randint(1, 2)
    
    if alnum[index].isalpha() == True and rd_selection == 1 and loop_alpha < alpha:
        password.append(alnum[index])
        loop_alpha += 1
    
    elif alnum[index].isnumeric() == True and rd_selection == 2 and loop_num < num:
        password.append(alnum[index])
        loop_num += 1
        
    if loop_alpha + loop_num == alpha + num:
        break

# unlist
password = ''.join(password)

print(f'''
--------------------------
Pembuatan password selesai
passwordmu adalah : {password}
''')
