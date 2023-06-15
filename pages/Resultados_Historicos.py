import pandas as pd
import streamlit as st
import plotly.express as px


df_clasification = pd.read_csv('df_clasification.csv')
st.title("Clasificación histórica")

df_historica=pd.DataFrame()
df_historica_agregada=pd.DataFrame()

df_historica['Year']=df_clasification['Year']
df_historica['Week']=df_clasification['Week']
df_historica['Team']=df_clasification['Team']
split_records = df_clasification['Record'].str.split('-', n=2, expand=True).apply(lambda x: x.str.strip())
df_historica['Win'] = split_records[0].astype(int)
df_historica['Lose'] = split_records[1].astype(int)
df_historica['Tie'] = split_records[2].astype(int)
df_historica=df_historica[df_historica['Week']==13]

Year=df_historica.Year.unique()
Year=[2019,2020,2021,2022,'Histórico']
position_choice_year = st.radio('Year:', Year,horizontal=True)
if position_choice_year == 'Histórico':

    df_historica_agregada['Win'] = df_historica[df_historica['Week'] == 13].groupby('Team')['Win'].sum()
    df_historica_agregada['Lose'] = df_historica[df_historica['Week'] == 13].groupby('Team')['Lose'].sum()
    df_historica_agregada=df_historica_agregada.sort_values(by='Win',ascending=False)
    st.dataframe(df_historica_agregada.style.format({'Win': '{:.0f}', 'Lose': '{:.0f}'}), width=300)

    Record = ['Win', 'Lose']
    position_choice_record = st.radio('Record:', Record, horizontal=True)
    if position_choice_record=='Win':
        df_historica_agregada = df_historica_agregada.sort_values(by='Win', ascending=True)
        fig = px.bar(df_historica_agregada, x=['Win'], orientation='h',
                     title="Historical Record", height=500, width=1000,
                     labels={'value': 'Record'}, barmode='group')
        fig.update_layout(showlegend=False)
        fig.update_traces(marker_color='#349EF6', marker_line_color='rgb(8,48,107)',
                          marker_line_width=1.5, opacity=0.6)
        st.write(fig)
    if position_choice_record=='Lose':
        df_historica_agregada = df_historica_agregada.sort_values(by='Lose', ascending=False)
        fig = px.bar(df_historica_agregada, x=['Lose'], orientation='h',
                     title="Historical Record",height=500,width=1000,
                     labels={'value':'Record'},barmode='group')
        fig.update_layout(showlegend=False)
        fig.update_traces(marker_color='#F64634', marker_line_color='#DE1500',
                          marker_line_width=1.5, opacity=0.6)
        st.write(fig)
else:
    df_historica = df_historica[df_historica['Year'] == position_choice_year]
    df_historica_agregada['Win']=df_historica[df_historica['Week']==13].groupby('Team')['Win'].sum()
    df_historica_agregada['Lose']=df_historica[df_historica['Week']==13].groupby('Team')['Lose'].sum()
    df_historica_agregada=df_historica_agregada.sort_values(by='Win',ascending=False)
    st.dataframe(df_historica_agregada.style.format({'Win': '{:.0f}', 'Lose': '{:.0f}'}),width=300)

    df_historica_agregada = df_historica_agregada.sort_values(by='Win', ascending=False)
    fig = px.bar(df_historica_agregada, y=['Win','Lose'], orientation='v',
                 title="Season Record", height=500, width=1000,
                 labels={'value': 'Record'})
    fig.update_layout(legend_title_text='')
    #fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                      #marker_line_width=1.5, opacity=0.6)
    st.write(fig)

