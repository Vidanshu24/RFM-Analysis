import pandas as pd

# Load CSV file
df = pd.read_csv("D:/online2.csv")

# Check column names
print(df.columns)

# Use the correct column name here
df = df[df["Customer ID"].notnull()]  # or "Customer ID" if your file has space

# Remove canceled orders
df = df[~df['Invoice'].astype(str).str.startswith('C')]

# Remove zero/negative quantity or price
df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]

# Calculate TotalAmount
df['Total Amount'] = df['Quantity'] * df['Price']

# Export clean file
df.to_csv("D:/clean_retail.csv", index=False)

print("✅ Cleaned data exported to D:/clean_retail.csv")
