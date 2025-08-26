import streamlit as st
import random

# List of quotes
quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Don’t let yesterday take up too much of today.",
    "It’s not whether you get knocked down, it’s whether you get up.",
    "If you are working on something exciting, it will keep you motivated.",
    "Success is not in what you have, but who you are.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don’t stop when you’re tired. Stop when you’re done.",
]

# Streamlit app UI
st.set_page_config(page_title="Random Quote Generator", page_icon="😁✨", layout="centered")

st.title("❤✨ Random Quote Generator")
st.write("Click the button to get a random motivational quote!")

if st.button("Get Quote"):
    quote = random.choice(quotes)
    st.success(f"🤣💡 {quote}")
