import streamlit as st
from st_pages import add_page_title
import requests
import pandas as pd

def callPage(page = None):
    try:
        response_API = requests.get(page)
        data = response_API.json()
        return data
    except requests.exceptions.RequestException as e:
        st.exception(e)
        return False

st.set_page_config(page_title="Logs", layout="wide")

add_page_title(layout="wide")

st.subheader("Api Logs Data")

# st.write("This is just a sample page!")
url = st.secrets["log_url"]
data = callPage(url)
if data != False:
    st.write("Total Data: ", data["total"])
    if 'currentPage' not in st.session_state:
        currentPage = data["current_page"]
        nextPage = data["next_page_url"]
        prevPage = data["prev_page_url"]
        firstPage = data["first_page_url"]
        lastPage = data["last_page_url"]
        st.session_state['currentPage'] = currentPage
        st.session_state['nextPage'] = nextPage
        st.session_state['prevPage'] = prevPage
        st.session_state['firstPage'] = firstPage
        st.session_state['lastPage'] = lastPage
    else:
        currentPage = st.session_state['currentPage']
        nextPage = st.session_state['nextPage']
        prevPage = st.session_state['prevPage']
        firstPage = st.session_state['firstPage']
        lastPage = st.session_state['lastPage']

    col1, col2, _, col3, col4 = st.columns([1, 1, 10, 1, 1])
    with col1:
        button1 = st.button('First Page')
    with col2:
        button2 = st.button('Previous Page')
    with col3:
        button3 = st.button('Next Page')
    with col4:
        button4 = st.button('Last Page')

    if(button1):
        data = callPage(st.session_state['firstPage'])
        st.session_state['currentPage'] = data["current_page"]
        st.session_state['nextPage'] = data["next_page_url"]
        st.session_state['prevPage'] = data["prev_page_url"]
    if(button2):
        if(st.session_state['prevPage'] == None):
            st.error("This is the first page!")
        else:
            data = callPage(st.session_state['prevPage'])
            st.session_state['currentPage'] = data["current_page"]
            st.session_state['nextPage'] = data["next_page_url"]
            st.session_state['prevPage'] = data["prev_page_url"]
    if(button3):
        if(st.session_state['nextPage'] == None):
            st.error("This is the last page!")
        else:
            data = callPage(st.session_state['nextPage'])
            st.session_state['currentPage'] = data["current_page"]
            st.session_state['nextPage'] = data["next_page_url"]
            st.session_state['prevPage'] = data["prev_page_url"]
    if(button4):
        data = callPage(st.session_state['lastPage'])
        st.session_state['currentPage'] = data["current_page"]
        st.session_state['nextPage'] = data["next_page_url"]
        st.session_state['prevPage'] = data["prev_page_url"]

    df = pd.DataFrame(data["data"])
    st.dataframe(df.set_index(df.columns[0]), use_container_width=True)
    st.write("Current page: ", st.session_state['currentPage'], " of ", data["last_page"])
else:
    st.error("Data not found")
    st.stop()