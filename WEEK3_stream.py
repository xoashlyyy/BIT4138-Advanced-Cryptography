import time

# --- 1. LFSR Generator Implementation ---
def lfsr(seed, taps, length):
    state = seed
    out = ""
    for _ in range(length):
        out += str(state & 1)
        feedback = sum((state >> t) & 1 for t in taps) % 2
        state = (state >> 1) | (feedback << 3)
    return out

# --- 2. RC4 Stream Cipher Simulation ---
def rc4(key, text):
    # Key Scheduling Algorithm (KSA)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    # Pseudo-Random Generation & Encryption (PRGA)
    i = j = 0
    res = []
    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        res.append(char ^ K)
    return bytes(res)

print("--- BIT4138 Lab Week 3: Stream Ciphers ---")

# Pseudorandom Sequence Generation
seq = lfsr(0b1011, [0, 2], 20)
print(f"Pseudorandom Sequence Output: {seq}")

# Statistical Randomness Testing (Monobit Test)
ones, zeros = seq.count('1'), seq.count('0')
passed = abs(ones - zeros) <= 4
print(f"Statistical Test (Monobit): 1s={ones}, 0s={zeros} -> Randomness Passed: {passed}")

# RC4 Performance Results
key = b"SECRET"
data = b"DEFEND THE NETWORK"

start_time = time.time()
encrypted = rc4(key, data)
end_time = time.time()

print(f"\nRC4 Encrypted (Hex): {encrypted.hex()}")
print(f"RC4 Decrypted: {rc4(key, encrypted).decode()}")
print(f"Encryption Performance Time: {(end_time - start_time):.6f} seconds")