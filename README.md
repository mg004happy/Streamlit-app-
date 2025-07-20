Overview: CICIDS Intrusion Detection using XGBoost
📌 Problem Statement
Intrusion Detection Systems (IDS) are essential for monitoring network traffic and detecting malicious activities or policy violations. With the increasing sophistication of cyberattacks, traditional signature-based systems are insufficient. This project leverages machine learning to build an anomaly-based IDS that detects attacks based on patterns in traffic data, using the CICIDS2017 dataset.

📚 Dataset: CICIDS 2017 (Friday-Merged-Binary.csv)
The Canadian Institute for Cybersecurity Intrusion Detection System (CICIDS) 2017 dataset includes realistic network traffic from benign and attack scenarios. The Friday-Merged-Binary.csv file, specifically used in this project, includes:

Normal traffic: Labeled as BENIGN

Attack types: Includes DDoS, PortScan, and Bot

Each record contains a set of network traffic features (e.g., Flow Duration, Fwd Packet Length, Bwd Packet Count) and a corresponding label identifying the type of traffic.

🔄 Data Preprocessing
Before training, the dataset undergoes several cleaning steps:

Trimming whitespace from column names

Removing null values and duplicates

Label encoding the categorical target variable (Label)

Splitting the data into training and test sets (60/40 split)

🤖 Model: XGBoost Classifier
XGBoost (Extreme Gradient Boosting) is a decision-tree-based ensemble machine learning algorithm that uses a gradient boosting framework. It is widely recognized for its high performance in classification tasks due to:

Handling both linear and non-linear relationships

Built-in regularization to avoid overfitting

Parallelized training for speed

Key Parameters Used:
max_depth=6: Limits the depth of individual trees to reduce overfitting

eval_metric='logloss': Optimizes the logarithmic loss

random_state=0: Ensures reproducibility

✅ Model Evaluation
The model is evaluated on a test dataset using:

Precision: How many predicted positives are correct

Recall: How many actual positives are captured

F1-score: Harmonic mean of precision and recall

Accuracy: Overall correctness of the model

In this binary attack detection setup, the model achieves near-perfect scores, indicating excellent separation between benign and malicious traffic.

🌐 Deployment: Streamlit Web Application
To make the model interactive, it is deployed using Streamlit, a Python-based framework for building web apps. Key components of the app include:

Dynamic Input Fields: Users enter values for each feature

Prediction Output: The predicted class (BENIGN, DDoS, Bot, PortScan)

Confidence Scores: Displayed as a probability bar chart for interpretability

📦 Saved Artifacts
Three files are saved using joblib for deployment:

cicids_rf_model.pkl: Trained XGBoost model

cicids_label_encoder.pkl: LabelEncoder to decode predictions

cicids_features.pkl: Feature list required for input

💡 Benefits of This Approach
Automated Detection: Detects known and unknown attacks based on traffic behavior

High Accuracy: Tree-based models like XGBoost handle outliers and skewed data well

Scalability: Can be extended to multiclass detection or integrated into real-time systems
