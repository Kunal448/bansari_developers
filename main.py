import streamlit as st
from streamlit_option_menu import option_menu

# Import your pages here
import home, sites

st.set_page_config(
    page_title="Bansari Developers",
    page_icon="🏭",
    initial_sidebar_state="expanded"
)
with st.sidebar:
    selected = option_menu(
        "Main Menu", ["Home", "Sites"],
        icons=[],
        menu_icon="cast", default_index=0,
        styles={
        }
    )
    
#st.write("[![Home](<https://unsplash.com/photos/logo-z7ICBEMUJfw>)](<https://www.google.com/>)")    

# Page content based on selection
if selected == "Home":
    home.page()
elif selected == "Sites":
    sites.page2()
else:
    st.warning("Select Page Above")