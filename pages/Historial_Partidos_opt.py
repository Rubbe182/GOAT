import pandas as pd
import streamlit as st
import numpy as np

df_Games = pd.read_csv('df_Games.csv')
df_Games = df_Games[['Year', 'Week', 'Home_Team', 'Away_Team', 'Home_Points', 'Away_Points']]

st.title("Historial Partidos")
st.sidebar.markdown('Historial Partidos Temporada Regular')

df_Games=df_Games[['Year','Week','Home_Team','Away_Team','Home_Points','Away_Points']]
Weeks=['1','2','3','4','5','6','7','8','9','10','11','12','13','14']
df_Games=df_Games[df_Games.Week.isin(Weeks)]

Week=['All Weeks','1','2','3','4','5','6','7','8','9','10','11','12','13','14']
Year=['All Seasons',2019,2020,2021,2022]
Teams=df_Games.Home_Team.unique()

position_choice_year = st.radio('Year:', Year,horizontal=True)
position_choice_week = st.selectbox('Week:', Week)

Display_options = ['Completo', 'Selección Franquicia', 'Head to Head']
position_choice_display = st.radio('', Display_options)

if position_choice_display == 'Selección Franquicia':
    position_choice_Team = st.multiselect('Team:', Teams)
    filtered_games = df_Games[(df_Games['Home_Team'].isin(position_choice_Team)) |
                              (df_Games['Away_Team'].isin(position_choice_Team))]
else:
    position_choice_Team1 = st.selectbox('Team 1:', Teams)
    position_choice_Team2 = st.selectbox('Team 2:', Teams)
    filtered_games = df_Games[((df_Games['Home_Team'] == position_choice_Team1) &
                               (df_Games['Away_Team'] == position_choice_Team2)) |
                              ((df_Games['Home_Team'] == position_choice_Team2) &
                               (df_Games['Away_Team'] == position_choice_Team1))]

if Week != 'All Weeks':
    filtered_games = filtered_games[filtered_games['Week'] == Week]
if Year != 'All Seasons':
    filtered_games = filtered_games[filtered_games['Year'] == Year]

st.table(filtered_games)
