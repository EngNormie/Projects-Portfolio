import streamlit as st
import re               # For API key input validation

@st.dialog("Enter API Keys")  # This creates a popup modal

#####################################################################################


###########################################
def api_key_form():
    """Function to display the API Key form with validation."""
    with st.form("api_key_form"):
        st.write("🔐 Please provide your OpenAI API Key and select a model.")

        # API Key input field (masked for security)
        api_key = st.text_input("OpenAI API Key", type="password", value=st.session_state.get("api_key", ""))

        # Dropdown for OpenAI models
        model_options = ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"]
        model = st.selectbox("Select OpenAI Model", model_options, 
                             index=model_options.index(st.session_state.get("model", "gpt-4")))

        # Submit button
        submitted = st.form_submit_button("✅ Submit")

        # Validation logic
        if submitted:
            errors = []

            # API Key validation
            if not api_key:
                errors.append("❌ API Key is required.")
            elif not re.match(r"sk-[A-Za-z0-9\-]+", api_key):
                errors.append("❌ Invalid API Key format. Must only consist of alpha-numeric and dash characters.")

            # Model selection validation (Dropdown ensures a valid value is always selected)

            if errors:
                for error in errors:
                    st.error(error)
            else:
                # Store values in session state
                st.session_state["api_key"] = api_key
                st.session_state["model"] = model
                st.success("✅ API Key and model saved! Pick a menu to proceed.")

    # Logout / Reset API Key Button
    if "api_key" in st.session_state:
        if st.button("🚪 Logout / Reset API Key"):
            del st.session_state["api_key"]  # Remove the stored API Key
            st.success("🔑 API Key has been cleared for security.")
            st.rerun()  # Refresh the app to remove stored key