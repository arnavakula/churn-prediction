import streamlit as st
import pandas as pd
from PIL import Image

st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title='Customer Churn Dashboard',
    page_icon='😎'
)

if 'df' not in st.session_state:
    df = pd.read_csv('churn.csv')
    df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)
    df = df.rename(columns = {'Exited': 'Churn'})

    st.session_state['df'] = df

    columns = []
    for column in st.session_state.df.columns:
        columns.append(str(column))

    st.session_state['columns'] = columns

    

st.title('home page')
st.sidebar.success('Select a page above')

st.write('using data to predict and prevent customer churn')

st.markdown(
    """
    <img src="https://www.touchpoint.com/wp-content/uploads/2023/02/5.-Customer-churn-article.png" alt="Customer Churn Prediction Dashboard Home Page Mockup" width="700">
    """,
    unsafe_allow_html=True
)

