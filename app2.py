import streamlit as st

# Judul aplikasi
st.title("Aplikasi Quiz Sederhana")

# Teks biasa
st.write("Selamat datang di aplikasi quiz!")

# Input teks
name = st.text_input("Masukkan nama kamu:")

# Tombol
if st.button("Mulai Quiz"):
    st.write(f"Halo, {name}! Ayo kita mulai kuisnya.")
	
st.image("logo.png", caption="Logo Quiz", width=200)

question = "Apa ibu kota Indonesia?"
options = ["Jakarta", "Bandung", "Surabaya"]

answer = st.radio(question, options)

if st.button("Submit Jawaban"):
    if answer == "Jakarta":
        st.success("Jawaban kamu benar!")
    else:
        st.error("Jawaban salah, coba lagi!")