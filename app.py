#Import Libraries
import streamlit as st
from groq import Groq

#Connect to groq
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

#App title and sidebar
st.sidebar.title("📚 Intellicore")
st.sidebar.write("Your AI study assistant for engineering students.")
st.sidebar.write("Ask any coding or engineering doubt!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#User Input
i = st.chat_input("Ask anything...")

#Get AI response and store in history
if i:
    st.session_state.messages.append({"role": "user", "content": i})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a study assistant for engineering students. Explain concepts simply with examples. Be encouraging when students are confused."},
            {"role": "user", "content": i}
        ]
    )
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

# Display all messages
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])