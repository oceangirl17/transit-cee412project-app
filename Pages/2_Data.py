import streamlit as st
import pandas as pd

st.title("Dataset")

st.write("Our data came from the Federal Transit Authority’s **Service Data and Operating Expenses (2024)** dataset. We downloaded four CSV files with information on fares, operating expenses, passenger miles traveled, and unlinked passenger trips. One challenge was that the numbers had extra spaces and commas, which made them hard to process, so we wrote a function to clean the data and convert the values to numbers. The two main groups in our data were the different transit agencies and the different types of data (fares, ridership, etc.), and we organized our data management plan to show how these groups are connected.")

st.image("photos/erdiagram.png", caption="Above is the ER Diagram that we put together to reflect our project and serve as visual representation as to what aspects we were to look at in our research.")

st.write("Once we had a completed E/R diagram where we created a data scheme in the form of tables that allowed us to organize and find certain data. This allowed us to create line plots relating each Agency (King County and Snohomish County) to the data associated with it.")

st.image("photos/kingcounty.png", caption="Above is the table with the data for King County.")

st.image("photos/snohomishcounty.png", caption="Above is the table with the data for Snohomish County.")

