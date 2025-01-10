import streamlit as st

# App title and navigation
st.title("Kind Villages Prototype")
st.sidebar.header("Navigation")
options = st.sidebar.radio(
    "Go to:", 
    ["Dashboard", "Play Dates", "Community Events", "Give Back", "Volunteer Opportunities", "Announcements"]
)

# walk through for first time visitors
if "first_visit" not in st.session_state:
    st.session_state.first_visit = True
if st.session_state.first_visit:
    st.info("Welcome to Kind Villages! Use the sidebar to explore features.")
    if st.button("Got It"):
        st.session_state.first_visit = False
# Dashboard
if options == "Dashboard":
    st.header("Dashboard")
    st.write("Welcome to Kind Villages! Here's a quick overview of your community:")
    st.metric("Total Members", 120)
    st.metric("Upcoming Events", 5)
    st.metric("Volunteer Spots Available", 15)
    # Play Dates
elif options == "Play Dates":
    st.header("Play Dates")
    st.write("Connect with others for play dates!")
    play_dates = [
        {"Host": "Sarah L.", "Date": "2025-01-15", "Location": "Central Park", "Kids": 3},
        {"Host": "Tom H.", "Date": "2025-01-20", "Location": "Community Center", "Kids": 2},
    ]
    for pd in play_dates:
        st.write(f"**Host**: {pd['Host']} | **Date**: {pd['Date']} | **Location**: {pd['Location']} | **Kids**: {pd['Kids']}")
    st.text_input("Host Name:")
    st.date_input("Date:")
    st.text_input("Location:")
    st.number_input("Number of Kids:", min_value=1, max_value=20, step=1)
    st.button("Post Play Date")

# Community Events
elif options == "Community Events":
    st.header("Community Events")
    st.write("Discover or create events for the community!")
    events = [
        {"Event": "Winter Carnival", "Date": "2025-01-25", "Location": "Town Square"},
        {"Event": "Book Drive", "Date": "2025-02-05", "Location": "Library"},
    ]
    for event in events:
        st.write(f"**Event**: {event['Event']} | **Date**: {event['Date']} | **Location**: {event['Location']}")
    st.text_input("Event Name:")
    st.date_input("Event Date:")
    st.text_input("Event Location:")
    st.button("Create Event")

# Give Back
elif options == "Give Back":
    st.header("Ways to Give Back")
    st.write("Explore opportunities to give back to the community.")
    opportunities = [
        {"Opportunity": "Donate Winter Coats", "Deadline": "2025-01-20", "Organization": "Local Shelter"},
        {"Opportunity": "Sponsor a Meal", "Deadline": "2025-02-10", "Organization": "Food Bank"},
    ]
    for opp in opportunities:
        st.write(f"**Opportunity**: {opp['Opportunity']} | **Deadline**: {opp['Deadline']} | **Organization**: {opp['Organization']}")
    st.text_input("Opportunity Name:")
    st.date_input("Deadline:")
    st.text_input("Organization:")
    st.button("Add Opportunity")

# Volunteer Opportunities
elif options == "Volunteer Opportunities":
    st.header("Volunteer Opportunities")
    st.write("Sign up for or create volunteer events.")
    volunteers = [
        {"Role": "Food Drive Organizer", "Date": "2025-01-30", "Spots": 5},
        {"Role": "Event Decorator", "Date": "2025-02-14", "Spots": 3},
    ]
    for vol in volunteers:
        st.write(f"**Role**: {vol['Role']} | **Date**: {vol['Date']} | **Spots Available**: {vol['Spots']}")
    st.text_input("Volunteer Role:")
    st.date_input("Event Date:")
    st.number_input("Spots Available:", min_value=1, max_value=50, step=1)
    st.button("Create Volunteer Opportunity")

# Announcements
elif options == "Announcements":
    st.header("Community Announcements")
    st.write("Share news or updates with the community.")
    st.text_area("Write an announcement:")
    st.button("Post Announcement")

# Footer
st.sidebar.write("---")
st.sidebar.write("Kind Villages Prototype v1.0")


