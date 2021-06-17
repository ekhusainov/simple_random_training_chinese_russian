"""Simulator translator Russian-Chinese for my sweet wife."""
import os
import random

import numpy as np
import pandas as pd
import streamlit as st

FAIL_HTML = "<h3 style='color: red;'>FAIL!</h3>"
OK_HTML = "<h3 style='color: green;'>OK!</h3>"
PERMUTATIONS_PATH = "permutations"
RU_CH_FILE_PATH = "ru_ch.txt"
TEMP_CH_FILE_PATH = "temp_ch_file"
TEMP_RUS_FILE_FOR_SECOND_PATH = "temp_rus_file_part_2"
TEMP_RUS_FILE_PATH = "temp_ru_file"


def create_permute_file_if_not_exist(count_example_text):
    if not os.path.exists(PERMUTATIONS_PATH):
        permute = list(np.random.permutation(count_example_text))
        permute = list(map(str, permute))
        permute = " ".join(permute)
        with open(PERMUTATIONS_PATH, "w") as file_output:
            file_output.write(permute)


def read_first_index_and_del_it():
    if os.path.exists(PERMUTATIONS_PATH):
        with open(PERMUTATIONS_PATH, "r") as file_input:
            input_array = file_input.read()
        input_array = input_array.split()
        input_array = list(map(int, input_array))
        if len(input_array) == 0:
            os.remove(PERMUTATIONS_PATH)
            return 0
        answer_index = input_array.pop()
        input_array = list(map(str, input_array))
        input_array = " ".join(input_array)
        with open(PERMUTATIONS_PATH, "w") as file_output:
            file_output.write(input_array)
        return answer_index


def main():
    ru_ch_dict = pd.read_csv(RU_CH_FILE_PATH, sep=",")

    count_example_text = ru_ch_dict.shape[0]
    random_index = random.randint(0, count_example_text - 1)

    create_permute_file_if_not_exist(count_example_text)

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
        random_index_from_permute = read_first_index_and_del_it()
        chinese_text = ru_ch_dict["ch"][random_index_from_permute]
        russian_text = ru_ch_dict["ru"][random_index_from_permute]
        with open(TEMP_CH_FILE_PATH, "w", encoding='utf-8') as file_output:
            file_output.write(chinese_text)
        with open(TEMP_RUS_FILE_FOR_SECOND_PATH, "w", encoding='utf-8') as \
                file_output:
            file_output.write(russian_text)

    if os.path.exists(TEMP_RUS_FILE_FOR_SECOND_PATH):
        with open(TEMP_RUS_FILE_FOR_SECOND_PATH, "r", encoding='utf-8') as \
                file_input:
            ru_text = file_input.read()
        st.text(ru_text)

    our_chinese_answer = st.text_input("Введите сюда ответ.")
    with open(TEMP_CH_FILE_PATH, "r", encoding='utf-8') as file_input:
        chinese_text = file_input.read()
    if our_chinese_answer == chinese_text:
        st.markdown(OK_HTML, unsafe_allow_html=True)
    else:
        st.markdown(FAIL_HTML, unsafe_allow_html=True)

    if st.button("Translate to Chinese"):
        with open(TEMP_CH_FILE_PATH, "r", encoding='utf-8') as file_input:
            chinese_text = file_input.read()
        st.text(chinese_text)


if __name__ == "__main__":
    main()
