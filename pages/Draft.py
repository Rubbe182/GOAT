import pandas as pd
import streamlit as st

df_Draft = pd.read_csv('Draft.csv',encoding='latin-1')
st.title("DRAFT")



Year=['All Seasons',2019,2020,2021,2022]
Picks=df_Draft.Pick.unique()
Franchise=df_Draft.Franchise.unique()
Position=df_Draft.Position.unique()

position_choice_year = st.radio('Year:', Year,horizontal=True)
position_choice_Picks = st.selectbox('Picks:', Picks)
position_choice_Franchise = st.multiselect('Franchise:', Franchise)

# Mostrar la tabla en Streamlit
st.dataframe(df_Draft)
