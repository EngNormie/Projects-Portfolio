import re               # importing regular expressions support library 
import streamlit as st
import requests

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

# Function to validate webhook URL
def is_valid_webhook(url):
    return bool(url.strip())  # Ensures it's not empty

# Function to validate email
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# Function to validate name (only letters and spaces, at least 2 characters)
def is_valid_name(name):
    return bool(re.match(r"^[A-Za-z\s]{2,}$", name))

# Function to validate message (not empty)
def is_valid_message(message):
    return len(message.strip()) > 0

@st.dialog("Contact Me")  # This creates a popup modal
def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_input("Your Message")
        submit_btn = st.form_submit_button("✅ Submit")
        
        if submit_btn:
            errors = []         # initializing an empty list named errors.
            
            if not is_valid_webhook(WEBHOOK_URL):
                errors.append("Webhook URL is not set.")
                  
            if not is_valid_email(email):
                errors.append("Invalid email format.")
                
            if not is_valid_name(name):
                errors.append("Name must contain only letters and spaces, at least 2 characters long.")
            
            if not is_valid_message(message):
                errors.append("Message cannot be empty.")
                
                            
            if errors:              # listing all errors improves user experience instead of making them fix one at a time.
                for error in errors:
                    st.error(error, icon="🫨")
            else:
                data = {"email": email, "name": name, "message": message} # data dictionary to hold user data
                
                try:
                    response = requests.post(WEBHOOK_URL, json=data)
                    
                    if response.status_code == 200:         # Displays an error message if the webhook request fails with a non-200 status code.
                        st.success("Message successfully sent!")
                    else:
                        st.error(f"Failed to send message. Server responded with: {response.status_code}", icon="🫨")
                
                except requests.exceptions.RequestException as e:   # Handles request exceptions to avoid app crashes if there's a network error.
                    st.error(f"An error occurred while sending the request: {e}")