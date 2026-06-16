import collections

print("--- BIT4138 Advanced Task: Mini Cryptanalysis Toolkit ---\n")

def run_toolkit(text1, text2):
    # 1. Calculate Input Differences
    print("[+] 1. Input Difference Analysis")
    # Pad strings to equal length for comparison
    max_len = max(len(text1), len(text2))
    t1_pad, t2_pad = text1.ljust(max_len), text2.ljust(max_len)
    
    diff_count = sum(1 for a, b in zip(t1_pad, t2_pad) if a != b)
    print(f"Original: {t1_pad}")
    print(f"Modified: {t2_pad}")
    print(f"Total Character Differences: {diff_count} out of {max_len}")

    # 2. Frequency Analysis
    print("\n[+] 2. Frequency Analysis (Original Text)")
    freq = collections.Counter(text1)
    for char, count in sorted(freq.items()):
        print(f"  Character '{char}': Occurs {count} times")

    # 3. Measure Statistical Bias
    print("\n[+] 3. Statistical Bias Measurement")
    if len(text1) > 0:
        expected_freq = len(text1) / len(set(text1))
        # Variance formula to measure how far the text deviates from random distribution
        bias_variance = sum((count - expected_freq)**2 for count in freq.values()) / len(freq)
        print(f"Expected uniform frequency: {expected_freq:.2f}")
        print(f"Calculated Bias Variance: {bias_variance:.2f}")
        if bias_variance > 2.0:
            print(" Warning: High statistical bias detected. Vulnerable to frequency analysis.")
        else:
            print(" Good: Low statistical bias. Characters are uniformly distributed.")

# Automatic Execution
user_t1 = input("Enter Original Plaintext: ")
user_t2 = input("Enter Modified Plaintext: ")

print("\nProcessing...\n" + "-"*40)
run_toolkit(user_t1, user_t2)
print("-" * 40)