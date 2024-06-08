import streamlit as st
# import ollama wrapper
import ollama

st.title("DIY Gen AI Chatbot")
# check messages variable in streamlit's session state
if "messages" not in st.session_state:
      # if no value set, (we're just starting out) then initialize with friendly message
      # role is either "user" or "assistant"
      st.session_state["messages"] = [ {"role":  "assistant",  "content":  "What can I help you with?"}]

# Write msg history
for msg in st.session_state.messages:
       st.chat_message(msg["role"]).write(msg["content"])

# Generator for streaming tokens
def generate_response():
        # call chat function in ollama, get response from the loaded model
        response = ollama.chat(model='phi3:mini', stream=True, messages=st.session_state.messages)
        for partial_resp in response:
               token = partial_resp["message"]["content"]
               # maintain history/context
               st.session_state["full_message"] += token
               yield token

if prompt := st.chat_input():
      # save the message for the user role
      st.session_state.messages.append({"role": "user", "content": prompt})
      st.chat_message("user").write(prompt)
      st.session_state["full_message"] = ""
      # call the generate_response function above
      st.chat_message("assistant").write_stream(generate_response)
      # save the message for the assistant role
      st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})
