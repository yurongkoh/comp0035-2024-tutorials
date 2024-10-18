import pathlib
import pandas as pd

def describe_dataframe(frame):
    print(f"Data has rowsxcolumns : {frame.shape}")

def columns_to_int(df, columns):
    for column in columns:
        df[column] = df[column].astype(int)

def columns_to_float(df, columns):
    for column in columns:
        df[column] = df[column].astype(float)

if __name__ == '__main__':
    # Locate the data file `paralmpics_raw.csv` relative to this file
    csv_file = pathlib.Path("src/tutorialpkg/data/paralympics_events_raw.csv")
    excel_file = pathlib.Path("src/tutorialpkg/data/paralympics_all_raw.xlsx")
    # Check if the file exists
    if csv_file.exists():
        print(f"CSV file found: {csv_file}")
    else:
        print("CSV file not found.")

    if excel_file.exists():
        print(f"Excel file found: {excel_file}")
    else:
        print("Excel file not found.")


# pd.read_csv for csv files
# pd.read_excel for xlsx files
    readcsv = pd.read_csv(csv_file)
    df1 = pd.read_excel(excel_file)
    df2 = pd.read_excel(excel_file, "medal_standings")
    print(df1.dtypes)

    #DataFrame.shape - Returns the number of rows and columns in the DataFrame
    #DataFrame.head and DataFrame.tail - Returns the first / last 5 rows of the dataframe
    #DataFrame.columns - Returns the column labels
    #DataFrame.dtypes - Returns the data types in the columns of the dataframe. Columns with mixed types are stored with the object dtype.
    #DataFrame.info - Prints information about a DataFrame including the index dtype and columns, non-null values and memory usage.
    #DataFrame.describe - descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution

    columns_to_change = ['countries', 'events', 'participants_m', 'participants_f', 'participants']
    #columns_to_float(df1, ['year'])
    #df1['countries'] = df1['countries'].astype('int')
    #print(df1.dtypes)