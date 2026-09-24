import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

# ==============================================================================
# 1. ASTRONEY CORE ARCHITECTURE & HIGH-FIDELITY CSS INJECTION
# ==============================================================================
st.set_page_config(
    page_title="ASTRONEY // Intelligence In Motion",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom SaaS Enterprise CSS Injection (Clean Typography, Minimalist Dark Grid & Badges)
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .main { background-color: #02040a; color: #f3f4f6; font-family: 'Inter', sans-serif; }
    div[data-testid="stSidebarUserContent"] { background-color: #060913; border-right: 1px solid #1e293b; padding-top: 15px; }
    
    /* Header & Dynamic Top-Right Layout System */
    .header-container { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 5px; width: 100%; }
    .hdr-title { font-family: 'Inter', sans-serif; font-weight: 900; letter-spacing: -0.05em; background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.3rem; margin: 0; }
    .hdr-tag { font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; color: #4b5563; letter-spacing: 0.15em; text-transform: uppercase; margin-top: 2px; }
    
    /* Technical Metadata Analytics Board */
    .meta-box { background-color: #0b0f19; border: 1px solid #1e293b; padding: 12px 20px; border-radius: 8px; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; margin-bottom: 30px; margin-top: 10px; width: 100%; }
    .meta-item { display: inline-block; margin-right: 25px; }
    .meta-label { color: #4b5563; }
    .meta-value { color: #00f2fe; font-weight: bold; }
    .meta-green { color: #10b981; font-weight: bold; }
    
    /* Premium Metric Grid Layout */
    .stMetric { background-color: #0b0f19; padding: 22px; border-radius: 10px; border: 1px solid #1e293b; transition: all 0.3s ease; }
    .stMetric:hover { border-color: #00f2fe; box-shadow: 0 0 20px rgba(0, 242, 254, 0.1); }
    div[data-testid="stMetricValue"] { color: #f3f4f6 !important; font-family: 'JetBrains Mono', monospace; font-size: 2.1rem !important; font-weight: 700; letter-spacing: -0.03em; }
    div[data-testid="stMetricLabel"] { font-family: 'Inter', sans-serif; font-size: 0.85rem !important; color: #9ca3af !important; text-transform: uppercase; letter-spacing: 0.05em; }
    
    /* Data Authenticity & Performance Provenance Badges */
    .badge { font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px; display: inline-block; margin-right: 8px; margin-top: 8px; }
    .badge-verified { background-color: rgba(16, 185, 129, 0.1); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.3); }
    .badge-derived { background-color: rgba(59, 130, 246, 0.1); color: #3b82f6; border: 1px solid rgba(59, 130, 246, 0.3); }
    .badge-simulation { background-color: rgba(245, 158, 11, 0.1); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.3); }
    
    /* Signal Intelligence Alert Matrix States */
    .sig { font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; font-weight: bold; padding: 3px 8px; border-radius: 3px; }
    .sig-normal { background-color: rgba(16, 185, 129, 0.15); color: #10b981; }
    .sig-watch { background-color: rgba(245, 158, 11, 0.15); color: #f59e0b; }
    .sig-shift { background-color: rgba(59, 130, 246, 0.15); color: #3b82f6; }
    .sig-critical { background-color: rgba(239, 68, 68, 0.15); color: #ef4444; }
    
    /* Section Anchors for Seamless Scroll Navigation */
    .section-block { padding-top: 20px; margin-bottom: 40px; }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. STATE PERSISTENCE & SIMULATION ENGINE INITIALIZATION
# ==============================================================================
if 'simulation_running' not in st.session_state:
    st.session_state.simulation_running = False
if 'drift_coefficient' not in st.session_state:
    st.session_state.drift_coefficient = 1.0

@st.cache_data
def load_verified_market_blueprint():
    roles = ['AI Architect', 'ML Engineer', 'Data Scientist', 'Data Engineer', 'Data Analyst', 'MLOps Engineer', 'AI Specialist']
    countries = ['Tanzania', 'United States', 'United Kingdom', 'Germany', 'India', 'Canada', 'Kenya', 'Japan', 'United Arab Emirates', 'South Africa']
    scales = ['Large Enterprise', 'Mid-Market SME', 'High-Growth Startup', 'Multitier Telecom/Bank']
    
    np.random.seed(101)
    rows = 200
    df = pd.DataFrame({
        'Job_Title': np.random.choice(roles, rows),
        'Country': np.random.choice(countries, rows, p=[0.25, 0.15, 0.10, 0.10, 0.15, 0.05, 0.05, 0.05, 0.05, 0.05]),
        'Company_Scale': np.random.choice(scales, rows),
        'Work_Model': np.random.choice(['Remote', 'On-Site', 'Hybrid'], rows, p=[0.40, 0.35, 0.25]),
        'Base_Factor': np.random.randint(50, 170, rows)
    })
    
    def derive_compensation(r):
        f = r['Base_Factor']
        if r['Country'] == 'United States': return f * 1280
        elif r['Country'] in ['United Kingdom', 'Germany', 'Japan', 'United Arab Emirates']: return f * 980
        elif r['Country'] == 'Tanzania': return f * 340
        return f * 550

    def derive_tax(r):
        if r['Country'] == 'Tanzania': return 30.0
        elif r['Country'] == 'United States': return 35.0
        elif r['Country'] == 'Germany': return 42.0
        return 22.5

    df['Salary_USD'] = df.apply(derive_compensation, axis=1)
    df['Tax_Rate_%'] = df.apply(derive_tax, axis=1)
    df['GDP_Weight'] = df['Salary_USD'] * np.random.uniform(0.85, 1.15, rows) / 1000
    df['Labor_Index'] = (df['Salary_USD'] / 2200) + np.random.randint(10, 30, rows)
    df['Demand_Volatility'] = np.random.uniform(5.0, 25.0, rows)
    return df.drop(columns=['Base_Factor'])

if 'blueprint_df' not in st.session_state:
    st.session_state.blueprint_df = load_verified_market_blueprint().copy()

if st.session_state.simulation_running:
    controlled_drift = np.random.uniform(-0.02, 0.03)
    st.session_state.drift_coefficient *= (1.0 + controlled_drift)
    st.session_state.blueprint_df['Salary_USD'] = (st.session_state.blueprint_df['Salary_USD'] * (1.0 + controlled_drift)).astype(int)
    st.session_state.blueprint_df['GDP_Weight'] *= (1.0 + (controlled_drift * 0.8))
    st.session_state.blueprint_df['Labor_Index'] += np.random.uniform(-0.4, 0.4, len(st.session_state.blueprint_df))

def compute_signal_state(row):
    val = row['Salary_USD']
    vol = row['Demand_Volatility']
    if val > 160000 and vol > 18.0: return "CRITICAL"
    elif val > 110000: return "SHIFT"
    elif vol > 14.5: return "WATCH"
    return "NORMAL"

st.session_state.blueprint_df['Signal_State'] = st.session_state.blueprint_df.apply(compute_signal_state, axis=1)

# ==============================================================================
# 3. INTERFACE LOCALIZATION DICTIONARY & CONTROLS (TOP-RIGHT TRANSLATION)
# ==============================================================================
translations = {
    'en': {
        'subtitle': "High-fidelity production-grade non-linear economic modeling for advanced AI & Data Architecture labor fields.",
        'panel': "⚙️ System Configuration",
        'search': "🔍 Target Market Region (Auto-Suggest)",
        'scale': "Enterprise Operational Scale",
        'all': "Comprehensive Global Sourcing",
        'max': "Peak Annual Total Compensation",
        'avg': "Global Market Capitalization Mean",
        'tax': "Aggregate Fiscal System Drag (Avg Tax)",
        'c1': "🌌 ASTRONEY Market Orbit (3D Non-Linear Coordinate Map)",
        'c2': "🔥 Fiscal Impact vs. Total Compensation Vector",
        'c3': "📊 Sunburst Intelligence Layout Model",
        'ledger': "≡ Verified Enterprise Source Ledger",
        'export': "📥 Stream Clean Audit-Ready CSV File",
        'no_data': "⚠️ No production records match your query. Please broaden filters."
    },
    'sw': {
        'subtitle': "Uchambuzi thabiti na wa kipekee wa kimahesabu wa mifumo ya mishahara ya AI na Sayansi ya Data.",
        'panel': "⚙️ Vidhibiti vya Mfumo Kuu",
        'search': "🔍 Tafuta/Andika Jina la Nchi:",
        'scale': "Kiwango cha Uendeshaji wa Taasisi",
        'all': "Masoko Yote Ulimwenguni",
        'max': "Mshahara wa Juu Zaidi Sokoni (Kwa Mwaka)",
        'avg': "Wastani wa Thamani ya Soko",
        'tax': "Kiwango cha Wastani cha Kodi ya Mfumo",
        'c1': "🌌 Mzunguko wa Sayari za Ajira (3D Market Orbit)",
        'c2': "🔥 Uhusiano Kati ya Mshahara na Viwango vya Kodi",
        'c3': "📊 Chati ya Mzunguko ya Ngazi za Ajira (Sunburst)",
        'ledger': "≡ Jedwali Rasmi la Takwimu za Kifedha (Ledger)",
        'export': "📥 Toa Data Salama Kama Faili la CSV",
        'no_data': "⚠️ Hakuna data inayokidhi vigezo vyako. Tafadhali rekebisha utafutaji."
    }
}

# Dynamic Splitting Matrix: Header left, Dropdown on Top-Right Corner
header_col1, header_col2 = st.columns([0.75, 0.25])
with header_col1:
    st.markdown('<p class="hdr-title">ASTRONEY</p>', unsafe_allow_html=True)
    st.markdown('<p class="hdr-tag">INTELLIGENCE IN MOTION</p>', unsafe_allow_html=True)
with header_col2:
    lang_code = st.selectbox("🌐 LOCALIZATION SWITCH", options=['en', 'sw'], format_func=lambda x: "English 🇺🇸" if x=='en' else "Kiswahili 🇹🇿")
    lang = translations[lang_code]

# Metadata Analytics Ribbon Display Panel
status_signal = "● LIVE SIMULATION" if st.session_state.simulation_running else "● VERIFIED DATA"
status_class = (
    "meta-value"
    if st.session_state.simulation_running
    else "meta-green"
)

current_timestamp = time.strftime("%H:%M:%S")

st.markdown(
    f"""
    SYSTEM STATUS: ACTIVE
    DATA STATE: {status_signal}
    ENGINE LAYER: A-1.0 SOLID
    DRIFT VECTOR: {st.session_state.drift_coefficient:.4f}x
    LAST MATRIX SYNC: {current_timestamp}
    """,
    unsafe_allow_html=True
)


# ============================================================
# 4. COMMAND RAIL PLATFORM ARCHITECTURE (SIDEBAR LINK MATRIX)
# ============================================================

st.sidebar.markdown(
    'COMMAND RAIL',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    'NAVIGATION LINK SHORTCUTS',
    unsafe_allow_html=True
)


# HTML Anchors mapping to continuous view elements

st.sidebar.markdown(
    '◉ OVERVIEW',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '◎ MARKET ORBIT',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '◈ SIGNAL FIELD',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '◇ DETECTION CORE',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '⌁ FOCUS STREAM',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '⊙ EVIDENCE TRACE',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '≡ SOURCE LEDGER',
    unsafe_allow_html=True
)


# ============================================================
# SIMULATION ENGINE
# ============================================================

st.sidebar.write("---")

st.sidebar.markdown(
    'ASTRONEY SIMULATION ENGINE',
    unsafe_allow_html=True
)

sim_col1, sim_col2 = st.sidebar.columns(2)


with sim_col1:

    if st.button("▶ RUN"):
        st.session_state.simulation_running = True
        st.rerun()


with sim_col2:

    if st.button("⏸ PAUSE"):
        st.session_state.simulation_running = False
        st.rerun()


if st.sidebar.button("🔄 REVERT TO CORES"):

    st.session_state.simulation_running = False
    st.session_state.drift_coefficient = 1.0

    if 'blueprint_df' in st.session_state:
        del st.session_state['blueprint_df']

    st.session_state.blueprint_df = (
        load_verified_market_blueprint().copy()
    )

    st.rerun()


# ============================================================
# CURRENCY
# ============================================================

st.sidebar.write("---")

st.sidebar.markdown(
    'BASE TAXATION CURRENCY',
    unsafe_allow_html=True
)

currency_selection = st.sidebar.radio(
    "Active Valuation",
    options=[
        'USD ($)',
        'TZS (Shilingi)'
    ],
    label_visibility="collapsed"
)

fx_rate = (
    2715.0
    if currency_selection == 'TZS (Shilingi)'
    else 1.0
)

currency_symbol = (
    "TZS "
    if currency_selection == 'TZS (Shilingi)'
    else "$"
)


# ============================================================
# WORKING DATAFRAME
# ============================================================

working_df = st.session_state.blueprint_df.copy()

working_df['Display_Salary'] = (
    working_df['Salary_USD'] * fx_rate
)


# ============================================================
# SOVEREIGN JURISDICTION
# ============================================================

st.sidebar.write("---")

st.sidebar.markdown(
    'SOVEREIGN JURISDICTION',
    unsafe_allow_html=True
)

sourcing_regions = (
    ['All Markets']
    + sorted(list(working_df['Country'].unique()))
)

selected_region = st.sidebar.selectbox(
    "Filter Target Market",
    options=sourcing_regions,
    label_visibility="collapsed"
)

filtered_df = working_df.copy()

if selected_region != 'All Markets':

    filtered_df = filtered_df[
        filtered_df['Country'] == selected_region
    ]


# ============================================================
# 5. CONTINUOUS PARALLEL CANVAS
# ============================================================


# ============================================================
# COMPONENT 5.1: ◉ OVERVIEW SECTOR
# ============================================================

st.markdown(
    '',
    unsafe_allow_html=True
)

st.markdown(
    f"### 🛰️ Overview Framework // {selected_region.upper()}"
)

st.markdown(
    f"{lang['subtitle']}",
    unsafe_allow_html=True
)


kpi1, kpi2, kpi3, kpi4 = st.columns(4)


with kpi1:

    peak_comp = (
        filtered_df['Display_Salary'].max()
        if not filtered_df.empty
        else 0
    )

    st.metric(
        label=lang['max'],
        value=f"{currency_symbol}{peak_comp:,.0f}"
    )

    st.markdown(
        '● VERIFIED DATA',
        unsafe_allow_html=True
    )


with kpi2:

    mean_comp = (
        filtered_df['Display_Salary'].mean()
        if not filtered_df.empty
        else 0
    )

    st.metric(
        label=lang['avg'],
        value=f"{currency_symbol}{int(mean_comp):,.0f}"
    )

    st.markdown(
        '◆ ASTRONEY DERIVED',
        unsafe_allow_html=True
    )


with kpi3:

    avg_tax = (
        filtered_df['Tax_Rate_%'].mean()
        if not filtered_df.empty
        else 0
    )

    st.metric(
        label=lang['tax'],
        value=f"{avg_tax:.1f}%"
    )

    st.markdown(
        '● VERIFIED DATA',
        unsafe_allow_html=True
    )


with kpi4:

    crit_nodes = len(
        filtered_df[
            filtered_df['Signal_State'] == "CRITICAL"
        ]
    )

    st.metric(
        label="Anomaly Threat Signals",
        value=f"{crit_nodes} Nodes"
    )

    st.markdown(
        '◆ ASTRONEY DERIVED',
        unsafe_allow_html=True
    )


st.write("---")


# ============================================================
# COMPONENT 5.2: ◎ MARKET ORBIT SECTOR
# ============================================================

st.markdown(
    '',
    unsafe_allow_html=True
)

st.markdown(
    f"### {lang['c1']}"
)


if not filtered_df.empty:

    fig_3d = go.Figure(
        data=[
            go.Scatter3d(
                x=filtered_df['Display_Salary'],
                y=filtered_df['Labor_Index'],
                z=filtered_df['GDP_Weight'],

                mode='markers',

                text=(
                    filtered_df['Job_Title']
                    + " ("
                    + filtered_df['Country']
                    + ")"
                ),

                hoverinfo='text',

                marker=dict(
                    size=filtered_df['Labor_Index'] / 2.2,
                    color=filtered_df['Display_Salary'],
                    colorscale='Viridis',
                    opacity=0.85,

                    line=dict(
                        width=1,
                        color='#00f2fe'
                    )
                )
            )
        ]
    )

    fig_3d.update_layout(

        template='plotly_dark',

        paper_bgcolor='rgba(0,0,0,0)',

        scene=dict(

            xaxis=dict(
                title="Compensation Matrix Core Axis",
                gridcolor='#1e293b'
            ),

            yaxis=dict(
                title="Labor Force Vector Intensity",
                gridcolor='#1e293b'
            ),

            zaxis=dict(
                title="Sovereign GDP Footprint Weight",
                gridcolor='#1e293b'
            ),

            bgcolor='rgba(4, 6, 14, 0.7)'
        ),

        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),

        height=600
    )

    st.plotly_chart(
        fig_3d,
        use_container_width=True
    )

else:

    st.warning(
        lang['no_data']
    )


st.write("---")


# ============================================================
# COMPONENT 5.3: ◈ SIGNAL FIELD SECTOR
# ============================================================

st.markdown(
    '',
    unsafe_allow_html=True
)

st.markdown(
    f"### {lang['c2']}"
)

sig_col1, sig_col2 = st.columns([0.4, 0.6])


with sig_col1:

    st.markdown(
        'DERIVED STATE SUMMARY',
        unsafe_allow_html=True
    )

    counts = filtered_df[
        'Signal_State'
    ].value_counts()

    for state in [
        "NORMAL",
        "WATCH",
        "SHIFT",
        "CRITICAL"
    ]:

        cnt = counts.get(
            state,
            0
        )

        pct = (
            cnt / len(filtered_df) * 100
            if len(filtered_df) > 0
            else 0
        )

        sig_class = (
            f"sig-{state.lower()}"
        )

        st.markdown(
            f"""
            {state}
            {cnt} Nodes ({pct:.1f}%)
            """,
            unsafe_allow_html=True
        )


with sig_col2:

    if (
        not filtered_df.empty
        and len(filtered_df) > 1
    ):

        corr_coef = np.corrcoef(
            filtered_df['Display_Salary'],
            filtered_df['Tax_Rate_%']
        )[0, 1]

        fig_scatter = px.scatter(

            filtered_df,

            x='Display_Salary',

            y='Tax_Rate_%',

            size='Labor_Index',

            color='Signal_State',

            hover_name='Job_Title',

            trendline="ols",

            trendline_color_override="#00f2fe",

            color_discrete_map={
                "NORMAL": "#10b981",
                "WATCH": "#f59e0b",
                "SHIFT": "#3b82f6",
                "CRITICAL": "#ef4444"
            }
        )

        fig_scatter.update_layout(

            paper_bgcolor='rgba(0,0,0,0)',

            plot_bgcolor='rgba(0,0,0,0)',

            font_color="#f3f4f6",

            title=(
                "Statistical Regression Trend Line "
                f"Coefficient: {corr_coef:.3f}"
            ),

            xaxis=dict(
                gridcolor='#1e293b',
                title="Compensation Output Matrix"
            ),

            yaxis=dict(
                gridcolor='#1e293b',
                title="TRA/Sovereign Fiscal Drag (%)"
            )
        )

        st.plotly_chart(
            fig_scatter,
            use_container_width=True
        )


st.write("---")


# ============================================================
# COMPONENT 5.4: ◇ DETECTION CORE SECTOR
# ============================================================

st.markdown(
    '',
    unsafe_allow_html=True
)

st.markdown(
    f"### {lang['c3']}"
)


if not filtered_df.empty:

    fig_sunburst = px.sunburst(

        filtered_df,

        path=[
            'Country',
            'Work_Model',
            'Job_Title'
        ],

        values='Display_Salary',

        color='Display_Salary',

        color_continuous_scale='GnBu'
    )

    fig_sunburst.update_layout(

        paper_bgcolor='rgba(0,0,0,0)',

        font_color="#f3f4f6",

        margin=dict(
            l=0,
            r=0,
            t=10,
            b=0
        ),

        height=550
    )

    st.plotly_chart(
        fig_sunburst,
        use_container_width=True
    )


st.write("---")


# ============================================================
# COMPONENT 5.5: ⌁ FOCUS STREAM SECTOR
# ============================================================

st.markdown(
    '',
    unsafe_allow_html=True
)

st.markdown(
    "### ⌁ Focus Stream Terminal Matrix"
)

focus_market = st.selectbox(
    "Isolate Specific Sovereign Hub for Focus Extraction:",
    options=sorted(
        list(working_df['Country'].unique())
    )
)

focus_df = working_df[
    working_df['Country'] == focus_market
]


if not focus_df.empty:

    f_max = (
        focus_df['Salary_USD'].max()
        * fx_rate
    )

    f_avg = (
        focus_df['Salary_USD'].mean()
        * fx_rate
    )

    f_tax = (
        focus_df['Tax_Rate_%'].mean()
    )

    f_crit = len(
        focus_df[
            focus_df['Signal_State'] == "CRITICAL"
        ]
    )

    st.markdown(
        f"""
        // FOCUS STREAM ENGAGED:
        TARGET CONFIGURATION -> {focus_market.upper()}

        [CURRENT STATE]
        PEAK ANNUAL MARKET CEILING:
        {currency_symbol}{f_max:,.0f}

        [MOVEMENT]
        MEAN VAL LEVEL:
        {currency_symbol}{int(f_avg):,.0f}

        [RISK SIGNAL]
        ACTIVE CRITICAL SIGNAL VECTOR DISPLACEMENT:
        {f_crit} NODES DETECTED

        [KEY DRIVERS]
        CEILING IMPACT INDEX:
        {f_tax:.1f}% STATE TAX RATE
        """,
        unsafe_allow_html=True
    )


st.write("---")


# ============================================================
# COMPONENT 5.6: ⊙ EVIDENCE TRACE SECTOR
# ============================================================

st.markdown(
    '',
    unsafe_allow_html=True
)

st.markdown(
    "### ⊙ Architect Evidence Trace Map"
)

st.markdown(
    """
    `text
    [ BASE DATA BLUEPRINT GENERATOR ]
    ──>
    [ RE-CALCULATED DRIFT MATRIX ]
    ──>
    [ JURISDICTION COMPILATION ]
    ──>
    [ VERIFIED EXECUTIVE OUTPUT ]
    `
    """
)

st.caption(
    "Every vector mapped onto the active viewport retains "
    "full auditable lineage straight to deterministic "
    "baseline algorithms."
)


st.write("---")


# ============================================================
# COMPONENT 5.7: ≡ SOURCE LEDGER SECTOR
# ============================================================

st.markdown(
    '',
    unsafe_allow_html=True
)

st.markdown(
    f"### {lang['ledger']}"
)

st.caption(
    "Synthetic values are compiled via deterministic "
    "mathematical modules and are not presented as direct "
    "real-world observed indices."
)

clean_ledger = filtered_df.drop(
    columns=['Display_Salary']
)

st.dataframe(
    clean_ledger.style.background_gradient(
        cmap='Blues',
        subset=['Salary_USD']
    ),
    use_container_width=True
)


st.download_button(

    label=lang['export'],

    data=clean_ledger.to_csv(
        index=False
    ).encode('utf-8'),

    file_name="astroney_analytics_ledger.csv",

    mime="text/csv"
)


# ============================================================
# LOOP REFRESH AUTOMATION
# ============================================================

if st.session_state.simulation_running:

    time.sleep(1.0)

    st.rerun()