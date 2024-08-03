import streamlit as st

st.set_page_config(
    page_title="DVWA Demo",
    page_icon=":lock:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("DVWA Exploits")
st.sidebar.image("https://example.com/logo.png", width=200)

pages = {
    "Introduction": "pages/Introduction.py",
    "Brute Force": "pages/Brute force.py",
    "Command Injection": "pages/command_injection.py",
    "File Inclusion": "pages/file_inclusion.py",
    "SQL Injection": "pages/sql_injection.py",
    "XSS": "pages/xss.py",
}

st.sidebar.subheader("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

selected_page = pages[selection]
exec(open(selected_page).read())
