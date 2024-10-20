import pathlib
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)

def describe_dataframe(frame):
    print(f"Data has rowsxcolumns : {frame.shape}")

def columns_to_int(df, columns):
    for column in columns:
        df[column] = df[column].astype(int)

def columns_to_float(df, columns):
    for column in columns:
        df[column] = df[column].astype(float)

#2-06
def drop_columns(df, columns):
    df_dropped = df.drop(columns, axis=1)
    return df_dropped

def remove_rows(df, row):
    df_removed = df.drop(index=row)
    return df_removed

#2-07
def identify_missing_rows(df):
    missing_rows = df[df.isna().any(axis=1)]
    #describe_dataframe(missing_rows)
    missing_rows = drop_columns(missing_rows, ['Name'])
    missing_rows = remove_rows(missing_rows, [0, 17, 31])
    #describe_dataframe(missing_rows)
    #print(missing_rows)
    missing_rows = missing_rows.reset_index(drop=True)
    #print(missing_rows)
    return missing_rows

if __name__ == '__main__':
    # Locate the data file `paralmpics_raw.csv` relative to this file
    csv_file = pathlib.Path("src/tutorialpkg/data/paralympics_events_raw.csv")
    excel_file = pathlib.Path("src/tutorialpkg/data/paralympics_all_raw.xlsx")
    npc_file_excel = pathlib.Path("src/tutorialpkg/data/npc_codes.xlsx")
    npc_file_csv = pathlib.Path("src/tutorialpkg/data/npc_codes.csv")
    # Check if the file exists
    if csv_file.exists():
        print(f"CSV file found: {npc_file_csv}")
    else:
        print("CSV file not found.")

    if excel_file.exists():
        print(f"Excel file found: {excel_file}")
    else:
        print("Excel file not found.")


    # pd.read_csv for csv files
    # pd.read_excel for xlsx files
    df1 = pd.read_excel(excel_file)
    df2 = pd.read_excel(excel_file, "medal_standings")
    df_npc_excel = pd.read_excel(npc_file_excel)
    df_npc_csv = pd.read_csv(npc_file_csv, encoding='utf-8', encoding_errors='ignore', usecols=['Code', 'Name'])

    #describe_dataframe(df1)
    #describe_dataframe(df_npc_csv)
    replacement_names = {
    'UK': 'Great Britain',
    'USA': 'United States of America',
    'Korea': 'Republic of Korea',
    'Russia': 'Russian Federation',
    'China': "People's Republic of China"}
    df1 = df1.replace(replacement_names)
    #2-04
    df1['start'] = pd.to_datetime(df1['start'], format='%d/%m/%Y')
    df1['end'] = pd.to_datetime(df1['end'], format='%d/%m/%Y')

    merged_df = df1.merge(df_npc_csv, how='left', left_on='country', right_on='Name')
    #print(merged_df[['country', 'Code', 'Name']])

    #2-06
    cols = ['URL', 'disabilities_included', 'highlights']
    df_prepared = drop_columns(df1, cols)
    #print(df1)
    #print(df_prepared)

    #DataFrame.shape - Returns the number of rows and columns in the DataFrame
    #DataFrame.head and DataFrame.tail - Returns the first / last 5 rows of the dataframe
    #DataFrame.columns - Returns the column labels
    #DataFrame.dtypes - Returns the data types in the columns of the dataframe. Columns with mixed types are stored with the object dtype.
    #DataFrame.info - Prints information about a DataFrame including the index dtype and columns, non-null values and memory usage.
    #DataFrame.describe - descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution

    columns_to_change = ['countries', 'events', 'participants_m', 'participants_f', 'participants']
    #columns_to_int(df1, ['countries'])
    #df1['countries'] = df1['countries'].astype('int')
    #print(df1['countries'])

    #2-07
    missing_rows = identify_missing_rows(merged_df)
    print(missing_rows)
    # missing_rows = merged_df[merged_df.isna().any(axis=1)]
    # describe_dataframe(missing_rows)
    # missing_rows = drop_columns(missing_rows, ['Name'])
    # missing_rows = remove_rows(missing_rows, [0, 17, 31])
    # describe_dataframe(missing_rows)
    # print(missing_rows)
    # missing_rows = missing_rows.reset_index(drop=True)
    # print(missing_rows)

    #print(missing_columns)
    #print(missing_rows)
    
    #2-08
    #print(merged_df['type'].unique())
    merged_df['type'] = merged_df['type'].str.strip().str.lower()
    print(merged_df['type'].unique())

    #2-09
    merged_df.insert(merged_df.columns.get_loc('end'), 'duration', (merged_df['end'] - merged_df['start']).dt.days.astype(int))
    
    #2-10
    merged_df.to_csv(pathlib.Path("src/tutorialpkg/data/paralympics_events_prepared.csv"), index=False)