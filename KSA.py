def ksa(key):
    key_length = len(key)

    S = list(range(256))

    j = 0
    for i in range(256):

        j = (j + S[i] + ord(key[i % key_length])) % 256

        S[i], S[j] = S[j], S[i]

    return S

def prga(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256


        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]

        k = S[(S[i] + S[j]) % 256]
        yield k

def encrypt(key, plaintext):
    S = ksa(key)

    prga_generator = prga(S)

    ciphertext = bytearray(len(plaintext))
    for i, b in enumerate(plaintext):
        ciphertext[i] = b ^ next(prga_generator)

    return ciphertext

def decrypt(key, ciphertext):
    S = ksa(key)

    prga_generator = prga(S)


    plaintext = bytearray(len(ciphertext))
    for i, b in enumerate(ciphertext):
        plaintext[i] = b ^ next(prga_generator)

    return plaintext

def main():
    key = 'saputra1'
    values = list(range(256))
    encrypted_values = encrypt(key, values)
    decrypted_values = decrypt(key, encrypted_values)

    
    values = list(values)
    encrypted_values = list(encrypted_values)
    decrypted_values = list(decrypted_values)
    
    print("awal : ", values)
    print("/////////////")
    print("hasil : ",encrypted_values)

if __name__ == '__main__':
    main()
