class LFSR:
    def __init__(self, seed, taps):
        self.state = seed
        self.taps = taps

    def step(self):
        # Calculate feedback bit using XOR logic on tap positions
        feedback = 0
        for tap in self.taps:
            feedback ^= (self.state >> tap) & 1
        
        # Output the rightmost bit
        output_bit = self.state & 1
        
        # Shift state right and prepend feedback bit
        self.state = (self.state >> 1) | (feedback << 3)
        return output_bit

# --- Run 4-bit LFSR simulation with Seed State 0b1011 ---
lfsr = LFSR(seed=0b1011, taps=[0, 2])
print("--- BIT4138 Lab Week 2: LFSR Keystream Generation ---")
print("Initial Seed Verified: 1011\n")

generated_bits = []
print("State Transitions:")
for i in range(10):
    current_state = bin(lfsr.state)[2:].zfill(4)
    bit = lfsr.step()
    generated_bits.append(bit)
    print(f"Cycle {i+1}: State = {current_state} -> Output Bit = {bit}")

print(f"\nFinal Generated Keystream Sequence: {''.join(map(str, generated_bits))}")