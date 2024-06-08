import streamlit as st
import ollama

st.title("title")
if "messages" not in st.session_state:
      st.session_state["messages"] = [ {"role":  "assistant",  "content":  "How can I help you?"}]

# Write msg history
for msg in st.session_state.messages:
       if msg["role"] == "user":
                 st.chat_message(msg["role"]).write(msg["content"])
       else: 
                 st.chat_message(msg["role"]).write(msg["content"])

# Generator for streaming tokens
def generate_response():
        response = ollama.chat(model='phi3:mini', stream=True, messages=st.session_state.messages)
        for partial_resp in response:
               token = partial_resp["message"]["content"]
               st.session_state["full_message"] += token
               yield token

if prompt := st.chat_input():
      st.session_state.messages.append({"role": "user", "content": prompt})
      st.chat_message("user").write(prompt)
      st.session_state["full_message"] = ""
      st.chat_message("assistant").write_stream(generate_response)
      st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})
