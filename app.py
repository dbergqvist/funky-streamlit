# Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the App
st.title("Funkiest decade")

# Text
st.text("This app explores the funkinesst year of the funkiest decade")

# Create a file uploader and display the file name
uploaded_file = st.file_uploader("Choose a funky file!")

if uploaded_file is not None:
    # Read the file to a dataframe using pandas
    df = pd.read_csv(uploaded_file)
    # Create a section for the dataframe statistics
    st.header("Statistics of Dataframe")
    st.write(df.describe())
    st.header("Years 1970 - 1979")
    st.write(df[df["year"].between(1970, 1979)])
    df = df[df["year"].between(1970, 1979)]
    # plot the data
    st.header("Plot of the data")
    fig, ax = plt.subplots(1, 1)
    ax.scatter(x=df["year"], y=df["danceability"])
    ax.set_xlabel("Year")
    ax.set_ylabel("Danceability")
    st.pyplot(fig)
    # Create a line chart  of the average danceability per year
    st.header("Average danceability per year")
    fig, ax = plt.subplots(1, 1)
    # insert range slider for the x-axis
    year_range = st.slider(
        "Select a range of years", min_value=1970, max_value=1979, value=(1970, 1979)
    )
    df = df[df["year"].between(year_range[0], year_range[1])]
    ax.plot(df.groupby("year")["danceability"].mean())
    ax.set_xlabel("Year")
    ax.set_ylabel("Average danceability")
    st.pyplot(fig)
    # Create a bar chart of the average danceability per year
    st.header("Average danceability per year")
    fig, ax = plt.subplots(1, 1)
    ax.bar(
        df.groupby("year")["danceability"].mean().index,
        df.groupby("year")["danceability"].mean(),
    )
    ax.set_xlabel("Year")
    ax.set_ylabel("Average danceability")
    st.pyplot(fig)
