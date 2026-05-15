import pandas as pd
import os

print("\n=== CSV to Excel Converter ===\n")

csv_file = input("Enter CSV file path: ")

if not os.path.exists(csv_file):
    print("\n[ERROR] File not found.")
    exit()

excel_name = input("Enter output Excel file name (without .xlsx): ")

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

output_path = os.path.join(output_folder, excel_name + ".xlsx")

try:
    df = pd.read_csv(csv_file)

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df = df.fillna("Unknown")

    df.to_excel(output_path, index=False)

    print("\n[SUCCESS] Excel file created successfully!")
    print(f"Saved at: {output_path}")

except Exception as e:
    print(f"\n[ERROR] {e}")