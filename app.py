import streamlit as st
import os

st.title("Personal Injury Assist - Story Ad Generator")

# Display Script from File
session_id = "12345"  # Replace with dynamic session management
script_file = f"{session_id}_script.txt"

if os.path.exists(script_file):
    with open(script_file, "r") as file:
        script_content = file.read()
    st.text_area("Generated Script", value=script_content, height=300)
else:
    st.write("No script available yet. Please wait...")
