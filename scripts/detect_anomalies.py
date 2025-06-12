"""
Detects anomalies in AWS API activity logs using Isolation Forest.
"""

import pandas as pd
from sklearn.ensemble import IsolationForest

# Load log data (mocked as CSV here)
df = pd.read_csv("mock_cloudtrail_logs.csv")

# Select relevant features
features = df[["eventTime", "eventSource", "userIdentity.type"]]

# Preprocess and encode
X = pd.get_dummies(features)

# Fit the model
model = IsolationForest(contamination=0.05)
df["anomaly_score"] = model.fit_predict(X)

# Output anomalies
anomalies = df[df["anomaly_score"] == -1]
anomalies.to_csv("detected_anomalies.csv", index=False)
print("Anomalies detected and exported.")
