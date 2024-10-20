from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)

#3-2 histograms
def hist_plot(df):
    df.hist()

#3-3 box plots
def box_plot(df):
    #df.boxplot()
    df.boxplot(subplots=True, sharey=False)
    plt.tight_layout()

def save_png(df, name):
    save_path = Path(__file__).parent.joinpath(f'{name}_boxplot.png')
    plt.savefig(save_path)

#3-4 timeseries
def time_series(df, x_axis, y_axis):

    # Sort the DataFrame by the date column
    df = df.sort_values(by=x_axis)

    # This version draws one line for each 'type'
    # df_summer = df[df['type'] == 'summer']
    # df_winter = df[df['type'] == 'winter']
    
    # ax = df_summer.plot(x=x_axis, y=y_axis, label='Summer games')
    # df_winter.plot(x=x_axis, y=y_axis, ax=ax, label='Winter games')
    df.plot(x=x_axis, y=y_axis, label='Participants')
    plt.xticks(rotation=90)

if __name__ == '__main__':
    df = pd.read_csv(Path("src/tutorialpkg/data/paralympics_events_prepared.csv"))

    #print(df.dtypes)
    
    #3-2 histograms
    # Create a histogram of the DataFrame
    summer_df = df[df['type'] == 'summer']
    winter_df = df[df['type'] == 'winter']
    #hist_plot(summer_df)
    #hist_plot(winter_df)

    #3-3 outliers
    # Lower_Bound = Q1 − 1.5 × IQR
    # Upper_Bound = Q3 + 1.5 × IQR
    #box_plot(df)

    #saving plot to png
    # save_png(summer_df, 'summer')

    #3-4 timeseries
    #time_series(df, 'Year', 'Total')
    time_series(df, 'start', 'participants')
    #print(df)

    #show plot
    plt.show()