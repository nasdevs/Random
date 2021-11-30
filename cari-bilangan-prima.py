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
