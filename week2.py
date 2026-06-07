def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def vigenere_cipher(text, key, encrypt=True):
    result = ""
    key = key.upper()
    key_idx = 0
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_idx % len(key)]) - ord('A')
            if not encrypt:
                shift = -shift
            result += chr((ord(char) - start + shift) % 26 + start)
            key_idx += 1
        else:
            result += char
    return result

gitint("---  Lab Week 2: Cipher Analysis ---")

# User Input Validation 
user_message = input("Enter a message to encrypt (letters and spaces only): ")
if not all(x.isalpha() or x.isspace() for x in user_message):
    print("Error: Invalid input. Please use letters only.")
else:
    print("Input validated successfully!\n")
    
    caesar_shift = 3
    vigenere_key = "SECRET"

    # Caesar Execution
    caesar_enc = caesar_cipher(user_message, caesar_shift)
    print(f"[Caesar Cipher (Shift {caesar_shift})]")
    print(f"Encrypted: {caesar_enc}")
    print(f"Decrypted: {caesar_cipher(caesar_enc, -caesar_shift)}\n")

    # Vigenère Execution
    vigenere_enc = vigenere_cipher(user_message, vigenere_key, encrypt=True)
    print(f"[Vigenère Cipher (Key: {vigenere_key})]")
    print(f"Encrypted: {vigenere_enc}")
    print(f"Decrypted: {vigenere_cipher(vigenere_enc, vigenere_key, encrypt=False)}")