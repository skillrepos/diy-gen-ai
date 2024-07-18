import streamlit as st
import ollama

st.title("Bryans cool chat app")

if "messages" not in st.session_state:
    st.session_state["messages"] = [ {"role": "assistant", "content": "What can I help you with today?"} ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

def generate_response():
    response = ollama.chat(model="phi3:mini", stream=True, messages=st.session_state.messages)
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        st.session_state["full_message"] += token
        yield token

if prompt := st.chat_input():
    st.session_state.messages.append({ "role": "user", "content": prompt })
    st.chat_message("user").write(prompt)
    st.session_state["full_message"] = ""
    st.chat_message("assistant").write_stream(generate_response)
    st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"] })

