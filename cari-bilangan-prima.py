def bilPrima(bilBulat):
    jmlBagi = 0
    for i in range(1, bilBulat+1):
        if bilBulat%i == 0:
            jmlBagi += 1
    if jmlBagi == 2: 
        print('Bilangan Bulat')
    else:
        print('Bukan Bilangan Prima')
    return
            
bilBulat = int(input('Masukkan bilangan bulat: '))
bilPrima(bilBulat)

# Setelah mode Khaby Lame. 

def bilPrima(bilBulat):
    for i in range(2, bilBulat):
        if bilBulat%i == 0:
            return ('Bukan Bilangan Prima')
    if bilBulat == 1:
        return ('Bukan Bilangan Prima')
    else: 
        return ('Bilangan Prima')
            
bilBulat = int(input('Masukkan Bilangan Bulat : '))
print(bilPrima(bilBulat))
