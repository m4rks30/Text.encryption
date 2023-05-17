from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'This is a key123'
iv = b'This is an IV456'
mode = AES.MODE_CBC

def encrypt(plaintext):
    cipher = AES.new(key, mode, iv)
    padded_plaintext = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt(ciphertext):
    cipher = AES.new(key, mode, iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size)
    return plaintext

plaintext = b'This is a secret message'
ciphertext = encrypt(plaintext)
decrypted_plaintext = decrypt(ciphertext)

print("Plaintext: ", plaintext)
print("Ciphertext: ", ciphertext)
print("Decrypted plaintext: ", decrypted_plaintext)
