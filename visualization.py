import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(df):
    """ Plot histograms for key variables """
    df.hist(figsize=(10, 5), bins=20, edgecolor='black')
    plt.suptitle("Histogram of Features", fontsize=14)
    plt.show()

def plot_boxplots(df):
    """ Boxplots to detect outliers """
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=df[['Temperature', 'Humidity', 'Storage_Time']])
    plt.title("Boxplot of Key Variables")
    plt.show()

def plot_trend(df):
    """ Line plot to analyze spoilage over time """
    if 'Spoilage_Status' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        trend = df.groupby(df['Date'].dt.date)['Spoilage_Status'].mean()

        plt.figure(figsize=(10, 5))
        plt.plot(trend.index, trend.values, marker='o', linestyle='-', color='b')
        plt.title("Spoilage Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Average Spoilage Status")
        plt.xticks(rotation=45)
        plt.show()
