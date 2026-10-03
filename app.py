import pandas as pd
import os
import streamlit as st

FILE_NAME = "boutique_master_db.xlsx"

# 🔒 Multi-User Secure Gateways (Aap ke 4-5 logon ke alag login)
USER_CREDENTIALS = {
    "admin": "Bedar@Executive1",
    "staff1": "Bedar*Staff1",
    "staff2": "Bedar*Staff2",
    "user3": "User3_Bedar",
    "user4": "User4_Bedar"
}

def init_database():
    if not os.path.exists(FILE_NAME):
        with pd.ExcelWriter(FILE_NAME, engine="openpyxl") as writer:
            pd.DataFrame(columns=["Date", "Type", "Amount", "Narration"]).to_excel(writer, sheet_name="LedgerHistory", index=False)
            default_summary = {
                "Total Sales": 43000.0, "Logistics Received": 1631292.0, "Sales Amount Received": 0.0,
                "Total Purchases": 0.0, "Vendor Payable": 0.0, "Operating Expenses": 2103150.0,
                "Personal Expenses": 169500.0, "Stock Value": 0.0
            }
            pd.DataFrame([default_summary]).to_excel(writer, sheet_name="ExecutiveSummary", index=False)

def get_summary_data():
    try:
        return pd.read_excel(FILE_NAME, sheet_name="ExecutiveSummary").iloc[0].to_dict()
    except:
        return {"Total Sales": 0, "Logistics Received": 0, "Sales Amount Received": 0, "Total Purchases": 0, "Vendor Payable": 0, "Operating Expenses": 0, "Personal Expenses": 0, "Stock Value": 0}

def update_summary_field(field_name, amount):
    df_sum = pd.read_excel(FILE_NAME, sheet_name="ExecutiveSummary")
    df_sum.at[0, field_name] = float(amount)
    with pd.ExcelWriter(FILE_NAME, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        df_sum.to_excel(writer, sheet_name="ExecutiveSummary", index=False)

# --- MODERN INTERFACE ARCHITECTURE ---
st.set_page_config(page_title="BizBalance FinTech Node - Bedar Branded", layout="wide")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #F8FAFC; }
    .brand-banner { background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%); padding: 35px; border-radius: 20px; color: white; text-align: center; margin-bottom: 30px; box-shadow: 0 15px 30px rgba(30, 58, 138, 0.12); }
    .brand-banner h1 { margin: 0; font-size: 30px; font-weight: 700; letter-spacing: 0.5px; }
    .brand-banner p { margin: 6px 0 0 0; font-size: 13px; color: #93C5FD; font-weight: 400; }
    .block-header { font-size: 16px; font-weight: 700; color: #1E293B; margin: 30px 0 15px 0; border-left: 5px solid #3B82F6; padding-left: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
    .stat-container { background: white; padding: 24px; border-radius: 18px; box-shadow: 0 4px 12px rgba(0,0,0,0.015); border: 1px solid #E2E8F0; margin-bottom: 20px; transition: all 0.2s ease-in-out; }
    .stat-container:hover { transform: translateY(-3px); box-shadow: 0 12px 20px rgba(0,0,0,0.04); border-color: #CBD5E1; }
    .stat-label { font-size: 12px; color: #64748B; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
    .stat-amount { font-size: 26px; font-weight: 700; color: #0F172A; margin-top: 10px; }
    .exec-grid-card { padding: 26px; border-radius: 18px; color: white; box-shadow: 0 10px 25px rgba(0,0,0,0.04); }
    .status-inflow { background: linear-gradient(135deg, #059669 0%, #047857 100%); }
    .status-outflow { background: linear-gradient(135deg, #DC2626 0%, #B91C1C 100%); }
    .status-surplus { background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%); }
    .status-deficit { background: linear-gradient(135deg, #7C3AED 0%, #6D28D9 100%); }
    .card-lbl { font-size: 13px; font-weight: 600; opacity: 0.9; text-transform: uppercase; }
    .card-val { font-size: 30px; font-weight: 700; margin-top: 8px; }
    </style>
""", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.markdown("<div style='max-width: 440px; margin: 100px auto; background: white; padding: 40px; border-radius: 24px; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.08); border: 1px solid #E2E8F0;'>", unsafe_allow_html=True)
    st.subheader("🔒 BizBalance Secure Gate")
    st.write("Bedar Branded Collections Node")
    uid = st.text_input("Username / ID")
    pin = st.text_input("Security Code / Password", type="password")
    if st.button("Unlock Dashboard Node", use_container_width=True, type="primary"):
        if uid in USER_CREDENTIALS and USER_CREDENTIALS[uid] == pin:
            st.session_state["logged_in"] = True
            st.session_state["username"] = uid
            st.rerun()
        else:
            st.error("Access Denied. Incorrect Security Key.")
    st.markdown("</div>", unsafe_allow_html=True)
else:
    init_database()
    data = get_summary_data()
    total_income = data["Total Sales"] + data["Logistics Received"] + data["Sales Amount Received"]
    total_expense = data["Total Purchases"] + data["Operating Expenses"] + data["Personal Expenses"]
    net_profit = total_income - total_expense

    st.markdown(f"<div class='brand-banner'><h1>BEDAR BRANDED COLLECTIONS</h1><p>BizBalance Live Enterprise Platform • Active Operator: {st.session_state['username'].upper()}</p></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='block-header'>📊 Real-Time Financial Standings (Hamesha Active)</div>", unsafe_allow_html=True)
    r1, r2, r3 = st.columns(3)
    with r1: st.markdown(f"<div class='exec-grid-card status-inflow'><div class='card-lbl'>Total Inflow (Gross Income)</div><div class='card-val'>Rs. {total_income:,.2f}</div></div>", unsafe_allow_html=True)
    with r2: st.markdown(f"<div class='exec-grid-card status-outflow'><div class='card-lbl'>Total Outflow (Gross Expense)</div><div class='card-val'>Rs. {total_expense:,.2f}</div></div>", unsafe_allow_html=True)
    with r3:
        current_state = "status-surplus" if net_profit >= 0 else "status-deficit"
        state_label = "Net Net Balance (Profit)" if net_profit >= 0 else "Net Position (Deficit)"
        st.markdown(f"<div class='exec-grid-card {current_state}'><div class='card-lbl'>{state_label}</div><div class='card-val'>Rs. {net_profit:,.2f}</div></div>", unsafe_allow_html=True)

    st.markdown("<div class='block-header'>💼 ACTIVE ACCOUNTS REGISTRY MATRIX</div>", unsafe_allow_html=True)
    grid1, grid2, grid3, grid4 = st.columns(4)
    with grid1: st.markdown(f"<div class='stat-container'><div class='stat-label'>🛍️ Total Sales</div><div class='stat-amount'>Rs. {data['Total Sales']:,.2f}</div></div>", unsafe_allow_html=True)
    with grid2: st.markdown(f"<div class='stat-container'><div class='stat-label'>📦 Logistics Received</div><div class='stat-amount'>Rs. {data['Logistics Received']:,.2f}</div></div>", unsafe_allow_html=True)
    with grid3: st.markdown(f"<div class='stat-container'><div class='stat-label'>📥 Sales Amt Received</div><div class='stat-amount'>Rs. {data['Sales Amount Received']:,.2f}</div></div>", unsafe_allow_html=True)
    with grid4: st.markdown(f"<div class='stat-container'><div class='stat-label'>🛒 Total Purchases</div><div class='stat-amount'>Rs. {data['Total Purchases']:,.2f}</div></div>", unsafe_allow_html=True)

    grid5, grid6, grid7, grid8 = st.columns(4)
    with grid5: st.markdown(f"<div class='stat-container'><div class='stat-label'>🤝 Vendor Payable</div><div class='stat-amount'>Rs. {data['Vendor Payable']:,.2f}</div></div>", unsafe_allow_html=True)
    with grid6: st.markdown(f"<div class='stat-container'><div class='stat-label'>⚙️ Operating Expenses</div><div class='stat-amount'>Rs. {data['Operating Expenses']:,.2f}</div></div>", unsafe_allow_html=True)
    with grid7: st.markdown(f"<div class='stat-container'><div class='stat-label'>👤 Personal Expenses</div><div class='stat-amount'>Rs. {data['Personal Expenses']:,.2f}</div></div>", unsafe_allow_html=True)
    with grid8: st.markdown(f"<div class='stat-container'><div class='stat-label'>🏬 Stock Value</div><div class='stat-amount'>Rs. {data['Stock Value']:,.2f}</div></div>", unsafe_allow_html=True)

    st.sidebar.markdown("### 🛠️ Terminal Manager")
    view_mode = st.sidebar.radio("Navigation Pane:", ["Dashboard Desk", "Modify Ledger Data", "Raw Spreadsheet Sync"])
    
    if view_mode == "Modify Ledger Data":
        st.sidebar.markdown("---")
        st.sidebar.subheader("🔄 Update Account Metrics")
        target_field = st.sidebar.selectbox("Select Account Row:", list(data.keys()))
        input_value = st.sidebar.number_input("Enter Updated Amount (PKR):", min_value=0.0, value=float(data[target_field]))
        if st.sidebar.button("Push Transactions To Cloud", use_container_width=True, type="primary"):
            update_summary_field(target_field, input_value)
            st.sidebar.success("✅ Database cluster updated!")
            st.rerun()
    elif view_mode == "Raw Spreadsheet Sync":
        st.subheader("📋 Core Database Ledger Sync Check")
        try:
            excel_df = pd.read_excel(FILE_NAME, sheet_name="ExecutiveSummary")
            st.dataframe(excel_df, use_container_width=True)
        except: st.error("Database connection fault.")

    st.sidebar.markdown("---")
    if st.sidebar.button("Terminate Session (Logout)", use_container_width=True):
        st.session_state["logged_in"] = False
        st.rerun()
