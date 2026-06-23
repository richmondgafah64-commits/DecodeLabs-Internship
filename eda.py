import pandas as pd


def main():
    # Load dataset
    df = pd.read_excel("final_cleaned.xlsx")

    # Basic overview
    print("=" * 50)
    print("📊 DATASET OVERVIEW")
    print("=" * 50)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nDataset Information:")
    df.info()

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nDescriptive Statistics:")
    print(df.describe())

    # Business insights section
    print("\n" + "=" * 50)
    print("📈 BUSINESS INSIGHTS")
    print("=" * 50)

    print(f"\nTotal Revenue: {df['total_price'].sum():,.2f}")
    print(f"Average Order Value: {df['total_price'].mean():,.2f}")

    print("\nProducts Sold:")
    print(df["product"].value_counts())

    print("\nPayment Methods:")
    print(df["payment_method"].value_counts())

    print("\nOrder Status:")
    print(df["order_status"].value_counts())

    print("\nReferral Sources:")
    print(df["referral_source"].value_counts())


if __name__ == "__main__":
    main()