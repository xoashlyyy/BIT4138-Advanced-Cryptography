print("--- BIT4138 Lab Week 6: Substitution-Permutation Network (SPN) ---")

# 1. Simple S-Box Mapping (Substitution)
S_BOX = {
    'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T', 'F': 'Y', 
    'G': 'U', 'H': 'I', 'I': 'O', 'J': 'P', 'K': 'A', 'L': 'S', 
    'M': 'D', 'N': 'F', 'O': 'G', 'P': 'H', 'Q': 'J', 'R': 'K', 
    'S': 'L', 'T': 'Z', 'U': 'X', 'V': 'C', 'W': 'V', 'X': 'B', 
    'Y': 'N', 'Z': 'M', ' ': '_'
}

# 2. Simple P-Box Mapping (Permutation/Transposition)

def apply_permutation(text):
    # Reverse the text block as a simple permutation step
    return text[::-1]

# Main execution flow
plaintext = input("Enter uppercase plaintext to encrypt: ").upper()

#  Substitution Layer
substituted_text = "".join(S_BOX.get(char, char) for char in plaintext)

#  Permutation Layer
ciphertext = apply_permutation(substituted_text)

print(f"\n[1] Original Plaintext: {plaintext}")
print(f"[2] After Substitution Layer (Confusion): {substituted_text}")
print(f"[3] After Permutation Layer (Diffusion): {ciphertext}")