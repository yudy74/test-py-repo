import streamlit as st
import requests
import os

# ========== CONFIG ==========
API_OPTIONS = {
    "Deepseek R1": {
        "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
        "api_url": "https://openrouter.ai/api/v1/chat/completions",
        "headers": lambda key: {
            "Authorization": f"Bearer {key}",
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": "AI Chatbot Streamlit"
        }
    },
    "Meta Llama": {
        "model": "meta-llama/llama-3.3-8b-instruct:free",
        "api_url": "https://openrouter.ai/api/v1/chat/completions",
        "headers": lambda key: {
            "Authorization": f"Bearer {key}",
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": "AI Chatbot Streamlit"
        }
    },
    "QWEN 3": {
        "model": "qwen/qwen3-235b-a22b:free",
        "api_url": "https://openrouter.ai/api/v1/chat/completions",
        "headers": lambda key: {
            "Authorization": f"Bearer {key}",
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": "AI Chatbot Streamlit"
        }
    },
    "Olympic Coder": {
        "model": "open-r1/olympiccoder-32b:free",
        "api_url": "https://openrouter.ai/api/v1/chat/completions",
        "headers": lambda key: {
            "Authorization": f"Bearer {key}",
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": "AI Chatbot Streamlit"
        }
    }
}

SYSTEM_PROMPT = "You are a helpful assistant."

# ========== STREAMLIT APP ==========
st.title("🧠 AI Chatbot Bubble Style")
api_choice = st.selectbox("Pilih API:", list(API_OPTIONS.keys()))
api_config = API_OPTIONS[api_choice]

# Only ask for API key once per session for all models
if "api_key_global" not in st.session_state:
    user_api_key = st.text_input(
        "Masukkan API Key OpenRouter (hanya sekali per sesi):",
        type="password"
    )
    if user_api_key.strip():
        st.session_state["api_key_global"] = user_api_key.strip()
        st.success("API Key berhasil disimpan untuk sesi ini. Silakan lanjutkan chat.")
        st.rerun()
else:
    api_key = st.session_state["api_key_global"]

    model = api_config["model"]
    api_url = api_config["api_url"]
    headers = api_config["headers"](api_key)

    st.markdown(f"Powered by `{model}` via {api_choice} 🤖")

    def get_bot_reply(history):
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        for chat in history:
            messages.append({"role": chat["role"], "content": chat["content"]})
        payload = {
            "model": model,
            "messages": messages
        }
        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"⚠️ Maaf, gagal mengambil respons dari {api_choice}. ({e})"

    if "chat_history" not in st.session_state or st.session_state.get("last_api") != api_choice:
        st.session_state.chat_history = []
        st.session_state.last_api = api_choice

    # Display chat history
    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.markdown(chat["content"])

    user_input = st.chat_input("Tulis pesan di sini...")

    if user_input:
        st.chat_message("user").markdown(user_input)
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        with st.spinner("Mengetik..."):
            bot_reply = get_bot_reply(st.session_state.chat_history)
        st.chat_message("assistant").markdown(bot_reply)
        st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})