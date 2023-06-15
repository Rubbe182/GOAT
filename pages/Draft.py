import pandas as pd
import streamlit as st

df_Draft = pd.read_csv('Draft.csv',encoding='latin-1')
st.title("DRAFT")

# Mostrar la tabla en Streamlit
st.dataframe(df_Draft)

# Agregar filtros para cada columna
for col in df_Draft.columns:
    filter_values = df_Draft[col].unique()
    selected_values = st.multiselect(f'Filtrar por {col}', filter_values)
    filtered_df = df_Draft[df_Draft[col].isin(selected_values)]
    
    # Mostrar el resultado filtrado
    st.dataframe(filtered_df)
