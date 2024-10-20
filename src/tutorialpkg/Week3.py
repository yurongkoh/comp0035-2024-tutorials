from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)

if __name__ == '__main__':
    df = pd.read_csv(Path("src/tutorialpkg/data/paralympics_events_prepared.csv"))

    print(df.dtypes)
    
    # Create a histogram of the DataFrame
    df.hist()
    summer_df = df[df['type'] == 'summer']
    winter_df = df[df['type'] == 'winter']
    summer_df.hist()
    

    # Show the plot
    plt.show()