'''
Project Structure:

dat_AI_app/
├── .streamlit/
│   ├── config.toml             # Consists of various app customization options
|   |── secrets.toml            # Store sensitive information like credentials and keys
│── app.py                      # Main app (Home page)
│── views/
|   |----- subsection Info -----
│   ├── about_me.py             # Page with "Enter API Key" button
|   |----- subsection Tasks -------
|   |── data_preprocs.py        # Data loading, preliminary checks, cleaning, exporting
|   |── data_viz.py             # Exploratory analysis and vizualization, shows code for each viz 
│   ├── EnterAPIKeys.py         # Form page for API details
|── forms/                      # Other forms and pop-ups
|   |── api_key.py              # Form page for API details
│── assets/                     # (Optional: Store images, styles, etc.)
│── requirements.txt            # (Optional: Dependencies)

'''
import streamlit as st

st.set_page_config(page_title="Main Menu", page_icon="🤖", layout="wide") # Set a global icon, only supports images or imojis

# --- Page Setup ---
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
data_preprocs_page = st.Page(
    page="views/data_preprocs.py",
    title="Data Preprocessing",
    icon=":material/mop:",
)
data_viz_page = st.Page(
    page="views/data_viz.py",
    title="Data Visualization",
    icon=":material/bar_chart:",
)

# ---- Navigation Setup [with Sections] ----
pg = st.navigation(
    {
        "Info": [about_page],
        "Tasks": [data_preprocs_page, data_viz_page],
    }
)


# ------- Global Assets ---------
# Display an image in the sidebar with specified width
st.logo("assets/data_vizl2.png")
st.sidebar.text("Data Visualization with datAI 🤖")

# ---- Run Navigation ----
pg.run()