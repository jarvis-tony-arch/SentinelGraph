import pandas as pd
from src.config.settings import AUTH_LOG_FILE


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

    print("\n========== Dataset Statistics ==========")
    print(f"\nTotal Events : {len(df)}")
    print(f"Unique Source Users : {df['source_user'].nunique()}")
    print(f"Unique Destination Users : {df['destination_user'].nunique()}")
    print(f"Unique Source Computers : {df['source_computer'].nunique()}")
    print(f"Unique Destination Computers : {df['destination_computer'].nunique()}")
    print("\nAuthentication Types:")
    print(df["authentication_type"].value_counts())
    print("\nLogin Status:")
    print(df["status"].value_counts())
    print("\nTop 10 Source Users:")
    print(df["source_user"].value_counts().head(10))

    print("\nTop 10 Destination Users:")
    print(df["destination_user"].value_counts().head(10))

    print("\nTop 10 Source Computers:")
    print(df["source_computer"].value_counts().head(10))

    print("\nTop 10 Destination Computers:")
    print(df["destination_computer"].value_counts().head(10))

def main():
    print("=" * 50)
    print("SentinelGraph - Authentication Parser")
    print("=" * 50)
    validate_auth_file()
    df = read_sample()
    analyze_datasets(df)



if __name__ == "__main__":
    main()