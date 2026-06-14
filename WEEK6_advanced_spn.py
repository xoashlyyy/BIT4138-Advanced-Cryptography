import random

print("--- BIT4138 Advanced Programming Task: Multi-Round SPN ---")

# 1. Dynamically generate a large 256-byte S-Box using a fixed seed
random_gen = random.Random(101)
S_BOX = list(range(256))
random_gen.shuffle(S_BOX)

def key_mixing(data, key):
    """Mixes a custom key with data using bitwise XOR."""
    key_bytes = key.encode('utf-8')
    # Using data[i] ensures the bytes are correctly matched with the key
    return bytes([data[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(data))])
def substitution_layer(data):
    """Maps every byte using the large 256-byte S-Box (Confusion)."""
    return bytes([S_BOX[b] for b in data])

def permutation_layer(data):
    """Spreads bit modifications across the block via string reversal (Diffusion)."""
    return data[::-1]

def run_spn(plaintext, key, total_rounds):
    """Executes the SPN framework over multiple rounds."""
    current_block = plaintext.encode('utf-8')
    for r in range(total_rounds):
        current_block = key_mixing(current_block, key)
        current_block = substitution_layer(current_block)
        current_block = permutation_layer(current_block)
    return current_block

#  Avalanche Effect Demo
user_plaintext1 = input("Enter main plaintext (e.g., HELLO): ")
user_plaintext2 = input("Enter second plaintext with 1 character changed (e.g., JELLO): ")
user_key = input("Enter your custom secret key: ")
num_rounds = int(input("Enter number of rounds (e.g., 4): "))

cipher1 = run_spn(user_plaintext1, user_key, num_rounds)
cipher2 = run_spn(user_plaintext2, user_key, num_rounds)

print(f"\n[+] Ciphertext 1 (Hex): {cipher1.hex()}")
print(f"[+] Ciphertext 2 (Hex): {cipher2.hex()}")

# Calculate Avalanche Effect
differences = sum(1 for b1, b2 in zip(cipher1, cipher2) if b1 != b2)
print(f"\n--- Avalanche Effect Analysis ---")
print(f"Changing 1 character disrupted {differences} out of {len(cipher1)} bytes in the final output block.")