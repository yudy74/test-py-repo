# import streamlit as st

# # Judul aplikasi
# st.title("Aplikasi Quiz Sederhana")

# # Teks biasa
# st.write("Selamat datang di aplikasi quiz!")

# # Input teks
# name = st.text_input("Masukkan nama kamu:")

# # Tombol
# if st.button("Mulai Quiz"):
#     st.write(f"Halo, {name}! Ayo kita mulai kuisnya.")


import streamlit as st

st.title("Mini Quiz App")

# Menampilkan pertanyaan
st.write("Pertanyaan: Siapa penemu bahasa Python?")

# Opsi jawaban
jawaban = st.radio(
    "Pilih jawaban kamu:",
    ["Guido van Rossum", "Dennis Ritchie", "James Gosling"]
)

# Button untuk submit
if st.button("Submit Jawaban"):
    if jawaban == "Guido van Rossum":
        st.success("Benar! 👏")
    else:
        st.error("Salah. Jawaban yang benar adalah Guido van Rossum.")