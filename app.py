import streamlit as st
import pandas as pd
import joblib

# NOTE: The cluster labels have been corrected to match the final analysis based on the centroids.
# 0: Active Budgeters (Low Value, High Recency)
# 1: Premium Seniors (Older, High Value Spenders)
# 2: Omnichannel Active Buyers (Balanced High Spend)
# 3: Dormant Low Spenders (Highest Churn Risk)
# 4: Older Budgeters (Moderate Income, Low Engagement)
# 5: Young Affluent Spenders (Highest Value, Youngest)
cluster_labels = {
    0: "Active Budgeters: Low annual spend, but highly recent purchase (Low Churn)",
    1: "Premium Seniors: Oldest group, very high income and high total spending (High Value)",
    2: "Omnichannel High-Value: Mid-range age, high income, balanced high spend across Web and Store",
    3: "Dormant Low Spenders: Lowest spending, highest recency (Highest Churn Risk)",
    4: "Older Budgeters: Moderate income, low spending, low engagement",
    5: "Young Affluent Spenders: Youngest group, highest total spending and highest value",
}

# Load model and scaler
# NOTE: These files must be present in the same directory as this Streamlit app.
try:
    kmeans = joblib.load("kmeans_model.pkl")
    scaler = joblib.load("scaler.pkl")
except FileNotFoundError:
    st.error(
        "Model files 'kmeans_model.pkl' or 'scaler.pkl' not found. Please ensure they are uploaded."
    )
    st.stop()


# Page setup
st.set_page_config(
    page_title="Customer Segmentation", page_icon="🛒", layout="centered"
)

# Custom CSS for button and result text
st.markdown(
    """
    <style>
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #FAFAFA;
        }

        .stButton > button {
            background-color: #28a745;
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 12px 24px;
            border-radius: 8px;
            border: none;
            transition: background-color 0.3s ease;
            width: 100%; /* Make the button full width of its column */
        }

        .stButton > button:hover {
            background-color: #218838;
        }

        .result-text {
            font-size: 24px;
            font-weight: 700;
            margin-top: 25px;
            padding: 15px;
            border-radius: 8px;
            background-color: #e6f7ff;
            border-left: 6px solid #1890ff;
            color: #000 !important;

        }
        .stNumberInput {
            margin-bottom: 0px; /* Adjust spacing for better form layout */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("## 👥 Customer Segmentation Predictor")

st.write(
    "Enter customer details below to predict their segment using the trained K-Means model."
)

# Input fields
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (Years)", min_value=18, max_value=100, value=45)
    income = st.number_input(
        "Income (Annual, USD)", min_value=0, max_value=200000, value=75000, step=1000
    )
    total_spending = st.number_input(
        "Total Spending (USD, Last 2 Years)", min_value=0, max_value=5000, value=1200
    )

    # Recency input
    recency = st.number_input(
        "Recency (Days since last purchase)", min_value=0, max_value=365, value=45
    )


with col2:
    num_web_purchases = st.number_input(
        "Number of Web Purchases", min_value=0, max_value=100, value=5
    )
    num_store_purchases = st.number_input(
        "Number of Store Purchases", min_value=0, max_value=100, value=7
    )
    num_web_visits = st.number_input(
        "Number of Web Visits/Month", min_value=0, max_value=50, value=6
    )

# Prediction button
st.markdown("---")
if st.button("Predict Customer Segment", key="predict_button"):
    input_data = pd.DataFrame(
        {
            "Age": [age],
            "Income": [income],
            "Total_Spending": [total_spending],
            "NumWebPurchases": [num_web_purchases],
            "NumStorePurchases": [num_store_purchases],
            "NumWebVisitsMonth": [num_web_visits],
            "Recency": [recency],
        }
    )

    # Scaling and Prediction
    input_scaled = scaler.transform(input_data)
    cluster = kmeans.predict(input_scaled)[0]
    label = cluster_labels.get(cluster, "Unknown Segment")

    # Display Result
    st.markdown(
        f"<div class='result-text'><strong>Predicted Segment (Cluster {cluster}):</strong> {label}</div>",
        unsafe_allow_html=True,
    )

st.markdown("---")
st.caption(
    "Note: This app requires 'kmeans_model.pkl' and 'scaler.pkl' files in the same directory to run."
)
