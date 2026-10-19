import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="I CONCEPT - Design Build Decor", layout="wide", page_icon="🏠")

# --- NEW THEME CSS - BLACK & GOLD ---
st.markdown("""
<style>
    .stApp { background-color: #0A0A0A; }
    h1, h2, h3, p, span, li { color: #F5E6C8 !important; }
    .header-box { background:#0A0A0A; border-bottom:2px solid #D4AF37; padding:15px 20px; display:flex; align-items:center; }
    .hero { background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), url('https://images.unsplash.com/photo-1618221195710-dd6b41faaea6'); background-size:cover; padding:130px 30px; text-align:center; border-radius:20px; border:1px solid #D4AF37; }
    .gold-btn { background:#D4AF37; color:#000 !important; padding:15px 35px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:16px; }
    .outline-btn { border:1px solid #D4AF37; color:#D4AF37 !important; padding:15px 35px; border-radius:8px; text-decoration:none; margin-left:15px; }
    .service-card { background:#141414; border:1px solid #222; border-left:3px solid #D4AF37; padding:20px; border-radius:10px; }
</style>
""", unsafe_allow_html=True)

# --- NEW HEADER WITH LOGO + I CONCEPT ---
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("logo.png", width=140)
    except:
        st.markdown("<h2 style='color:#D4AF37;'>I CONCEPT</h2>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="padding-top:15px;">
        <h2 style="margin:0; color:#D4AF37 !important; letter-spacing:3px; font-family: serif;">I CONCEPT</h2>
        <p style="margin:0; color:#D4AF37 !important; letter-spacing:5px; font-size:13px;">DESIGN • BUILD • DECOR</p>
        <p style="margin:8px 0 0 0; color:#AAAAAA !important; font-size:14px;">📞 0339-9292000 • 0312-4111011 &nbsp; | &nbsp; 📍 96 A Block Al-Hafiz Town, Marghzar Lahore</p>
    </div>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero">
<h1 style="font-size:52px; color:#F5E6C8 !important; margin-bottom:10px;">Design • Build • Decor</h1>
<p style="font-size:20px; color:#D4AF37 !important; letter-spacing:2px;">TRANSFORMING SPACES IN LAHORE</p>
<p style="color:#CCCCCC !important; max-width:700px; margin:20px auto;">Luxury Interiors | Custom Builds | Elegant Design Solutions for Modern Homes - Kitchens, Bedrooms, Living & Offices</p>
<br><br>
<a class="gold-btn" href="https://wa.me/923399292000?text=Salam I CONCEPT, mujhe interior ka quote chahiye">BOOK CONSULTATION</a>
<a class="outline-btn" href="https://wa.me/923399292000">VIEW PROJECTS</a>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# --- SERVICES ---
st.markdown("<h2 style='color:#D4AF37 !important;'>Our Expertise</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("<div class='service-card'><h4>🏠 Full House Interior</h4><p style='color:#aaa !important;'>Complete home transformation from concept to completion.</p></div>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1618221195710-dd6b41faaea6", use_container_width=True)
with c2:
    st.markdown("<div class='service-card'><h4>🍳 Modular Kitchen</h4><p style='color:#aaa !important;'>Modern, functional kitchens with premium finishes.</p></div>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1556911220-bff31c812dba", use_container_width=True)
with c3:
    st.markdown("<div class='service-card'><h4>🛏️ Bedrooms & Wardrobes</h4><p style='color:#aaa !important;'>Luxury wardrobes and cozy bedroom designs.</p></div>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1616594039964-ae9021a400a0", use_container_width=True)

st.divider()

# --- FOOTER ---
st.markdown("""
<div style="text-align:center; padding:30px; border-top:1px solid #222;">
<p style="color:#D4AF37 !important; font-size:18px; letter-spacing:3px;">I CONCEPT - DESIGN • BUILD • DECOR</p>
<p style="color:#888 !important;">Trusted by 200+ Clients in Lahore | Est. 2018<br>96 A Block Al-Hafiz Town, Marghzar Lahore<br>0339-9292000 • 0312-4111011</p>
<br>
<a class="gold-btn" href="https://wa.me/923399292000">Contact on WhatsApp</a>
</div>
""", unsafe_allow_html=True)
