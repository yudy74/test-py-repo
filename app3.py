import streamlit as st

score = 0

qna = {
    "1 + 1 = ?": "2",
    "Hewan berkaki 8?": "Laba-laba",
    "Bahasa pemrograman populer untuk AI?": "Python"
}

for q, a in qna.items():
    user_answer = st.text_input(q, key=q)
    if user_answer:
        if user_answer.lower() == a.lower():
            st.success("Benar!")
            score += 1
        else:
            st.warning("Salah!")

if st.button("Lihat Skor"):
    st.write(f"Skor akhir kamu adalah: {score} dari {len(qna)}")