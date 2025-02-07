# ELBRUSE Bootcamp 
# 06-02-2025
# Home Work Week 8 Day 5
# team: Sergei, Vladislav, Andrey 
# abramov.andre@yandex.ru

import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#import yfinance as yf
import functools


#initialization ----------------------------

if 'train_file_value' not in st.session_state: 
    st.session_state['train_file_value'] = None
if 'test_file_value' not in st.session_state:
    st.session_state['test_file_value'] = None

if 'file_test_name' not in st.session_state:
    st.session_state['file_test_name'] = None
if 'train_file_name' not in st.session_state:
    st.session_state['train_file_name'] = None

if 'train_file_details' not in st.session_state:
    st.session_state['train_file_details'] = ''
if 'test_file_details' not in st.session_state:
    st.session_state['test_file_details'] = ''

# если определены два столбца из загруженного массива
if 'date_column' not in st.session_state:
    st.session_state['date_column'] = ''
if 'numeric_column' not in st.session_state:
    st.session_state['numeric_column'] = ''


#Основная страница  ----------------------------


# боковая панель
page01 = st.Page("page_01.py", title = 'Описание поставленной задачи')
page02 = st.Page("page_02.py", title = 'Модель спортивной фотографии')
page03 = st.Page("page_04.py", title = 'Модель клеток крови')
page04 = st.Page("page_07.py", title = 'Классификация по фотографии')

pg = st.navigation([page01, page02, page03, page04], expanded=True)
pg.run()

file_csv_train = None
file_csv_test = None


@st.cache_data
def load_selected_file(filename):
    answer = pd.read_csv(file_csv_train)
    return answer



st.sidebar.title('Команда проекта: ')
st.sidebar.write('Владислав Мороз')
st.sidebar.write('Сергей Чучалин')
st.sidebar.write('Андрей Абрамов')

    


    






