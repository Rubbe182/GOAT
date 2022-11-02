import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np


df_Games = pd.read_csv('df_Games.csv')
st.title("Historial Playoffs")
st.sidebar.markdown('Historial Partidos Playoffs')
df_Games=df_Games[['Year','Week','Home_Team','Away_Team','Home_Points','Away_Points']]
Rounds=['Divisional playoffs ','Conference Championship','GOAT Bowl']
df_Games=df_Games[df_Games.Week.isin(Rounds)]
df_Games = df_Games.rename(columns={'Home_Points': 'H_P', 'Away_Points': 'A_P'})
data = [['Darko LaDainian Texas *', 3,0], ['Isma Ray Ravens', 4,2], ["Jrz French Faulk's", 4,3],
        ['Javier Big Ben Steelers', 0,2], ['GronkSpike', 0,2], ["Pittsburgh Terror Lambert", 0,1],
        ['Nafarroa Bills Kelly', 1,3], ['El Predicador Almogávar', 0,1], ["Smith's Terrible Showdown", 4,3],
        ['Malaka Reed Poe', 0,1], ["Vlc Tigers Watt's", 5,1]]
df_Games_PO=pd.DataFrame(data,columns=['Team','Win','Lose'])
df_Games_PO['Total']=df_Games_PO['Win']+df_Games_PO['Lose']
df_Games_PO=df_Games_PO.set_index('Team')

Week=['All Weeks','Divisional playoffs ','Conference Championship','GOAT Bowl']
Year=['All Seasons',2019,2020,2021]
Teams=df_Games.Home_Team.unique()
Data=['Records','Games']
position_choice_data = st.radio('', Data, horizontal=True)

if position_choice_data=='Records':
    df_Games_PO = df_Games_PO.sort_values(by='Win', ascending=False)
    st.dataframe(df_Games_PO)
if position_choice_data=='Games':
    position_choice_year = st.radio('Year:', Year, horizontal=True)
    position_choice_week = st.selectbox('Week:', Week)

    Display_options = ['Completo', 'Selección Franquicia', 'Head to Head']
    position_choice_display = st.radio('', Display_options, horizontal=True)
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