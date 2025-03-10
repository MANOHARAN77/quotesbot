import streamlit as st
import random

# List of motivational quotes
quotes = [
    "Believe in yourself and all that you are. - Christian D. Larson",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs",
    "The secret of getting ahead is getting started. - Mark Twain",
    "It always seems impossible until it’s done. - Nelson Mandela",
    "Act as if what you do makes a difference. It does. - William James",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Keep your face always toward the sunshine, and shadows will fall behind you. - Walt Whitman",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson"
]

# Streamlit Chatbot UI
st.title("💬 Motivational Chatbot")
st.write("Talk to me! Type your message below and I'll send you a motivational quote. ✨")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.write(msg)

# User input
user_input = st.text_input("You:", "")

if user_input:
    # Select a random motivational quote
    bot_reply = random.choice(quotes)
    
    # Store chat history
    st.session_state.messages.append(f"**You:** {user_input}")
    st.session_state.messages.append(f"**Bot:** {bot_reply}")
    
    # Display response
    st.write(f"**Bot:** {bot_reply}")
