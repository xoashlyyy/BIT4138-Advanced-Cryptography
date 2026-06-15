import streamlit as st
import random

st.set_page_config(page_title="Advanced SPN Simulator", layout="centered")

st.title("🔒 Advanced Multi-Round SPN Simulator")
st.write("This graphical dashboard demonstrates confusion, diffusion, and the avalanche effect.")

# Core Logic
random_gen = random.Random(101)
S_BOX = list(range(256))
random_gen.shuffle(S_BOX)

def key_mixing(data, key):
    key_bytes = key.encode('utf-8')
    return bytes([data[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(data))])

def substitution_layer(data):
    return bytes([S_BOX[b] for b in data])

def permutation_layer(data):
    return data[::-1]

def run_spn(plaintext, key, total_rounds):
    current_block = plaintext.encode('utf-8')
    for r in range(total_rounds):
        current_block = key_mixing(current_block, key)
        current_block = substitution_layer(current_block)
        current_block = permutation_layer(current_block)
    return current_block

# Graphical Inputs
user_plaintext1 = st.text_input("Main Plaintext Message:", "ASHLEY")
user_plaintext2 = st.text_input("Test Plaintext (1 character changed):", "FSHLEY")
user_key = st.text_input("Custom Secret Key:", "MYSECRETKEY")
num_rounds = st.slider("Number of Security Rounds:", min_value=1, max_value=10, value=4)

if st.button("Run SPN & Analyze Avalanche"):
    if user_plaintext1 and user_plaintext2 and user_key:
        cipher1 = run_spn(user_plaintext1, user_key, num_rounds)
        cipher2 = run_spn(user_plaintext2, user_key, num_rounds)
        
        # Display Outputs in beautiful UI blocks
        st.subheader("🔑 Generated Ciphertexts")
        st.code(f"Ciphertext 1 (Hex): {cipher1.hex()}")
        st.code(f"Ciphertext 2 (Hex): {cipher2.hex()}")
        
        # Avalanche calculation
        differences = sum(1 for b1, b2 in zip(cipher1, cipher2) if b1 != b2)
        
        st.subheader("📊 Avalanche Effect Analysis")
        st.warning(f"Changing exactly 1 character disrupted **{differences}** out of **{len(cipher1)}** bytes in the final output block.")