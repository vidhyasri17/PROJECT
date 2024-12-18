Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit
Project Overview
The Redbus Data Scraping and Filtering with Streamlit Application is designed to streamline the transportation industry by automating the collection, analysis, and visualization of bus travel data. By using Selenium for web scraping and integrating dynamic filtering with Streamlit, this project enables better decision-making and operational efficiency.

Features
Automated Web Scraping: Extract detailed data from the Redbus website, including bus routes, schedules, prices, and seat availability.
Dynamic Filtering: Users can filter data by state, route, and price range to explore specific information.
Interactive Data Display: The application presents filtered data in an easily accessible format using Streamlit.
Database Integration: Data is stored in a PostgreSQL database for easy retrieval and manipulation.
Importing libraries
pandas psycopg2 streamlit as slt streamlit_option_menu plotly.express as px #Technologies Used Python: The core programming language used. Selenium: Automates web scraping from the Redbus website. Pandas: Data manipulation and preprocessing. psycopg2: Connects and interacts with the PostgreSQL database. Streamlit: Builds an interactive web application for data display. Plotly Express: For creating interactive visualizations.

Project Structure
redbus-data-scraping/ │ ├── REDBUS_PROJECT.py
├── requirements.txt
├── README.md
├── assets/
├── df_k.csv
├── df_A.csv ├── df_T.csv ├── df_G.csv ├── df_R.csv ├── df_SB.csv ├── df_H.csv ├── df_AS.csv ├── df_UP.csv └── df_WB.csv
