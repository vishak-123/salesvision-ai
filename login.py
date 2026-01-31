import streamlit as st

def login_page():

    st.markdown("## 🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.session_state.role = "admin"
            st.success("Login successful!")
            st.rerun()

        elif username == "user" and password == "user123":
            st.session_state.logged_in = True
            st.session_state.role = "user"
            st.success("Login successful!")
            st.rerun()

        else:
            st.error("Invalid username or password")
