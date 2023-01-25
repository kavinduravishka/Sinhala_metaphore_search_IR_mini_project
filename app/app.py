from process_results import process_result
from process_search_query import *
# srcs/streamlit_app/app.py
import streamlit as st
from esConnect import *
import pandas as pd

def main():
    st.title('Sinhala Song Metaphors')
    st.title('සිංහල ගීත රූපක')
    search_field = st.text_input('Enter search words:')

    if search_field: # and st.button("Search"):
        st.write("Results:")

        query = generate_query(search_field)
        search_result = es_search(query["body"])
        # st.write(query["type"])
        # st.write(search_result)
        processed_result = process_result(search_result,query["type"])
        df = pd.DataFrame.from_dict(processed_result)
        if len(df)>0:
            st.dataframe(df)
        else:
            st.write("No results were found")


if __name__ == '__main__':
    main()