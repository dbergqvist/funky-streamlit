# Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the App
st.title("Funkiest decade")

# Text
st.text("This app explores the funkiness of the decades")

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
    df_filter = df[df["year"].between(1970, 1979)]
    # plot the data
    st.header("Plot of the data")
    fig, ax = plt.subplots(1, 1)
    ax.scatter(x=df_filter["year"], y=df_filter["danceability"])
    ax.set_xlabel("Year")
    ax.set_ylabel("Danceability")
    st.pyplot(fig)
