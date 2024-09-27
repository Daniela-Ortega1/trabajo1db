import streamlit as st
import pandas as pd
from telepi_herlper import insert_merged_data_in_bulk

def extract_data_from_excel(excel_file):
    try:
        df = pd.read_excel(excel_file)
        return df
    except Exception as e:
        st.error(f"Error reading the Excel file: {e}")
        return pd.DataFrame()

st.title("Upload and Merge Excel Files")

uploaded_file1 = st.file_uploader("Excel file 1", type=["xls", "xlsx"], key="file1")
uploaded_file2 = st.file_uploader("Excel file 2", type=["xls", "xlsx"], key="file2")

 
if uploaded_file1 is not None and uploaded_file2 is not None:
    st.success("Files were uploaded successfully.")
    
    df1 = extract_data_from_excel(uploaded_file1)
    df2 = extract_data_from_excel(uploaded_file2)
    

    if df1.empty or df2.empty:
        st.error("Error: One or both files could not be read.")
    else:

        st.write("DataFrame from file 1:")
        st.write(df1)
        

        st.write("DataFrame from file 2:")
        st.write(df2)
        

        if st.button("Merge DataFrames"):
            try:

                merged_df = pd.merge(df1, df2, on='IdCliente', how='inner')
                

                st.success("Merged DataFrame")
                st.write(merged_df)


                insert_merged_data_in_bulk(merged_df)


            except KeyError as e:
                st.error(f"Error: {e}. Make sure both files contain the 'IdCliente' column.")
else:
    st.info("Please upload both Excel files to proceed.")
