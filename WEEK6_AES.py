import random

print("--- BIT4138 Challenge Task: Mini-AES Simulator ---")

# Generate invertible S-Box pair for Encryption & Decryption
aes_seed = random.Random(500)
AES_S_BOX = list(range(256))
aes_seed.shuffle(AES_S_BOX)
# Create inverse mapping array
AES_INV_S_BOX = [AES_S_BOX.index(byte) for byte in range(256)]

def add_round_key(state, key):
    """XOR state with the custom key matrix."""
    k_bytes = key.encode('utf-8')
    return bytes([state[i] ^ k_bytes[i % len(k_bytes)] for i in range(len(state))])

def sub_bytes(state, sbox):
    """Applies non-linear substitution."""
    return bytes([sbox[b] for b in state])

def shift_rows_permutation(state):
    """Permutes the state block by performing a left circular shift."""
    if len(state) <= 1: return state
    return bytes(list(state[1:]) + [state[0]])

def inv_shift_rows_permutation(state):
    """Reverses the left circular shift by shifting right."""
    if len(state) <= 1: return state
    return bytes([state[-1]] + list(state[:-1]))

# --- MAIN ENCRYPTION & DECRYPTION LOOPS ---

def aes_encrypt(plaintext, key, rounds):
    state = plaintext.encode('utf-8')
    for _ in range(rounds):
        state = add_round_key(state, key)
        state = sub_bytes(state, AES_S_BOX)
        state = shift_rows_permutation(state)
    return state

def aes_decrypt(ciphertext_bytes, key, rounds):
    state = ciphertext_bytes
    for _ in range(rounds):
        # Operations run in strict reverse structural order during decryption
        state = inv_shift_rows_permutation(state)
        state = sub_bytes(state, AES_INV_S_BOX)
        state = add_round_key(state, key)
    return state.decode('utf-8', errors='ignore')

# Execution
msg = input("Enter your secure message: ")
key = input("Enter your custom secret key: ")
rounds = int(input("Enter simulation rounds (e.g., 5): "))

encrypted_bytes = aes_encrypt(msg, key, rounds)
print(f"\n[Encrypted] Ciphertext Hex: {encrypted_bytes.hex()}")

decrypted_string = aes_decrypt(encrypted_bytes, key, rounds)
print(f"[Decrypted] Restored Plaintext: {decrypted_string}")