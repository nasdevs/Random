import random

plat_daerah = {
    'sulawesi barat': 'DC',
    'sulawesi selatan': 'DD',
    'sulawesi tengah': 'DN',
    'sulawesi tenggara': 'DT',
    'gorontalo': 'DM',
}

daerah = str(input('Input daerah : '))
nomor_plat = random.randint(1000, 2000)
daerah2 = str(input('Input daerah belakang : '))
bln_beli = int(input('Input bln beli : '))
thn_beli = int(input('Input thn beli : '))
thn_exp = thn_beli + 5 - 2000

print('{} {} {}'.format(plat_daerah[daerah.lower()], nomor_plat, daerah2))
print('  {}.{}'.format(bln_beli, thn_exp))
