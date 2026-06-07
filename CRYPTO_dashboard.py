import streamlit as st
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as sym_padding

st.set_page_config(page_title="Crypto Vault", layout="wide")
st.title("🔒 The All-in-One Crypto Vault")
st.write("Interactive Cryptography Portfolio")

cipher_choice = st.sidebar.selectbox("Select a Cipher Algorithm", ["Caesar Cipher (Classical)", "AES-256 (Block Cipher)", "RSA (Asymmetric)"])
user_message = st.text_input("Enter your secret message:", "DEFEND THE NETWORK")

if cipher_choice == "Caesar Cipher (Classical)":
    st.subheader("Caesar Cipher Simulation")
    shift = st.slider("Select Shift Key", 1, 25, 3)
    if st.button("Encrypt"):
        result = "".join(
            chr((ord(char) - (65 if char.isupper() else 97) + shift) % 26 + (65 if char.isupper() else 97)) 
            if char.isalpha() else char for char in user_message
        )
        st.success(f"**Encrypted Text:** {result}")

elif cipher_choice == "AES-256 (Block Cipher)":
    st.subheader("Advanced Encryption Standard (AES-256 CBC)")
    if st.button("Encrypt"):
        key = os.urandom(32)
        iv = os.urandom(16)
        padder = sym_padding.PKCS7(128).padder()
        padded_data = padder.update(user_message.encode()) + padder.finalize()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        st.write(f"**Generated AES Key (Hex):** `{key.hex()}`")
        st.success(f"**Encrypted Ciphertext (Hex):** `{ciphertext.hex()}`")

elif cipher_choice == "RSA (Asymmetric)":
    st.subheader("RSA Public-Key Encryption")
    if st.button("Generate Keys & Encrypt"):
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()
        
        ciphertext = public_key.encrypt(
            user_message.encode(),
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
        st.success(f"**RSA Ciphertext (Hex):** `{ciphertext.hex()[:100]}...`")
        st.info("Notice how much longer the asymmetric ciphertext is compared to the original message.")