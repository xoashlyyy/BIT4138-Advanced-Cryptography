def string_to_binary(text):
    """Converts a string to a continuous binary sequence."""
    return ''.join(format(ord(c), '08b') for c in text)

def calculate_xor_difference(bin1, bin2):
    """Calculates the bitwise XOR difference between two binary strings."""
    # Ensure equal length for comparison by padding with zeros
    max_len = max(len(bin1), len(bin2))
    b1 = bin1.zfill(max_len)
    b2 = bin2.zfill(max_len)
    
    # Calculate flipped bits and generate the XOR string
    diff_count = sum(1 for bit1, bit2 in zip(b1, b2) if bit1 != bit2)
    diff_string = ''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(b1, b2))
    
    return diff_string, diff_count, max_len

def run_differential_simulation():
    print("--- BIT4138 Practical Task 1: Differential Cryptanalysis Simulation ---\n")
    
    # 1. Accept two plaintext inputs
    plaintext1 = input("Enter Plaintext 1 (Original): ")
    plaintext2 = input("Enter Plaintext 2 (Modified): ")
    
    print("\n" + "="*50)
    print(" PROCESSING DATA...")
    print("="*50)
    
    bin1 = string_to_binary(plaintext1)
    bin2 = string_to_binary(plaintext2)
    
    print(f"Input 1 (Binary): {bin1}")
    print(f"Input 2 (Binary): {bin2}")
    
    # 2. Compute differences
    diff_string, diff_count, total_bits = calculate_xor_difference(bin1, bin2)
    diff_percentage = (diff_count / total_bits) * 100 if total_bits > 0 else 0
    
    # 3. Display observations
    print("\n" + "="*50)
    print(" DIFFERENTIAL OBSERVATIONS & ANALYSIS")
    print("="*50)
    print(f"XOR Difference Map: {diff_string}")
    print(f"Total Bits Flipped: {diff_count} out of {total_bits} bits")
    print(f"Difference Rate   : {diff_percentage:.2f}%\n")
    
    print("Conclusion:")
    if diff_percentage == 0:
        print("[-] Inputs are identical. No differential mapping to track.")
    elif diff_percentage < 30:
        print("[-] Weak differential separation. Inputs share too many structural similarities.")
    else:
        print("[+] Strong differential variance. Differences propagated widely across the bit structure.")

if __name__ == "__main__":
    run_differential_simulation()