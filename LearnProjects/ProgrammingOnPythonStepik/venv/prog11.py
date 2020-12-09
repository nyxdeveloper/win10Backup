# расшифровщик бинарных файлов

import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

passwords = open('passwords.txt', 'r').read().split('\n')

for i in passwords:
    try:
        print(simplecrypt.decrypt(i, encrypted))
        break
    except (simplecrypt.DecryptionException, ValueError):
        print('key ' + i + ' does not fit')