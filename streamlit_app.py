"""Title"""
import random
import os

import pandas as pd
import numpy as np
import streamlit as st

RU_CH_FILE_PATH = "ru_ch.txt"
TEMP_RUS_FILE_PATH = "temp_ru_file"
TEMP_CH_FILE_PATH = "temp_ch_file"
TEMP_RUS_FILE_FOR_SECOND_PATH = "temp_rus_file_part_2"


def main():
    ru_ch_dict = pd.read_csv(RU_CH_FILE_PATH, sep=",")

    count_example_text = ru_ch_dict.shape[0]
    random_index = random.randint(0, count_example_text - 1)
    if st.button("Random Chinese text"):
        chinese_text = ru_ch_dict["ch"][random_index]
        russian_text = ru_ch_dict["ru"][random_index]
        st.text(chinese_text)
        with open(TEMP_RUS_FILE_PATH, "w") as file_output:
            file_output.write(russian_text)

    if st.button("Translate to Rusian"):
        with open(TEMP_RUS_FILE_PATH, "r") as file_input:
            russian_text = file_input.read()
        st.text(russian_text)

    st.markdown("<hr align='center' width='500' size='1' color='#ff0000' />",
                unsafe_allow_html=True)

    if st.button("Random Russian text"):
        chinese_text = ru_ch_dict["ch"][random_index]
        russian_text = ru_ch_dict["ru"][random_index]
        # st.text(russian_text)
        with open(TEMP_CH_FILE_PATH, "w", encoding='utf-8') as file_output:
            file_output.write(chinese_text)
        with open(TEMP_RUS_FILE_FOR_SECOND_PATH, "w", encoding='utf-8') as file_output:
            file_output.write(russian_text)

    if os.path.exists(TEMP_RUS_FILE_FOR_SECOND_PATH):
        with open(TEMP_RUS_FILE_FOR_SECOND_PATH, "r", encoding='utf-8') as file_input:
            ru_text = file_input.read()
        st.text(ru_text)

    our_chinese_answer = st.text_input("Введите сюда ответ.")
    with open(TEMP_CH_FILE_PATH, "r", encoding='utf-8') as file_input:
        chinese_text = file_input.read()
    if our_chinese_answer == chinese_text:
        st.markdown("<h3 style='color: green;'>OK!</h3>",
                    unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color: red;'>FAIL!</h3>",
                    unsafe_allow_html=True)

    if st.button("Translate to Chinese"):
        with open(TEMP_CH_FILE_PATH, "r", encoding='utf-8') as file_input:
            chinese_text = file_input.read()
        st.text(chinese_text)


if __name__ == "__main__":
    main()
