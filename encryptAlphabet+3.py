import sys
def checkSymbol(teks):
    for i in range(0, len(teks)):
        if ord(teks[i]) < 65:
            print('Hanya boleh pakai Alphabet')
            sys.exit()

encrypt = []
decrypt = []
alphabet = 'abcdefghijklmnopqrstuvwxyz012ABCDEFGHIJKLMNOPQRSTUVWXYZ012'

teks = str(input('Input : '))
checkSymbol(teks)

for i in range(0, len(teks)):
    a = alphabet.index(teks[i])
    encrypt.append(alphabet[a+3])
encryptTeks = "".join(encrypt)

for i in range(0, len(encryptTeks)):
    a = alphabet.index(encryptTeks[i])
    decrypt.append(alphabet[a-3])
decryptTeks = "".join(decrypt)

print(encryptTeks)
print(decryptTeks)
