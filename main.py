import streamlit as st
import random
import time

# Set page config
st.set_page_config(page_title="Python Quiz Application", page_icon="💻", layout="centered")

# Custom CSS for gradient background
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #ff758c, #ff7eb3);
            color: white;
        }
        .stApp {
            background: linear-gradient(to right, #ff758c, #ff7eb3);
        }
        .stButton > button {
            background-color: #ff4b5c;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background-color: #ff1e42;
        }
        .stRadio > div {
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('💻 Python Quiz Application')

# List of Python-related questions
questions = [
    {"question": "What is the output of print(2 ** 3)?", "options": ["5", "6", "8", "9"], "answer": "8"},
    {"question": "Which keyword is used for function in Python?", "options": ["func", "define", "def", "function"], "answer": "def"},
    {"question": "Which of these data types is immutable?", "options": ["List", "Dictionary", "Tuple", "Set"], "answer": "Tuple"},
    {"question": "What does the len() function return?", "options": ["Length of an object", "Last element", "First element", "None"], "answer": "Length of an object"},
    {"question": "Which module is used for regular expressions in Python?", "options": ["regex", "re", "pyregex", "string"], "answer": "re"},
    {"question": "What is the correct syntax to open a file named 'data.txt' in read mode?", "options": ["open('data.txt', 'r')", "open('data.txt', 'w')", "open('data.txt', 'rw')", "open('data.txt', 'rb')"], "answer": "open('data.txt', 'r')"},
    {"question": "What is the output of print(type([]))?", "options": ["<class 'list'>", "<class 'dict'>", "<class 'tuple'>", "<class 'set'>"], "answer": "<class 'list'>"},
    {"question": "Which method is used to remove an item from a list?", "options": ["delete()", "remove()", "pop()", "discard()"], "answer": "remove()"},
    {"question": "What keyword is used to handle exceptions in Python?", "options": ["error", "catch", "try", "except"], "answer": "try"},
    {"question": "Which Python function is used to get user input?", "options": ["get()", "input()", "read()", "scan()"], "answer": "input()"},
    {"question": "How do you start a comment in Python?", "options": ["//", "#", "/*", "--"], "answer": "#"},
    {"question": "Which keyword is used to create a class in Python?", "options": ["class", "struct", "define", "object"], "answer": "class"},
    {"question": "What is the output of print(bool(0))?", "options": ["True", "False", "None", "Error"], "answer": "False"},
    {"question": "Which operator is used for exponentiation in Python?", "options": ["^", "**", "exp", "pow"], "answer": "**"},
    {"question": "Which of these is NOT a valid Python variable name?", "options": ["my_var", "123var", "_var", "var_1"], "answer": "123var"},
    {"question": "Which function is used to convert a string into an integer?", "options": ["int()", "str()", "float()", "ord()"], "answer": "int()"},
    {"question": "What does the range(5) function return?", "options": ["A list of numbers from 1 to 5", "A list of numbers from 0 to 5", "A list of numbers from 0 to 4", "An error"], "answer": "A list of numbers from 0 to 4"},
    {"question": "Which function is used to get the length of an object?", "options": ["len()", "length()", "size()", "count()"], "answer": "len()"},
    {"question": "What is the output of print(type(None))?", "options": ["<class 'NoneType'>", "<class 'null'>", "<class 'void'>", "<class 'object'>"], "answer": "<class 'NoneType'>"},
    {"question": "Which of these is a valid Python identifier?", "options": ["123abc", "abc123", "abc_123", "_abc123"], "answer": "abc_123"},
    {"question": "Which function is used to convert a string into a float?", "options": ["float()", "str()", "int()", "bool()"], "answer": "float()"},
    {"question": "What does the enumerate() function return?", "options": ["A list of tuples", "A list of numbers", "A list of strings", "An error"], "answer": "A list of tuples"},
    {"question": "Which of these is a valid Python function name?", "options": ["my_func", "123func", "_func", "func_123"], "answer": "my_func"},
    {"question": "Which function is used to get the maximum value in a list?", "options": ["max()", "min()", "sum()", "len()"], "answer": "max()"},
    {"question": "What is the output of print(type(5))?", "options": ["<int>", "<float>", "<str>", "<list>"], "answer": "<int>"},
    {"question": "Which of these is a valid Python variable name?", "options": ["my_var", "123var", "_var", "var_1"], "answer": "my_var"},
    {"question": "Which function is used to convert a string into a boolean?", "options": ["bool()", "str()", "int()", "float()"], "answer": "bool()"},
    {"question": "Which of these is a valid Python keyword?", "options": ["def", "class", "while", "for"], "answer": "def"},    
    {"question": "What does the zip() function return?", "options": ["A list of tuples", "A list of numbers", "A list of strings", "An error"], "answer": "A list of tuples"},
    {"question": "Which function is used to get the minimum value in a list?", "options": ["max()", "min()", "sum()", "len()"], "answer": "min()"},
    {"question": "Which of these is a valid Python keyword?", "options": ["def", "class", "while", "for"], "answer": "def"},
    {"question": "Which function is used to get the sum of all elements in a list?", "options": ["sum()", "max()", "min()", "len()"], "answer": "sum()"},
    {"question": "Which of these is a valid Python keyword?", "options": ["def", "class", "while", "for"], "answer": "def"},
    {"question": "Which function is used to get the product of all elements in a list?", "options": ["sum()", "max()", "min()", "len()"], "answer": "prod()"},
    {"question": "Which of these is a valid Python keyword?", "options": ["def", "class", "while", "for"], "answer": "def"}
    
]

# Initialize session state for current question
if 'current_question' not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Fetch the current question
current_question = st.session_state.current_question

# Display question
st.subheader(current_question['question'])

# Radio button for answer selection
selected_option = st.radio('‼ Choose Your Answer:', current_question['options'], key='Answer')

# Submit button
if st.button('Submit Your Answer'):
    if selected_option == current_question['answer']:
        st.success('✨ Correct Answer!')
    else:
        st.error(f'❌ Wrong Answer! The correct answer is: {current_question["answer"]}')
    
    time.sleep(2)  # Small delay before loading next question

    # Load a new random question
    st.session_state.current_question = random.choice(questions)
    st.rerun()
    
st.markdown('<h5 style="text-align: center; margin-top: 50px;">Built with ❤️ By Shan E Zehra</h5>', unsafe_allow_html=True)
