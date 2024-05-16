import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
from transformers import pipeline
from translator import translate

# zaczynamy od zaimportowania bibliotek
st.header('Aplikacja jezykowa')
st.image("https://assets-global.website-files.com/636953b3e258388b531936b5/6394e363831ce21ffda36ab2_become.png", use_column_width=True)
# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

# Inne przykłady do wypróbowania:
st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
#st.info('Informacja...')
# st.success('Udało się!')

#st.spinner()
#with st.spinner(text='Pracuję...'):
#    time.sleep(2)
#    st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.header('Opis aplikacji')
st.text("Moja aplikacja ma dwa zastosowania:")
st.text("Pierwszy to ocenia nam wydzwięk emocjonalny tekstu czyli czy podane słowo jest ")
st.text("negatywne czy pozytywne, a drugim zastosowaniem jest tłumacz angielsko-niemiecki.")
st.text("Wpisz dowolną fraze, a on ją przetłumaczy :D")
st.header("Instrukcja")
st.text("1.Wybierz opcje z listy")
st.text("2.Wpisz słowo lub fraze po angielsku")
st.text("3.W zależności co wybrałeś ciesz się przetłumaczonym textem lub")
st.text("programem do wyznaczania wydzwięku emocjonalnego w jezyku angielskim")
st.text("4.Zatwierdz kombinacją przycisków 'Ctrl+Enter'")
option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tlumacz angielsko-niemiecki",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.spinner()
        with st.spinner(text='Pracuję...'):
            time.sleep(3)
            st.success('Done')
        st.write(answer) 
if option == "Tlumacz angielsko-niemiecki":
    text = st.text_area(label="Wpisz tekst")
    if text:
        answer = translate(text)
        st.spinner()
        with st.spinner(text='Pracuję...'):
            time.sleep(3)
            st.success('Done')
        st.write(answer)

st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/docs/transformers/index')
st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')

st.header('Indeks: s22595')