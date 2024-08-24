# Importing libraries
import pandas as pd
import psycopg2
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image

# Establish connection
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    port="5432",
    database="redbus_data",
    password="05.svidhya.17"
)

cursor = conn.cursor()

# Load bus route data from CSV files and populate lists
def load_bus_routes(filename):
    df = pd.read_csv(filename)
    return list(df["Route_name"])

lists_k = load_bus_routes("df_k.csv")
lists_A = load_bus_routes("df_A.csv")
lists_T = load_bus_routes("df_T.csv")
lists_g = load_bus_routes("df_G.csv")
lists_R = load_bus_routes("df_R.csv")
lists_SB = load_bus_routes("df_SB.csv")
lists_H = load_bus_routes("df_H.csv")
lists_AS = load_bus_routes("df_AS.csv")
lists_UP = load_bus_routes("df_UP.csv")
lists_WB = load_bus_routes("df_WB.csv")

# Setting up Streamlit page
with slt.sidebar:
    slt.set_page_config(layout="wide")
    web = option_menu(
        menu_title="🚌OnlineBus",
        options=["Home", "📍States and Routes"],
        icons=["house", "info-circle"],
        orientation="horizontal"
    )



# Home page setting
if web == "Home":
    slt.image(Image.open(r"C:/Users/TmC/Desktop/New_folder/download.png"))
    slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    slt.subheader(":blue[Domain:]  Transportation")
    slt.subheader(":blue[Objective:] ")
    slt.markdown(
        "The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry."
    )
    slt.subheader(":blue[Overview:]")
    slt.markdown(
        """Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites. Selenium allows you to simulate human interactions with a web page, such as clicking buttons, filling out forms, and navigating through pages, to collect the desired data."""
    )
    slt.markdown(
        """Pandas: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe. Pandas helps with data manipulation, cleaning, and preprocessing, ensuring that data is ready for analysis."""
    )
    slt.markdown(
        """psycopg2: With the help of psycopg2 to establish a connection to a PostgreSQL database, enabling seamless integration of the transformed dataset, and the data was efficiently inserted into relevant tables for storage and retrieval."""
    )
    slt.markdown(
        "Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis."
    )
    slt.subheader(":blue[Skill-take:]")
    slt.markdown("Selenium, Python, Pandas, psycopg2, Streamlit.")

# States and Routes page setting
if web == "📍States and Routes":
    S = slt.selectbox(
        "Lists of States", 
        ["Kerala", "Adhra Pradesh", "Telugana", "Goa", "Rajastan", 
         "South Bengal", "Haryana", "Assam", "Uttar Pradesh", "West Bengal"]
    )

    route_name = None
    if S == "Kerala":
        route_name = slt.selectbox("List of routes", lists_k)
    elif S == "Adhra Pradesh":
        route_name = slt.selectbox("List of routes", lists_A)
    elif S == "Telugana":
        route_name = slt.selectbox("List of routes", lists_T)
    elif S == "Goa":
        route_name = slt.selectbox("List of routes", lists_g)
    elif S == "Rajastan":
        route_name = slt.selectbox("List of routes", lists_R)
    elif S == "South Bengal":
        route_name = slt.selectbox("List of routes", lists_SB)
    elif S == "Haryana":
        route_name = slt.selectbox("List of routes", lists_H)
    elif S == "Assam":
        route_name = slt.selectbox("List of routes", lists_AS)
    elif S == "Uttar Pradesh":
        route_name = slt.selectbox("List of routes", lists_UP)
    elif S == "West Bengal":
        route_name = slt.selectbox("List of routes", lists_WB)

    if route_name:
        select_fare = slt.radio("Choose bus fare range", ("50-1000", "1000-2000", "2000 and above"))

        query = None
        if select_fare == "50-1000":
            query = f'''SELECT * FROM bus_details 
                        WHERE Price BETWEEN 50 AND 1000 
                        AND Route_name = '{route_name}'
                        ORDER BY Price DESC'''
        elif select_fare == "1000-2000":
            query = f'''SELECT * FROM bus_details 
                        WHERE Price BETWEEN 1000 AND 2000 
                        AND Route_name = '{route_name}'
                        ORDER BY Price DESC'''
        elif select_fare == "2000 and above":
            query = f'''SELECT * FROM bus_details 
                        WHERE Price > 2000 
                        AND Route_name = '{route_name}'
                        ORDER BY Price DESC'''

        if query:
            cursor.execute(query)
            out = cursor.fetchall()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            slt.write(df)
