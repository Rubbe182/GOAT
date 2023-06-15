import pandas as pd
import streamlit as st

df_Draft = pd.read_csv('Draft.csv',encoding='latin-1')
st.title("DRAFT")
df_Draft['Points']=df_Draft['Points'].replace({'-':'0'}).astype(int)



Year = ['All Seasons'] + list(df_Draft['Year'].unique())
Positions = ['All'] + list(df_Draft['Position'].unique())

Picks=df_Draft.Pick.unique()
Franchise=df_Draft.Franchise.unique()

position_choice_year = st.radio('Year:', Year,horizontal=True)
selected_position = st.selectbox('Position', Positions, index=0)


if position_choice_year != 'Todos los años':
    df_filtered = df_Draft[df_Draft['Year'] == position_choice_year]
else:
    df_filtered = df_Draft
    
if selected_position != 'Todas las posiciones':
    df_filtered = df_filtered[df_filtered['Position'] == selected_position]

# Mostrar la tabla en Streamlit
st.dataframe(df_filtered)