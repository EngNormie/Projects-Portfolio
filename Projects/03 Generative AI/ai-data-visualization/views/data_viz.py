# imports
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import textwrap
import os
import io
from io import BytesIO

import openai

# to run app, use terminal - type "streamlit run appname.py" Replace appname.py with your app's name

# setup the app
st.title("📊 Data Visualization")
st.write("AI Assisted Data Visualization!")

# Now you can use st.session_state["api_key"] wherever needed
if "api_key" in st.session_state:
    st.success(f"🔑 API Key is set. Using model: {st.session_state.get('model', 'gpt-4')}.")
    
    # Button to clear the API Key form
    if st.button("🔐 Clear your OpenAI API Key"):
        from forms.api_key import api_key_form  # import api_key_form function
        api_key_form()  # Call the function to display the form
    
    ######################### PERFORM AI ASSISTED DATA VISUALIZATION TASKS ########################################
    # Anywhere in your app where you need to send requests, retrieve the API Key from session state:
    api_key = st.session_state.get("api_key", None)
    model = st.session_state.get("model", "gpt-4")

    #client = openai.OpenAI()  # Initialize the client
    client = openai.OpenAI(api_key=api_key)  # Set API key here

    ###++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # User Data Input & Upload Options
    uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"],
                                    accept_multiple_files=True)

    if uploaded_files:
        for file in uploaded_files:
            file_ext = os.path.splitext(file.name)[-1].lower()
            
            if file_ext == ".csv":
                df = pd.read_csv(file)
                
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)
            else: 
                st.error("Unsupported file type: {file_ext}")
                continue
            
            # Display info about file
            st.write(f"**File Name:** {file.name}")
            st.write(f"File Size:** {file.size/1024}")
            
            # Print head
            st.write("🔍 Preview of the Dataset", df.head())
            
            # Show the shape of the DataFrame
            st.write("⚖️ Shape of the New Dataframe:", df.shape)


            ###++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++      
            # Options for Data Visualization
            st.subheader("📊 Generate AI-Powered Visualizations")

            # Checkbox options for visualization
            basic_visuals = st.checkbox("Basic Visuals")
            univariate_analysis = st.checkbox("Univariate Analysis")
            bivariate_analysis = st.checkbox("Bivariate & Multivariate Analysis")

            # BASIC VISUALS (Single Plot)
            if basic_visuals:
                st.subheader("📊 Basic Visuals")
                visualization_type = st.selectbox("Select visualization type", [
                    "Bar Chart", 
                    "Line Chart", 
                    "Scatter Plot"
                    ])
                columns = st.multiselect("Choose columns to plot", df.columns)

                if columns:
                    prompt = (
                        f"Generate a Python script using matplotlib to create a {visualization_type} "
                        f"for the following columns: {columns} from an already loaded pandas dataframe named 'df'. "
                        f"Use 'fig' as the figure variable."
                    )

                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}]
                    )

                    generated_code = response.choices[0].message.content

                    if "```python" in generated_code:
                        generated_code = generated_code.split("```python")[1].split("```")[0]

                    st.subheader("💡 AI-Generated Code")
                    st.code(textwrap.dedent(generated_code), language="python")

                    exec(generated_code, {"df": df, "plt": plt}, locals())

                    fig = locals().get("fig", None)
                    if fig:
                        st.pyplot(fig)
                    else:
                        st.error("🚨 AI-generated code did not produce a figure.")

            # UNIVARIATE ANALYSIS (Histograms, KDE, Boxplots)
            if univariate_analysis:
                st.subheader("📈 Univariate Analysis")
                num_columns = df.select_dtypes(include="number").columns.tolist()
                selected_col = st.selectbox("Select a column for univariate analysis", num_columns)

                if selected_col:
                    prompt = (
                        f"Generate a Python script using matplotlib and seaborn to perform Univariate Analysis "
                        f"on the column '{selected_col}' from a pandas dataframe named 'df'. "
                        f"Create a single figure with subplots containing a histogram, KDE plot, and a boxplot. "
                        f"Use 'fig' as the figure variable."
                    )

                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}]
                    )

                    generated_code = response.choices[0].message.content

                    if "```python" in generated_code:
                        generated_code = generated_code.split("```python")[1].split("```")[0]

                    st.subheader("💡 AI-Generated Code")
                    st.code(textwrap.dedent(generated_code), language="python")

                    exec(generated_code, {"df": df, "plt": plt, "sns": sns}, locals())

                    fig = locals().get("fig", None)
                    if fig:
                        st.pyplot(fig)
                    else:
                        st.error("🚨 AI-generated code did not produce a figure.")

            # BIVARIATE & MULTIVARIATE ANALYSIS (Pairplots, Correlation Heatmaps)
            if bivariate_analysis:
                st.subheader("📉 Bivariate & Multivariate Analysis")
                num_columns = df.select_dtypes(include="number").columns.tolist()
                selected_cols = st.multiselect("Select multiple columns for analysis", num_columns)

                if len(selected_cols) >= 2:
                    prompt = (
                        f"Generate a Python script using matplotlib and seaborn to perform Bivariate and Multivariate Analysis "
                        f"on the selected columns '{selected_cols}' from a pandas dataframe named 'df'. "
                        f"Create a single figure with subplots: a scatter plot matrix (pairplot) and a correlation heatmap. "
                        f"Use 'fig' as the figure variable."
                    )

                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}]
                    )

                    generated_code = response.choices[0].message.content

                    if "```python" in generated_code:
                        generated_code = generated_code.split("```python")[1].split("```")[0]

                    st.subheader("💡 AI-Generated Code")
                    st.code(textwrap.dedent(generated_code), language="python")

                    exec(generated_code, {"df": df, "plt": plt, "sns": sns}, locals())

                    fig = locals().get("fig", None)
                    if fig:
                        st.pyplot(fig)
                    else:
                        st.error("🚨 AI-generated code did not produce a figure.")
        ######################### END OF AI ASSISTED DATA VISUALIZATION TASKS ########################################
            
else:
    st.warning("⚠️ Please enter your API Key in the About Me Page to continue.")

    

    