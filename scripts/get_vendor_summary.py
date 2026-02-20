import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db

# logging setup – error / process logs file me save honge
logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def create_vendor_summary(conn):
    # SQL query ko pandas dataframe me load kar rahe hain
    vendor_sales_summary = pd.read_sql_query("""
    
    -- FreightSummary: har vendor ka total freight cost
    WITH FreightSummary AS (
        SELECT
            VendorNumber,
            SUM(Freight) AS FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),

    -- PurchaseSummary: purchase + price info ko combine karke totals
    PurchaseSummary AS (
        SELECT
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price AS ActualPrice,
            pp.Volume,
            SUM(p.Quantity) AS TotalPurchaseQuantity,   -- total units purchased
            SUM(p.Dollars) AS TotalPurchaseDollars     -- total purchase amount
        FROM purchases p
        JOIN purchase_prices pp
            ON p.Brand = pp.Brand                      -- brand ke basis pe join
        WHERE p.PurchasePrice > 0                      -- invalid price filter
        GROUP BY
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price,
            pp.Volume
    ),

    -- SalesSummary: sales table se brand + vendor wise sales totals
    SalesSummary AS (
        SELECT
            VendorNo,
            Brand,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(SalesDollars) AS TotalSalesDollars,
            SUM(SalesPrice) AS TotalSalesPrice,
            SUM(ExciseTax) AS TotalExciseTax
        FROM sales
        GROUP BY VendorNo, Brand
    )

    -- Final SELECT: purchase + sales + freight sabko combine karna
    SELECT
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost
    FROM PurchaseSummary ps

    -- sales data ko left join kiya
    LEFT JOIN SalesSummary ss
        ON ps.VendorNumber = ss.VendorNo
        AND ps.Brand = ss.Brand

    -- freight data ko vendor ke basis pe join kiya
    LEFT JOIN FreightSummary fs
        ON ps.VendorNumber = fs.VendorNumber

    -- highest purchase wale vendor upar aayenge
    ORDER BY ps.TotalPurchaseDollars DESC

    """, conn)

    # final dataframe return
    return vendor_sales_summary


def clean_data(df):
    # Volume column ko float me convert kiya
    df["Volume"] = df["Volume"].astype(float)

    # missing values ko 0 se fill kiya
    df.fillna(0, inplace=True)

    # extra spaces remove kiye text columns se
    df["VendorName"] = df["VendorName"].str.strip()
    df["Description"] = df["Description"].str.strip()

    # Gross Profit = Sales - Purchase
    df["GrossProfit"] = df["TotalSalesDollars"] - df["TotalPurchaseDollars"]

    # Profit Margin %
    df["ProfitMargin"] = (df["GrossProfit"] / df["TotalSalesDollars"]) * 100

    # Stock Turnover = sold quantity / purchased quantity
    df["StockTurnover"] = df["TotalSalesQuantity"] / df["TotalPurchaseQuantity"]

    # Sales to Purchase ratio
    df["SalesToPurchaseRatio"] = df["TotalSalesDollars"] / df["TotalPurchaseDollars"]

    return df


if __name__ == '__main__':
    # creating database connection
    conn = sqlite3.connect('inventory.db')

    logging.info('Creating Vendor Summary Table.....')
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info('Cleaning Data.....')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting data.....')
    ingest_db(clean_df, 'vendor_sales_summary', conn)

    logging.info('Completed')



