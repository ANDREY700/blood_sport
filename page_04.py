# ELBRUSE Bootcamp 
# 06-02-2025
# Home Work Week 8 Day 5
# team: Sergei, Vladislav, Andrey 
# abramov.andre@yandex.ru

# Page 04 of Streamlit project

import streamlit as st
import pandas as pd

st.title('Модель классификации клеток крови')
st.write('Описание модели')

st.write('Базовая модель: ResNet18')
st.subheader('График потерь при обучении модели: ')

data2 = pd.read_csv('data_blood_eff3.csv')
#char_data = pd.DataFrame([np.random.randint(20), np.random.randint(20)], columns = ['train loss', 'valid loss']) 
#st.dataframe(data1)
st.line_chart(data2[['train_losses', 'valid_losses']])

st.subheader('График метрик при обучении модели: ')
st.line_chart(data2[['train_metric', 'valid_metric']])

st.subheader('График времени обучения модели по каждой эпохе: ')
temp01 = data2.loc[0, 'time']
data2['total_time'] = temp01
for i in range(1, len(data2)):
    temp01 += data2.loc[i, 'time']
    data2.loc[i, 'total_time'] = temp01

st.line_chart(data2[['total_time']])

st.subheader('Состав dataset обучения модели:')
st.write(' - число объектов')
st.write(' - распределение по классам')
st.write(' - метрика f1')
st.write(' - confusion matrix')
