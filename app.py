import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. Page Configuration
st.set_page_config(
    page_title="QuickStats Dashboard",
    page_icon="🚀",
    layout="wide"
)

# 2. Sidebar Controls
st.sidebar.header("Configuration")
st.sidebar.text("Adjust the settings below to update the chart.")

# Slider to control data points
num_points = st.sidebar.slider("Number of Data Points", min_value=10, max_value=100, value=50)

# Checkbox to toggle data view
show_raw_data = st.sidebar.checkbox("Show Raw Data", value=False)

# Button to simulate a refresh
if st.sidebar.button("Refresh Data"):
    st.cache_data.clear()

# 3. Main Content
st.title("🚀 QuickStats Interactive Dashboard")
st.markdown("""
This is a demo app to show how easy it is to build data tools in **Streamlit**.
Use the sidebar to adjust the parameters!
""")

st.divider()

# 4. Generate Mock Data
# We use a simple function to generate random data based on user input
def get_data(points):
    date_range = pd.date_range(start="2024-01-01", periods=points)
    data = pd.DataFrame(
        np.random.randn(points, 3),
        index=date_range,
        columns=['Sales', 'Profit', 'Traffic']
    )
    # Scale numbers to look realistic
    data['Sales'] = data['Sales'].abs() * 1000
    data['Profit'] = data['Profit'].abs() * 200
    data['Traffic'] = data['Traffic'].abs() * 500
    return data

df = get_data(num_points)

# 5. Metrics Row
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Sales", value=f"${df['Sales'].sum():,.2f}", delta="12%")
with col2:
    st.metric(label="Total Profit", value=f"${df['Profit'].sum():,.2f}", delta="-5%")
with col3:
    st.metric(label="Avg Daily Traffic", value=f"{int(df['Traffic'].mean())}", delta="8%")

# 6. Charts
st.subheader("📈 Trends Over Time")
# Streamlit handles interactive charts automatically
st.line_chart(df)

# 7. Raw Data Display (Conditional)
if show_raw_data:
    st.subheader("Raw Data")
    st.dataframe(df, use_container_width=True)

# 8. Interactive Form Example
st.divider()
st.subheader("📬 Feedback")
with st.form("feedback_form"):
    name = st.text_input("Your Name")
    feedback = st.text_area("Leave us a comment")
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.success(f"Thanks, {name}! We received your feedback.")