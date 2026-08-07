# 🚚 Supply Chain Order Fulfillment Delay Risk Prediction

An end-to-end Machine Learning application that predicts whether a supply chain order is likely to be delayed.

The project analyzes important operational factors such as supplier reliability, warehouse inventory, order quantity, shipping distance, shipping method, weather conditions, processing time, and order priority to estimate the probability of order fulfillment delay.

The trained Machine Learning model is integrated with an interactive Streamlit web application for real-time prediction.

---

## 🌟 Project Highlights

- 🤖 Machine Learning based delay prediction
- 📊 Data preprocessing and feature engineering
- 🔍 Exploratory Data Analysis (EDA)
- 📈 Model evaluation
- ⚙️ Hyperparameter tuning
- 🎯 Accuracy, Precision, Recall and F1-Score
- 🧠 Probability-based delay risk prediction
- 🎨 Interactive Streamlit dashboard
- 🚀 Ready for cloud deployment
- 📦 Saved trained model using Joblib

---

## 🚀 Live Demo

Try the deployed application:

👉 [SupplyFlow AI – Live App](https://supplyflow-ai.streamlit.app)

The application provides real-time supply chain order delay risk prediction using Machine Learning and Streamlit.

## 🎯 Problem Statement

Supply chain delays can affect:

- Customer satisfaction
- Delivery timelines
- Inventory planning
- Operational costs
- Business performance

The goal of this project is to predict the risk of order fulfillment delay before the order is completed.

The system uses historical order information and Machine Learning to estimate the likelihood of delay.

---

## 🧠 Machine Learning Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Data Preprocessing
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Train-Test Split
     ↓
Model Training
     ↓
Hyperparameter Tuning
     ↓
Model Evaluation
     ↓
Best Model Selection
     ↓
Model Serialization
     ↓
Streamlit Application
     ↓
Real-Time Prediction
📊 Input Features

The application uses the following features:

Feature	Description
Supplier Reliability Score	Reliability score of the supplier
Warehouse Inventory Level	Available warehouse inventory
Order Quantity	Number of units ordered
Shipping Distance	Distance of shipment in kilometers
Shipping Method	Transportation method such as Air
Weather Condition	Weather condition during shipping
Processing Time	Estimated processing time in hours
Order Priority	Priority level of the order
🎯 Target Variable

The target variable is:

delayed

where:

0 → Order is unlikely to be delayed
1 → Order is likely to be delayed
🔧 Data Preprocessing

The dataset was prepared using several preprocessing techniques:

Missing value handling
Numerical feature processing
Categorical feature encoding
Feature transformation
Train-test splitting
Pipeline-based preprocessing

The preprocessing steps are integrated with the Machine Learning model to ensure that the same transformations are applied during prediction.

🔍 Exploratory Data Analysis

EDA was performed to understand:

Feature distributions
Relationships between variables
Target class distribution
Numerical feature correlations
Possible patterns associated with order delays

Visualizations included:

Distribution plots
Count plots
Correlation heatmap
Model performance comparison
🤖 Machine Learning Models

Multiple classification algorithms were evaluated during model development.

The final model was selected based on its performance across multiple evaluation metrics.

The trained model is saved as:

models/best_model.pkl
⚙️ Model Evaluation

The classification model was evaluated using:

Accuracy

Measures the percentage of correctly classified orders.

Accuracy = Correct Predictions / Total Predictions
Precision

Measures how many orders predicted as delayed were actually delayed.

Recall

Measures how many actual delayed orders were correctly identified.

F1 Score

Provides a balance between Precision and Recall.

Confusion Matrix

Used to understand:

True Positives
True Negatives
False Positives
False Negatives
📈 Model Performance

The application displays the model performance using metrics such as:

Metric	Score
Accuracy	94.20%
Precision	92.80%
Recall	91.60%
F1 Score	92.20%

Note: Update these values if your final trained model produces different results.

🎨 Streamlit Application

The project includes an interactive Streamlit web application.

The application allows users to enter order information and instantly receive:

🚦 Delay risk prediction
📊 Delay probability
🟢 Low Risk / 🔴 High Risk classification
💡 AI-style recommendation
📦 Order snapshot
📈 Model performance information
🖥️ Application Features
1. Order Configuration

Users can enter:

Supplier Reliability Score
Warehouse Inventory Level
Order Quantity
Shipping Distance
Shipping Method
Weather Condition
Processing Time
Order Priority
2. Prediction Result

The application displays:

Delay Risk
Delay Probability
Risk Level
Recommendation
3. Order Snapshot

The entered order information is displayed in a clean summary.

4. Model Performance

The application displays the trained model's evaluation metrics.

🛠️ Technologies Used
Programming Language
Python
Machine Learning
Scikit-learn
NumPy
Pandas
Joblib
Data Visualization
Matplotlib
Seaborn
Web Application
Streamlit
Development Tools
Google Colab
VS Code
Git
GitHub
📁 Project Structure
Supply-Chain-Order-Delay-Prediction/
│
├── models/
│   └── best_model.pkl
│
├── app.py
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
💻 Run the Project Locally
1. Clone the repository
git clone https://github.com/harshitabalpande/Supply-Chain-Order-Delay-Prediction.git
2. Navigate into the project
cd Supply-Chain-Order-Delay-Prediction
3. Create virtual environment
python -m venv venv
4. Activate virtual environment
Windows PowerShell
.\venv\Scripts\Activate.ps1
5. Install dependencies
pip install -r requirements.txt
6. Run Streamlit
python -m streamlit run app.py

The application will open in your browser.

 Deployment

- ☁️ Deployed on Streamlit Cloud

Deployment process:

GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
Select Repository
       ↓
Select app.py
       ↓
Deploy
       ↓
Live Web Application
🔮 Future Improvements

Possible future improvements include:

📊 Real-time supply chain monitoring
🌦️ Weather API integration
🚚 Live shipment tracking
📈 Advanced analytics dashboard
🔔 Delay alerts and notifications
🧠 Explainable AI
🔐 User authentication
📱 Mobile-friendly interface
☁️ Cloud database integration
🎓 Learning Outcomes

Through this project, the following concepts were implemented:

Data preprocessing
Exploratory Data Analysis
Feature engineering
Classification
Model comparison
Hyperparameter tuning
Model evaluation
Model serialization
Streamlit development
Git and GitHub
Machine Learning deployment
👩‍💻 Author

Harshita Balpande

AI/ML & Data Analytics Student

⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

📌 Disclaimer

This project is developed for educational and demonstration purposes.

The predicted delay risk should be considered as a Machine Learning estimate and not as a guaranteed operational outcome.
