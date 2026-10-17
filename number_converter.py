import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Computer Architecture Converter",
    page_icon="💻",
    layout="centered"
)

# --- CUSTOM CSS STYLING ---
st.markdown("""
    <style>
    /* Main background and font styling */
    .stApp {
        background-color: #f4f6f9;
        font-family: 'Arial', sans-serif;
    }
    
    /* Header title style */
    h1 {
        color: #2c3e50;
        text-align: center;
        font-weight: 700;
        padding-bottom: 10px;
    }

    /* Container Card Style */
    div.block-container {
        padding-top: 2rem;
    }
    
    /* Custom button style */
    .stButton>button {
        background-color: #2980b9;
        color: white;
        font-size: 16px;
        font-weight: bold;
        width: 100%;
        border-radius: 8px;
        border: none;
        padding: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #1f618d;
        color: #ffffff;
    }

    /* Result metric card styles */
    .metric-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 10px;
        border-left: 5px solid #2980b9;
    }
    
    .twos-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 10px;
        border-left: 5px solid #c0392b;
    }
    </style>
""", unsafe_allow_html=True)

# --- APP UI CONTENT ---
st.title("💻 Architecture & Organization")
st.subheader("Number System & Data Representation Converter")
st.write("Convert values across bases and analyze computer word sizes and signed 2's complement representations.")

st.markdown("---")

# Layout columns for inputs
col1, col2 = st.columns(2)

with col1:
    base_type = st.selectbox(
        "Select Input Base",
        ["Decimal", "Binary", "Hexadecimal", "Octal"]
    )
    bit_str = st.selectbox(
        "Bit Width (Word Size)",
        ["8-bit", "16-bit", "32-bit"]
    )
    bits = int(bit_str.split("-")[0])

with col2:
    raw_input = st.text_input("Enter Value:", value="12")

st.markdown("<br>", unsafe_allow_html=True)

# Conversion Execution on Button Click
if st.button("Convert Representation"):
    if not raw_input.strip():
        st.error("Input field cannot be empty!")
    else:
        try:
            # Parse input based on selected base
            if base_type == "Decimal":
                dec_val = int(raw_input, 10)
            elif base_type == "Binary":
                dec_val = int(raw_input, 2)
            elif base_type == "Hexadecimal":
                dec_val = int(raw_input, 16)
            elif base_type == "Octal":
                dec_val = int(raw_input, 8)

            # Range checks
            max_val = (2 ** (bits - 1)) - 1
            min_val = -(2 ** (bits - 1))
            
            bin_val = bin(dec_val & 0xFFFFFFFF)[2:]
            hex_val = hex(dec_val).upper()
            oct_val = oct(dec_val)

            # 2's Complement Logic
            if dec_val < min_val or dec_val > (2**bits - 1):
                twos_comp_str = f"Out of range for {bits}-bit integer!"
            else:
                if dec_val < 0:
                    twos_val = (1 << bits) + dec_val
                else:
                    twos_val = dec_val
                twos_comp_str = f"{twos_val:0{bits}b}"

            # Display Results using stylized HTML cards
            st.markdown("### 📊 Converted Outputs")
            
            st.markdown(f'<div class="metric-card"><b>Decimal (Base 10):</b> {dec_val}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-card"><b>Binary (Base 2):</b> {bin_val}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-card"><b>Hexadecimal (Base 16):</b> {hex_val}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-card"><b>Octal (Base 8):</b> {oct_val}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="twos-card"><b style="color: #c0392b;">2\'s Complement ({bits}-bit signed):</b> {twos_comp_str}</div>', unsafe_allow_html=True)

        except ValueError:
            st.error(f"The value '{raw_input}' is invalid for base {base_type}.")