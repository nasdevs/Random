import os
import time

# !pip install pyautogui
import pyautogui as pag

from tqdm.auto import tqdm

# contoh kode barang : 2022/III/S/ROU/02/{{ID}}/41

def main(kode_barang):
    jumlah = int(kode_barang.split('/')[-1])

    kode_barang = kode_barang.replace('{', '', 1).replace('}', '', 1).replace(' ', '').split('/')
    kode_barang = kode_barang[:-1] + ['0' * (3 - len(kode_barang[-1])) + kode_barang[-1]]
    kode_barang = '/'.join(kode_barang)

    pag.hotkey('alt', 'tab')

    print('Program running...')
    time.sleep(1)

    for id in tqdm(range(1, jumlah+1)):
        ID = '0' * (3 - len(str(id))) + str(id)
        result = kode_barang.format(ID=ID)
        pag.write(result)
        pag.press('enter') 

    print('DONE!')
    
ID = str(input('Input kode barang : '))
main(ID)
