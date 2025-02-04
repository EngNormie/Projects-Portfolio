import streamlit as st

from forms.contact import contact_form  # import contact_form function

def show_contact_form():
    contact_form()

from forms.api_key import api_key_form  # import api_key_form function

def show_apikey_form():
    api_key_form()
    

# ---- Intro Section -----
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/Bot.png")

# Button to display the API Key form
if st.button("📧 Contact Me"):
    contact_form()  # Call the function to display the contact form
    
        
with col2:
    st.title("datAI Agent", anchor=False)
    st.write(
        "Data Visualization Agent, assists with various vizualization approaches used in Data Science."
    )
###+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Check if API key is stored in session state
if "api_key" in st.session_state and st.session_state["api_key"]:
    st.success(f"🔑 API Key is set. Using model: {st.session_state.get('model', 'gpt-4')}.")

    # Button to clear the API Key form
    if st.button("🔐 Clear your OpenAI API Key"):

        show_apikey_form()  # Call the function to display the form
        
        if "api_key" not in st.session_state:
            st.rerun()

else:
    st.warning("⚠️ No OpenAI API Key detected. Please enter your API key to continue.")

    # Create two side-by-side buttons
    colm1, colm2 = st.columns([1, 1])  # Equal width columns

    with colm1:
        if st.button("🔐 Enter your OpenAI API Key"):
            show_apikey_form()      # Set flag to show form      

            # Show a manual refresh button instead of auto-refresh
            if st.button("🔄 Refresh Page"):
                st.rerun()
    
    # Button to open OpenAI API Key creation page in a new tab        
    with colm2:
        st.link_button("🔑 Get New OpenAI API Key", "https://platform.openai.com/account/api-keys", use_container_width=False)
    
###++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   
# ------ Capabilities ------
st.write("\n")
st.subheader("Capable Tasks", anchor=False)
st.write(
    """
    - Data loading
    - Data cleaning
    - Handling missing values
    - Exploratory analysis (Univariate, Bivariate, Multivariate)
    - Data visualization
    - Data exportation/ downloading
    """
)

# ------ Skillset ------
st.write("\n")
st.subheader("Skillset", anchor=False)
st.write(
    """
    - Data types: (xlsx, csv)
    - Python Programming: (Pandas, PySpark)
    - Data Visualization: (Plotly, Matplotlib, Seaborn, Geoplotlib, GGplot, Pygal, NumPy, SciPy, Statsmodels)
    - Database Programming Language: SQL
    """
)

    

