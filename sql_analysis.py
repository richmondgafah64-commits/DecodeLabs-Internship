import pandas as pd
import sqlite3


def main():
    # LOAD CLEAN DATASET
    df = pd.read_excel("final_cleaned.xlsx")

    # CREATE SQLITE DATABASE
    
    conn = sqlite3.connect("orders.db")

    df.to_sql("orders", conn, if_exists="replace", index=False)

    print("=" * 50)
    print("DATABASE CREATED SUCCESSFULLY")
    print("=" * 50)

    # SQL QUERIES
    # 1. Preview data
    query = """
    SELECT *
    FROM orders
    LIMIT 7;
    """
    result = pd.read_sql(query, conn)
    print("\n📊 SAMPLE DATA (FIRST 7 ROWS)")
    print(result)

    # 2. Filter data
    query = """
    SELECT *
    FROM orders
    WHERE payment_method = 'Email';
    """
    result = pd.read_sql(query, conn)
    print("\n💳 PAYMENT METHOD = EMAIL")
    print(result)

    # 3. Sort data
    query = """
    SELECT *
    FROM orders
    ORDER BY total_price DESC;
    """
    result = pd.read_sql(query, conn)
    print("\n📈 TOP ORDERS BY REVENUE")
    print(result.head())

    # 4. Group by product
    query = """
    SELECT product,
           COUNT(*) AS total_orders
    FROM orders
    GROUP BY product;
    """
    result = pd.read_sql(query, conn)
    print("\n📦 TOTAL ORDERS PER PRODUCT")
    print(result)

    # 5. Total orders
    query = """
    SELECT COUNT(*) AS total_orders
    FROM orders;
    """
    result = pd.read_sql(query, conn)
    print("\n📊 TOTAL ORDERS")
    print(result)

    # 6. Total revenue
    query = """
    SELECT SUM(total_price) AS total_revenue
    FROM orders;
    """
    result = pd.read_sql(query, conn)
    print("\n💰 TOTAL REVENUE")
    print(result)

    # 7. Average order value
    query = """
    SELECT AVG(total_price) AS average_order_value
    FROM orders;
    """
    result = pd.read_sql(query, conn)
    print("\n📉 AVERAGE ORDER VALUE")
    print(result)

    # Close connection (important in real projects)
    conn.close()
    print("\n🔒 DATABASE CONNECTION CLOSED")


if __name__ == "__main__":
    main()