# ELBRUSE Bootcamp 
# 06-02-2025
# Home Work Week 8 Day 5
# team: Sergei, Vladislav, Andrey 
# abramov.andre@yandex.ru

import streamlit as st
import pandas as pd



#initialization ----------------------------


#Основная страница  ----------------------------
# боковая панель
page01 = st.Page("page_01.py", title = 'Описание поставленной задачи')
page02 = st.Page("page_02.py", title = 'Модель спортивной фотографии')
page03 = st.Page("page_04.py", title = 'Модель клеток крови')
page04 = st.Page("page_07.py", title = 'Классификация по фотографии')

pg = st.navigation([page01, page02, page03, page04], expanded=True)
pg.run()


st.sidebar.title('Команда проекта: ')
st.sidebar.write('Владислав Мороз')
st.sidebar.write('Сергей Чучалин')
st.sidebar.write('Андрей Абрамов')

    


    






