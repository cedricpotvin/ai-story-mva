import streamlit as st
import requests
import uuid

# FastAPI server URL
FASTAPI_URL = "https://ai-story-mva.onrender.com/receive-script/"

# Session State for unique session ID
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Session State for generated script
if "generated_script" not in st.session_state:
    st.session_state.generated_script = ""

st.title("Personal Injury Assist - Story Ad Generator")

# Section 1: Generate New Concept (Simulated Message)
st.header("1. Generate a New Concept")
st.write("Send your request to Zapier or FastAPI as appropriate.")

# Section 2: Fetch Script from Server
st.header("2. Fetch the Script from Server")
if st.button("Fetch Script"):
    try:
        # Fetch script using GET request from FastAPI
        response = requests.get(f"{FASTAPI_URL}?session_id={st.session_state.session_id}")
        if response.status_code == 200:
            st.session_state.generated_script = response.json().get("script", "No script found.")
            st.success("Script fetched successfully!")
        else:
            st.warning("Script not found. Make sure it was sent to FastAPI.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching script: {e}")

# Display the script if available
if st.session_state.generated_script:
    st.text_area("Generated Script", value=st.session_state.generated_script, height=300)
else:
    st.write("No script available yet. Click 'Fetch Script' to retrieve it.")
