import os
import pandas as pd
import streamlit as st

def convert_xlsx_to_csv(input_file, output_file):
    try:
        df = pd.read_excel(input_file, engine='openpyxl')
        df.to_csv(output_file, index=False)
        st.success(f"Conversion successful. CSV file saved as '{output_file}'.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title('XLSX to CSV Converter')

    uploaded_file = st.file_uploader("Choose an XLSX file", type=["xlsx"])

    if uploaded_file is not None:
        if uploaded_file.name.lower().endswith('.xlsx'):
            # Save the uploaded file temporarily
            temp_path = 'temp.xlsx'
            with open(temp_path, 'wb') as temp_file:
                temp_file.write(uploaded_file.getvalue())

            # Convert XLSX to CSV
            output_file_path = 'output.csv'
            convert_xlsx_to_csv(temp_path, output_file_path)

            # Remove the temporary XLSX file
            os.remove(temp_path)

            st.success("Conversion successful. CSV file ready for download.")
            st.markdown(get_download_link(output_file_path), unsafe_allow_html=True)
        else:
            st.error("Invalid file format. Only XLSX files are supported.")

def get_download_link(file_path):
    with open(file_path, 'rb') as temp_file:
        file_data = temp_file.read()
    st.download_button(label="Download CSV", data=file_data, file_name="output.csv")

if __name__ == "__main__":
    main()
