import streamlit as st
import pandas as pd
from merged_data import insert_merged_data_in_bulk

def extract_data_from_excel(excel_file):
    """Extracts data from the provided Excel file."""
    try:
        df = pd.read_excel(excel_file)
        return df
    except Exception as e:
        st.error(f"Error reading the Excel file: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

st.title("Upload and Merge Excel Files")

uploaded_file1 = st.file_uploader("Attendance list Excel file 1", type=["xls", "xlsx"], key="file1")
uploaded_file2 = st.file_uploader("Attendance list Excel file 2", type=["xls", "xlsx"], key="file2")

if uploaded_file1 is not None and uploaded_file2 is not None:
    st.write("Files were uploaded successfully.")
    
    # Extract data from both files
    df1 = extract_data_from_excel(uploaded_file1)
    df2 = extract_data_from_excel(uploaded_file2)
    
    if df1.empty or df2.empty:
        st.error("Error: One or both files could not be read.")
    else:
        st.write("DataFrame from file 1:")
        st.write(df1)
        
        st.write("DataFrame from file 2:")
        st.write(df2)
        
        # Add a button to merge DataFrames
        if st.button("Merge DataFrames"):
            try:
                # Merge the dataframes on 'IdCliente' using an inner join
                merged_df = pd.merge(df1, df2, on='IdCliente', how='inner')
                
                # Display the merged dataframe
                st.success("Merged DataFrame")
                st.write(merged_df)

                # Insert merged data into the database
                insert_merged_data_in_bulk(merged_df)

            except KeyError as e:
                st.error(f"Error: {e}. Make sure both files contain the 'IdCliente' column.")
else:
    st.info("Please upload both Excel files to proceed.")
