# imports
import streamlit as st
import pandas as pd
import numpy as np
import os
import io
from io import BytesIO
# to run app, use terminal - type "streamlit run appname.py" Replace appname.py with your app's name

# setup the app
st.title("🧹 Data Preprocessing") # press windows & periods [Win + .] keys simultaneously where u need emoji
st.write("Perform file transformation, with inbuit data cleaning!")


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


        ###########################################################################################################       
        # Options for Data cleaning
        st.subheader("🔍 Data Assessment")
        
        # Show the shape of our df
        st.write("⚖️ Shape of the Dataframe")
        df.shape
        
        # Show first 5 rows of our df
        st.write("🔍 Preview the Head of the Dataframe")
        st.dataframe(df.head())
        
        # Show last 5 rows of our df
        st.write("🔍 Preview the Tail of the Dataframe")
        st.dataframe(df.tail())
        
        # Check distribution of categorical features
        st.write("➗ Distribution of Categorical Features")
        df.describe(include=['O']).T
        
        # Check distribution of numerical features (max , min, std of values)
        st.write("➗ Distribution of Numerical Features")
        df.describe().T

        # Capture df.info() output since it can't be printed directly on UI
        buffer = io.StringIO()
        df.info(buf=buffer)
        df_info = buffer.getvalue()
        
        st.write("ℹ️ Dataframe Info")
        st.code(df_info, language="python")
        ###########################################################################################################
        
        
        ###########################################################################################################
        # Compute duplicate rows
        duplicates = df[df.duplicated()]
        all_duplicates = duplicates.shape[0]
        
        if all_duplicates == 0:
            st.success("No duplicate rows found! 🎉")
        else:
            st.warning(f"⚠️ Found {all_duplicates} duplicate rows!")
            st.dataframe(duplicates)  # Display duplicate rows
        
        #############################################################################################################

        #############################################################################################################
        # checking the missing values in the data
        all_missing_values = df.isnull().sum()  # Compute missing values
        if all_missing_values.sum() == 0:       # Check if there are missing values
            st.success("No missing values in the dataset! 🎉")
        else:
            st.warning(f"⚠️ Found Null Values!")
            st.dataframe(all_missing_values.to_frame(name="Missing Count"))  # Show as DataFrame for better readability
        #############################################################################################################
        

        #############################################################################################################
        # Options for Data cleaning
        
        # Initialize session state for cleaned data if not already set
        if "cleaned_df" not in st.session_state:
            st.session_state.cleaned_df = df.copy()
            
        st.subheader("🛠️ Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):

            # Duplicate Removal Options
            st.markdown("##### Handle Duplicates")
            duplicate_method = st.selectbox("Select a method:", [
                "None", 
                "Drop All Duplicates", 
                "Keep First Occurrence", 
                "Keep Last Occurrence"
            ], key="duplicate_method")

            # Missing Value Handling Options
            st.markdown("##### Handle Missing Values")
            null_method = st.selectbox("Select a method:", [
                "None", 
                "Drop Rows", 
                "Drop Columns", 
                "Fill with Mean (Numeric Only)", 
                "Fill with Median (Numeric Only)", 
                "Forward Fill", 
                "Backward Fill", 
                "Fill with Mode (Categorical Only)", 
                "Fill with 'Unknown' (Categorical Only)"
            ], key="null_method")

            # Single Apply Button
            if st.button(f"Apply Data Cleaning for {file.name}"):
                
                cleaned_df = st.session_state.cleaned_df.copy()

                total_duplicates = cleaned_df.duplicated().sum()
                missing_values = cleaned_df.isnull().sum().sum()

                # Apply duplicate cleaning first
                if total_duplicates > 0 and duplicate_method != "None":
                    if duplicate_method == "Drop All Duplicates":
                        cleaned_df = cleaned_df.drop_duplicates(keep=False)
                        st.success("Dropped all duplicate rows.")

                    elif duplicate_method == "Keep First Occurrence":
                        cleaned_df = cleaned_df.drop_duplicates(keep="first")
                        st.success("Kept first occurrence, removed other duplicates.")

                    elif duplicate_method == "Keep Last Occurrence":
                        cleaned_df = cleaned_df.drop_duplicates(keep="last")
                        st.success("Kept last occurrence, removed other duplicates.")
                elif total_duplicates == 0:
                    st.success("No duplicate rows found! 🎉")

                # Apply missing values handling
                if missing_values.sum() > 0 and null_method != "None":
                    if null_method == "Drop Rows":
                        cleaned_df = cleaned_df.dropna()
                        st.success("Dropped rows with missing values.")

                    elif null_method == "Drop Columns":
                        cleaned_df = cleaned_df.dropna(axis=1)
                        st.success("Dropped columns with missing values.")

                    elif null_method == "Fill with Mean (Numeric Only)":
                        cleaned_df = cleaned_df.fillna(cleaned_df.mean(numeric_only=True))
                        st.success("Filled missing values with column means.")

                    elif null_method == "Fill with Median (Numeric Only)":
                        cleaned_df = cleaned_df.fillna(cleaned_df.median(numeric_only=True))
                        st.success("Filled missing values with column medians.")

                    elif null_method == "Forward Fill":
                        cleaned_df = cleaned_df.fillna(method="ffill")
                        st.success("Applied forward fill (propagated previous values).")

                    elif null_method == "Backward Fill":
                        cleaned_df = cleaned_df.fillna(method="bfill")
                        st.success("Applied backward fill (filled with next available values).")

                    elif null_method == "Fill with Mode (Categorical Only)":
                        cleaned_df = cleaned_df.fillna(cleaned_df.mode().iloc[0])
                        st.success("Filled missing categorical values with mode.")

                    elif null_method == "Fill with 'Unknown' (Categorical Only)":
                        cleaned_df = cleaned_df.fillna("Unknown")
                        st.success("Filled missing categorical values with 'Unknown'.")
                elif missing_values.sum() == 0:
                    st.success("No missing values in the dataset! 🎉")
                
                # Store the cleaned data in session state
                st.session_state.cleaned_df = cleaned_df.copy()


                # Show the final shape of the new DataFrame
                st.write("⚖️ Shape of the New Dataframe:", cleaned_df.shape)
        #############################################################################################################
        

        #############################################################################################################
        # Use cleaned dataset for subsequent operations
        new_df = st.session_state.cleaned_df

        # Choose Specific Columns to Keep or Convert
        st.subheader("Select Columns to Convert")
        columns = st.multiselect(f"Choose Columns for {file.name}", new_df.columns, default=new_df.columns)
        new_df = new_df[columns]
        
        # Create Some Visualizations
        st.subheader("📈 Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            st.bar_chart(new_df.select_dtypes(include='number').iloc[:,:2])
            
            
        # Convert File -> CSV/Excel
        st.header("🔀 Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()  # Create an in-memory buffer for the file
            
            if conversion_type == "CSV":
                new_df.to_csv(buffer, index=False)  # Write the DataFrame to buffer as CSV
                file_name = file.name.replace(".csv", "_cleaned.csv")
                mime_type = "text/csv"

            elif conversion_type == "Excel":
                new_df.to_excel(buffer, index=False)  # Write the DataFrame to buffer as Excel
                file_name = file.name.replace(".csv", "_cleaned.xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            # Download Button
            st.download_button(
                label=f"⬇️ Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )
        #############################################################################################################
            
st.success("🎉 All files processed!")