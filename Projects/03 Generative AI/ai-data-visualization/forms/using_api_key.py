import streamlit as st

import openai

# Anywhere in your app where you need to send requests, retrieve the API Key from session state:

api_key = st.session_state.get("api_key", None)
model = st.session_state.get("model", "gpt-4")

if api_key:
    openai.api_key = api_key  # Set API key dynamically per user
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": "Hello!"}]
    )
    st.write(response["choices"][0]["message"]["content"])
else:
    st.error("Please enter your OpenAI API Key to proceed.")
