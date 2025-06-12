import streamlit as st
import requests
import os

# ========== CONFIG ==========
API_OPTIONS = {
    "Deepseek R1": {
        "api_key_env": "OPENROUTER_API_KEY",
        "default_key": "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",
        "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
        "api_url": "https://openrouter.ai/api/v1/chat/completions",
        "headers": lambda key: {
            "Authorization": f"Bearer {key}",
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": "AI Chatbot Streamlit"
        }
    },
    "Meta Llama": {
        "api_key_env": "OPENROUTER_API_KEY",
        "default_key": "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",  # Replace with your OpenAI key or leave as placeholder
        "model": "meta-llama/llama-3.3-8b-instruct:free",
        "api_url": "https://openrouter.ai/api/v1/chat/completions",
        "headers": lambda key: {
            "Authorization": f"Bearer {key}"
        }
    },
    "QWEN 3": {
        "api_key_env": "OPENROUTER_API_KEY",
        "default_key": "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",  # Replace with your OpenAI key or leave as placeholder
        "model": "qwen/qwen3-235b-a22b:free",
        "api_url": "https://openrouter.ai/api/v1/chat/completions",
        "headers": lambda key: {
            "Authorization": f"Bearer {key}"
        }
    },
    "Olympic Coder": {
        "api_key_env": "OPENROUTER_API_KEY",
        "default_key": "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",  # Replace with your OpenAI key or leave as placeholder
        "model": "open-r1/olympiccoder-32b:free",
        "api_url": "https://openrouter.ai/api/v1/chat/completions",
        "headers": lambda key: {
            "Authorization": f"Bearer {key}"
        }
    }
}

SYSTEM_PROMPT = "You are a helpful assistant."

# ========== STREAMLIT APP ==========
st.title("🧠 AI Chatbot Bubble Style")
api_choice = st.selectbox("Pilih API:", list(API_OPTIONS.keys()))

api_config = API_OPTIONS[api_choice]
api_key = os.getenv(api_config["api_key_env"], api_config["default_key"])
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
        # OpenAI and OpenRouter have similar response structure for chat completions
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