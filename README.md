👥 Smart Customer Segmentation Model & Predictor

This project deploys a machine learning model designed to perform real-time customer segmentation for a retail business. By analyzing key behavioral and demographic features, the application classifies new customers into one of six distinct, high-value personas, enabling targeted marketing campaigns.

🚀 Live Application

The final, fully containerized application is deployed live on Render:

[Live Demo Link (Render):] https://smart-seg-model.onrender.com/

🎯 Key Features

Real-time Inference: Accepts 8 customer input features (Age, Income, Spending, etc.) and returns the predicted segment immediately.

6 Distinct Segments: Identifies high-value groups (e.g., 'Young Affluent Spenders') and high-risk groups (e.g., 'Dormant Low Spenders') for strategic action.

End-to-End MLOps: Showcases the full lifecycle of a Data Science project, from model training to cloud deployment.

💻 Technical Stack

Category

Technology

Purpose

Language

Python

Core logic and scripting.

Model

Scikit-learn (K-Means)

Unsupervised clustering for segmentation (K=6).

Preprocessing

StandardScaler, PCA

Feature scaling and dimensionality reduction for visualization.

Frontend

Streamlit

Interactive, user-friendly web interface for input and prediction.

Deployment

Render

Cloud platform hosting the live Streamlit application.

Version Control

Git / GitHub

Continuous deployment (CI/CD) and project management.

📊 Model Segments and Strategic Insights

The K-Means model identified 6 highly actionable customer clusters. The Streamlit app provides the following strategic insights for each segment:

Cluster

Persona Title

Key Characteristics

Strategic Action

0

Active Budgeters

Low annual spend, but highly recent purchase (Low Churn).

Retention: Offer loyalty points or small discounts to increase overall basket size.

1

Premium Seniors

Oldest group, very high income and high total spending (High Value).

Exclusive Offers: Target with high-margin, luxury items and personalized service.

2

Omnichannel High-Value

Mid-range age, high income, balanced high spend across Web and Store.

Cross-Channel Upsell: Promote new product lines via unified online/in-store campaigns.

3

Dormant Low Spenders

Lowest spending, highest recency (Highest Churn Risk).

Reactivation: Implement an aggressive win-back campaign (deep discounts or free shipping).

4

Older Budgeters

Moderate income, low spending, low engagement.

Education: Focus on product use-cases and value to increase engagement frequency.

5

Young Affluent Spenders

Youngest group, highest total spending and highest value.

Growth: Feature next-generation products; incentivize referrals for similar demographics.

⚙️ How to Run Locally

You can run this predictor application locally by following these steps:

Clone the Repository:

git clone [https://github.com/krish5143/Smart_segments_model.git](https://github.com/krish5143/Smart_segments_model.git)
cd Smart_segments_model


Setup Environment (Recommended):

# Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1  # (Use 'source venv/bin/activate' on Linux/Mac)


Install Dependencies:

pip install -r requirements.txt


Run the Application:

streamlit run app.py


The application will open in your default browser at http://localhost:8501.
