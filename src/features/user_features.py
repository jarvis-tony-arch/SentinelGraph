import pandas as pd
def build_user_features(df):
    """
    Build user-level security features.
    """

    print("\nBuilding User Features...")

    user_features = (
        df.groupby("source_user")
        .size()
        .reset_index(name="total_events")
    )

    
    success_counts = (
        df[df["status"] == "Success"]
        .groupby("source_user")
        .size()
        .reset_index(name="success_events")
    )
    failed_counts = (
        df[df["status"] == "Fail"]
        .groupby("source_user")
        .size()
        .reset_index(name="failed_events")
    )
    unique_computers = (
            df.groupby("source_user")["source_computer"]
            .nunique()
            .reset_index(name="unique_computers")
        )
    unique_destination_computers = (
            df.groupby("source_user")["destination_computer"]
            .nunique()
            .reset_index(name="unique_destination_computers")
    )
    authentication_methods = (
        df.groupby("source_user")["authentication_type"]
        .nunique()
        .reset_index(name="unique_authentication_methods")
    )
    user_features = user_features.merge(
        success_counts,
        on="source_user",
        how="left"
    )
    user_features = user_features.merge(
        authentication_methods,
        on="source_user",
        how="left"
    )
    user_features = user_features.merge(
        unique_destination_computers,
        on="source_user",
        how="left"
    ) 

    user_features = user_features.merge(
            failed_counts,
            on="source_user",
            how="left"
    )
    user_features = user_features.merge(
        unique_computers,
        on="source_user",
        how="left"
    )
    user_features["success_events"] = user_features["success_events"].fillna(0).astype(int)
    user_features["failed_events"] = user_features["failed_events"].fillna(0).astype(int)
    user_features["failure_rate"] = (
        user_features["failed_events"] /
        user_features["total_events"]
    ) * 100
    user_features["risk_score"] = (
        user_features["failed_events"] * 5
        + user_features["failure_rate"] * 2
        + user_features["unique_computers"] * 3
    )

    

    print("\nUser Feature Table")
    print("-" * 50)
    print(user_features.head(10))

    return user_features
