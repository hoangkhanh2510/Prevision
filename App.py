import streamlit as st
import pandas as pd
import base64
from io import BytesIO

@st.cache(allow_output_mutation=True)
def get_data():
    return []
with st.beta_expander("Visualisation du fichier log"):
    user_id = st.text_input("User ID")
    foo = st.slider("foo", 0, 100)
    bar = st.slider("bar", 0, 100)

    if st.button("Add row"):
        get_data().append({"UserID": user_id, "foo": foo, "bar": bar})

    df = pd.DataFrame(get_data())
    def to_excel(df):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    def get_table_download_link(df):
        """Generates a link allowing the data in a given panda dataframe to be downloaded
        in:  dataframe
        out: href string
        """
        val = to_excel(df)
        b64 = base64.b64encode(val)  # val looks like b'...'
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.xlsx">Download csv file</a>' # decode b'abc' => abc

    #df = get_data() # your dataframe
    st.markdown(get_table_download_link(df), unsafe_allow_html=True)

    st.write(pd.DataFrame(get_data()))