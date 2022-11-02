import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np


df_Games = pd.read_csv('df_Games.csv')
st.title("Historial Partidos")
st.sidebar.markdown('Historial Partidos Temporada Regular')
df_Games=df_Games[['Year','Week','Home_Team','Away_Team','Home_Points','Away_Points']]
Weeks=['1','2','3','4','5','6','7','8','9','10','11','12','13']
df_Games=df_Games[df_Games.Week.isin(Weeks)]

Week=['All Weeks','1','2','3','4','5','6','7','8','9','10','11','12','13']
Year=['All Seasons',2019,2020,2021]
Teams=df_Games.Home_Team.unique()

position_choice_year = st.radio('Year:', Year,horizontal=True)
position_choice_week = st.selectbox('Week:', Week)


Display_options=['Completo','Selección Franquicia','Head to Head']
position_choice_display = st.radio('', Display_options)

if position_choice_display=='Selección Franquicia':
    position_choice_Team = st.multiselect('Team:', Teams)
    if position_choice_year=='All Seasons' and position_choice_week=='All Weeks':
        df_Games = df_Games.loc[(df_Games['Home_Team'].isin(position_choice_Team)) |
                                (df_Games['Away_Team'].isin(position_choice_Team))]
        st.dataframe(df_Games, width=2000)
    elif position_choice_week=='All Weeks':
        df_Games = df_Games.loc[(df_Games['Home_Team'].isin(position_choice_Team)) |
                                (df_Games['Away_Team'].isin(position_choice_Team))]
        df_Games = df_Games[df_Games['Year']==(position_choice_year)]
        st.dataframe(df_Games, width=2000)
    elif position_choice_year=='All Seasons':
        df_Games = df_Games.loc[(df_Games['Home_Team'].isin(position_choice_Team)) |
                                (df_Games['Away_Team'].isin(position_choice_Team))]
        df_Games = df_Games[df_Games['Week']==(position_choice_week)]
        st.dataframe(df_Games, width=2000)
    else:
        df_Games = df_Games.loc[(df_Games['Home_Team'].isin(position_choice_Team)) |
                                (df_Games['Away_Team'].isin(position_choice_Team))]
        df_Games = df_Games[df_Games['Year']==(position_choice_year)]
        df_Games = df_Games[df_Games['Week']==(position_choice_week)]
        st.dataframe(df_Games,width=2000)

elif position_choice_display=='Head to Head':
    position_choice_Team1 = st.selectbox('Team 1:', Teams)
    position_choice_Team2 = st.selectbox('Team 2:', Teams)
    if position_choice_year=='All Seasons' and position_choice_week=='All Weeks':
        df_Games = df_Games.loc[(df_Games['Home_Team']==(position_choice_Team1)) &
                                (df_Games['Away_Team']==(position_choice_Team2))|
                                (df_Games['Away_Team']==(position_choice_Team1))&
                                (df_Games['Away_Team']==(position_choice_Team2))]
        st.dataframe(df_Games, width=2000)
    elif position_choice_week=='All Weeks':
        df_Games = df_Games.loc[(df_Games['Home_Team'] == (position_choice_Team1)) &
                                (df_Games['Away_Team'] == (position_choice_Team2)) |
                                (df_Games['Away_Team'] == (position_choice_Team1)) &
                                (df_Games['Away_Team'] == (position_choice_Team2))]
        df_Games = df_Games[df_Games['Year']==(position_choice_year)]
        st.dataframe(df_Games, width=2000)
    elif position_choice_year=='All Seasons':
        df_Games = df_Games.loc[(df_Games['Home_Team'] == (position_choice_Team1)) &
                                (df_Games['Away_Team'] == (position_choice_Team2)) |
                                (df_Games['Away_Team'] == (position_choice_Team1)) &
                                (df_Games['Away_Team'] == (position_choice_Team2))]
        df_Games = df_Games[df_Games['Week']==(position_choice_week)]
        st.dataframe(df_Games, width=2000)
    else:
        df_Games = df_Games.loc[(df_Games['Home_Team'] == (position_choice_Team1)) &
                                (df_Games['Away_Team'] == (position_choice_Team2)) |
                                (df_Games['Away_Team'] == (position_choice_Team1)) &
                                (df_Games['Away_Team'] == (position_choice_Team2))]
        df_Games = df_Games[df_Games['Year']==(position_choice_year)]
        df_Games = df_Games[df_Games['Week']==(position_choice_week)]
        st.dataframe(df_Games,width=2000)

else:
    if position_choice_year=='All Seasons' and position_choice_week=='All Weeks':
        st.dataframe(df_Games, width=2000)
    elif position_choice_week=='All Weeks':
        df_Games = df_Games[df_Games['Year']==(position_choice_year)]
        st.dataframe(df_Games, width=2000)
    elif position_choice_year=='All Seasons':
        df_Games = df_Games[df_Games['Week']==(position_choice_week)]
        st.dataframe(df_Games, width=2000)
    else:
        df_Games = df_Games[df_Games['Year']==(position_choice_year)]
        df_Games = df_Games[df_Games['Week']==(position_choice_week)]
        st.dataframe(df_Games,width=2000)