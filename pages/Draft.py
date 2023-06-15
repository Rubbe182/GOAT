import pandas as pd
import streamlit as st

df_Draft = pd.read_csv('Draft.csv',encoding='latin-1')
st.title("DRAFT")
df_Draft['Points']=df_Draft['Points'].replace({'-':'0'}).astype(int)



Year = ['All Seasons'] + list(df_Draft['Year'].unique())
Positions = ['All'] + list(df_Draft['Position'].unique())
Franchise = ['All'] + list(df_Draft['Franchise'].unique())

position_choice_year = st.radio('Year:', Year,horizontal=True)
selected_position = st.selectbox('Position', Positions, index=0)
selected_franchise = st.selectbox('Franchise', Franchise, index=0)
player_search = st.text_input('Buscar Jugador:', '')

if position_choice_year != 'All Seasons':
    df_filtered = df_Draft[df_Draft['Year'] == position_choice_year]
else:
    df_filtered = df_Draft

if selected_position != 'All':
    df_filtered = df_filtered[df_filtered['Position'] == selected_position]

if selected_franchise != 'All':
    df_filtered = df_filtered[df_filtered['Franchise'] == selected_franchise]
    
if player_search:
    df_filtered = df_filtered[df_filtered['Player'].str.contains(player_search, case=False)]


# Mostrar la tabla en Streamlit
st.dataframe(df_filtered)
