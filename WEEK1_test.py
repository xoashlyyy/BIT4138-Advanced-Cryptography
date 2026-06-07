from cryptography.fernet import Fernet

print("---  Week 1: Environment Test ---")

# Generate a test key and encrypt a simple message
key = Fernet.generate_key()
cipher_suite = Fernet(key)
ciphertext = cipher_suite.encrypt(b"Environment Setup Successful")

print("Cryptography Library successfully loaded.")
print(f"Test Ciphertext: {ciphertext}")