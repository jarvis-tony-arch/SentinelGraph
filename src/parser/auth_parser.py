import pandas as pd
from src.config.settings import AUTH_LOG_FILE
from src.features.user_features import build_user_features

def validate_auth_file():
    """
    Check whether the authentication log file exists.
    """

    if AUTH_LOG_FILE.exists():
        print("✅ Authentication log file found.")
        print(f"Location : {AUTH_LOG_FILE}")
    else:
        print("❌ Authentication log file not found.")
def read_sample():
    """
    Read the authentication log file and display a sample of the data.
    """
    df = pd.read_csv(AUTH_LOG_FILE,compression="gzip",nrows=10000,header=None)
    df.columns = ["timestamp","source_user","destination_user","source_computer","destination_computer","authentication_type","logon_type","authentication_orientation","status"]

    print("\n First 10 rows  :\n")
    print(df.head(10))
    print("\nData Shape:")
    print(df.shape)
    print("\nData Types:")
    print(df.dtypes)
    print("\nAuthentication Types:")
    print(df["authentication_type"].unique())
    print("\nLogin Status:") 
    print(df["status"].value_counts())
    return df


def analyze_datasets(df):
    """
    Perform basic analysis on the authentication logs.
    """
    print("\n" + "=" * 60)
    print("      SentinelGraph  Security Report")
    print("=" * 60)

    print(f"\nTotal Authentication Events : {len(df)}")
    print("-" * 40)
    print(f"Unique Source Users      : {df['source_user'].nunique()}")
    print(f"Unique Destination Users : {df['destination_user'].nunique()}")
    print("\nComputer")
    print("-" * 40)
    print(f"Unique Source Computers    : {df['source_computer'].nunique()}")
    print(f"Unique Destination Computers : {df['destination_computer'].nunique()}")
    print("\nAuthentication Methods")
    print("-" * 40)
    print(df["authentication_type"].value_counts())
    print("\nLogin Status")
    print("-" * 40)
    print(df["status"].value_counts())
    print("\n" + "=" * 60)
    print("\nTop 10 source users")
    print("-" * 40)
    print(df["source_user"].value_counts().head(10))
    print("\nTop 10 destination users")
    print("-" * 40)
    print(df["destination_user"].value_counts().head(10))
    print("\nTop 10 Source Computers")
    print("-" * 40)
    print(df["source_computer"].value_counts().head(10))
    print("\nTop 10 Destination Computers")
    print("-" * 40)
    print(df["destination_computer"].value_counts().head(10))

    print("\nTop 10 failed login Users")
    print("-" * 40)
    failed_logins = df[df["status"] == "Fail"]
    print(failed_logins["source_user"].value_counts().head(10))
    print("\nPotential Suspicious Users")
    print("-" * 40)
    failed_counts = failed_logins["source_user"].value_counts() 
    suspicious_users = failed_counts[failed_counts >= 5]
    if suspicious_users.empty:

        print("No suspicious users detected.")
    else:

        for user, count in suspicious_users.items():
           if count >= 20:
            severity = "🔴 CRITICAL"

           elif count >= 10:
            severity = "🟠 HIGH"

           else:
            severity = "🟡 MEDIUM"

            print("=" * 50)
            print("🚨 SECURITY ALERT")
            print(f"Severity    : {severity}")
            print(f"User          : {user}")
            print(f"Failed Logins : {count}")
            print("Reason        : Exceeded failed login threshold (5)")

def main():
    print("=" * 50)
    print("SentinelGraph - Authentication Parser")
    print("=" * 50)
    validate_auth_file()
    df = read_sample()
    analyze_datasets(df)
    build_user_features(df)



if __name__ == "__main__":
    main()