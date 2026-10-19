import streamlit as st

st.set_page_config(page_title="Interior Studio | Lahore", layout="wide", page_icon="🏠")

# --- CUSTOM CSS ---
st.markdown("""
<style>
.hero { background-color: #1a1a1a; padding: 80px 40px; color: white; text-align: center; border-radius: 15px; }
.service-card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-align: center; }
.btn { background: #C19A5B; color: white; padding: 12px 30px; border-radius: 30px; text-decoration: none; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="hero"><h1>Your Space, Our Design</h1><p>Premium Interior Solutions in Lahore - Kitchen | Bedroom | Office</p><br><a class="btn" href="https://wa.me/923000000000">Get Free Quotation on WhatsApp</a></div>', unsafe_allow_html=True)

st.write("---")

# --- SERVICES ---
st.header("Our Services")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://images.unsplash.com/photo-1556911220-bff31c812dba", caption="Modular Kitchen")
    st.write("**Modular Kitchen** - Modern & Functional")
with col2:
    st.image("https://images.unsplash.com/photo-1616594039964-ae9021a400a0", caption="Bedroom Interior")
    st.write("**Bedroom Design** - Luxury & Comfort")
with col3:
    st.image("https://images.unsplash.com/photo-1497366216548-37526070297c", caption="Office Interior")
    st.write("**Office / Commercial** - Professional Look")

st.write("---")

# --- PORTFOLIO ---
st.header("Our Recent Work")
p1, p2, p3, p4 = st.columns(4)
p1.image("https://images.unsplash.com/photo-1586023492125-27b2c045efd7")
p2.image("https://images.unsplash.com/photo-1618221195710-dd6b41faaea6")
p3.image("https://images.unsplash.com/photo-1615874959474-d609969a20ed")
p4.image("https://images.unsplash.com/photo-1616046229478-9901c5536a45")

st.write("---")

# --- CONTACT ---
st.header("Contact Us for Free Visit")
st.write("📍 Location: Lahore | 📞 Call: 0300-0000000")
name = st.text_input("Your Name")
phone = st.text_input("Phone Number")
msg = st.text_area("Tell us about your project (e.g., 5 Marla House Full Interior)")
if st.button("Send Inquiry"):
    st.success(f"Thanks {name}! We will contact you soon on {phone} for quotation.")
    st.balloons()
