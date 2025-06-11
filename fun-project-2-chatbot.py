import streamlit as st
import requests

# ========== CONFIG ==========
OPENROUTER_API_KEY = "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"  # Ganti dengan OpenRouter API Key-mu
MODEL = "deepseek/deepseek-r1-0528-qwen3-8b:free"  # Atau ganti sesuai model favoritmu

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": "http://localhost:8501",  # Ganti dengan domain kamu
    "X-Title": "AI Chatbot Streamlit"
}

API_URL = "https://openrouter.ai/api/v1/chat/completions"

# ========== STREAMLIT APP ==========
st.title("🧠 AI Chatbot Bubble Style")
st.markdown(f"Powered by `{MODEL}` via OpenRouter 🤖")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Tampilkan chat sebelumnya
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# Input dari pengguna
user_input = st.chat_input("Tulis pesan di sini...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Kirim ke OpenRouter API
    with st.spinner("Mengetik..."):
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)

        if response.status_code == 200:
            bot_reply = response.json()['choices'][0]['message']['content']
        else:
            bot_reply = "⚠️ Maaf, gagal mengambil respons dari OpenRouter."

    st.chat_message("assistant").markdown(bot_reply)
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})