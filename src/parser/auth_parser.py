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
    df = pd.read_csv(AUTH_LOG_FILE,compression="gzip",nrows=5,header=None)
    print("\n First 5 rows  :\n")
    print(df)        


def main():
    print("=" * 50)
    print("SentinelGraph - Authentication Parser")
    print("=" * 50)
    validate_auth_file()
    read_sample()


if __name__ == "__main__":
    main()