import streamlit as st
import os
from groq import Groq
import subprocess
import sys
import io
from streamlit_ace import st_ace

# Get API key from secrets
api_key = st.secrets["API_KEY"]

# Debug mode (opsional)
debug_mode = st.secrets.get("DEBUG", "False")

# Initialize Groq client
if api_key:
    client = Groq(api_key=api_key)
else:
    st.error("API key is missing. Please check your secrets.toml file.")
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

# Function for generating question
def generate_questions(language, topics, count):
    topics_str = ", ".join(topics)
    prompt = f"""
    Generate exactly {count} coding problems based on the selected topics ({', '.join(topics_str)}) in {language}.
    Each problem must strictly relate to one of the selected topics and should be written in a pseudocode style.
    Distribute the problems across the selected topics, ensuring each topic is covered.

    Guidelines:
    1. For "Variables and Data Types", focus on defining variables, assigning values, and using different data types.
    Example:
    - Define a variable: variable_name = value
    - Assign a specific data type: variable_name = "string", variable_name = 123
    - Print or display the variable.

    2. For "Control Structures", focus on if-else statements and logical conditions.
    Example:
    - Write a condition: if condition print("message")
    - Use else statements to handle other conditions.

    3. For "Functions", focus on defining functions, passing arguments, and returning values.
    Example:
    - Define a function: def function_name(parameters):
    - Call the function with arguments.

    Ensure all problems are clear, concise, and directly relevant to the topics.
    Provide the problems in a numbered list format, one problem per line.
    """
    
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        top_p=0.95,
        stream=False,
        stop=None,
    )
    
    return completion.choices[0].message.content

# Streamlit UI
st.title("Programming Question Generator")

language = st.selectbox("Select Programming Language", options=list(LANGUAGE_TOPICS.keys()))
st.subheader(f"Select topics for {language}")

selected_topics = []
for topic in LANGUAGE_TOPICS[language]:
    if st.checkbox(topic):
        selected_topics.append(topic)

question_count = st.number_input("Number of Questions", min_value=1, max_value=10, value=3)

if st.button("Generate Questions"):
    if not selected_topics:
        st.error("Please select at least one topic.")
    else:
        with st.spinner("Generating questions..."):
            questions = generate_questions(language, selected_topics, question_count)
            st.text_area("Generated Questions", value=questions, height=200)

# Code editor with line numbering using streamlit-ace
st.subheader("Code Editor")
code = st_ace(
    language=language.lower(),  # Automatically set language based on selection
    theme="monokai",            # You can choose other themes like "github", "dracula", etc.
    value="",                   # Placeholder code
    key="ace-editor",           # Unique key for the editor
    height=600,                 # Set the height of the editor
    show_gutter=True,           # Show line numbers
    show_print_margin=False,    # Hide the print margin
    font_size=18
)

# Rest of the code remains the same...
