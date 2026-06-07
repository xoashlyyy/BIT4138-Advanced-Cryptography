from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

print("--- BIT4138 Lab Week 5: RSA Asymmetric Cryptography ---")

# 1. Key Generation
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

message = b"Secure Asymmetric Data"

# 2. Encryption (Using Public Key)
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
print(f"Ciphertext (Hex): {ciphertext.hex()[:60]}...")

# 3. Decryption (Using Private Key)
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
print(f"Decrypted: {plaintext.decode()}")