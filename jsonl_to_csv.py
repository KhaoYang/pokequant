import pandas as pd
import sys
import os
import json

def jsonl_to_csv(jsonl_file, csv_file):
    """
    Converts a JSON Lines (.jsonl) file into a single standard CSV (.csv) file,
    flattening all nested JSON objects (including 'pricing') into separate columns.

    Args:
        jsonl_file (str): The path to the input .jsonl file.
        csv_file (str): The path where the output .csv file will be saved.
    """
    print(f"Starting conversion of '{jsonl_file}' to '{csv_file}'...")
    
    # 1. Check if the input file exists
    if not os.path.exists(jsonl_file):
        raise FileNotFoundError(
            f"Error: Input file not found at path: '{jsonl_file}'. "
            f"Please ensure the file exists and the path is correct."
        )

    # 2. Read the JSON Lines file into a list of dictionaries
    all_records = []
    try:
        with open(jsonl_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    record = json.loads(line)
                    # Check if the record looks like a data entry (not just metadata)
                    # A data record should typically have an 'id' or 'name' field.
                    if 'id' in record or 'name' in record:
                         all_records.append(record)
                    
                except json.JSONDecodeError as e:
                    # In case of malformed JSON line, print and continue
                    print(f"Skipping malformed JSON line: {e}")
                    continue
    except Exception as e:
        print(f"Error reading JSONL file: {e}")
        sys.exit(1)
        
    if not all_records:
        print("Error: No valid data records were found in the JSONL file.")
        sys.exit(1)


    # 3. Flatten the nested data using json_normalize
    print("\n--- Processing and Flattening Nested Data ---")
    
    try:
        # Use json_normalize on the list of records. This flattens all nested data.
        df_flattened = pd.json_normalize(
            all_records, 
            sep='.', # Use a dot separator for clarity (e.g., 'pricing.cardmarket.avg')
        )
        print(f"Data successfully flattened. Total columns: {len(df_flattened.columns)}")
        
    except Exception as e:
        # Catch any remaining normalization errors
        print(f"Error during data normalization (flattening): {e}")
        print("The data structure may be too complex or inconsistent for automatic flattening.")
        sys.exit(1)

    # 4. Write the final flattened DataFrame to a CSV file
    try:
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(csv_file) or '.', exist_ok=True)
        
        df_flattened.to_csv(csv_file, index=False, encoding='utf-8')
        print(f"\n✅ Success! Data successfully converted and saved to '{csv_file}'.")
        print(f"Total rows processed: {len(df_flattened)}")
    except Exception as e:
        print(f"Error writing CSV file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python jsonl_to_csv.py <input_file.jsonl> <output_file.csv>")
        print("Example: python jsonl_to_csv.py data/final_data.jsonl final_data.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Execute the conversion
    jsonl_to_csv(input_file, output_file)