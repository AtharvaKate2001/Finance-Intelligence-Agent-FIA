import streamlit as st
import requests

API_URL = "http://backend:8000/ask"

st.set_page_config(page_title="Finance AI Assistant", page_icon="💰")

st.title("💰 Finance AI Assistant")
st.caption("Powered by Agentic RAG + Ollama")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask a finance question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = requests.post(
                API_URL,
                json={"query": user_input}
            )

            answer = response.json()["response"]

            st.write(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )