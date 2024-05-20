# main.py
import pandas as pd
from fetch_product_links import fetch_and_save_product_links
from extract_product_info import extract_and_save_product_info
from config.websites import websites

# Convert websites to DataFrame
df = pd.DataFrame(websites, columns=["Website"])

# Fetch and save product links
fetch_and_save_product_links(df)

# Extract and save product information
extract_and_save_product_info()
