import pandas as pd

def load_and_clean_data():
    """Load the dataset and remove duplicate columns."""
    df = pd.read_csv('all_data.csv')

    df = df.loc[:, ~df.columns.str.endswith('.1')]

    df['dteday'] = pd.to_datetime(df['dteday'])
    
    return df

import plotly.express as px

def plot_total_rentals_over_time(df):
    fig = px.line(df, x='dteday', y='cnt', title='Total Bike Rentals Over Time',
                  labels={'dteday': 'Date', 'cnt': 'Total Rentals'})
    return fig

def plot_rentals_by_season(df):
    fig = px.bar(df, x='season', y='cnt', title='Total Bike Rentals by Season',
                 labels={'season': 'Season', 'cnt': 'Total Rentals'},
                 category_orders={'season': [1, 2, 3, 4]})  # 1: Winter, 2: Spring, 3: Summer, 4: Fall
    return fig

def plot_rentals_by_weather(df):
    fig = px.box(df, x='weathersit', y='cnt', title='Bike Rentals by Weather Situation',
                 labels={'weathersit': 'Weather Condition', 'cnt': 'Total Rentals'},
                 category_orders={'weathersit': [1, 2, 3, 4]})  # Weather categories 1 to 4
    return fig

def plot_rentals_by_hour(df):
    hourly_rentals = df.groupby('hr')['cnt'].mean().reset_index()
    fig = px.bar(hourly_rentals, x='hr', y='cnt', title='Average Bike Rentals by Hour',
                 labels={'hr': 'Hour of Day', 'cnt': 'Average Rentals'})
    return fig

def plot_rentals_vs_temperature(df):
    fig = px.scatter(df, x='temp', y='cnt', title='Bike Rentals vs Temperature',
                     labels={'temp': 'Temperature (Normalized)', 'cnt': 'Total Rentals'})
    return fig

import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_heatmap(df):
    corr = df.corr()
    plt.figure(figsize=(16, 12))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    st.pyplot(plt)

import streamlit as st

df = load_and_clean_data()

st.sidebar.title("Bike Sharing Data Visualizations")
vis_option = st.sidebar.selectbox("Choose a visualization", 
                                  ["Total Rentals Over Time", 
                                   "Rentals by Season",
                                   "Rentals by Weather Situation",
                                   "Rentals by Hour",
                                   "Rentals vs Temperature",
                                   "Correlation Heatmap"])

if vis_option == "Total Rentals Over Time":
    st.markdown("### Total Bike Rentals Over Time")
    st.write("This line chart show the total number of bike rental for each day. "
             "It provides insights into overal usage patterns and trends over time.")
    st.plotly_chart(plot_total_rentals_over_time(df))

elif vis_option == "Rentals by Season":
    st.markdown("### Bike Rentals by Season")
    st.write("This bar chart shows the total number of bike rentals across different season. "
             "It helps to observe any seasonal trends in bike rentals. ")
    st.plotly_chart(plot_rentals_by_season(df))

elif vis_option == "Rentals by Weather Situation":
    st.markdown("### Bike Rentals by Weather Condition")
    st.write("This box plot shows the distribution of bike rentals across different weather condition. "
             "The weather condition are categorized into 1 (Clear), 2 (Misty/Cloudy), and 3 (Light Snow/Rain). "
             "It helps understand how different wether condition affect user behavor.")
    st.plotly_chart(plot_rentals_by_weather(df))

elif vis_option == "Rentals by Hour":
    st.markdown("### Average Bike Rentals by Hour")
    st.write("This bar chart displays the average number of bike rentals at each hour of the day. "
             "It helps to identify peak hours for bike rentals, which are typically early mornings and late afternoons, coinciding with commuting times.")
    st.plotly_chart(plot_rentals_by_hour(df))

elif vis_option == "Rentals vs Temperature":
    st.markdown("### Relationship Between Bike Rentals and Temperature")
    st.write("This scatter plots show how bike rentals change with temperature. "
             "Generally, warmer temperatures are associated with more bike rentals.")
    st.plotly_chart(plot_rentals_vs_temperature(df))

elif vis_option == "Correlation Heatmap":
    st.markdown("### Correlation Heatmap of Numerical Features")
    st.write("This heatmap show the correlation between various numerical features in the dataset. "
             "Hight correlation (closer to 1 or -1) indicate a strong relationship between variables, "
             "while values close to 0 indicate little to no relationship.")
    plot_correlation_heatmap(df)
