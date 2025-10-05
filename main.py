import streamlit as st
from streamlit_option_menu import option_menu

# Import your pages here
import home, add_site, sites, jcb_work

st.set_page_config(page_title="Bansari Developers", page_icon="🏭", initial_sidebar_state="collapsed")



with st.sidebar:
    selected = option_menu(
        "Main Menu", ["Home", "Add Site", "Sites", "JCB Work"],
        icons=[],
        menu_icon="cast", default_index=0,
        styles={
        }
    )

if selected == "Home":
    home.page()
elif selected == "Add Site":
    add_site.page1()
elif selected == "Sites":
    sites.page2()
elif selected == "JCB Work":
    jcb_work.page3()
else:
    st.warning("Select Page Above")
