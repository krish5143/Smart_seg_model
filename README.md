👥 Smart Customer Segmentation Model & Predictor

This project deploys a machine learning model designed to perform real-time customer segmentation for a retail business.
By analyzing key behavioral and demographic features, the application classifies customers into six high-value personas, enabling data-driven targeted marketing.

🚀 Live Application

The complete, containerized application is deployed on Render:

🔗 Live Demo (Render): https://smart-seg-model.onrender.com/

🖼️ Demo (UI Screenshot)

Below is a preview screenshot of the application UI:

✔️ Image Loaded from GitHub Folder

(Your file name is correct: smart_segment_webapp_demo.png)

![Demo Screenshot](smart_segment_webapp_demo.png)


So the rendered version will show like this:

🎯 Key Features

Real-Time Predictions:
Accepts 8 customer input features (Age, Income, Spending, etc.) and instantly returns a predicted segment.

6 Distinct Segments:
Captures both high-value and high-risk customer groups.

End-to-End MLOps Pipeline:
Full workflow from preprocessing ✔️ training ✔️ deployment ✔️ monitoring.

Streamlit Frontend:
Clean, interactive user interface for real-time inference.

💻 Technical Stack
Category	Technology	Purpose
Language	Python	Core application logic
Model	Scikit-learn (K-Means)	Unsupervised clustering (K=6)
Preprocessing	StandardScaler, PCA	Feature scaling & dimensionality reduction
Frontend	Streamlit	User UI & live prediction interface
Deployment	Render	Cloud hosting platform for the live app
Version Control	Git / GitHub	Project management & CI/CD
📊 Model Segments & Strategic Insights
Cluster	Persona Name	Characteristics	Strategic Action
0	Active Budgeters	Low spending, recent purchase activity (low churn)	Offer loyalty rewards
1	Premium Seniors	Oldest, high income, high spending	Luxury/premium product targeting
2	Omnichannel High-Value	Mid-age, high income, high spend via Web + Store	Promote unified cross-channel campaigns
3	Dormant Low Spenders	High recency, lowest spending (highest churn risk)	Run aggressive win-back campaigns
4	Older Budgeters	Moderate income, low spend, low engagement	Educate & increase engagement touchpoints
5	Young Affluent Spenders	Youngest, extremely high spend & lifetime value	Referral incentives + next-gen product focus
⚙️ How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/krish5143/Smart_segments_model.git
cd Smart_segments_model

2️⃣ Set Up Environment
python -m venv venv
.\venv\Scripts\Activate.ps1    # Windows
# OR
source venv/bin/activate       # Mac / Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
streamlit run app.py
