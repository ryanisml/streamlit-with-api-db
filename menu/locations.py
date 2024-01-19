import streamlit as st
from streamlit_folium import st_folium
import folium

from st_pages import add_page_title

add_page_title(layout="wide")

st.write("Location with folium")

data = folium.Map(location=[st.secrets["latitude_sgt"], st.secrets["longitude_sgt"]], zoom_start=15)
folium.Marker([st.secrets["latitude_sgt"], st.secrets["longitude_sgt"]], popup='<i>'+st.secrets["location_name"]+'</i>').add_to(data)

st_folium(data, use_container_width=True, height=500)