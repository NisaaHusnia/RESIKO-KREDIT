
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import base64

from streamlit_option_menu import option_menu

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Risk Scoring Koperasi",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# LOAD BACKGROUND IMAGE
# =====================================================
def get_base64(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_img = get_base64("bg 2.png")

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown(f"""
<style>

/* =====================================================
BACKGROUND
===================================================== */
.stApp {{

    background-image:
        linear-gradient(
            rgba(5,15,40,0.25),
            rgba(5,15,40,0.35)
        ),
        url("data:image/png;base64,{bg_img}");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* =====================================================
HIDE STREAMLIT
===================================================== */
header {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

/* =====================================================
SIDEBAR
===================================================== */
section[data-testid="stSidebar"] {{

    background: rgba(255,255,255,0.92);
    backdrop-filter: blur(15px);
    border-right: 1px solid rgba(0,0,0,0.08);
}}

/* =====================================================
SIDEBAR TEXT
===================================================== */
section[data-testid="stSidebar"] * {{
    color: #1F2937 !important;
}}

/* =====================================================
OPTION MENU
===================================================== */
.nav-link {{

    font-size: 18px !important;
    border-radius: 14px !important;
    margin-bottom: 10px !important;
    padding: 12px !important;
    background-color: rgba(0,0,0,0.04);
    transition: 0.3s;
}}

.nav-link:hover {{
    transform: translateX(3px);
    background-color: rgba(0,0,0,0.08);
}}

/* =====================================================
ACTIVE MENU
===================================================== */
.nav-link-selected {{

    background: linear-gradient(
        90deg,
        #FF416C,
        #FF4B2B
    ) !important;

    color: white !important;
    font-weight: bold;
    box-shadow:
        0px 0px 15px rgba(255,75,43,0.4);
}}

/* =====================================================
TITLE
===================================================== */
h1, h2, h3, h4 {{

    color: white !important;
    font-weight: 700 !important;
}}

/* =====================================================
TEXT
===================================================== */
p {{
    color: #E5E7EB;
}}

/* =====================================================
INPUT
===================================================== */
.stNumberInput input {{

    background-color: rgba(255,255,255,0.08);
    color: white;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.2);
}}

/* =====================================================
SELECTBOX
===================================================== */
.stSelectbox div[data-baseweb="select"] {{

    background-color: rgba(255,255,255,0.08);
    border-radius: 10px;
}}

/* =====================================================
BUTTON
===================================================== */
.stButton>button {{

    background: linear-gradient(
        90deg,
        #4F46E5,
        #2563EB
    );

    color: white;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    padding: 12px 25px;
}}

.stButton>button:hover {{

    transform: scale(1.03);

    box-shadow:
        0px 0px 20px rgba(79,70,229,0.5);
}}

/* =====================================================
DATAFRAME
===================================================== */
[data-testid="stDataFrame"] {{

    background: rgba(255,255,255,0.05);

    border-radius: 15px;

    border: 1px solid rgba(255,255,255,0.1);

    overflow: hidden;
}}

/* =====================================================
CHART CONTAINER
===================================================== */
.element-container:has(canvas) {{

    background: rgba(255,255,255,0.05);

    padding: 20px;

    border-radius: 20px;

    border: 1px solid rgba(255,255,255,0.1);
}}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD MODEL
# =====================================================
kmeans = joblib.load('model/kmeans_model.pkl')
rf_model = joblib.load('model/random_forest_model.pkl')
scaler = joblib.load('model/scaler.pkl')

# =====================================================
# LOAD DATA
# =====================================================
df = pd.read_excel('data/data_hasil_kmeans.xlsx')

# =====================================================
# SIDEBAR MENU
# =====================================================
with st.sidebar:

    st.markdown("## 📋 Menu")

    menu = option_menu(
        menu_title=None,
        options=[
            "Dashboard",
            "Prediksi Risiko",
            "Data Nasabah"
        ],
        icons=[
            "speedometer2",
            "search",
            "table"
        ],
        default_index=0
    )

# =====================================================
# DASHBOARD
# =====================================================
if menu == "Dashboard":

    st.markdown("""
    <h1 style='
        font-size:60px;
        color:white;
        font-weight:800;
        margin-bottom:10px;
    '>
    📈 Dashboard Risiko Kredit
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style='
        font-size:22px;
        color:#E5E7EB;
        margin-bottom:30px;
    '>
    Sistem penilaian risiko kredit koperasi menggunakan metode
    Hybrid K-Means dan Random Forest
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # METRIC
    # =====================================================
    total_nasabah = len(df)

    risiko_rendah = len(df[df['Risiko'] == 'Rendah'])
    risiko_sedang = len(df[df['Risiko'] == 'Sedang'])
    risiko_tinggi = len(df[df['Risiko'] == 'Tinggi'])

# =====================================================
# PREMIUM GLASSMORPHISM CARD
# =====================================================

card_style = """
background: rgba(15,23,42,0.55);
backdrop-filter: blur(20px);
-webkit-backdrop-filter: blur(20px);

padding:25px;
border-radius:28px;

height:180px;

box-shadow:
0 10px 30px rgba(0,0,0,0.35);

text-align:center;
"""

col1, col2, col3, col4 = st.columns(4)

# =====================================================
# TOTAL NASABAH
# =====================================================

with col1:

st.markdown(f"""
<div style="
{card_style}
border:1px solid rgba(96,165,250,0.45);
">
<div style="
color:#93C5FD;
font-size:20px;
font-weight:700;
">
👥 Total Nasabah
</div>

<div style="
color:white;
font-size:60px;
font-weight:900;
margin-top:18px;
">
{total_nasabah}
</div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# RISIKO RENDAH
# =====================================================

with col2:

st.markdown(f"""
<div style="
{card_style}
border:1px solid rgba(74,222,128,0.45);
">
<div style="
color:#4ADE80;
font-size:20px;
font-weight:700;
">
🟢 Risiko Rendah
</div>

<div style="
color:white;
font-size:60px;
font-weight:900;
margin-top:18px;
">
{risiko_rendah}
</div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# RISIKO SEDANG
# =====================================================

with col3:

st.markdown(f"""
<div style="
{card_style}
border:1px solid rgba(250,204,21,0.45);
">
<div style="
color:#FACC15;
font-size:20px;
font-weight:700;
">
🟡 Risiko Sedang
</div>

<div style="
color:white;
font-size:60px;
font-weight:900;
margin-top:18px;
">
{risiko_sedang}
</div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# RISIKO TINGGI
# =====================================================

with col4:

st.markdown(f"""
<div style="
{card_style}
border:1px solid rgba(248,113,113,0.45);
">
<div style="
color:#F87171;
font-size:20px;
font-weight:700;
">
🔴 Risiko Tinggi
</div>

<div style="
color:white;
font-size:60px;
font-weight:900;
margin-top:18px;
">
{risiko_tinggi}
</div>
</div>
""", unsafe_allow_html=True)


# =====================================================
# DATA NASABAH
# =====================================================
elif menu == "Data Nasabah":

    st.markdown("""
    <h1 style='font-size:45px;'>
    📋 Data Nasabah
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size:18px; color:#E5E7EB;'>
    Data hasil clustering dan klasifikasi risiko kredit nasabah.
    </p>
    """, unsafe_allow_html=True)

    st.divider()

    selected_risk = st.selectbox(
        "Filter Risiko",
        ['Semua', 'Rendah', 'Sedang', 'Tinggi']
    )

    if selected_risk != 'Semua':

        filtered_df = df[df['Risiko'] == selected_risk]

        st.dataframe(filtered_df)

    else:

        st.dataframe(df)

    st.write("Jumlah Data :", len(df))

