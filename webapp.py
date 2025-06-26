import streamlit as st
import subprocess
import sys
import io

st.title("Auto Generate challenge")
st.caption("This app is an app that will help you to create challenges automatically. Select the programming language you want and select the material you want. after that click the make a challenge button.")

option = st.selectbox(
    "Choose your programming language",
    ("Python", "Javascript", "LUA")
)
st.write("You selected:", option)

# option1 = st.selectbox(
#     "Choose your Materi",
#     ("Variable", "Data Types", "Conditional Statement")
# )

# checkbox
Varibale = st.checkbox("Variable 📦")
Datatypes= st.checkbox("Data Types ✍🏼")
Conditional_statement = st.checkbox("Conditional Statement 🤔")

# Make a challenge
st.button("Make a challenge", type="primary")

# Code editor
code = st.text_area("Write your code here:", height=300, placeholder="Write your Python code here...")

# Button to run the code
if st.button("Run Code"):
    # Only execute Python code
    if option == "Python":
        # Redirect stdout to capture print statements
        output = io.StringIO()
        sys.stdout = output

        try:
            # Execute the user's code
            exec(code)
            result = output.getvalue()  # Get the output
            st.success("Code executed successfully!")
            st.text_area("Output", value=result, height=200, disabled=True)
        except Exception as e:
            # Handle errors
            st.error("An error occurred!")
            st.text_area("Error", value=str(e), height=200, disabled=True)
        finally:
            # Reset stdout
            sys.stdout = sys.__stdout__
    else:
        st.error("Code execution is only supported for Python at this time.")
