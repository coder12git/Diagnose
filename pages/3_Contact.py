# Contact Feature

import streamlit as st
import pandas as pd
import pydeck as pdk
import requests

st.set_page_config(
    page_title="Diagnose",
    page_icon="♋",
    layout="centered",
    initial_sidebar_state="expanded",
)


st.title("Find a dermatologist")

# Create a function to search for nearby doctors based on city name
def search_doctors(city):
    # Google Maps API key
    api_key = st.secrets["API_KEY"]
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=dermatologists+in+{city}&key={api_key}"
    results = requests.get(url).json()
    return results["results"]


# Input city name
city = st.text_input(
    label="Enter your city",
    placeholder="City (e.g. New Delhi)",
    help="Enter the name of the city where you want to find a dermatologist",
).strip()

if city:
    # Search for nearby doctors
    doctors = search_doctors(city)

    # Display the results to the user
    st.write("Results for Dermatologist doctors in: ", city)
    lat_long = [
        (doc["geometry"]["location"]["lat"], doc["geometry"]["location"]["lng"])
        for doc in doctors
    ]
    df = pd.DataFrame(lat_long, columns=["latitude", "longitude"])
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/streets-v12",
            initial_view_state=pdk.ViewState(
                latitude=df["latitude"].mean(),
                longitude=df["longitude"].mean(),
                zoom=11,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    "ScatterplotLayer",
                    data=df,
                    get_position=["longitude", "latitude"],
                    get_radius=100,
                    get_color=[200, 30, 0],
                    pickable=True,
                    auto_highlight=True,
                )
            ],
        )
    )

    for i, doctor in enumerate(doctors):
        st.write(f"{i+1}. **Name**: ", doctor["name"])
        st.write("> **Address**: ", doctor["formatted_address"])