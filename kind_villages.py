import streamlit as st

# App title and navigation
st.title("Kind Villages Prototype")
st.sidebar.header("Navigation")
options = st.sidebar.radio(
    "Go to:", 
    ["Dashboard", "Play Dates", "Community Events", "Give Back", "Volunteer Opportunities", "Announcements"]
)

# Dashboard
if options == "Dashboard":
    st.header("Dashboard")
    st.write("Welcome to Kind Villages! Here's a quick overview of your community:")
    st.metric("Total Members", 120)
    st.metric("Upcoming Events", 5)
    st.metric("Volunteer Spots Available", 15)
