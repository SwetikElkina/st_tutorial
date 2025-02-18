import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Название приложения
st.title('Анализ данных по DataFrame')

# Шаг 1: Загрузка CSV файла
uploaded_file = st.sidebar.file_uploader('Загрузите CSV файл', type='csv')

if uploaded_file is not None:
    # Чтение загруженного файла в датафрейм
    df = pd.read_csv(uploaded_file)
    st.write("Первые 5 строк загруженного датафрейма:")
    st.write(df.head())

    # Шаг 2: Выбор типа графика
    chart_type = st.sidebar.selectbox("Выберите тип графика:", ["Гистограмма", "Коробчатая диаграмма"])

    if chart_type == "Гистограмма":
        # Построение гистограммы
        col = st.sidebar.selectbox("Выберите колонку для гистограммы:", df.columns)
        plt.figure(figsize=(10, 5))
        sns.histplot(df[col], kde=True)
        plt.title(f'Гистограмма для {col}')
        plt.xlabel(col)
        plt.ylabel('Частота')
        st.pyplot(plt)

        # Скачивание графика
        plt.savefig('histogram.png')
        with open('histogram.png', 'rb') as f:
            st.download_button("Скачать график", f, "histogram.png", "image/png")

    elif chart_type == "Коробчатая диаграмма":
        # Построение коробчатой диаграммы
        col = st.sidebar.selectbox("Выберите колонку для коробчатой диаграммы:", df.columns)
        plt.figure(figsize=(12, 5))
        sns.boxplot(y=df[col])
        plt.title(f'Коробчатая диаграмма для {col}')
        st.pyplot(plt)

        # Скачивание графика
        plt.savefig('boxplot.png')
        with open('boxplot.png', 'rb') as f:
            st.download_button("Скачать график", f, "boxplot.png", "image/png")
