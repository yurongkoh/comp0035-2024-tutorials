import pathlib
import pandas as pd


if __name__ == '__main__':
    # Locate the data file `paralmpics_raw.csv` relative to this file
    csv_file = pathlib.Path("src/tutorialpkg/data/paralympics_events_raw.csv")
    # Check if the file exists
    if csv_file.exists():
        print(f"CSV file found: {csv_file}")
    else:
        print("CSV file not found.")

    read = pd.read_csv(csv_file)
    print(read)