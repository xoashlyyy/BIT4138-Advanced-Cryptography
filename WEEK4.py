import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

print("---  Lab Week 4: AES Block Cipher ---")

# 1. Key and IV Generation (256-bit AES)
key = os.urandom(32) 
iv = os.urandom(16)  

# 2. Data Padding (AES requires fixed 128-bit blocks)
plaintext = b"Confidential AES Block Data"
padder = padding.PKCS7(128).padder()
padded_data = padder.update(plaintext) + padder.finalize()

# 3. Encryption Process (CBC Mode)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

print(f"Original Plaintext: {plaintext.decode()}")
print(f"Ciphertext (Hex): {ciphertext.hex()}")

# 4. Decryption Process
decryptor = cipher.decryptor()
decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

unpadder = padding.PKCS7(128).unpadder()
decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()

print(f"Decrypted Data: {decrypted_data.decode()}")