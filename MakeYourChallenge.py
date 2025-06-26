import streamlit as st
from groq import Groq
import subprocess
import sys
import io
from streamlit_ace import st_ace

# Get API key from Streamlit Secrets
api_key = st.secrets["API_KEY"]

# Initialize Groq client with API key
if api_key:
    client = Groq(api_key=api_key)
else:
    st.error("API key is missing. Please check your Streamlit Secrets configuration.")
    st.stop()

# Define programming languages and their related topics
LANGUAGE_TOPICS = {
    "Python": [
        "Variables 📦",
        "Data Types ✍🏼",
        "Conditional Statement 🤔",
        "Functions 🧏🏼‍♀️",
        "Loop ♾️",
        "Logic Operator 🚫",
        "Logic Comparison ◀️ ▶️"
    ],
    "JavaScript": [
        "Variables and Hoisting",
        "Data Types",
        "Functions and Closures",
        "DOM Manipulation",
        "Asynchronous Programming"
    ],
    "Lua": [
        "Variables 📦",
        "Data Types ✍🏼",
        "Conditional Statement 🤔",
        "Functions 🧏🏼‍♀️",
        "Loop ♾️",
        "Logic Operator 🚫",
        "Logic Comparison ◀️ ▶️"
    ]
}

