
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import base64
import streamlit.components.v1 as components

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

bg_img = get_base64("bg3.png")
dashboard_img = get_base64("assets/dashboard.png")
icon_prediksi = get_base64("assets/chart.png")
database_icon = get_base64("assets/database.png")

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown(f"""
<style>
.menu-icon{{
    width:30px;
    height:30px;
    vertical-align:middle;
    margin-right:10px;
}}
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Poppins:wght@300;400;500&display=swap'); {{
    font-family: 'Montserrat'Poppins', sans-serif;
}}
table {{
    width:100%;
    border-collapse:collapse;
    overflow:hidden;
    border-radius:15px;
}}

thead tr{{
    background:#1D4ED8;
}}

thead th{{
    color:white;
    padding:12px;
    text-align:center;
}}

tbody td{{
    padding:12px;
    text-align:center;
    color:white;
    background:rgba(255,255,255,0.04);
}}

tbody tr:hover{{
    background:rgba(59,130,246,0.12);
}}
            
/* DATA NASABAH */

[data-testid="stDataFrame"]{{
    background:transparent !important;
    border:none !important;
}}

[data-testid="stDataFrame"] div{{
    color:white !important;
}}

.stSelectbox div[data-baseweb="select"]{{
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:14px;
}}

.stTextInput input{{
    color: black !important;
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 14px !important;
    backdrop-filter: blur(15px);
    box-shadow: 0 0 15px rgba(59,130,246,0.08);
}}

.stTextInput input::placeholder{{
    color: rgba(255,255,255,0.45) !important;
}}
                
table td{{
    padding:15px;
    text-align:center;
    color:white;
    border-bottom:1px solid rgba(255,255,255,0.05);
}}

table tr:hover{{
    background:rgba(59,130,246,0.05);
}}
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

    background: rgba(8,15,35,0.90);

    backdrop-filter: blur(20px);

    border-right: 1px solid rgba(255,255,255,0.08);

    box-shadow:
    5px 0px 25px rgba(0,0,0,0.35);
}}

/* =====================================================
SIDEBAR TEXT
===================================================== */
section[data-testid="stSidebar"] * {{
    color: #F8FAFC !important;
}}

/* =====================================================
OPTION MENU
===================================================== */
.st-emotion-cache-1r6slb0,
.st-emotion-cache-16txtl3,
[data-testid="stSidebar"] ul {{

    background: rgba(255,255,255,0.05) !important;

    backdrop-filter: blur(15px);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 18px;

    padding: 15px;
}}
.nav-link {{

    font-size:18px !important;

    border-radius:16px !important;

    margin-bottom:10px !important;

    padding:14px !important;

    background:rgba(255,255,255,0.06);

    border:1px solid rgba(255,255,255,0.08);

    transition:all .3s ease;
}}
.nav-link:hover {{

    transform:translateX(6px);

    background:rgba(59,130,246,0.15);

    border:1px solid rgba(59,130,246,0.25);
}}

/* =====================================
HILANGKAN KOTAK PUTIH SIDEBAR
===================================== */

section[data-testid="stSidebar"] .block-container {{

    background: transparent !important;

    padding-top: 1rem !important;
}}

/* Container option menu */

section[data-testid="stSidebar"] ul {{

    background: rgba(255,255,255,0.05) !important;

    backdrop-filter: blur(15px);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 20px;

    padding: 15px !important;
}}
/* =====================================================
ACTIVE MENU
===================================================== */
.nav-link-selected {{

    background: linear-gradient(
        90deg,
        #2563EB,
        #3B82F6
    ) !important;

    color:white !important;

    font-weight:700;

    box-shadow:
    0px 0px 18px rgba(59,130,246,0.45);
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

    background: rgba(15,23,42,0.85) !important;

    color: #FFFFFF !important;

    font-size: 20px !important;

    font-weight: 700 !important;

    border: 1px solid rgba(59,130,246,0.5) !important;

    border-radius: 14px !important;

    padding-left: 12px !important;
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

    background:
    rgba(255,255,255,0.05);

    border:
    1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(15px);

    border-radius:16px;

    height:48px;

    color:white;

    font-size:17px;

    font-weight:600;

    transition:all .3s ease;

    margin-bottom:8px;

    text-align:left;
}}

.stButton>button:hover {{

    transform:translateX(5px);

    background:
    rgba(59,130,246,0.12);

    border:
    1px solid rgba(59,130,246,0.25);
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
if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"

with st.sidebar:

    st.markdown("""
    <div style="
    display:flex;
    align-items:center;
    gap:15px;
    padding:10px 0 25px 10px;
    ">

    <div style="
    width:80px;
    height:80px;
    border-radius:24px;
    background:linear-gradient(135deg,#1D4ED8,#60A5FA);
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:42px;
    color:white;
    font-weight:bold;
    box-shadow:
    0 0 30px rgba(59,130,246,0.45),
    0 10px 30px rgba(0,0,0,0.35);
    ">
    K
    </div>

    <div>
    <div style="
    color:white;
    font-size:34px;
    font-weight:800;
    letter-spacing:-1px;
    line-height:1;
    ">
    Koperasi
    </div>

    <div style="
    color:#94A3B8;
    font-size:13px;
    letter-spacing:2px;
    text-transform:uppercase;
    margin-top:4px;
    ">
    Credit Risk Assessment
    </div>
    </div>

    </div>
    """, unsafe_allow_html=True)
    
    menu = st.session_state.menu

    dashboard_label = "◫ Dashboard"
    prediksi_label = "⌕ Prediksi Risiko"
    nasabah_label = "☰ Data Nasabah"

    if menu == "Dashboard":
        dashboard_label = "🔵 Dashboard"

    if menu == "Prediksi Risiko":
        prediksi_label = "🔵 Prediksi Risiko"

    if menu == "Data Nasabah":
        nasabah_label = "🔵 Data Nasabah"

    if st.button(dashboard_label, use_container_width=True):
        st.session_state.menu = "Dashboard"

    if st.button(prediksi_label, use_container_width=True):
        st.session_state.menu = "Prediksi Risiko"

    if st.button(nasabah_label, use_container_width=True):
        st.session_state.menu = "Data Nasabah"

    menu = st.session_state.menu
# =====================================================
# DASHBOARD
# =====================================================
if menu == "Dashboard":

    st.markdown(f"""
    <div style="
    display:flex;
    align-items:center;
    gap:25px;
    margin-top:10px;
    margin-bottom:25px;
    ">

    <div style="
    width:95px;
    height:95px;
    border-radius:24px;
    background:rgba(255,255,255,0.05);
    display:flex;
    align-items:center;
    justify-content:center;
    box-shadow:0 0 20px rgba(59,130,246,0.15);
    ">

    <img src="data:image/png;base64,{dashboard_img}"
    style="
    width:65px;
    height:65px;
    ">

    </div>

    <div>

    <div style="
    font-size:52px;
    font-weight:700;
    color:white;
    line-height:1.1;
    letter-spacing:-1px;
    font-family:'Segoe UI',sans-serif;
    ">
    Dashboard Risiko Kredit
    </div>

    <div style="
    margin-top:10px;
    font-size:15px;
    letter-spacing:3px;
    text-transform:uppercase;
    color:#60A5FA;
    font-weight:500;
    ">
    Hybrid K-Means • Random Forest
    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)


    
    # =====================================================
    # METRIC
    # =====================================================
    total_nasabah = len(df)

    risiko_rendah = len(df[df['Risiko'] == 'Rendah'])
    risiko_sedang = len(df[df['Risiko'] == 'Sedang'])
    risiko_tinggi = len(df[df['Risiko'] == 'Tinggi'])

    # =====================================================
    # CARD STYLE
    # =====================================================

    card_style = """
    background: rgba(8,15,35,0.55);
    backdrop-filter: blur(18px);
    padding:18px;
    border-radius:24px;
    height:140px;
    text-align:center;
    box-shadow:
    0 10px 30px rgba(0,0,0,0.35);
    """

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div style='{card_style} border:1px solid #60A5FA;'>
            <h4 style=
            'color:#93C5FD;
            font-size:20px;
            font-weight:600;
            line-height:1;
            margin-bottom:-30px;
            '>👥 Total Nasabah</h4>
            <h1 style=
            'color:white;
            font-size:36px;
            font-weight:800;
            line-height:1;
            margin-top:-20px;
            '>{total_nasabah}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='{card_style} border:1px solid #4ADE80;'>
            <h4 style=
            'color:#4ADE80;
            font-size:20px;
            font-weight:600;
            line-height:1;
            margin-bottom:-30px;
            '>🟢 Risiko Rendah</h4>
            <h1 style=
            'color:white;
            font-size:36px;
            font-weight:800;
            line-height:1;
            margin-top:-20px;
            '>{risiko_rendah}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style='{card_style} border:1px solid #FACC15;'>
            <h4 style='color:#FACC15;
            font-size:20px;
            font-weight:600;
            line-height:1;
            margin-bottom:-30px;
            '>🟡 Risiko Sedang</h4>
            <h1 style='color:white;            
            font-size:36px;
            font-weight:800;
            line-height:1;
            margin-top:-20px;
            '>{risiko_sedang}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div style='{card_style} border:1px solid #F87171;'>
            <h4 style='color:#F87171;
            font-size:20px;
            font-weight:600;
            line-height:1;
            margin-bottom:-30px;
            '>🔴 Risiko Tinggi</h4>
            <h1 style='color:white;
            font-size:36px;
            font-weight:800;
            line-height:1;
            margin-top:-20px;'>{risiko_tinggi}</h1>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
    # =====================================================
    # CHART + DATA PREVIEW
    # =====================================================

    col_chart, col_table = st.columns([1, 1.5], gap="large")

    with col_chart:

        st.markdown("""
        <div style="
        text-align:center;
        color:white;
        font-size:22px;
        font-weight:700;
        margin-bottom:15px;
        ">
        Distribusi Risiko
        </div>
        """, unsafe_allow_html=True)

        chart_data = df['Risiko'].value_counts()

        fig, ax = plt.subplots(figsize=(5,3))

        bars = ax.bar(
            chart_data.index,
            chart_data.values,
            color=['#4ADE80', '#FACC15', '#F87171']
        )

        fig.patch.set_alpha(0)
        ax.set_facecolor((0,0,0,0))

        ax.tick_params(
            axis='x',
            colors='white',
            labelsize=14
        )

        ax.tick_params(
            axis='y',
            colors='white',
            labelsize=12
        )

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')

        ax.set_title("")

        for bar in bars:
            height = bar.get_height()

            ax.text(
                bar.get_x() + bar.get_width()/2,
                height + 5,
                f"{int(height)}",
                ha='center',
                color='white',
                fontsize=14,
                fontweight='bold'
            )

        st.pyplot(fig)

    with col_table:

        st.markdown("""
        <div style="
        text-align:center;
        color:white;
        font-size:22px;
        font-weight:700;
        margin-bottom:15px;
        ">
        Preview Data Nasabah
        </div>
        """, unsafe_allow_html=True)

        preview_df = df.head(5)

        st.markdown(
            preview_df[
                ['ID Anggota','Nama Anggota','Risiko']
            ].to_html(index=False),
            unsafe_allow_html=True
    )

# =====================================================
# PREDIKSI RISIKO
# =====================================================
elif menu == "Prediksi Risiko":

    st.markdown(f"""
    <div style="
    display:flex;
    align-items:center;
    gap:22px;
    margin-bottom:25px;
    ">

    <div style="
    width:70px;
    height:70px;
    border-radius:20px;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    display:flex;
    align-items:center;
    justify-content:center;
    backdrop-filter:blur(20px);
    box-shadow:0 0 25px rgba(139,92,246,0.15);
    ">

    <img src="data:image/png;base64,{icon_prediksi}"
    style="
    width:34px;
    height:34px;
    ">

    </div>

    <div>

    <div style="
    font-size:52px;
    font-weight:700;
    color:white;
    line-height:1.1;
    letter-spacing:-1px;
    font-family:'Segoe UI',sans-serif;
    ">
    Prediksi Risiko Kredit
    </div>

    <div style="
    margin-top:10px;
    font-size:15px;
    letter-spacing:1px;
    color:#CBD5E1;
    font-weight:500;
    ">
    Masukkan informasi pinjaman untuk memprediksi tingkat risiko kredit
    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
    "<div style='height:8px'></div>",
    unsafe_allow_html=True
)
    
    col1, col2 = st.columns(2)

    with col1:

        besar_pinjaman = st.number_input(
            "Besar Pinjaman",
            min_value=0.0
        )

        sisa_pinjaman = st.number_input(
            "Sisa Pinjaman",
            min_value=0.0
        )

        angsuran_pokok = st.number_input(
            "Angsuran Pokok",
            min_value=0.0
        )

    with col2:

        tenor = st.number_input(
            "Tenor",
            min_value=1
        )

        tunggakan_maksimum = st.number_input(
            "Tunggakan Maksimum",
            min_value=0.0
        )

    st.markdown(
        "<div style='height:15px'></div>",
        unsafe_allow_html=True
    )

    if st.button("🔍 Prediksi Risiko"):

        data_input = pd.DataFrame({
            'Besar Pinjaman': [besar_pinjaman],
            'Sisa Pinjaman': [sisa_pinjaman],
            'Angsuran Pokok': [angsuran_pokok],
            'Tenor': [tenor],
            'Tunggakan Maksimum': [tunggakan_maksimum]
        })

        scaled_data = scaler.transform(data_input)

        prediction = rf_model.predict(data_input)[0]

        probability = rf_model.predict_proba(data_input)[0]

        risk_score = round(max(probability) * 100, 2)

        st.markdown("""
        <div style="
        background:linear-gradient(
        90deg,
        rgba(16,185,129,0.18),
        rgba(6,182,212,0.10)
        );
        border:1px solid rgba(52,211,153,0.25);
        border-radius:18px;
        padding:22px 28px;
        margin-top:10px;
        margin-bottom:25px;
        backdrop-filter:blur(20px);
        ">

        <div style="
        display:flex;
        align-items:center;
        gap:18px;
        ">

        <div style="
        width:42px;
        height:42px;
        border-radius:50%;
        border:2px solid #34D399;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:22px;
        font-weight:bold;
        color:#34D399;
        ">
        ✓
        </div>

        <div>

        <div style="
        color:#34D399;
        font-size:20px;
        font-weight:700;
        margin-bottom:4px;
        ">
        Prediksi Berhasil!
        </div>

        <div style="
        color:#D1FAE5;
        font-size:16px;
        ">
        Berikut adalah hasil prediksi risiko kredit berdasarkan data yang Anda masukkan.
        </div>

        </div>

        </div>

        </div>
        """, unsafe_allow_html=True)


        col_risk, col_score = st.columns(2)
    
        with col_risk:

            st.markdown(
                f"""
        <div style="
        background:rgba(255,255,255,0.05);
        backdrop-filter:blur(20px);
        border:1px solid rgba(139,92,246,0.35);
        border-radius:24px;
        padding:12px;
        min-height:80px;
        ">
        

        <div style="
        color:#A78BFA;
        font-size:18px;
        font-weight:600;
        ">
         🛡️ Risiko Kredit
        </div>

        <h1 style="
        color:white;
        font-size:30px;
        font-weight:800;
        margin-top:5px;
        margin-bottom:0;
        ">
        {prediction}
        </h1>

        </div>
        """,
                unsafe_allow_html=True
            )
                            
        with col_score:

            st.markdown(
                f"""
        <div style="
        background:rgba(255,255,255,0.05);
        backdrop-filter:blur(20px);
        border:1px solid rgba(34,211,238,0.35);
        border-radius:24px;
        padding:12px;
        min-height:80px;
        ">

        <div style="
        color:#22D3EE;
        font-size:18px;
        font-weight:600;
        ">
         ⚡Risk Score
        </div>

        <h1 style="
        color:#5EEAD4;
        font-size:30px;
        font-weight:800;
        margin-top:5px;
        margin-bottom:0;
        ">
        {risk_score}%
        </h1>

        </div>
        """,
                unsafe_allow_html=True
            )

        st.markdown("""
        <h2 style="
        color:white;
        font-size:20px;
        font-weight:600;
        margin-top:0px;
        margin-bottom:0px;
        ">
        ✨ Interpretasi Hasil
        </h2>
        """, unsafe_allow_html=True)

        if prediction == "Rendah":

            st.markdown("""
            <div style="
            background:rgba(34,197,94,0.08);
            border:1px solid rgba(34,197,94,0.35);
            border-radius:22px;
            padding:25px;
            ">

            <h3 style="
            color:#86EFAC;
            font-size:30px;
            ">
            ✅ Risiko Rendah
            </h3>

            <p style="
            color:#E2E8F0;
            font-size:18px;
            line-height:1.8;
            ">
            Pengajuan pinjaman sangat aman.
            Anggota memiliki profil risiko yang baik dan
            peluang gagal bayar sangat kecil.
            </p>

            <div style="
            margin-top:15px;
            background:rgba(34,197,94,0.12);
            padding:15px;
            border-radius:14px;
            color:#86EFAC;
            font-weight:700;
            ">
            ✔ Rekomendasi: Pengajuan dapat disetujui.
            </div>

            </div>
            """, unsafe_allow_html=True)

        elif prediction == "Sedang":

            st.markdown("""
                <div style="
                background:rgba(250,204,21,0.08);
                border:1px solid rgba(250,204,21,0.35);
                border-radius:22px;
                padding:25px;
                ">

                <h3 style="
                color:#FACC15;
                font-size:30px;
                ">
                ⚠ Risiko Sedang
                </h3>

                <p style="
                color:#E2E8F0;
                font-size:18px;
                line-height:1.8;
                ">
                Pengajuan perlu evaluasi lebih lanjut.
                Terdapat beberapa faktor risiko yang perlu diperhatikan.
                </p>

                <div style="
                margin-top:15px;
                background:rgba(250,204,21,0.12);
                padding:15px;
                border-radius:14px;
                color:#FACC15;
                font-weight:700;
                ">
                ✔ Rekomendasi: Pengajuan dapat dipertimbangkan dengan perhatian khusus.
                </div>

                </div>
                """, unsafe_allow_html=True)


        elif prediction == "Tinggi":

            st.markdown("""
                <div style="
                background:rgba(239,68,68,0.08);
                border:1px solid rgba(239,68,68,0.35);
                border-radius:22px;
                padding:25px;
                ">

                <h3 style="
                color:#F87171
                font-size:30px;
                ">
                ❌ Risiko Tinggi
                </h3>

                <p style="
                color:#E2E8F0;
                font-size:18px;
                line-height:1.8;
                ">
                Pengajuan memiliki risiko tinggi.
                Peluang gagal bayar besar sehingga tidak disarankan untuk disetujui.
                </p>

                <div style="
                margin-top:15px;
                background:rgba(239,68,68,0.12);
                padding:15px;
                border-radius:14px;
                color:#F81717;
                font-weight:700;
                ">
                ✔ Rekomendasi: Pengajuan tidak disarankan.
                </div>

                </div>
                """, unsafe_allow_html=True)
# =====================================================
# DATA NASABAH
# =====================================================
elif menu == "Data Nasabah":

    st.markdown(f"""
    <div style="
    display:flex;
    align-items:center;
    gap:25px;
    margin-top:0px;
    margin-bottom:5px;
    ">

    <div>
    <img src="data:image/png;base64,{database_icon}"
    style="
    width:80px;
    height:80px;
    ">
    </div>

    <div>

    <div style="
    font-size:52px;
    font-weight:700;
    color:white;
    line-height:1.1;
    letter-spacing:-1px;
    font-family:'Segoe UI',sans-serif;
    ">
    Data Nasabah
    </div>

    <div style="
    margin-top:8px;
    font-size:15px;
    color:#CBD5E1;
    font-weight:500;
    ">
    Data hasil clustering dan klasifikasi risiko kredit nasabah.
    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <hr style="
    margin-top:10px;
    margin-bottom:20px;
    border:0.5px solid rgba(255,255,255,0.08);
    ">
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        selected_risk = st.selectbox(
            "Filter Risiko",
            ['Semua','Rendah','Sedang','Tinggi']
        )

    with col2:
        search = st.text_input(
            "Cari Nasabah",
            placeholder="Cari berdasarkan nama atau ID anggota..."
        )

    filtered_df = df.copy()

    if selected_risk != "Semua":
        filtered_df = filtered_df[
            filtered_df["Risiko"] == selected_risk
        ]

    if search:
        filtered_df = filtered_df[
            filtered_df["Nama Anggota"]
            .astype(str)
            .str.contains(search, case=False)
        ]

    total_data = len(filtered_df)

    page_size = st.selectbox(
            "Jumlah Data",
            [10,25,50,100]
        )
    
    total_pages = max(
    1,
    (total_data + page_size - 1) // page_size
)
    
    page = st.number_input(
    "Halaman",
    min_value=1,
    max_value=max(
        1,
        (total_data + page_size - 1) // page_size
    ),
    value=1,
    step=1
)

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    start = start_idx + 1
    end = min(end_idx, total_data)

    show_df = filtered_df[
        [
            "ID Anggota",
            "Nama Anggota",
            "Besar Pinjaman",
            "Sisa Pinjaman",
            "Angsuran Pokok",
            "Risiko"
        ]
    ]

    show_df = show_df.iloc[start_idx:end_idx].copy()

    table_html = """
    <div style="
    background:rgba(5,15,40,0.65);
    backdrop-filter:blur(20px);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:20px;
    overflow:hidden;
    ">

    <table style="
    width:100%;
    border-collapse:collapse;
    color:white;
    font-family:Segoe UI,sans-serif;
    ">

    <thead>
    <tr>
    """

    table_html += """
    <tr style="
    background:linear-gradient(
    90deg,
    rgba(37,99,235,0.20),
    rgba(37,99,235,0.08)
    );
    ">
"""
    
    for col in show_df.columns:
        table_html += f"""
        <th style="
        padding:18px;
        color:#60A5FA;
        text-align:center;
        font-weight:700;
        font-size:18px;
        border-bottom:1px solid rgba(255,255,255,0.10);
        border-right:1px solid rgba(255,255,255,0.06);
        ">
        {col}
        </th>
        """

    table_html += """
    </tr>
    </thead>
    <tbody>
    """

    for _, row in show_df.iterrows():

        risiko = row["Risiko"]

        if risiko == "Rendah":
            badge = """
            <span style="
            background:rgba(34,197,94,0.15);
            color:#22C55E;
            padding:10px 20px;
            display:inline-block;
            min-width:110px;
            text-align:center;
            border-radius:20px;
            font-weight:600;
            ">
            ● Rendah
            </span>
            """
        elif risiko == "Sedang":
            badge = """
            <span style="
            background:rgba(250,204,21,0.15);
            color:#FACC15;
            padding:10px 20px;
            display:inline-block;
            min-width:110px;
            text-align:center;
            border-radius:20px;
            font-weight:600;
            ">
            ● Sedang
            </span>
            """
        else:
            badge = """
            <span style="
            background:rgba(239,68,68,0.15);
            color:#EF4444;
            padding:10px 20px;
            display:inline-block;
            min-width:110px;
            text-align:center;
            border-radius:20px;
            font-weight:600;
            ">
            ● Tinggi
            </span>
            """

        table_html += f"""
        <tr style="
        border-bottom:1px solid rgba(255,255,255,0.08);
        ">

            <td style="
            padding:14px;
            text-align:center;
            border-right:1px solid rgba(255,255,255,0.06);
            ">
            {row['ID Anggota']}
            </td>

            <td style="
            padding:14px;
            border-right:1px solid rgba(255,255,255,0.06);
            ">
            {row['Nama Anggota']}
            </td>

            <td style="
            padding:14px;
            text-align:center;
            border-right:1px solid rgba(255,255,255,0.06);
            ">
            {row['Besar Pinjaman']:,.0f}
            </td>

            <td style="
            padding:14px;
            text-align:center;
            border-right:1px solid rgba(255,255,255,0.06);
            ">
            {row['Sisa Pinjaman']:,.0f}
            </td>

            <td style="
            padding:14px;
            text-align:center;
            border-right:1px solid rgba(255,255,255,0.06);
            ">
            {row['Angsuran Pokok']:,.0f}
            </td>

            <td style="
            padding:14px;
            text-align:center;
            ">
            {badge}
            </td>

        </tr>
        """

    table_html += """
    </tbody>
    </table>
    </div>
    """

    st.components.v1.html(
        table_html,
        height=520,
        scrolling=True
    )

    st.markdown(f"""
    <div style="
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-top:15px;
    color:white;
    ">
    <div>
    Menampilkan {start}-{end} dari {total_data} data
    </div>

    <div>
    Halaman {page} dari {total_pages}
    </div>
    </div>
    """, unsafe_allow_html=True)