import streamlit as st

st.set_page_config(page_title="I CONCEPT - Design Build Decor", layout="wide", page_icon="🏠")

st.markdown("""
<style>
    .stApp { background-color: #0A0A0A; }
    h1, h2, h3, p, span, li { color: #F5E6C8 !important; }
    .hero { background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), url('https://images.unsplash.com/photo-1618221195710-dd6b41faaea6'); background-size:cover; padding:130px 30px; text-align:center; border-radius:20px; border:1px solid #D4AF37; }
    .gold-btn { background:#D4AF37; color:#000 !important; padding:15px 35px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:16px; }
    .outline-btn { border:1px solid #D4AF37; color:#D4AF37 !important; padding:15px 35px; border-radius:8px; text-decoration:none; margin-left:15px; }
    .service-card { background:#141414; border:1px solid #222; border-left:3px solid #D4AF37; padding:20px; border-radius:10px; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
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
        <p style="margin:8px 0 0 0; color:#AAAAAA !important; font-size:14px;">📞 0312-4111011 &nbsp; | &nbsp; 📍 96 A Block Al-Hafiz Town, Marghzar Lahore</p>
    </div>
    """, unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
<div class="hero">
<h1 style="font-size:52px; color:#F5E6C8 !important;">Design • Build • Decor</h1>
<p style="font-size:20px; color:#D4AF37 !important; letter-spacing:2px;">TRANSFORMING SPACES IN LAHORE</p>
<p style="color:#CCCCCC !important;">Luxury Interiors | Custom Builds | Elegant Design Solutions</p>
<br><br>
<a class="gold-btn" href="https://wa.me/923124111011?text=Salam I CONCEPT, mujhe interior ka quote chahiye">BOOK CONSULTATION</a>
<a class="outline-btn" href="https://wa.me/923124111011">VIEW PROJECTS</a>
</div>
""", unsafe_allow_html=True)

st.write("")
c1,c2,c3 = st.columns(3)
with c1:
    st.markdown("<div class='service-card'><h4>🏠 Full House</h4><p style='color:#aaa !important;'>Complete transformation</p></div>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1618221195710-dd6b41faaea6", use_container_width=True)
with c2:
    st.markdown("<div class='service-card'><h4>🍳 Kitchen</h4><p style='color:#aaa !important;'>Modern modular kitchens</p></div>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1556911220-bff31c812dba", use_container_width=True)
with c3:
    st.markdown("<div class='service-card'><h4>🛏️ Bedrooms</h4><p style='color:#aaa !important;'>Luxury wardrobes</p></div>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1616594039964-ae9021a400a0", use_container_width=True)

st.divider()
st.markdown("""
<div style="text-align:center; padding:30px;">
<p style="color:#D4AF37 !important; font-size:18px; letter-spacing:3px;">I CONCEPT - DESIGN • BUILD • DECOR</p>
<p style="color:#888 !important;">96 A Block Al-Hafiz Town, Marghzar Lahore<br>📞 0312-4111011</p>
<br><a class="gold-btn" href="https://wa.me/923124111011">WhatsApp: 0312-4111011</a>
</div>
""", unsafe_allow_html=True)
