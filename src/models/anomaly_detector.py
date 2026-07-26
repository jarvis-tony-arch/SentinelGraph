import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


def train_anomaly_detector(user_features):
    """
    Train an Isolation Forest model for anomaly detection on user features.
    """

    print("\nTraining Isoalation Forest Model...")

    feature_columns = [
        "total_events",
        "success_events",
        "failed_events",
        "failure_rate",
        "unique_computers",
        "unique_destination_computers",
        "unique_authentication_methods"

    ]

    X = user_features[feature_columns]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("\nscaled features Matrix Shape ")
    print(X_scaled.shape)

    model = IsolationForest(
        contamination = 0.02,
        random_state = 42
    )
    model.fit(X_scaled)
    print("\nIsolation Forest Model Trained Successfuly !")
    return model, scaler


