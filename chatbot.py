import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

st.title("🤖 Chatbot DialoGPT")

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

chat_history_ids = None
input_text = st.text_input("Ketik pertanyaanmu:")

if st.button("Kirim") and input_text:
    new_input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='pt')

    if chat_history_ids is None:
        chat_history_ids = new_input_ids
    else:
        chat_history_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)

    output = model.generate(chat_history_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[:, chat_history_ids.shape[-1]:][0], skip_special_tokens=True)

    st.text_area("Bot:", value=response, height=150)