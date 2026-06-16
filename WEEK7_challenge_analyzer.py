import streamlit as st
import pandas as pd
from collections import Counter

st.set_page_config(page_title="Cipher Security Analyzer", layout="wide")

st.title(" Block Cipher Security Analyzer")
st.write("Challenge Task: Visual cryptanalysis, Avalanche Effect testing, and report exportation.")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.header("Input Parameters")
    text_original = st.text_input("Original Plaintext/Ciphertext:", "CLASSIFIED DATA")
    text_modified = st.text_input("Modified Text (Change 1 letter):", "CLASSIFIED DATS")
    
with col2:
    st.header("Frequency Distribution")
    if text_original:
        # Generate Frequency DataFrame
        counts = Counter(text_original)
        df_freq = pd.DataFrame(counts.items(), columns=['Character', 'Frequency']).set_index('Character')
        st.bar_chart(df_freq)

st.divider()

# --- Analysis Engine ---
if text_original and text_modified:
    st.header("Avalanche Effect & Difference Analysis")
    
    # Binary Conversion for Avalanche Testing
    bin1 = ''.join(format(ord(c), '08b') for c in text_original)
    bin2 = ''.join(format(ord(c), '08b') for c in text_modified)
    
    max_len = max(len(bin1), len(bin2))
    bin1, bin2 = bin1.zfill(max_len), bin2.zfill(max_len)
    
    diff_count = sum(1 for b1, b2 in zip(bin1, bin2) if b1 != b2)
    avalanche_percent = (diff_count / max_len) * 100 if max_len > 0 else 0
    
    col3, col4 = st.columns(2)
    with col3:
        st.metric(label="Bits Flipped (Avalanche)", value=f"{diff_count} bits", delta=f"{avalanche_percent:.2f}% shift")
    with col4:
        if avalanche_percent < 30:
            st.error(" Failed Avalanche Test: Low diffusion detected.")
        else:
            st.success(" Passed Avalanche Test: Strong cryptographic diffusion.")

    # --- Bonus Feature: Export Results ---
    st.subheader("Export Statistical Report")
    
    # Create a summary dictionary to export
    report_data = {
        "Metric": ["Original Length", "Modified Length", "Total Bits", "Bits Flipped", "Avalanche Percentage"],
        "Value": [len(text_original), len(text_modified), max_len, diff_count, f"{avalanche_percent:.2f}%"]
    }
    df_report = pd.DataFrame(report_data)
    
    st.dataframe(df_report, use_container_width=True)
    
    # Convert dataframe to CSV for the download button
    csv_data = df_report.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label=" Download Security Report (CSV)",
        data=csv_data,
        file_name="cryptanalysis_report.csv",
        mime="text/csv",
    )