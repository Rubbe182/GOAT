import pandas as pd
import streamlit as st

st.set_page_config(
        page_title="1. Temporada_Regular",
)

#READ DATA
df_clasification = pd.read_csv('df_clasification.csv')
df_Games = pd.read_csv('df_Games.csv')
df_players = pd.read_csv('df_Players.csv')

st.sidebar.markdown('Temporada Regular')
#SELECTORS
st.title('Temporada Regular')
Week=df_clasification.Week.unique()
Year=df_clasification.Year.unique()
position_choice_year = st.radio('Year:', Year,horizontal=True)
position_choice_week = st.selectbox('Week:', Week)

#FILTER
df_clasification = df_clasification[df_clasification['Week']==(position_choice_week)]
df_clasification = df_clasification[df_clasification['Year']==(position_choice_year)]
df_clasification=df_clasification[['Team','Record','%W','GB','STRK','PF','AVG_PF','PA',
                                                'AVG_PA','DIV_Record','CON_Record']]

# FRANCHISE
Vince_Lombardi = ['Isma Ray Ravens', "Jrz French Faulk's", 'Darko LaDainian Texas *', 'Zgz Marino Phins',
             "Mile High Champ's",'Snake Stabler Raiders','Medina Allen Bills']
Brett_Favre = ['Javier Big Ben Steelers', 'GronkSpike', "The Adam´s Family", 'San Joe Montana 49ers'
               ,'Cowher Straight Outta Albacete']
Bruce_Smith = ['Franquicia Sin Nombre', 'Triana Bills Kelly', 'NavaWarner Rams', 'Indiana James',
               'El Predicador Almogávar', 'Pittsburgh Terror Lambert', 'Nafarroa Bills Kelly']
Marv_Levy = ["Smith's Terrible Showdown", 'Malaka Reed Poe', 'Córdoba Gunslingers Favre', "Vlc Tigers Watt's"]

# PRINT
st.subheader("CONFERENCIA REGGIE WHITE - DIVISIÓN VINCE LOMBARDI")
df_clasification_Shula = df_clasification[df_clasification['Team'].isin(Vince_Lombardi)]
df_clasification_Shula = df_clasification_Shula.set_index('Team')
st.dataframe(df_clasification_Shula.style.format({'%W': '{:.1f}', 'AVG_PF': '{:.1f}', 'AVG_PA': '{:.1f}'}))

st.subheader("CONFERENCIA REGGIE WHITE - DIVISIÓN BRETT FAVRE")
df_clasification_Csonka = df_clasification[df_clasification['Team'].isin(Brett_Favre)]
df_clasification_Csonka = df_clasification_Csonka.set_index('Team')
st.dataframe(df_clasification_Csonka.style.format({'%W': '{:.1f}', 'AVG_PF': '{:.1f}', 'AVG_PA': '{:.1f}'}))

st.subheader("CONFERENCIA JIM KELLY - DIVISIÓN BRUCE SMITH")
df_clasification_Smith = df_clasification[df_clasification['Team'].isin(Bruce_Smith)]
df_clasification_Smith = df_clasification_Smith.set_index('Team')
st.dataframe(df_clasification_Smith.style.format({'%W': '{:.1f}', 'AVG_PF': '{:.1f}', 'AVG_PA': '{:.1f}'}))

st.subheader("CONFERENCIA JIM KELLY - DIVISIÓN MARV LEVY")
df_clasification_Levy = df_clasification[df_clasification['Team'].isin(Marv_Levy)]
df_clasification_Levy = df_clasification_Levy.set_index('Team')
st.dataframe(df_clasification_Levy.style.format({'%W': '{:.1f}', 'AVG_PF': '{:.1f}', 'AVG_PA': '{:.1f}'}))


