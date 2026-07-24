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
            .reset_index(name="unique_computers ")
        )
    user_features = user_features.merge(
        success_counts,
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

    

    print("\nUser Feature Table")
    print("-" * 50)
    print(user_features.head(10))

    return user_features
