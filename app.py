import pandas as pd
import plotly.express as px
import streamlit as st

# --- Configuración general de la página ---
st.set_page_config(page_title="Car Sales Dashboard",
                   page_icon=":car:", layout="wide")

# --- Importamos los datos procesados ---
df = pd.read_csv('processed.csv')
# Mejoramos la visualización
df['brand'] = df['brand'].str.title()
df['condition'] = df['condition'].str.title()
df['sale_date'] = pd.to_datetime(df['sale_date']).dt.date

# --- Sidebar ---
st.sidebar.header('Por favor filtre aquí:')
period = st.sidebar.slider(
    'Periodo',
    min_value=df['sale_date'].min(),
    max_value=df['sale_date'].max(),
    value=(df['sale_date'].min(), df['sale_date'].max())
)
brand = st.sidebar.multiselect(
    'Marca',
    options=sorted(df['brand'].unique()),
    default=df['brand'].unique()
)
condition = st.sidebar.multiselect(
    'Condición',
    options=sorted(df['condition'].unique()),
    default=df['condition'].unique()
)
odometer = st.sidebar.slider(
    'Kilometraje',
    value=[int(df['odometer'].min()), int(df['odometer'].max())],
)

# -- Filtrado de datos --
my_query = 'sale_date >= @period[0] & sale_date <= @period[1] & brand == @brand & condition == @condition & odometer >= @odometer[0] & odometer <= @odometer[1]'
df_in_screen = df.query(my_query)

# --- Main page ---
st.title(':car: Car Sales Dashboard')
st.markdown('##')

# Abstract
total_sales = df_in_screen['price'].sum()
sales_percentage = df_in_screen['price'].sum() / df['price'].sum()
money_rating = ':moneybag:' * int(sales_percentage * 10)

if (len(df_in_screen) != 0):
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader('Total de ventas:')
        st.subheader(f'US ${total_sales:,}')

    with middle_column:
        st.subheader('Porcentaje de ventas:')
        st.subheader(f'{money_rating}')
        st.text(f'{sales_percentage:.0%}')

    with right_column:
        st.subheader('Vehículos vendidos:')
        st.subheader(f'{len(df_in_screen)}')

    st.markdown('---')

    # --- Graficos ---
    count_pivot = df_in_screen.pivot_table(
        index='brand', columns='type', values='price', aggfunc='count'
    ).fillna(0)
    count_pivot['total'] = count_pivot.sum(axis=1)
    count_pivot.sort_values(by='total', ascending=False, inplace=True)

    brand_pivot = df_in_screen.pivot_table(
        index='brand', columns='type', values='price', aggfunc='sum'
    ).fillna(0).sort_values(by='brand', ascending=False)
    brand_pivot['total'] = brand_pivot.sum(axis=1)
    brand_pivot.sort_values(by='total', ascending=False, inplace=True)

    date_pivot = df_in_screen.pivot_table(
        index='sale_date', columns='brand', values='price', aggfunc='sum'
    ).fillna(0)

    fig1 = px.bar(count_pivot, x=count_pivot.index,
                y=count_pivot.columns[:-1],
                title='<b>Cantidad de ventas por marca</b>',
                labels={'brand': 'Marca', 'value': 'Número de autos vendidos'})
    fig2 = px.bar(brand_pivot, x=brand_pivot.index,
                y=brand_pivot.columns[:-1],
                title='<b>Suma de ventas totales por marcas</b>',
                labels={'brand': 'Marca', 'value': 'Ventas totales en dólares'})

    # --- Middle ---
    left_column, right_column = st.columns(2)
    with left_column:
        st.plotly_chart(fig1)

    with right_column:
        st.plotly_chart(fig2)
        
    fig3 = px.line(date_pivot, x=date_pivot.index,
                y=date_pivot.columns, markers=True,
                title='<b>Ventas totales diarias por marca</b>',
                labels={'sale_date': 'Día', 'value': 'Ventas en dólares'})
    st.plotly_chart(fig3)
else:
    st.header('No hay datos que mostrar')
    st.subheader(':eyes: Por favor actualiza los filtros')
