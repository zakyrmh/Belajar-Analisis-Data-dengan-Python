import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Title page
st.set_page_config(page_title="Air Quality from Dongsi Analysis by Zaxxy")

# Load dataset
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "data.csv")

# Baca file CSV
data = pd.read_csv(file_path)

# Title of the dashboard
st.title('Air Quality Analysis Dashboard: Dongsi Station')

# Description
st.write('Interactive dashboard to explore air quality data in Dongsi.')

# About me
st.markdown("""
### About Me
- **Name**: Zaky Ramadhan
- **Email Address**: zaxxyyramadhan@gmail.com
- **Dicoding ID**: [zaxxyrmh](https://www.dicoding.com/users/zaxxyrmh)

### Project Overview
This dashboard is designed to analyze air quality based on PM2.5 and wind speed (WSPM) data. Visualization of the relationship between wind speed and pollutant concentrations, as well as the number of days in each air quality category, such as "Good," "Moderate," to "Hazardous." This dashboard makes it easier for users to understand air quality patterns and the factors that influence them through interactive and informative graphics.
""")

# Fungsi untuk klasifikasi kualitas udara berdasarkan PM2.5
def classify_air_quality(pm25):
    if pm25 <= 50:
        return 'Good'
    elif 51 <= pm25 <= 100:
        return 'Moderate'
    elif 101 <= pm25 <= 150:
        return 'Unhealthy for Sensitive Groups'
    elif 151 <= pm25 <= 200:
        return 'Unhealthy'
    elif 201 <= pm25 <= 300:
        return 'Very Unhealthy'
    else:
        return 'Hazardous'

# Pastikan kolom penting ada di data
if 'PM2.5' in data.columns and 'WSPM' in data.columns:
    # Tambahkan kolom 'Date' berdasarkan 'year', 'month', dan 'day'
    data['Date'] = pd.to_datetime(data[['year', 'month', 'day']])
    
    # Tambahkan kolom kategori kualitas udara
    data['Air_Quality'] = data['PM2.5'].apply(classify_air_quality)
    
    # Filter berdasarkan tanggal
    st.sidebar.header('Filter by Date Range')
    start_date = st.sidebar.date_input('Start Date', data['Date'].min())
    end_date = st.sidebar.date_input('End Date', data['Date'].max())
    
    # Filter data berdasarkan rentang tanggal yang dipilih
    filtered_data = data[(data['Date'] >= pd.to_datetime(start_date)) & (data['Date'] <= pd.to_datetime(end_date))]

    # Filter berdasarkan kategori kualitas udara
    st.sidebar.header('Filter by Air Quality')
    air_quality_options = filtered_data['Air_Quality'].unique()
    selected_quality = st.sidebar.multiselect('Select Air Quality Categories', air_quality_options, default=air_quality_options)
    
    # Filter data berdasarkan kualitas udara
    filtered_data = filtered_data[filtered_data['Air_Quality'].isin(selected_quality)]
    
    # Visualisasi hubungan kecepatan angin (WSPM) dengan konsentrasi PM2.5
    st.subheader("Analisis Hubungan Kecepatan Angin dengan Konsentrasi Polutan")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=filtered_data, x='WSPM', y='PM2.5', alpha=0.5, ax=ax)
    sns.regplot(data=filtered_data, x='WSPM', y='PM2.5', scatter=False, color='red', ax=ax)
    ax.set_title("Hubungan Kecepatan Angin (WSPM) dengan PM2.5")
    ax.set_xlabel("Kecepatan Angin (WSPM)")
    ax.set_ylabel("Konsentrasi PM2.5")
    st.pyplot(fig)
    
    # Analisis jumlah hari berdasarkan kategori kualitas udara
    st.subheader("Jumlah Hari Berdasarkan Kategori Kualitas Udara")
    air_quality_counts = filtered_data.groupby(['Air_Quality']).size().reset_index(name='count')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=air_quality_counts, x='Air_Quality', y='count', hue='Air_Quality', palette='viridis', ax=ax)
    ax.set_title("Jumlah Hari Berdasarkan Kategori Kualitas Udara")
    ax.set_xlabel("Kategori Kualitas Udara")
    ax.set_ylabel("Jumlah Hari")
    ax.set_xticks(range(len(air_quality_counts)))
    ax.set_xticklabels(air_quality_counts['Air_Quality'], rotation=45)
    st.pyplot(fig)
else:
    st.error("Data tidak memiliki kolom yang sesuai ('PM2.5' dan 'WSPM'). Harap periksa file Anda.")
