import streamlit as st

def require_role(allowed_roles):
    if "role" not in st.session_state:
        st.error("Not logged in")
        st.stop()

    if st.session_state.role not in allowed_roles:
        st.warning("⛔ You are not allowed to access this page.")
        st.stop()
