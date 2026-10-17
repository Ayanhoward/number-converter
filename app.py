import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Supernova Architecture Converter", page_icon="🌌", layout="wide"
)

# Immersive Cosmic Supernova & RGB Neon CSS Styling
st.markdown(
    """
    <style>
    /* Cosmic Deep Space Background */
    .stApp {
        background: radial-gradient(circle at 50% 20%, #1e1b4b 0%, #090d16 60%, #030712 100%);
        color: #f8fafc;
    }
    
    /* Global Typography Fix */
    h1, h2, h3, h4, h5, h6, p, label, span {
        color: #f8fafc !important;
    }
    
    /* Animated RGB Rainbow Header Title */
    @keyframes rgb-shine {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .main-title {
        font-size: 2.3rem;
        font-weight: 800;
        background: linear-gradient(270deg, #38bdf8, #818cf8, #c084fc, #ec4899, #38bdf8);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: rgb-shine 8s ease infinite;
        margin-bottom: 0rem;
        text-shadow: 0 0 30px rgba(192, 132, 252, 0.3);
    }
    
    .subtitle {
        font-size: 1.05rem;
        color: #94a3b8 !important;
        margin-bottom: 1.8rem;
        letter-spacing: 0.05em;
    }
    
    /* Supernova Pulsing RGB Border Animation for Output Cards */
    @keyframes supernova-glow {
        0% { 
            border-color: #38bdf8; 
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.3), inset 0 0 10px rgba(56, 189, 248, 0.1); 
        }
        33% { 
            border-color: #c084fc; 
            box-shadow: 0 0 20px rgba(192, 132, 252, 0.4), inset 0 0 12px rgba(192, 132, 252, 0.15); 
        }
        66% { 
            border-color: #ec4899; 
            box-shadow: 0 0 20px rgba(236, 72, 153, 0.4), inset 0 0 12px rgba(236, 72, 153, 0.15); 
        }
        100% { 
            border-color: #38bdf8; 
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.3), inset 0 0 10px rgba(56, 189, 248, 0.1); 
        }
    }
    
    .supernova-card {
        background: linear-gradient(135deg, rgba(30, 27, 75, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 2px solid #38bdf8;
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 14px;
        backdrop-filter: blur(10px);
        animation: supernova-glow 6s infinite ease-in-out;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .supernova-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 30px rgba(236, 72, 153, 0.6);
    }
    
    .metric-title {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #38bdf8 !important;
        font-weight: 700;
        margin-bottom: 6px;
    }
    
    .metric-value {
        font-size: 1.3rem;
        font-family: monospace;
        color: #ffffff !important;
        font-weight: bold;
        word-break: break-all;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
    }
    
    /* Input Container Styling */
    .input-panel {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(56, 189, 248, 0.3);
        padding: 24px;
        border-radius: 16px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# App Header
st.markdown(
    '<p class="main-title">🌌 Supernova Architecture & Organization</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="subtitle">Advanced Number System & Data Representation Converter</p>',
    unsafe_allow_html=True,
)

# Layout Setup
col_left, col_right = st.columns([1.1, 1.1], gap="large")

with col_left:
    st.markdown('<div class="input-panel">', unsafe_allow_html=True)
    st.markdown("### ⚙️ Conversion Parameters")
    input_base = st.selectbox(
        "Select Input Base", ["Decimal", "Binary", "Hexadecimal", "Octal"]
    )
    bit_width = st.selectbox(
        "Bit Width (Word Size)", ["8-bit", "16-bit", "32-bit"]
    )
    raw_value = st.text_input("Enter Value:", value="255")
    st.markdown("</div>", unsafe_allow_html=True)

# Conversion Core Logic
bits = int(bit_width.split("-")[0])
max_val = (2**bits) - 1
signed_max = (2 ** (bits - 1)) - 1
signed_min = -(2 ** (bits - 1))

error_flag = False
decimal_value = 0

if raw_value.strip() == "":
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
        error_flag = True

with col_right:
    st.markdown("### 📊 Converted Outputs")

    if error_flag:
        st.warning(
            f"⚠️ Please enter a valid value for **{input_base}** format."
        )
    else:
        binary_str = bin(decimal_value & max_val)[2:].zfill(bits)
        hex_str = hex(decimal_value & max_val)[2:].upper()
        oct_str = oct(decimal_value & max_val)[2:]

        if decimal_value < 0:
            twos_comp = bin(
                (decimal_value + (1 << bits)) & max_val
            )[2:].zfill(bits)
        else:
            twos_comp = bin(decimal_value & max_val)[2:].zfill(bits)

        # Output Cards with Glowing Supernova RGB Animation
        sub_c1, sub_c2 = st.columns(2)

        with sub_c1:
            st.markdown(
                f"""
            <div class="supernova-card">
                <div class="metric-title">Decimal (Base 10)</div>
                <div class="metric-value">{decimal_value}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                f"""
            <div class="supernova-card">
                <div class="metric-title">Hexadecimal</div>
                <div class="metric-value">0x{hex_str}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with sub_c2:
            st.markdown(
                f"""
            <div class="supernova-card">
                <div class="metric-title">Binary ({bit_width})</div>
                <div class="metric-value">{binary_str}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                f"""
            <div class="supernova-card">
                <div class="metric-title">Octal (Base 8)</div>
                <div class="metric-value">0o{oct_str}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
        <div class="supernova-card">
            <div class="metric-title">Signed 2's Complement ({bit_width})</div>
            <div class="metric-value">{twos_comp}</div>
            <p style="font-size: 0.75rem; color: #a5b4fc; margin-top: 6px; margin-bottom: 0;">
                Valid Range: {signed_min} to {signed_max}
            </p>
        </div>
        """,
                unsafe_allow_html=True,
            )