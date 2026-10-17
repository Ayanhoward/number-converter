import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Computer Architecture Number Converter",
    page_icon="💻",
    layout="centered",
)

# Professional CSS Styling with High Contrast
st.markdown(
    """
    <style>
    /* Main Background & Text Color */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    
    /* Header Styling */
    h1, h2, h3, h4, h5, h6, p, label, span {
        color: #f8fafc !important;
    }
    
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #38bdf8 !important;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    
    .subtitle {
        font-size: 1.1rem;
        color: #94a3b8 !important;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Card Container */
    .metric-card {
        background-color: #1e293b;
        border: 1px solid #334155;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .metric-title {
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #38bdf8 !important;
        font-weight: 600;
        margin-bottom: 5px;
    }
    
    .metric-value {
        font-size: 1.4rem;
        font-family: monospace;
        color: #ffffff !important;
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# App Header
st.markdown(
    '<p class="main-title">💻 Architecture & Organization</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="subtitle">Number System & Data Representation Converter</p>',
    unsafe_allow_html=True,
)

# Input Section in a Clean Form Layout
with st.container():
    st.markdown("### ⚙️ Conversion Parameters")
    col1, col2 = st.columns(2)

    with col1:
        input_base = st.selectbox(
            "Select Input Base", ["Decimal", "Binary", "Hexadecimal", "Octal"]
        )

    with col2:
        bit_width = st.selectbox(
            "Bit Width (Word Size)", ["8-bit", "16-bit", "32-bit"]
        )

    raw_value = st.text_input("Enter Value:", value="12")

# Processing and Conversion Logic
bits = int(bit_width.split("-")[0])
max_val = (2**bits) - 1
signed_max = (2 ** (bits - 1)) - 1
signed_min = -(2 ** (bits - 1))

error_flag = False
decimal_value = 0

if raw_value.strip() == "":
    st.warning("⚠️ Please enter a value to convert.")
    error_flag = True
else:
    try:
        if input_base == "Decimal":
            decimal_value = int(raw_value)
        elif input_base == "Binary":
            decimal_value = int(raw_value, 2)
        elif input_base == "Hexadecimal":
            decimal_value = int(raw_value, 16)
        elif input_base == "Octal":
            decimal_value = int(raw_value, 8)
    except ValueError:
        st.error(
            f"❌ Invalid characters entered for **{input_base}** base format."
        )
        error_flag = True

if not error_flag:
    # Range check for unsigned/standard view
    binary_str = bin(decimal_value & max_val)[2:].zfill(bits)
    hex_str = hex(decimal_value & max_val)[2:].upper()
    oct_str = oct(decimal_value & max_val)[2:]

    # 2's Complement representation for signed values
    if decimal_value < 0:
        twos_comp = bin((decimal_value + (1 << bits)) & max_val)[2:].zfill(bits)
    else:
        twos_comp = bin(decimal_value & max_val)[2:].zfill(bits)

    st.markdown("---")
    st.markdown("### 📊 Converted Outputs")

    # Display Results in Responsive Cards
    r_col1, r_col2 = st.columns(2)

    with r_col1:
        st.markdown(
            f"""
        <div class="metric-card">
            <div class="metric-title">Decimal (Base 10)</div>
            <div class="metric-value">{decimal_value}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
        <div class="metric-card">
            <div class="metric-title">Hexadecimal (Base 16)</div>
            <div class="metric-value">0x{hex_str}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with r_col2:
        st.markdown(
            f"""
        <div class="metric-card">
            <div class="metric-title">Binary (Base 2 - {bit_width})</div>
            <div class="metric-value">{binary_str}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
        <div class="metric-card">
            <div class="metric-title">Octal (Base 8)</div>
            <div class="metric-value">0o{oct_str}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # Signed 2's Complement Card Section
    st.markdown(
        f"""
    <div class="metric-card">
        <div class="metric-title">Signed 2's Complement Representation ({bit_width})</div>
        <div class="metric-value">{twos_comp}</div>
        <p style="font-size: 0.8rem; color: #94a3b8; margin-top: 8px; margin-bottom: 0;">
            Valid Range for {bit_width}: {signed_min} to {signed_max}
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )