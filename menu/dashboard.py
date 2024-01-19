import streamlit as st
from st_pages import add_page_title, show_pages
from barfi import st_barfi, barfi_schemas, Block
from streamlit_ace import st_ace
from streamlit_calendar import calendar
import os
from pathlib import Path
import datetime

add_page_title(layout="wide")
st.subheader("OCR Scanner")
expander = st.expander("OCR Scanner")
uploaded_files = st.file_uploader("Choose a Image file", accept_multiple_files=False, type=['png', 'jpg', 'jpeg'])
if uploaded_files is not None:
    save_folder = str(Path().absolute()) + '/images/' 
    save_path = Path(save_folder, uploaded_files.name)
    with open(save_path, mode='wb') as w:
        w.write(uploaded_files.getvalue())
    
    if save_path.exists():
        st.toast(f'File {uploaded_files.name} is successfully saved!', icon='😍')
        # st.session_state[uploaded_files.name] = "has_set"
    
list_file = os.listdir("images")
# st.session_state['list_file'] = list_file
# if 'list_file' in st.session_state:
    # print(len(st.session_state['list_file']))
    # if len(st.session_state['list_file']) > 0:
for file in list_file:
    # st.session_state[file] = "has_set"
    # if st.session_state[file] == "has_set":
    st.image("images/" + file, width=300, caption=file)
    if st.button("Delete Image "+file):
        os.remove("images/" + file)
        if os.path.exists("images/" + file) == False:
            st.toast(f'File {file} is successfully deleted!', icon='😍')
            st.rerun()
pass

calendar_options = {
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    }
}
custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
"""
st.divider()
st.subheader("Calendar")
calendar = calendar(events=None, options=calendar_options, custom_css=custom_css)
st.write(calendar)
st.divider()
st.subheader("Code Console")
# Spawn a new Ace editor
content = st_ace()
# Display editor's content as you type
content
st.divider()
st.subheader("Barfi Diagram")
feed = Block(name='Feed')
feed.add_output()
def feed_func(self):
    self.set_interface(name='Output 1', value=4)
feed.add_compute(feed_func)

splitter = Block(name='Splitter')
splitter.add_input()
splitter.add_output()
splitter.add_output()
def splitter_func(self):
    in_1 = self.get_interface(name='Input 1')
    value = (in_1/2)
    self.set_interface(name='Output 1', value=value)
    self.set_interface(name='Output 2', value=value)
splitter.add_compute(splitter_func)

mixer = Block(name='Mixer')
mixer.add_input()
mixer.add_input()
mixer.add_output()
def mixer_func(self):
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = (in_1 + in_2)
    self.set_interface(name='Output 1', value=value)
mixer.add_compute(mixer_func)

result = Block(name='Result')
result.add_input()
def result_func(self):
    in_1 = self.get_interface(name='Input 1')
result.add_compute(result_func)

load_schema = st.selectbox('Select a saved schema:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=False)

barfi_result = st_barfi(base_blocks=[feed, result, mixer, splitter],
                    compute_engine=compute_engine, load_schema=load_schema)

if barfi_result:
    st.write(barfi_result)
