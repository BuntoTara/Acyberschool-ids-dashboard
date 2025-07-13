
import streamlit as st
import pandas as pd
import numpy as np

# Basic IDS Dashboard Setup
st.set_page_config(page_title="Network IDS", layout="wide")
st.title("🛡️ Intrusion Detection Dashboard")

# Create sample data
import streamlit as st
import pandas as pd
import joblib
from utils import run_detection, generate_report, visualize_data

# Styling
BARCLAYS_BLUE = "#00395D"
GREY = "#B0B0B0"

st.set_page_config(page_title="Network IDS", layout="wide")
st.markdown(f"<h1 style='color:{BARCLAYS_BLUE};'>🛡️ Intrusion Detection Dashboard</h1>", unsafe_allow_html=True)

# Upload network traffic data
uploaded_file = st.file_uploader("📎 Upload a CSV or Excel file", type=["csv", "xlsx"])
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
        st.success("✅ File uploaded successfully.")
        st.dataframe(df.head())

        # Run detection using the ML model
        if st.button("🛡️ Run Detection"):
            model = joblib.load("models/network_guard_model.pkl")
            result_df = run_detection(df, model)
            st.dataframe(result_df)

        # Generate Report
        if st.button("📄 Generate Report"):
            path = generate_report(df)
            st.success(f"📁 Report saved: {path}")

        # Visualize
        if st.button("📊 Visualize Data"):
            visualize_data(df)

    except Exception as e:
        st.error(f"❌ Error: {e}")
if st.button("Generate Demo Data"):
    data = pd.DataFrame({
        "timestamp": pd.date_range(end=pd.Timestamp.now(), periods=100, freq="S"),
        "source_ip": ["192.168.1." + str(i) for i in range(1, 101)],
        "destination_ip": ["10.0.0." + str(i) for i in range(1, 101)],
        "packet_size": np.random.randint(64, 1500, 100),
        "protocol": np.random.choice(["TCP", "UDP", "ICMP", "HTTP"], 100),
        "anomaly": np.random.choice([0, 1], 100, p=[0.9, 0.1])
    })
    
    st.session_state.network_data = data
    st.success("Generated 100 sample packets!")
    
if 'network_data' in st.session_state:
    st.subheader("Network Traffic Sample")
    st.dataframe(st.session_state.network_data.head(10))
    
    st.subheader("Protocol Distribution")
    protocol_counts = st.session_state.network_data['protocol'].value_counts()
    st.bar_chart(protocol_counts)
