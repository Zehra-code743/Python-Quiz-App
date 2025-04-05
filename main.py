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
    [
  {
    "question": "Who developed Python Programming Language?",
    "options": ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup"],
    "answer": "Guido van Rossum"
  },
  {
    "question": "Which of the following is the correct extension of Python file?",
    "options": [".python", ".pl", ".py", ".p"],
    "answer": ".py"
  },
  {
    "question": "What is the output of print(10 // 3)?",
    "options": ["3.33", "3", "4", "3.0"],
    "answer": "3"
  },
  {
    "question": "Which keyword is used for function in Python?",
    "options": ["func", "define", "function", "def"],
    "answer": "def"
  },
  {
    "question": "Which of the following is a valid variable name in Python?",
    "options": ["2var", "var-name", "_var", "var name"],
    "answer": "_var"
  }
  [
  {
    "question": "Which of the following is a numeric data type in Python?",
    "options": ["str", "bool", "int", "list"],
    "answer": "int"
  },
  {
    "question": "What is the data type of: x = 3.14?",
    "options": ["int", "float", "str", "complex"],
    "answer": "float"
  },
  {
    "question": "What is the output of type(True)?",
    "options": ["<class 'bool'>", "<class 'int'>", "<class 'str'>", "<class 'float'>"],
    "answer": "<class 'bool'>"
  },
  {
    "question": "Which data type is used to store a sequence of characters?",
    "options": ["int", "list", "str", "bool"],
    "answer": "str"
  },
  {
    "question": "Which one is a mutable data type in Python?",
    "options": ["tuple", "int", "str", "list"],
    "answer": "list"
  },
  {
    "question": "What is the data type of: x = (1, 2, 3)?",
    "options": ["list", "tuple", "set", "dict"],
    "answer": "tuple"
  },
  {
    "question": "What is the result of type({'a':1})?",
    "options": ["<class 'set'>", "<class 'dict'>", "<class 'list'>", "<class 'tuple'>"],
    "answer": "<class 'dict'>"
  },
  {
    "question": "Which of these is an immutable data type?",
    "options": ["list", "set", "tuple", "dict"],
    "answer": "tuple"
  },
  {
    "question": "Which type is used for unordered collection of unique items?",
    "options": ["list", "tuple", "set", "dict"],
    "answer": "set"
  },
  {
    "question": "Which function is used to check the data type of a variable?",
    "options": ["typeof()", "checktype()", "datatype()", "type()"],
    "answer": "type()"
  },
  {
    "question": "What is the output of type(10 + 5j)?",
    "options": ["<class 'float'>", "<class 'complex'>", "<class 'int'>", "<class 'str'>"],
    "answer": "<class 'complex'>"
  },
  {
    "question": "What will be the data type of: x = [1, 'two', 3.0]?",
    "options": ["list", "tuple", "set", "dict"],
    "answer": "list"
  },
  {
    "question": "Which one of these is a valid set declaration?",
    "options": ["{1, 2, 3}", "[1, 2, 3]", "(1, 2, 3)", "{'a':1}"],
    "answer": "{1, 2, 3}"
  },
  {
    "question": "What is the default data type of input() in Python?",
    "options": ["str", "int", "float", "bool"],
    "answer": "str"
  },
  {
    "question": "Which type allows key-value pair storage?",
    "options": ["list", "tuple", "set", "dict"],
    "answer": "dict"
  },
  {
    "question": "What is the output of: type([])?",
    "options": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"],
    "answer": "<class 'list'>"
  },
  {
    "question": "Which data type supports indexing and is mutable?",
    "options": ["tuple", "set", "list", "int"],
    "answer": "list"
  },
  {
    "question": "Which of the following can be used as a dictionary key?",
    "options": ["list", "set", "tuple", "dict"],
    "answer": "tuple"
  },
  {
    "question": "Which data type does not allow duplicate values?",
    "options": ["list", "tuple", "set", "str"],
    "answer": "set"
  },
  {
    "question": "Which of these data types is not built-in in Python?",
    "options": ["array", "set", "str", "int"],
    "answer": "array"
  },
  {
    "question": "What is the output of: type((1))?",
    "options": ["<class 'tuple'>", "<class 'int'>", "<class 'list'>", "<class 'str'>"],
    "answer": "<class 'int'>"
  },
  {
    "question": "How can you declare an empty set in Python?",
    "options": ["{}", "[]", "set()", "set[]"],
    "answer": "set()"
  },
  {
    "question": "What will be the output of: isinstance(True, int)?",
    "options": ["True", "False", "TypeError", "None"],
    "answer": "True"
  },
  {
    "question": "Which method is used to convert a list to a tuple?",
    "options": ["list()", "set()", "tuple()", "dict()"],
    "answer": "tuple()"
  },
  {
    "question": "Which data type is unordered and unindexed?",
    "options": ["list", "tuple", "set", "str"],
    "answer": "set"
  },
  {
    "question": "Which operation will throw an error: {1, 2, 3}[0]?",
    "options": ["Yes, set is not subscriptable", "No error", "It will return 1", "Returns random item"],
    "answer": "Yes, set is not subscriptable"
  },
  {
    "question": "Which of the following is a frozen set in Python?",
    "options": ["frozen()", "frozenset()", "setfreeze()", "freezeset()"],
    "answer": "frozenset()"
  },
  {
    "question": "What is the output of: type([1, 2] + (3, 4))?",
    "options": ["<class 'list'>", "Error", "<class 'tuple'>", "<class 'set'>"],
    "answer": "Error"
  },
  {
    "question": "Which of the following will create a dictionary with 3 key-value pairs?",
    "options": ["{1,2,3}", "{'a':1, 'b':2, 'c':3}", "[1,2,3]", "('a', 'b', 'c')"],
    "answer": "{'a':1, 'b':2, 'c':3}"
  },
  {
    "question": "Which method converts a string to a list of characters?",
    "options": ["split()", "list()", "str()", "chars()"],
    "answer": "list()"
  },
  {
    "question": "What is the output of len({'a': 1, 'b': 2, 'c': 3})?",
    "options": ["3", "6", "1", "0"],
    "answer": "3"
  },
  {
    "question": "What will be the output of: {1, 2, 2, 3}?",
    "options": ["{1, 2, 3}", "{1, 2, 2, 3}", "[1, 2, 3]", "(1, 2, 3)"],
    "answer": "{1, 2, 3}"
  },
  {
    "question": "Which of the following is NOT allowed as a dictionary key?",
    "options": ["int", "str", "tuple", "list"],
    "answer": "list"
  },
  {
    "question": "Which statement is true about strings in Python?",
    "options": ["They are mutable", "They can be changed by index", "They are immutable", "They are of type list"],
    "answer": "They are immutable"
  },
  {
    "question": "Which function returns the memory location (identity) of an object?",
    "options": ["type()", "id()", "loc()", "ref()"],
    "answer": "id()"
  },
  {
    "question": "What is the output of type(range(5))?",
    "options": ["<class 'list'>", "<class 'range'>", "<class 'tuple'>", "<class 'generator'>"],
    "answer": "<class 'range'>"
  },
  {
    "question": "Which of the following creates an immutable set?",
    "options": ["set()", "frozen()", "frozenset()", "tuple(set())"],
    "answer": "frozenset()"
  },
  {
    "question": "Which of the following types is not iterable?",
    "options": ["str", "int", "tuple", "dict"],
    "answer": "int"
  },
  {
    "question": "What is the output of: len(set('hello'))?",
    "options": ["5", "4", "3", "2"],
    "answer": "4"
  },
  {
    "question": "What is the result of: type({})?",
    "options": ["<class 'set'>", "<class 'dict'>", "<class 'list'>", "<class 'NoneType'>"],
    "answer": "<class 'dict'>"
  },
  {
    "question": "What is the output of: 2 ** 3 ** 2?",
    "options": ["64", "512", "36", "8"],
    "answer": "512"
  },
  {
    "question": "Which operator has the highest precedence in Python?",
    "options": ["**", "*", "+", "//"],
    "answer": "**"
  },
  {
    "question": "What is the output of: not (True and False)?",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "What is the result of: 3 > 2 > 1?",
    "options": ["True", "False", "Error", "None"],
    "answer": "True"
  },
  {
    "question": "Which operator is right-associative in Python?",
    "options": ["**", "+", "-", "*"],
    "answer": "**"
  },
  {
    "question": "What will be the output of: 4 & 5?",
    "options": ["4", "5", "0", "1"],
    "answer": "4"
  },
  {
    "question": "What is the result of: 4 | 5?",
    "options": ["4", "5", "1", "None"],
    "answer": "5"
  },
  {
    "question": "Which is the result of ~4 in Python?",
    "options": ["-5", "3", "-4", "5"],
    "answer": "-5"
  },
  {
    "question": "Which of the following is a bitwise operator?",
    "options": ["and", "or", "&", "not"],
    "answer": "&"
  },
  {
    "question": "What is the output of: 1 << 2?",
    "options": ["2", "4", "8", "1"],
    "answer": "4"
  },
  {
    "question": "What is the output of: 8 >> 2?",
    "options": ["2", "4", "1", "0"],
    "answer": "2"
  },
  {
    "question": "What will be the result of: 0 and 5?",
    "options": ["0", "5", "True", "False"],
    "answer": "0"
  },
  {
    "question": "What is the result of: 1 or 0?",
    "options": ["0", "1", "True", "False"],
    "answer": "1"
  },
  {
    "question": "Which operator is used for identity comparison?",
    "options": ["==", "!=", "is", "in"],
    "answer": "is"
  },
  {
    "question": "What is the output of: [] is []?",
    "options": ["True", "False", "None", "Error"],
    "answer": "False"
  },
  {
    "question": "Which of these is used to test membership in a sequence?",
    "options": ["is", "==", "in", "has"],
    "answer": "in"
  },
  {
    "question": "What is the result of: 'a' in 'apple'?",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "What is the result of: not 0?",
    "options": ["True", "False", "0", "1"],
    "answer": "True"
  },
  {
    "question": "What is the precedence of 'not' compared to 'and'?",
    "options": ["Higher", "Lower", "Same", "Undefined"],
    "answer": "Higher"
  },
  {
    "question": "Which expression short-circuits: False and print('Hello')?",
    "options": ["Yes", "No", "Error", "None"],
    "answer": "Yes"
  },
  {
    "question": "What is the result of: True + True?",
    "options": ["1", "2", "True", "Error"],
    "answer": "2"
  },
  {
    "question": "Which operator can be used to swap values without a temp variable?",
    "options": ["^", "=", "//", "+"],
    "answer": "^"
  },
  {
    "question": "Which operator would you use for floor division?",
    "options": ["/", "//", "%", "**"],
    "answer": "//"
  },
  {
    "question": "Which of these evaluates to True: (not 0 and 1)?",
    "options": ["True", "False", "Error", "None"],
    "answer": "True"
  },
  {
    "question": "What is the result of: (1 + 2) * 3?",
    "options": ["9", "7", "6", "8"],
    "answer": "9"
  },
  {
    "question": "What does 'is not' check for?",
    "options": ["Value inequality", "Reference inequality", "Bitwise check", "Assignment"],
    "answer": "Reference inequality"
  },
  {
    "question": "What is the output of: True and False or True?",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "What is the output of: 3 * 0.1 == 0.3?",
    "options": ["True", "False", "Error", "None"],
    "answer": "False"
  },
  {
    "question": "What is the result of: 10 > 9 > 8?",
    "options": ["True", "False", "Error", "None"],
    "answer": "True"
  },
  {
    "question": "Which operator does NOT support chaining?",
    "options": ["==", "<", "+", "is"],
    "answer": "+"
  },
  {
    "question": "What is the result of: not True == False?",
    "options": ["True", "False", "Error", "None"],
    "answer": "True"
  },
  {
    "question": "Which operator can work with both numbers and strings?",
    "options": ["+", "*", "-", "%"],
    "answer": "+"
  },
  {
    "question": "What is the result of: '5' + '6'?",
    "options": ["11", "'11'", "'56'", "Error"],
    "answer": "'56'"
  },
  {
    "question": "Which operator is overloaded by the __add__() method?",
    "options": ["+", "*", "-", "**"],
    "answer": "+"
  },
  {
    "question": "What is the result of: True * 5?",
    "options": ["5", "0", "True", "False"],
    "answer": "5"
  },
  {
    "question": "What is the output of: 3 and 4?",
    "options": ["True", "3", "4", "False"],
    "answer": "4"
  },
  {
    "question": "What is the output of: 0 or []?",
    "options": ["[]", "0", "False", "None"],
    "answer": "[]"
  },
  {
    "question": "Which operator is used to unpack iterable objects?",
    "options": ["*", "**", "&", "@"],
    "answer": "*"
  },
  {
    "question": "Which operator can unpack dictionaries in function arguments?",
    "options": ["*", "**", "&", "#"],
    "answer": "**"
  },
  {
    "question": "What is the output of: not not True?",
    "options": ["True", "False", "Error", "None"],
    "answer": "True"
  },
  {
    "question": "Which of the following will evaluate to False?",
    "options": ["None", "[]", "0", "All of these"],
    "answer": "All of these"
  },
  {
    "question": "What is the result of: bool(1 and 0)?",
    "options": ["True", "False", "Error", "None"],
    "answer": "False"
  },
  {
    "question": "Which of the following expressions is valid?",
    "options": ["10 = a", "a += 1", "if a = 10", "5 ++"],
    "answer": "a += 1"
  },
  {
    "question": "What will be the output: 'a' * 3?",
    "options": ["aaa", "a3", "Error", "None"],
    "answer": "aaa"
  },
  {
    "question": "Which operator is overloaded by __eq__()?",
    "options": ["==", "=", "!=", "is"],
    "answer": "=="
  },
  {
    "question": "What will be the result of: 'a' in ['a', 'b']?",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "What does the '//' operator return?",
    "options": ["Float division", "Integer division", "Exponentiation", "Modulo"],
    "answer": "Integer division"
  },
  {
    "question": "Which operator has the lowest precedence?",
    "options": ["or", "and", "not", "+"],
    "answer": "or"
  },
  
  {
    "question": "Which keyword is used to define a function in Python?",
    "options": ["func", "define", "def", "function"],
    "answer": "def"
  },
  {
    "question": "Which keyword is used to handle exceptions?",
    "options": ["except", "error", "catch", "handle"],
    "answer": "except"
  },
  {
    "question": "Which keyword is used to import modules?",
    "options": ["require", "include", "import", "module"],
    "answer": "import"
  },
  {
    "question": "What is the keyword used to create a class?",
    "options": ["function", "define", "class", "object"],
    "answer": "class"
  },
  {
    "question": "Which keyword is used to begin a conditional block?",
    "options": ["for", "if", "else", "elif"],
    "answer": "if"
  },
  {
    "question": "Which keyword is used to exit a loop prematurely?",
    "options": ["stop", "exit", "break", "end"],
    "answer": "break"
  },
  {
    "question": "Which keyword is used to skip an iteration?",
    "options": ["skip", "pass", "continue", "break"],
    "answer": "continue"
  },
  {
    "question": "Which keyword is used to define an anonymous block?",
    "options": ["pass", "empty", "blank", "none"],
    "answer": "pass"
  },
  {
    "question": "Which keyword is used to define a generator function?",
    "options": ["return", "yield", "gen", "async"],
    "answer": "yield"
  },
  {
    "question": "Which keyword defines an asynchronous function?",
    "options": ["await", "async", "thread", "future"],
    "answer": "async"
  },
  {
    "question": "What does the 'global' keyword do?",
    "options": ["Creates a new variable", "Declares a constant", "Accesses a global variable", "Defines a class"],
    "answer": "Accesses a global variable"
  },
  {
    "question": "What is the purpose of the 'nonlocal' keyword?",
    "options": ["Defines a static variable", "Accesses a global var", "Accesses a variable from the outer function", "Declares an external module"],
    "answer": "Accesses a variable from the outer function"
  },
  {
    "question": "Which keyword is used in exception handling along with 'except'?",
    "options": ["else", "catch", "try", "raise"],
    "answer": "try"
  },
  {
    "question": "Which keyword is used to manually throw an exception?",
    "options": ["throw", "raise", "except", "error"],
    "answer": "raise"
  },
  {
    "question": "Which keyword is used to declare the end of a loop or exception block?",
    "options": ["finally", "end", "exit", "terminate"],
    "answer": "finally"
  },
  {
    "question": "What is the keyword for defining a constant value in Python?",
    "options": ["const", "final", "val", "None of these"],
    "answer": "None of these"
  },
  {
    "question": "Which keyword is used to create a lambda function?",
    "options": ["lambda", "function", "def", "fn"],
    "answer": "lambda"
  },
  {
    "question": "Which keyword is used to test object identity?",
    "options": ["==", "equals", "is", "in"],
    "answer": "is"
  },
  {
    "question": "Which keyword is used to check membership?",
    "options": ["with", "in", "has", "includes"],
    "answer": "in"
  },
  {
    "question": "Which keyword is used to define a context manager?",
    "options": ["context", "open", "with", "using"],
    "answer": "with"
  },
  {
    "question": "Which of the following is a keyword?",
    "options": ["map", "filter", "assert", "range"],
    "answer": "assert"
  },
  {
    "question": "Which keyword is used in a ternary conditional expression?",
    "options": ["then", "if", "elif", "when"],
    "answer": "if"
  },
  {
    "question": "Which keyword is used to define an else-if condition?",
    "options": ["elseif", "elif", "else if", "elthen"],
    "answer": "elif"
  },
  {
    "question": "Which of the following is not a Python keyword?",
    "options": ["assert", "def", "var", "pass"],
    "answer": "var"
  },
  {
    "question": "What is the result of using 'del' on a list element?",
    "options": ["Removes the item", "Deletes the entire list", "Raises error", "Ignores the operation"],
    "answer": "Removes the item"
  },
  {
    "question": "Which keyword is used to declare a variable as immutable?",
    "options": ["immutable", "const", "None of these", "static"],
    "answer": "None of these"
  },
  {
    "question": "Which keyword is used to check if two variables point to the same object?",
    "options": ["==", "equals", "is", "in"],
    "answer": "is"
  },
  {
    "question": "Which keyword is used to indicate a block that will always run after try-except?",
    "options": ["finally", "last", "end", "close"],
    "answer": "finally"
  },
  {
    "question": "Which Python keyword is used for documentation?",
    "options": ["comment", "doc", "None", "There is no keyword for that"],
    "answer": "There is no keyword for that"
  },
  {
    "question": "Which keyword is used to initialize a for loop?",
    "options": ["loop", "do", "for", "while"],
    "answer": "for"
  },
  {
    "question": "Which keyword is used to create infinite loops (with condition)?",
    "options": ["repeat", "while", "loop", "forever"],
    "answer": "while"
  },
  {
    "question": "Which of the following is a logical operator keyword?",
    "options": ["and", "not", "or", "All of these"],
    "answer": "All of these"
  },
  {
    "question": "What does 'None' represent in Python?",
    "options": ["Empty string", "Zero", "No value", "False"],
    "answer": "No value"
  },
  {
    "question": "What does the 'assert' keyword do?",
    "options": ["Defines a constant", "Raises an exception if condition is false", "Declares a class", "Creates a loop"],
    "answer": "Raises an exception if condition is false"
  },
  {
    "question": "What does 'await' do in an async function?",
    "options": ["Blocks until async task finishes", "Creates new thread", "Returns immediately", "Stops execution forever"],
    "answer": "Blocks until async task finishes"
  },
  {
    "question": "Which keyword is used to define an enumeration?",
    "options": ["enum", "class", "define", "Python doesn't support enums via keywords"],
    "answer": "Python doesn't support enums via keywords"
  },
  {
    "question": "What happens if you use 'return' outside a function?",
    "options": ["Returns nothing", "Raises SyntaxError", "Ends script", "Prints return value"],
    "answer": "Raises SyntaxError"
  },
  {
    "question": "Which of these keywords is used for function decorators?",
    "options": ["@", "decorator", "def", "lambda"],
    "answer": "@"
  },
  {
    "question": "What is the scope of a variable declared as global?",
    "options": ["Only inside function", "Only inside loop", "Throughout the module", "Inside class only"],
    "answer": "Throughout the module"
  },
  {
    "question": "Which keyword is used to refer to the current object?",
    "options": ["this", "self", "me", "obj"],
    "answer": "self"
  },
  {
    "question": "Which of these is a valid keyword in Python 3?",
    "options": ["exec", "print", "nonlocal", "long"],
    "answer": "nonlocal"
  },
  {
    "question": "Which keyword is used to define a block of code but do nothing?",
    "options": ["ignore", "null", "pass", "continue"],
    "answer": "pass"
  },
  {
    "question": "How many total keywords does Python have (Python 3.10)?",
    "options": ["33", "35", "36", "Reserved - depends on version"],
    "answer": "Reserved - depends on version"
  },
  {
    "question": "Which keyword is used for literal truth value?",
    "options": ["Yes", "True", "1", "On"],
    "answer": "True"
  },
  {
    "question": "Which keyword is used to test for equality of two objects?",
    "options": ["is", "==", "equals", "match"],
    "answer": "=="
  },
  {
    "question": "Which keyword can be used to free memory by removing a variable?",
    "options": ["remove", "free", "del", "None"],
    "answer": "del"
  },
  {
    "question": "What will 'not True or False' evaluate to?",
    "options": ["True", "False", "Error", "None"],
    "answer": "False"
  },
  {
    "question": "Which keyword allows defining a scope for working with a file?",
    "options": ["file", "with", "open", "as"],
    "answer": "with"
  },
  
  {
    "question": "Which of the following is a valid variable name in Python?",
    "options": ["2var", "var_name", "var-name", "var name"],
    "answer": "var_name"
  },
  {
    "question": "Which keyword is used to declare a variable in Python?",
    "options": ["var", "int", "let", "None of these"],
    "answer": "None of these"
  },
  {
    "question": "What will be the output of: x = 5; print(x)?",
    "options": ["x", "5", "None", "Error"],
    "answer": "5"
  },
  {
    "question": "Which of the following is not allowed in variable names?",
    "options": ["_", "digits", "-", "letters"],
    "answer": "-"
  },
  {
    "question": "Which of the following is a valid Python variable name?",
    "options": ["my variable", "my_variable", "my-variable", "123var"],
    "answer": "my_variable"
  },
  {
    "question": "What will happen if you print an undefined variable?",
    "options": ["Prints null", "Returns 0", "Syntax Error", "NameError"],
    "answer": "NameError"
  },
  {
    "question": "Which function is used to check the type of a variable?",
    "options": ["typeof()", "type()", "checktype()", "gettype()"],
    "answer": "type()"
  },
  {
    "question": "What is the output of: a = b = c = 10; print(b)?",
    "options": ["10", "b", "c", "None"],
    "answer": "10"
  },
  {
    "question": "Which of the following variable names is invalid?",
    "options": ["my_var", "_var", "9var", "var9"],
    "answer": "9var"
  },
  {
    "question": "Python variables are:",
    "options": ["Case-insensitive", "Case-sensitive", "Only lowercase", "Static"],
    "answer": "Case-sensitive"
  },
  {
    "question": "Which assignment is correct in Python?",
    "options": ["x := 5", "x = 5", "x == 5", "let x = 5"],
    "answer": "x = 5"
  },
  {
    "question": "What will be the output: a = '5'; print(type(a))?",
    "options": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'bool'>"],
    "answer": "<class 'str'>"
  },
  {
    "question": "What type of variable is created: x = 10.5?",
    "options": ["int", "float", "str", "bool"],
    "answer": "float"
  },
  {
    "question": "Which symbol is not allowed in variable names?",
    "options": ["_", "$", "letters", "digits"],
    "answer": "$"
  },
  {
    "question": "What will happen: x = 5; del x; print(x)?",
    "options": ["Prints 5", "Error", "Prints None", "Deletes x"],
    "answer": "Error"
  },
  {
    "question": "Which statement creates a new variable 'age' with value 20?",
    "options": ["let age = 20", "age: 20", "age = 20", "int age = 20"],
    "answer": "age = 20"
  },
  {
    "question": "Which of the following is a dynamic variable assignment?",
    "options": ["x = 5", "int x = 5", "x := 5", "x -> 5"],
    "answer": "x = 5"
  },
  {
    "question": "What will be the value of `z`? x=2; y=3; z=x+y",
    "options": ["5", "6", "23", "Error"],
    "answer": "5"
  },
  {
    "question": "Can a variable name start with an underscore?",
    "options": ["Yes", "No", "Only in classes", "Only with numbers"],
    "answer": "Yes"
  },
  {
    "question": "What is the result of: name = 'Ali'; print(Name)?",
    "options": ["Ali", "name", "NameError", "None"],
    "answer": "NameError"
  },
  {
    "question": "Which of the following assigns multiple variables in one line?",
    "options": ["a = 1; b = 2", "a, b = 1, 2", "a = b = 1", "All of these"],
    "answer": "All of these"
  },
  {
    "question": "Which keyword declares a variable with global scope?",
    "options": ["global", "Global", "GLOBAL", "var"],
    "answer": "global"
  },
  {
    "question": "Which function can delete a variable?",
    "options": ["del()", "remove()", "delete()", "del"],
    "answer": "del"
  },
  {
    "question": "What is the output: a = 10; b = '10'; print(a == b)?",
    "options": ["True", "False", "Error", "None"],
    "answer": "False"
  },
  {
    "question": "What is a variable?",
    "options": ["A memory container", "A function", "A loop", "A constant"],
    "answer": "A memory container"
  },
  {
    "question": "Which of these are valid variable assignments?",
    "options": ["_x = 1", "x1 = 2", "X = 3", "All of these"],
    "answer": "All of these"
  },
  {
    "question": "Can a variable name contain spaces?",
    "options": ["Yes", "No", "Only with underscore", "Only with quotes"],
    "answer": "No"
  },
  {
    "question": "What is the output: a = 2; a += 3; print(a)?",
    "options": ["2", "3", "5", "6"],
    "answer": "5"
  },
  {
    "question": "What does 'id(x)' return?",
    "options": ["Value of x", "Memory address", "Type of x", "Name of x"],
    "answer": "Memory address"
  },
  {
    "question": "Which of the following is not a valid assignment?",
    "options": ["a, b = 1, 2", "a = b = 3", "a == 4", "a = 5"],
    "answer": "a == 4"
  },
  {
    "question": "What is the output: a = 10; b = a; print(b)?",
    "options": ["10", "a", "b", "None"],
    "answer": "10"
  },
  {
    "question": "Python variables are:",
    "options": ["Statically typed", "Dynamically typed", "Type-less", "Weakly typed"],
    "answer": "Dynamically typed"
  },
  {
    "question": "Which keyword is used to access an outer scope variable?",
    "options": ["global", "nonlocal", "outer", "extern"],
    "answer": "nonlocal"
  },
  {
    "question": "Can a variable be reassigned to a different data type?",
    "options": ["Yes", "No", "Only in functions", "Only if mutable"],
    "answer": "Yes"
  },
  {
    "question": "Which of the following is true for variable naming?",
    "options": ["Can't start with digit", "Can include _", "Case-sensitive", "All of these"],
    "answer": "All of these"
  },
  {
    "question": "What is the output of: a = '5'; b = 5; print(a + str(b))?",
    "options": ["10", "55", "5", "Error"],
    "answer": "55"
  },
  {
    "question": "Can a variable name contain uppercase letters?",
    "options": ["Yes", "No", "Only constants", "Only class names"],
    "answer": "Yes"
  },
  {
    "question": "Which of these would raise an error?",
    "options": ["x = 'Hello'", "x = 123", "123x = 1", "_x = 1"],
    "answer": "123x = 1"
  },
  {
    "question": "What is the output: x = None; print(type(x))?",
    "options": ["<class 'NoneType'>", "<class 'null'>", "<class 'str'>", "<class 'bool'>"],
    "answer": "<class 'NoneType'>"
  },
  {
    "question": "Can Python variables hold multiple data types in one assignment?",
    "options": ["Yes, using tuple/list", "No", "Only integers", "Only strings"],
    "answer": "Yes, using tuple/list"
  },
  {
    "question": "Which symbol is used for assignment?",
    "options": ["==", ":=", "=", "->"],
    "answer": "="
  },
  {
    "question": "What is the output: a = 10; b = '10'; print(a is b)?",
    "options": ["True", "False", "Error", "10"],
    "answer": "False"
  },
  {
    "question": "Can variables be created at runtime?",
    "options": ["Yes", "No", "Only constants", "Only in functions"],
    "answer": "Yes"
  },
  {
    "question": "What is the default value of an uninitialized variable?",
    "options": ["None", "0", "Error", "Depends on data type"],
    "answer": "Error"
  },
  {
    "question": "Can two variables point to the same value?",
    "options": ["Yes", "No", "Only in lists", "Only in dict"],
    "answer": "Yes"
  },
  {
    "question": "How to declare a constant in Python?",
    "options": ["const x = 10", "final x = 10", "x = 10 (by convention, use uppercase)", "constant x = 10"],
    "answer": "x = 10 (by convention, use uppercase)"
  },
  {
    "question": "What is the convention for naming constants?",
    "options": ["camelCase", "snake_case", "UPPERCASE", "lowercase"],
    "answer": "UPPERCASE"
  },
  {
    "question": "Which built-in function returns all variable names in current scope?",
    "options": ["vars()", "globals()", "locals()", "All of these"],
    "answer": "All of these"
  },
  
  {
    "question": "What is the output of 'python'.upper()?",
    "options": ["PYTHON", "Python", "python", "None"],
    "answer": "PYTHON"
  },
  {
    "question": "'HELLO'.lower() returns:",
    "options": ["hello", "HELLO", "Hello", "None"],
    "answer": "hello"
  },
  {
    "question": "'hello world'.title() returns:",
    "options": ["Hello World", "HELLO WORLD", "hello world", "Hello world"],
    "answer": "Hello World"
  },
  {
    "question": "'Python'.startswith('P') returns:",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "'Python'.endswith('n') returns:",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "'abc123'.isalnum() returns:",
    "options": ["True", "False", "Error", "None"],
    "answer": "True"
  },
  {
    "question": "'123'.isdigit() returns:",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "'abc'.isalpha() returns:",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "'  space  '.strip() returns:",
    "options": ["space", "  space  ", "space  ", "  space"],
    "answer": "space"
  },
  {
    "question": "'Test'.find('e') returns:",
    "options": ["1", "2", "0", "-1"],
    "answer": "1"
  },
  {
    "question": "'Test'.index('e') returns:",
    "options": ["1", "2", "0", "-1"],
    "answer": "1"
  },
  {
    "question": "'Test'.replace('e', 'a') returns:",
    "options": ["Tast", "Test", "Tastt", "TastTest"],
    "answer": "Tast"
  },
  {
    "question": "'hello'.capitalize() returns:",
    "options": ["Hello", "HELLO", "hello", "HeLLo"],
    "answer": "Hello"
  },
  {
    "question": "'   hello   '.lstrip() returns:",
    "options": ["hello   ", "   hello", "hello", "   hello   "],
    "answer": "hello   "
  },
  {
    "question": "'   hello   '.rstrip() returns:",
    "options": ["   hello", "hello", "hello   ", "   hello   "],
    "answer": "   hello"
  },
  {
    "question": "'Hello'.swapcase() returns:",
    "options": ["hELLO", "HELLO", "hello", "Hello"],
    "answer": "hELLO"
  },
  {
    "question": "'hello'.isnumeric() returns:",
    "options": ["False", "True", "Error", "None"],
    "answer": "False"
  },
  {
    "question": "'Python Programming'.count('P') returns:",
    "options": ["2", "1", "0", "3"],
    "answer": "2"
  },
  {
    "question": "'Hello,World'.split(',') returns:",
    "options": [["Hello", "World"], "Hello World", "Hello,World", "['Hello World']"],
    "answer": ["Hello", "World"]
  },
  {
    "question": "What is the output of '-'.join(['a','b','c'])?",
    "options": ["a-b-c", "abc", "a b c", "a,b,c"],
    "answer": "a-b-c"
  },
  {
    "question": "'123abc'.isdecimal() returns:",
    "options": ["False", "True", "None", "Error"],
    "answer": "False"
  },
  {
    "question": "'hello'.zfill(8) returns:",
    "options": ["000hello", "hello000", "hello", "0000hello"],
    "answer": "000hello"
  },
  {
    "question": "'PYTHON'.islower() returns:",
    "options": ["False", "True", "None", "Error"],
    "answer": "False"
  },
  {
    "question": "'python'.isupper() returns:",
    "options": ["False", "True", "None", "Error"],
    "answer": "False"
  },
  {
    "question": "'Python'.center(10, '*') returns:",
    "options": ["**Python**", "***Python*", "*Python***", "**Python***"],
    "answer": "**Python**"
  },
  {
    "question": "'\\tPython'.expandtabs(4) returns:",
    "options": ["    Python", "Python", "\\tPython", "  Python"],
    "answer": "    Python"
  },
  {
    "question": "'python'.startswith('py') returns:",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "'python'.endswith('on') returns:",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "'@python@'.strip('@') returns:",
    "options": ["python", "@python", "python@", "@python@"],
    "answer": "python"
  },
  {
    "question": "'Python'.ljust(10, '*') returns:",
    "options": ["Python****", "****Python", "**Python**", "Python"],
    "answer": "Python****"
  },
  {
    "question": "'Python'.rjust(10, '-') returns:",
    "options": ["----Python", "Python----", "Python", "--Python--"],
    "answer": "----Python"
  },
  {
    "question": "'apple'.replace('p','b',1) returns:",
    "options": ["abple", "abble", "apple", "abbb"],
    "answer": "abple"
  },
  {
    "question": "'banana'.find('a', 2) returns:",
    "options": ["3", "1", "5", "2"],
    "answer": "3"
  },
  {
    "question": "'banana'.rfind('a') returns:",
    "options": ["5", "1", "3", "0"],
    "answer": "5"
  },
  {
    "question": "'banana'.rindex('a') returns:",
    "options": ["5", "3", "1", "0"],
    "answer": "5"
  },
  {
    "question": "'python123'.isalnum() returns:",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "'123'.isidentifier() returns:",
    "options": ["False", "True", "None", "Error"],
    "answer": "False"
  },
  {
    "question": "'myVar'.isidentifier() returns:",
    "options": ["True", "False", "Error", "None"],
    "answer": "True"
  },
  {
    "question": "'a b c'.split() returns:",
    "options": [["a", "b", "c"], "a b c", "['a b c']", "['abc']"],
    "answer": ["a", "b", "c"]
  },
  {
    "question": "'-'.join('abc') returns:",
    "options": ["a-b-c", "abc", "['a','b','c']", "a b c"],
    "answer": "a-b-c"
  },
  {
    "question": "What is the output of: len('Python')?",
    "options": ["6", "7", "5", "Error"],
    "answer": "6"
  },
  {
    "question": "'Python'.casefold() returns:",
    "options": ["python", "PYTHON", "Python", "pYTHON"],
    "answer": "python"
  },
  {
    "question": "What is returned by: '42'.isnumeric()?",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "Which method checks if all characters are whitespace?",
    "options": ["isspace()", "isblank()", "isnull()", "checkspace()"],
    "answer": "isspace()"
  },
  {
    "question": "What is 'hello world'.count('l')?",
    "options": ["3", "2", "1", "4"],
    "answer": "3"
  },
  {
    "question": "What does 'py123'.isalpha() return?",
    "options": ["False", "True", "None", "Error"],
    "answer": "False"
  },
  {
    "question": "What is the result of 'HELLO'.isupper()?",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "'abcDEF'.islower() returns:",
    "options": ["False", "True", "None", "Error"],
    "answer": "False"
  },
  {
    "question": "Which string method returns True if all characters are digits?",
    "options": ["isdigit()", "isnumber()", "isalnum()", "isnumeric()"],
    "answer": "isdigit()"
  },
  
  {
    "question": "What is the result of int(3.9)?",
    "options": ["3", "4", "3.9", "Error"],
    "answer": "3"
  },
  {
    "question": "float('10') returns:",
    "options": ["10.0", "10", "'10'", "Error"],
    "answer": "10.0"
  },
  {
    "question": "str(123) returns:",
    "options": ["'123'", "123", "int", "None"],
    "answer": "'123'"
  },
  {
    "question": "int('abc') results in:",
    "options": ["Error", "0", "None", "'abc'"],
    "answer": "Error"
  },
  {
    "question": "bool(0) returns:",
    "options": ["False", "True", "0", "None"],
    "answer": "False"
  },
  {
    "question": "bool(10) returns:",
    "options": ["True", "False", "10", "None"],
    "answer": "True"
  },
  {
    "question": "What is type(float(5))?",
    "options": ["<class 'float'>", "<class 'int'>", "<class 'str'>", "<class 'bool'>"],
    "answer": "<class 'float'>"
  },
  {
    "question": "What is the result of int(True)?",
    "options": ["1", "0", "True", "Error"],
    "answer": "1"
  },
  {
    "question": "What is the result of float(False)?",
    "options": ["0.0", "1.0", "False", "Error"],
    "answer": "0.0"
  },
  {
    "question": "str(None) returns:",
    "options": ["'None'", "None", "Error", "''"],
    "answer": "'None'"
  },
  {
    "question": "What does list('abc') return?",
    "options": [["a", "b", "c"], "['abc']", "'abc'", "Error"],
    "answer": ["a", "b", "c"]
  },
  {
    "question": "tuple([1,2,3]) returns:",
    "options": ["(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "Error"],
    "answer": "(1, 2, 3)"
  },
  {
    "question": "set('aaab') returns:",
    "options": ["{'a', 'b'}", "{'a', 'a', 'b'}", "['a', 'b']", "Error"],
    "answer": "{'a', 'b'}"
  },
  {
    "question": "int('10.5') gives:",
    "options": ["Error", "10", "10.5", "None"],
    "answer": "Error"
  },
  {
    "question": "float('NaN') returns:",
    "options": ["nan", "None", "Error", "0"],
    "answer": "nan"
  },
  {
    "question": "bool('False') returns:",
    "options": ["True", "False", "Error", "None"],
    "answer": "True"
  },
  {
    "question": "Which of these conversions is invalid?",
    "options": ["int('abc')", "int('123')", "str(123)", "float(10)"],
    "answer": "int('abc')"
  },
  {
    "question": "bool('') returns:",
    "options": ["False", "True", "Error", "None"],
    "answer": "False"
  },
  {
    "question": "int('0b101', 2) returns:",
    "options": ["5", "2", "101", "Error"],
    "answer": "5"
  },
  {
    "question": "float('inf') returns:",
    "options": ["inf", "Error", "Infinity", "None"],
    "answer": "inf"
  },
  {
    "question": "complex(1, 2) returns:",
    "options": ["(1+2j)", "1 + 2i", "(1,2)", "Error"],
    "answer": "(1+2j)"
  },
  {
    "question": "int(False) returns:",
    "options": ["0", "1", "False", "Error"],
    "answer": "0"
  },
  {
    "question": "float('abc') raises:",
    "options": ["ValueError", "TypeError", "NameError", "SyntaxError"],
    "answer": "ValueError"
  },
  {
    "question": "int(3.9999) gives:",
    "options": ["3", "4", "3.9999", "Error"],
    "answer": "3"
  },
  {
    "question": "bool([]) returns:",
    "options": ["False", "True", "None", "Error"],
    "answer": "False"
  },
  {
    "question": "bool([0]) returns:",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "list((1,2,3)) returns:",
    "options": ["[1, 2, 3]", "(1,2,3)", "{1,2,3}", "Error"],
    "answer": "[1, 2, 3]"
  },
  {
    "question": "tuple('ab') returns:",
    "options": ["('a', 'b')", "('ab')", "['a', 'b']", "Error"],
    "answer": "('a', 'b')"
  },
  {
    "question": "set([1,1,2]) returns:",
    "options": ["{1, 2}", "{1, 1, 2}", "[1, 2]", "Error"],
    "answer": "{1, 2}"
  },
  {
    "question": "int('101', 2) returns:",
    "options": ["5", "2", "101", "Error"],
    "answer": "5"
  },
  {
    "question": "What is type(complex(1))?",
    "options": ["<class 'complex'>", "<class 'int'>", "<class 'float'>", "<class 'str'>"],
    "answer": "<class 'complex'>"
  },
  {
    "question": "What is the result of str([1,2,3])?",
    "options": ["'[1, 2, 3]'", "[1,2,3]", "1 2 3", "Error"],
    "answer": "'[1, 2, 3]'"
  },
  {
    "question": "Which of the following can convert string to integer?",
    "options": ["int('42')", "str(42)", "float(42)", "bool(42)"],
    "answer": "int('42')"
  },
  {
    "question": "float(int('20')) returns:",
    "options": ["20.0", "20", "Error", "None"],
    "answer": "20.0"
  },
  {
    "question": "int(float('5.6')) returns:",
    "options": ["5", "6", "5.6", "Error"],
    "answer": "5"
  },
  {
    "question": "What is type(str(10.5))?",
    "options": ["<class 'str'>", "<class 'float'>", "<class 'int'>", "<class 'bool'>"],
    "answer": "<class 'str'>"
  },
  {
    "question": "bool(None) returns:",
    "options": ["False", "True", "None", "Error"],
    "answer": "False"
  },
  {
    "question": "bool('0') returns:",
    "options": ["True", "False", "0", "None"],
    "answer": "True"
  },
  {
    "question": "Which function converts to a set?",
    "options": ["set()", "list()", "tuple()", "dict()"],
    "answer": "set()"
  },
  {
    "question": "What is int('0x10', 16)?",
    "options": ["16", "10", "0", "Error"],
    "answer": "16"
  },
  {
    "question": "Which of these returns a float?",
    "options": ["float(5)", "int(5)", "bool(5)", "str(5)"],
    "answer": "float(5)"
  },
  {
    "question": "str([]) returns:",
    "options": ["'[]'", "[]", "None", "Error"],
    "answer": "'[]'"
  },
  {
    "question": "What is int('0010')?",
    "options": ["10", "8", "0010", "Error"],
    "answer": "10"
  },
  {
    "question": "int('0o10', 8) returns:",
    "options": ["8", "10", "0", "Error"],
    "answer": "8"
  },
  {
    "question": "What is float('nan')?",
    "options": ["nan", "0", "None", "Error"],
    "answer": "nan"
  },
  {
    "question": "Can you cast a string to boolean using bool()?",
    "options": ["Yes", "No", "Only if numeric", "Only if 'True'"],
    "answer": "Yes"
  },
  {
    "question": "bool({}) returns:",
    "options": ["False", "True", "None", "Error"],
    "answer": "False"
  },
  {
    "question": "What is list(range(3))?",
    "options": ["[0, 1, 2]", "[1, 2, 3]", "[0, 1, 2, 3]", "[1, 2]"],
    "answer": "[0, 1, 2]"
  },
  
  {
    "question": "Which keyword is used for a conditional statement in Python?",
    "options": ["if", "for", "def", "while"],
    "answer": "if"
  },
  {
    "question": "What will be the output of: if True: print('Yes') else: print('No')?",
    "options": ["Yes", "No", "Error", "None"],
    "answer": "Yes"
  },
  {
    "question": "Which statement is used to skip the current iteration in a loop?",
    "options": ["continue", "pass", "break", "exit"],
    "answer": "continue"
  },
  {
    "question": "Which statement is used to stop a loop?",
    "options": ["break", "exit", "continue", "pass"],
    "answer": "break"
  },
  {
    "question": "What is the output of: if 0: print('Yes') else: print('No')?",
    "options": ["No", "Yes", "Error", "0"],
    "answer": "No"
  },
  {
    "question": "Which Python keyword is used to define a loop?",
    "options": ["for", "loop", "iterate", "repeat"],
    "answer": "for"
  },
  {
    "question": "What does the range(3) return in a for loop?",
    "options": ["0,1,2", "1,2,3", "0,1,2,3", "3,2,1"],
    "answer": "0,1,2"
  },
  {
    "question": "What is the purpose of 'pass' in Python?",
    "options": ["Do nothing", "Break loop", "Raise error", "Restart loop"],
    "answer": "Do nothing"
  },
  {
    "question": "What will this code output?\nfor i in range(2):\n    print(i)\nelse:\n    print('Done')",
    "options": ["0 1 Done", "0 1", "Done", "1 2 Done"],
    "answer": "0 1 Done"
  },
  {
    "question": "Which statement is used to handle multiple conditions?",
    "options": ["elif", "elseif", "else if", "or"],
    "answer": "elif"
  },
  {
    "question": "What will be the output of:\nfor i in range(3):\n  if i == 1:\n    break\n  print(i)",
    "options": ["0", "0 1", "0 1 2", "1"],
    "answer": "0"
  },
  {
    "question": "Which keyword is used to test multiple expressions?",
    "options": ["elif", "switch", "match", "elif or"],
    "answer": "elif"
  },
  {
    "question": "What will be the output of:\nx = 10\nif x > 5: print('A')\nelse: print('B')",
    "options": ["A", "B", "Error", "None"],
    "answer": "A"
  },
  {
    "question": "What will this code return?\nwhile False:\n    print('Loop')",
    "options": ["Nothing", "Loop", "Error", "False"],
    "answer": "Nothing"
  },
  {
    "question": "Which loop is preferred when the number of iterations is unknown?",
    "options": ["while", "for", "loop", "range"],
    "answer": "while"
  },
  {
    "question": "Can we use else with while loop?",
    "options": ["Yes", "No", "Only in Python 3", "Only with break"],
    "answer": "Yes"
  },
  {
    "question": "What will be printed?\nfor i in [1,2,3]:\n    if i == 2:\n        continue\n    print(i)",
    "options": ["1 3", "1 2 3", "2 3", "1 2"],
    "answer": "1 3"
  },
  {
    "question": "What is the purpose of nested if statements?",
    "options": ["To check multiple conditions", "To loop", "To call functions", "To raise errors"],
    "answer": "To check multiple conditions"
  },
  {
    "question": "What does 'break' do inside nested loops?",
    "options": ["Exits only inner loop", "Exits all loops", "Pauses loop", "Skips to end"],
    "answer": "Exits only inner loop"
  },
  {
    "question": "Which control structure allows repeating a block of code?",
    "options": ["loop", "for/while", "def", "lambda"],
    "answer": "for/while"
  },
  {
    "question": "What is the output of:\nif not False:\n    print('Yes')",
    "options": ["Yes", "No", "Error", "None"],
    "answer": "Yes"
  },
  {
    "question": "Which operator is used for combining multiple conditions?",
    "options": ["and/or", "&&/||", "&/|", "if/else"],
    "answer": "and/or"
  },
  {
    "question": "What does 'continue' do in a loop?",
    "options": ["Skips current iteration", "Ends loop", "Raises error", "Passes"],
    "answer": "Skips current iteration"
  },
  {
    "question": "What is a loop that never ends called?",
    "options": ["Infinite loop", "Constant loop", "Forever loop", "Null loop"],
    "answer": "Infinite loop"
  },
  {
    "question": "What is the output of:\nfor i in range(3):\n  pass\nprint('End')",
    "options": ["End", "0 1 2 End", "0 End", "Error"],
    "answer": "End"
  },
  {
    "question": "How many times will the loop run?\ni = 0\nwhile i < 3:\n  i += 1",
    "options": ["3", "2", "0", "4"],
    "answer": "3"
  },
  {
    "question": "What is the purpose of indentation in control flow?",
    "options": ["Define blocks", "Style", "Comments", "None"],
    "answer": "Define blocks"
  },
  {
    "question": "What does 'if x:' do?",
    "options": ["Checks if x is truthy", "Compares x", "Always true", "Assigns x"],
    "answer": "Checks if x is truthy"
  },
  {
    "question": "Which of the following is invalid?",
    "options": ["if = 10", "if x > 5", "if True", "if not False"],
    "answer": "if = 10"
  },
  {
    "question": "Can you use for...else?",
    "options": ["Yes", "No", "Only with break", "Only in Python 2"],
    "answer": "Yes"
  },
  {
    "question": "What does 'else' in a for loop execute?",
    "options": ["If loop completes", "If loop breaks", "Always", "Never"],
    "answer": "If loop completes"
  },
  {
    "question": "Which of the following is used to stop execution of a program?",
    "options": ["exit()", "break", "continue", "return"],
    "answer": "exit()"
  },
  {
    "question": "What happens if you don't indent after an if statement?",
    "options": ["IndentationError", "SyntaxError", "LogicError", "No output"],
    "answer": "IndentationError"
  },
  {
    "question": "Which loop runs at least once even if condition is false?",
    "options": ["do...while (not in Python)", "for", "while", "None"],
    "answer": "None"
  },
  {
    "question": "What is a nested loop?",
    "options": ["Loop inside another loop", "Function loop", "List loop", "Error"],
    "answer": "Loop inside another loop"
  },
  {
    "question": "Can you use logical operators in if condition?",
    "options": ["Yes", "No", "Only 'and'", "Only 'or'"],
    "answer": "Yes"
  },
  {
    "question": "What does 'elif' stand for?",
    "options": ["Else if", "Else iterate", "Else loop", "Extra if"],
    "answer": "Else if"
  },
  {
    "question": "Which of the following is optional in a control structure?",
    "options": ["else", "if", "for", "while"],
    "answer": "else"
  },
  {
    "question": "What happens when break is used in for loop?",
    "options": ["Exits the loop", "Skips an iteration", "Goes to else", "Does nothing"],
    "answer": "Exits the loop"
  },
  {
    "question": "What is the output:\nfor i in range(2):\n  for j in range(2):\n    print(i,j)",
    "options": ["0 0 0 1 1 0 1 1", "0 0 1 1", "0 1", "0 0 1 1"],
    "answer": "0 0 0 1 1 0 1 1"
  },
  {
    "question": "What will be printed:\nif 1 and 0:\n  print('Yes')\nelse:\n  print('No')",
    "options": ["No", "Yes", "Error", "1"],
    "answer": "No"
  },
  {
    "question": "What is the output:\nx = 5\nif x < 10 and x > 2:\n  print('Good')",
    "options": ["Good", "Bad", "None", "Error"],
    "answer": "Good"
  },
  {
    "question": "What does 'not' do in a condition?",
    "options": ["Inverts result", "Returns same", "Always true", "Compares values"],
    "answer": "Inverts result"
  },
  {
    "question": "Can you use return in a loop inside a function?",
    "options": ["Yes", "No", "Only break", "Only pass"],
    "answer": "Yes"
  },
  {
    "question": "What is the output:\nx = [1,2]\nif x:\n  print('Yes')",
    "options": ["Yes", "No", "Error", "False"],
    "answer": "Yes"
  },
  {
    "question": "What is the output:\nwhile 1 == 1:\n  break\nprint('Done')",
    "options": ["Done", "Error", "None", "Loop"],
    "answer": "Done"
  },
  
  {
    "question": "Which method adds an element to the end of a list?",
    "options": ["append()", "insert()", "extend()", "add()"],
    "answer": "append()"
  },
  {
    "question": "Which method removes the last item from a list?",
    "options": ["pop()", "remove()", "del", "clear()"],
    "answer": "pop()"
  },
  {
    "question": "What is the result of the following code?\n\nlst = [1, 2, 3]\nlst.insert(1, 10)\nprint(lst)",
    "options": ["[1, 10, 2, 3]", "[10, 1, 2, 3]", "[1, 2, 3, 10]", "[1, 10, 3, 2]"],
    "answer": "[1, 10, 2, 3]"
  },
  {
    "question": "Which method removes the first occurrence of a specified element from the list?",
    "options": ["remove()", "pop()", "clear()", "del"],
    "answer": "remove()"
  },
  {
    "question": "Which method returns the index of the first occurrence of a specified value in a list?",
    "options": ["index()", "find()", "search()", "locate()"],
    "answer": "index()"
  },
  {
    "question": "Which method is used to add all the elements from another list to the current list?",
    "options": ["extend()", "append()", "insert()", "concat()"],
    "answer": "extend()"
  },
  {
    "question": "What does the pop() method return if the list is empty?",
    "options": ["IndexError", "None", "Empty", "ValueError"],
    "answer": "IndexError"
  },
  {
    "question": "What will be the result of the following code?\n\nlst = [10, 20, 30, 40]\nprint(lst[1:3])",
    "options": ["[20, 30]", "[10, 20, 30]", "[20, 30, 40]", "[30, 40]"],
    "answer": "[20, 30]"
  },
  {
    "question": "Which method removes all elements from a list?",
    "options": ["clear()", "remove()", "pop()", "del"],
    "answer": "clear()"
  },
  {
    "question": "Which method is used to reverse the elements of a list?",
    "options": ["reverse()", "flip()", "rev()", "reverse_list()"],
    "answer": "reverse()"
  },
  {
    "question": "What is the output of the following code?\n\nlst = [1, 2, 3, 4, 5]\nlst.remove(3)\nprint(lst)",
    "options": ["[1, 2, 4, 5]", "[1, 2, 3, 4, 5]", "[2, 3, 4, 5]", "[1, 2, 4]"],
    "answer": "[1, 2, 4, 5]"
  },
  {
    "question": "Which method returns a new sorted list without modifying the original list?",
    "options": ["sorted()", "sort()", "order()", "arrange()"],
    "answer": "sorted()"
  },
  {
    "question": "What will the following code print?\n\nlst = [1, 2, 3]\nlst.append([4, 5])\nprint(lst)",
    "options": ["[1, 2, 3, 4, 5]", "[1, 2, 3, [4, 5]]", "[1, 2, 3, 4, 5, 6]", "[1, 2, 3]"],
    "answer": "[1, 2, 3, [4, 5]]"
  },
  {
    "question": "Which method can be used to find the length of a list?",
    "options": ["len()", "length()", "size()", "count()"],
    "answer": "len()"
  },
  {
    "question": "What will be the output of the following code?\n\nlst = [5, 10, 15]\nprint(lst * 2)",
    "options": ["[5, 10, 15, 5, 10, 15]", "[5, 5, 10, 10, 15, 15]", "[10, 15, 20]", "[5, 10, 15]"],
    "answer": "[5, 10, 15, 5, 10, 15]"
  },
  {
    "question": "Which of the following methods will return True if a specified value is in the list?",
    "options": ["in", "contains()", "exists()", "find()"],
    "answer": "in"
  },
  {
    "question": "Which method is used to remove the last item of a list without raising an error if the list is empty?",
    "options": ["pop()", "clear()", "del", "remove()"],
    "answer": "pop()"
  },
  {
    "question": "What will be the output of the following code?\n\nlst = [10, 20, 30]\nlst.insert(2, 25)\nprint(lst)",
    "options": ["[10, 20, 25, 30]", "[10, 20, 30, 25]", "[10, 25, 20, 30]", "[20, 30, 10, 25]"],
    "answer": "[10, 20, 25, 30]"
  },
  {
    "question": "Which method removes all occurrences of a specified element in a list?",
    "options": ["remove()", "clear()", "del", "pop()"],
    "answer": "remove()"
  },
  {
    "question": "What is the result of this code?\n\nlst = [10, 20, 30]\nprint(lst[::-1])",
    "options": ["[30, 20, 10]", "[10, 20, 30]", "[10, 20]", "[30, 40, 50]"],
    "answer": "[30, 20, 10]"
  },
  {
    "question": "Which method is used to join two lists together?",
    "options": ["extend()", "append()", "insert()", "join()"],
    "answer": "extend()"
  },
  {
    "question": "What is the output of the following code?\n\nlst = [1, 2, 3]\nlst.sort(reverse=True)\nprint(lst)",
    "options": ["[3, 2, 1]", "[1, 2, 3]", "[2, 1, 3]", "[1, 3, 2]"],
    "answer": "[3, 2, 1]"
  },
  {
    "question": "What does the count() method do in a list?",
    "options": ["Counts occurrences of a value", "Adds an element", "Removes an element", "Finds the index of an element"],
    "answer": "Counts occurrences of a value"
  },
  {
    "question": "Which method returns a shallow copy of the list?",
    "options": ["copy()", "duplicate()", "clone()", "shallow_copy()"],
    "answer": "copy()"
  },
  {
    "question": "Which method checks if a list is empty?",
    "options": ["not", "is_empty()", "empty()", "len() == 0"],
    "answer": "len() == 0"
  },
  {
    "question": "What will be the output of the following code?\n\nlst = [1, 2, 3, 4, 5]\nprint(lst[1:4])",
    "options": ["[2, 3, 4]", "[1, 2, 3]", "[2, 3]", "[3, 4, 5]"],
    "answer": "[2, 3, 4]"
  },
  {
    "question": "What will be the output of the following code?\n\nlst = [1, 2, 3]\nprint(lst[1:])",
    "options": ["[2, 3]", "[1, 2]", "[1, 3]", "[2]"],
    "answer": "[2, 3]"
  },
  {
    "question": "Which method is used to remove elements from a list based on their index?",
    "options": ["del", "remove()", "pop()", "clear()"],
    "answer": "del"
  },
  {
    "question": "What will the following code return?\n\nlst = [1, 2, 3]\nprint(lst[0])",
    "options": ["1", "2", "3", "None"],
    "answer": "1"
  },
  {
    "question": "What will be the output of the following code?\n\nlst = [1, 2, 3]\nprint(lst[-1])",
    "options": ["3", "1", "2", "None"],
    "answer": "3"
  },
  {
    "question": "What is the correct way to make a copy of a list?",
    "options": ["lst.copy()", "copy(lst)", "lst[:]"],
    "answer": "lst.copy()"
  },
  {
    "question": "Which of the following methods sorts the list in ascending order?",
    "options": ["sort()", "sorted()", "order()", "arrange()"],
    "answer": "sort()"
  },
  {
    "question": "What does the reverse() method do in a list?",
    "options": ["Reverses the order of the list", "Sorts the list", "Deletes the list", "Adds a new element"],
    "answer": "Reverses the order of the list"
  },
  {
    "question": "What is the output of the following code?\n\nlst = ['apple', 'banana', 'cherry']\nprint(lst[1:2])",
    "options": ["['banana']", "['apple']", "['cherry']", "['banana', 'cherry']"],
    "answer": "['banana']"
  },
  {
    "question": "Which of the following is used to insert an element at the start of the list?",
    "options": ["insert(0, value)", "append(value)", "extend(value)", "insert(value)"],
    "answer": "insert(0, value)"
  },
  {
    "question": "Which method is used to remove all items from the list?",
    "options": ["clear()", "remove()", "pop()", "del"],
    "answer": "clear()"
  },
  {
    "question": "What is the result of this code?\n\nlst = [1, 2, 3]\nprint(lst[-2])",
    "options": ["2", "3", "1", "None"],
    "answer": "2"
  },
  {
    "question": "What is the output of the following code?\n\nlst = [1, 2, 3]\nprint(lst[:2])",
    "options": ["[1, 2]", "[2, 3]", "[1, 3]", "[1, 2, 3]"],
    "answer": "[1, 2]"
  },
  {
    "question": "Which method is used to count the number of occurrences of a specific element in a list?",
    "options": ["count()", "occurrences()", "find()", "index()"],
    "answer": "count()"
  },
  {
    "question": "What is the output of this code?\n\nlst = [1, 2, 3, 4]\nlst.remove(3)\nprint(lst)",
    "options": ["[1, 2, 4]", "[1, 2, 3, 4]", "[2, 3, 4]", "[1, 4]"],
    "answer": "[1, 2, 4]"
  },
  {
    "question": "Which of the following methods is used to remove an item from the list by its index?",
    "options": ["pop()", "remove()", "clear()", "del"],
    "answer": "pop()"
  },
  
  {
    "question": "Which of the following is a correct way to define a tuple?",
    "options": ["(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "tuple(1, 2, 3)"],
    "answer": "(1, 2, 3)"
  },
  {
    "question": "What is the output of the following code?\n\ntuple1 = (1, 2, 3)\nprint(len(tuple1))",
    "options": ["1", "2", "3", "None"],
    "answer": "3"
  },
  {
    "question": "Can elements of a tuple be changed after it is created?",
    "options": ["Yes", "No", "Only if the tuple contains lists", "Only if the tuple contains mutable elements"],
    "answer": "No"
  },
  {
    "question": "What will be the result of the following code?\n\ntuple1 = (1, 2, 3)\nprint(tuple1[1])",
    "options": ["1", "2", "3", "None"],
    "answer": "2"
  },
  {
    "question": "Which method can be used to find the index of a value in a tuple?",
    "options": ["index()", "find()", "search()", "locate()"],
    "answer": "index()"
  },
  {
    "question": "What is the output of the following code?\n\ntuple1 = (1, 2, 3)\nprint(tuple1[::-1])",
    "options": ["(3, 2, 1)", "(1, 2, 3)", "(2, 1, 3)", "(3, 1, 2)"],
    "answer": "(3, 2, 1)"
  },
  {
    "question": "What is the output of this code?\n\ntuple1 = (1, 2, 3, 4)\nprint(tuple1[1:3])",
    "options": ["(2, 3)", "(1, 2)", "(3, 4)", "(2, 3, 4)"],
    "answer": "(2, 3)"
  },
  {
    "question": "What does the 'count()' method do in a tuple?",
    "options": ["Counts occurrences of a value", "Removes a value", "Finds the index of a value", "Checks if the tuple is empty"],
    "answer": "Counts occurrences of a value"
  },
  {
    "question": "Which of the following operations is allowed on a tuple?",
    "options": ["Concatenation", "Insertion", "Deletion", "Modification"],
    "answer": "Concatenation"
  },
  {
    "question": "What is the result of this code?\n\ntuple1 = (1, 2, 3)\nprint(2 in tuple1)",
    "options": ["True", "False", "Error", "None"],
    "answer": "True"
  },
  {
    "question": "What is the output of the following code?\n\ntuple1 = (10, 20, 30)\nprint(tuple1 * 2)",
    "options": ["(10, 20, 30, 10, 20, 30)", "(20, 30, 10)", "(10, 20, 30)", "(10, 20)"],
    "answer": "(10, 20, 30, 10, 20, 30)"
  },
  {
    "question": "Which of the following data types can be stored in a tuple?",
    "options": ["Any data type", "Only integers", "Only strings", "Only boolean values"],
    "answer": "Any data type"
  },
  {
    "question": "What is the output of the following code?\n\ntuple1 = (1, 2, 3, 4)\nprint(tuple1[-1])",
    "options": ["4", "1", "3", "None"],
    "answer": "4"
  },
  {
    "question": "What is the result of the following code?\n\ntuple1 = (1, 2, 3)\nprint(tuple1 + (4, 5))",
    "options": ["(1, 2, 3, 4, 5)", "(1, 2, 3, 4)", "(1, 2, 3)", "(4, 5, 1, 2, 3)"],
    "answer": "(1, 2, 3, 4, 5)"
  },
  {
    "question": "Can you remove elements from a tuple?",
    "options": ["Yes", "No", "Only if the tuple contains lists", "Only if the tuple is empty"],
    "answer": "No"
  },
  {
    "question": "What will be the result of the following code?\n\ntuple1 = (1, 2, 3)\ntuple2 = (4, 5)\ntuple3 = tuple1 + tuple2\nprint(tuple3)",
    "options": ["(1, 2, 3, 4, 5)", "(4, 5, 1, 2, 3)", "(1, 2, 3)", "(4, 5)"],
    "answer": "(1, 2, 3, 4, 5)"
  },
  {
    "question": "What is the output of the following code?\n\ntuple1 = (1, 2, 3)\nprint(tuple1[1:])",
    "options": ["(2, 3)", "(1, 2)", "(1, 3)", "(2)"],
    "answer": "(2, 3)"
  },
  {
    "question": "What is the result of this code?\n\ntuple1 = (1, 2, 3)\nprint(tuple1[-2])",
    "options": ["2", "3", "1", "None"],
    "answer": "2"
  },
  {
    "question": "What is the output of the following code?\n\ntuple1 = (10, 20, 30)\nprint(tuple1.index(20))",
    "options": ["1", "2", "0", "None"],
    "answer": "1"
  },
  {
    "question": "What is the type of the following variable?\n\ntuple1 = (1, 2, 3)\nprint(type(tuple1))",
    "options": ["tuple", "list", "set", "dict"],
    "answer": "tuple"
  },
  {
    "question": "Can you change the value of an element in a tuple?",
    "options": ["Yes", "No", "Only if the tuple contains mutable elements", "Only if the element is a string"],
    "answer": "No"
  },
  {
    "question": "What will the following code output?\n\ntuple1 = (1, 2, 3, 4)\nprint(tuple1[1:3])",
    "options": ["(2, 3)", "(1, 2)", "(3, 4)", "(2, 3, 4)"],
    "answer": "(2, 3)"
  },
  {
    "question": "What is the result of this code?\n\ntuple1 = (1, 2, 3)\ntuple2 = tuple1 * 3\nprint(tuple2)",
    "options": ["(1, 2, 3, 1, 2, 3, 1, 2, 3)", "(3, 2, 1)", "(2, 1, 3)", "(1, 2, 3)"],
    "answer": "(1, 2, 3, 1, 2, 3, 1, 2, 3)"
  },
  {
    "question": "What is the output of this code?\n\ntuple1 = (1, 2, 3)\nprint(3 in tuple1)",
    "options": ["True", "False", "Error", "None"],
    "answer": "True"
  },
  {
    "question": "What is the result of the following code?\n\ntuple1 = (1, 2, 3)\ntuple2 = tuple1 + (4, 5)\ntuple2 = tuple2 * 2\nprint(tuple2)",
    "options": ["(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)", "(1, 2, 3, 4, 5)", "(1, 2, 3)", "(4, 5, 1, 2, 3)"],
    "answer": "(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)"
  },
  {
    "question": "What will be the output of the following code?\n\ntuple1 = (1, 2, 3)\nprint(tuple1[::-2])",
    "options": ["(3, 1)", "(1, 3)", "(3, 2, 1)", "(2, 1)"],
    "answer": "(3, 1)"
  },
  {
    "question": "What does the tuple unpacking feature allow you to do?",
    "options": ["Assign tuple values to variables", "Change tuple values", "Find the length of a tuple", "Combine multiple tuples"],
    "answer": "Assign tuple values to variables"
  },
  {
    "question": "What is the output of the following code?\n\ntuple1 = (1, 2, 3)\ntuple2 = (4, 5)\ntuple3 = tuple1 + tuple2\nprint(tuple3)",
    "options": ["(1, 2, 3, 4, 5)", "(4, 5, 1, 2, 3)", "(1, 2, 3)", "(4, 5)"],
    "answer": "(1, 2, 3, 4, 5)"
  },
  {
    "question": "What is the result of the following code?\n\ntuple1 = (1, 2, 3)\ntuple2 = (3, 2, 1)\nprint(tuple1 == tuple2)",
    "options": ["True", "False", "None", "Error"],
    "answer": "False"
  },
  {
    "question": "Which of the following is true about a tuple?",
    "options": ["It is immutable", "It is mutable", "It can only store integers", "It has variable length"],
    "answer": "It is immutable"
  },
  {
    "question": "Can a tuple contain other tuples?",
    "options": ["Yes", "No", "Only if the tuple is empty", "Only if the nested tuple is of different size"],
    "answer": "Yes"
  },
  {
    "question": "Which of the following methods is used to convert a list to a tuple?",
    "options": ["tuple()", "list()", "convert()", "to_tuple()"],
    "answer": "tuple()"
  },
  {
    "question": "What will be the output of the following code?\n\ntuple1 = (1, 2, 3, 4)\ntuple2 = tuple1[:2]\nprint(tuple2)",
    "options": ["(1, 2)", "(2, 3)", "(1, 3)", "(1, 2, 3)"],
    "answer": "(1, 2)"
  },
  {
    "question": "What is the result of this code?\n\ntuple1 = (1, 2, 3)\ntuple2 = (1, 2, 3)\nprint(tuple1 == tuple2)",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  
  {
    "question": "Which of the following is the correct way to define a dictionary?",
    "options": ["{1: 'a', 2: 'b'}", "[1: 'a', 2: 'b']", "(1: 'a', 2: 'b')", "dict(1: 'a', 2: 'b')"],
    "answer": "{1: 'a', 2: 'b'}"
  },
  {
    "question": "What is the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\nprint(len(dict1))",
    "options": ["1", "2", "3", "None"],
    "answer": "2"
  },
  {
    "question": "Which method is used to add a key-value pair to an existing dictionary?",
    "options": ["add()", "insert()", "update()", "append()"],
    "answer": "update()"
  },
  {
    "question": "What is the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\nprint(dict1['a'])",
    "options": ["1", "2", "Error", "None"],
    "answer": "1"
  },
  {
    "question": "What will be the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\nprint('a' in dict1)",
    "options": ["True", "False", "Error", "None"],
    "answer": "True"
  },
  {
    "question": "Which of the following methods is used to remove a specific key from a dictionary?",
    "options": ["remove()", "del()", "pop()", "delete()"],
    "answer": "pop()"
  },
  {
    "question": "What is the result of the following code?\n\ndict1 = {'a': 1, 'b': 2}\ndict2 = dict1.copy()\nprint(dict2)",
    "options": ["{'a': 1, 'b': 2}", "None", "Error", "Empty dictionary"],
    "answer": "{'a': 1, 'b': 2}"
  },
  {
    "question": "Which method returns the value for the specified key in a dictionary?",
    "options": ["get()", "value()", "fetch()", "retrieve()"],
    "answer": "get()"
  },
  {
    "question": "What will be the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\ndict1['c'] = 3\nprint(dict1)",
    "options": ["{'a': 1, 'b': 2, 'c': 3}", "{'a': 1, 'b': 2}", "{'a': 1, 'c': 3}", "None"],
    "answer": "{'a': 1, 'b': 2, 'c': 3}"
  },
  {
    "question": "What will be the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\ndict1.pop('a')\nprint(dict1)",
    "options": ["{'b': 2}", "{'a': 1, 'b': 2}", "{'a': 1}", "None"],
    "answer": "{'b': 2}"
  },
  {
    "question": "Which of the following methods returns a list of all keys in a dictionary?",
    "options": ["keys()", "values()", "items()", "list()"],
    "answer": "keys()"
  },
  {
    "question": "What is the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\nprint(dict1.get('c'))",
    "options": ["None", "Error", "0", "2"],
    "answer": "None"
  },
  {
    "question": "Which method returns a list of all the values in a dictionary?",
    "options": ["values()", "keys()", "items()", "list()"],
    "answer": "values()"
  },
  {
    "question": "What is the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\ndict1.clear()\nprint(dict1)",
    "options": ["{}", "None", "Error", "Empty list"],
    "answer": "{}"
  },
  {
    "question": "Which method is used to merge two dictionaries?",
    "options": ["merge()", "update()", "join()", "combine()"],
    "answer": "update()"
  },
  {
    "question": "Can a dictionary contain other dictionaries as values?",
    "options": ["Yes", "No", "Only if keys are strings", "Only if the value is a list"],
    "answer": "Yes"
  },
  {
    "question": "What is the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\ndict1['a'] = 3\nprint(dict1)",
    "options": ["{'a': 3, 'b': 2}", "{'a': 1, 'b': 2}", "{'a': 1, 'b': 3}", "{'b': 2}"],
    "answer": "{'a': 3, 'b': 2}"
  },
  {
    "question": "Which of the following is used to check if a key exists in a dictionary?",
    "options": ["in", "has()", "has_key()", "key()"],
    "answer": "in"
  },
  {
    "question": "Which of the following statements is correct regarding dictionary keys?",
    "options": ["Keys can be mutable types", "Keys must be immutable types", "Keys can be mutable if the dictionary contains only strings", "Keys must be strings"],
    "answer": "Keys must be immutable types"
  },
  {
    "question": "What will be the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\ndict2 = {'c': 3, 'd': 4}\nprint(dict1.update(dict2))",
    "options": ["None", "({'a': 1, 'b': 2, 'c': 3, 'd': 4})", "{'c': 3, 'd': 4}", "({'a': 1, 'b': 2})"],
    "answer": "None"
  },
  {
    "question": "Which of the following methods returns a list of tuples containing each key-value pair?",
    "options": ["items()", "keys()", "values()", "pairs()"],
    "answer": "items()"
  },
  {
    "question": "What will be the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\nprint('a' in dict1.keys())",
    "options": ["True", "False", "Error", "None"],
    "answer": "True"
  },
  {
    "question": "What is the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\nprint(list(dict1))",
    "options": ["['a', 'b']", "['1', '2']", "[(1, 2)]", "None"],
    "answer": "['a', 'b']"
  },
  {
    "question": "What will be the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\ndict1.update({'a': 3})\nprint(dict1)",
    "options": ["{'a': 3, 'b': 2}", "{'a': 1, 'b': 2}", "{'a': 1, 'b': 3}", "Error"],
    "answer": "{'a': 3, 'b': 2}"
  },
  {
    "question": "What is the result of this code?\n\ndict1 = {'a': 1, 'b': 2}\nprint('c' in dict1)",
    "options": ["True", "False", "Error", "None"],
    "answer": "False"
  },
  {
    "question": "Which of the following is true about dictionary values?",
    "options": ["Values can be mutable", "Values must be immutable", "Values must be strings", "Values are always numbers"],
    "answer": "Values can be mutable"
  },
  {
    "question": "Which of the following methods is used to get all the items of a dictionary?",
    "options": ["items()", "values()", "keys()", "list()"],
    "answer": "items()"
  },
  {
    "question": "What is the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\ndict1.update({'a': 4, 'b': 5})\nprint(dict1)",
    "options": ["{'a': 4, 'b': 5}", "{'a': 1, 'b': 2}", "{'a': 1, 'b': 5}", "{'a': 4}"],
    "answer": "{'a': 4, 'b': 5}"
  },
  {
    "question": "Which of the following is a method that cannot be used to access dictionary elements?",
    "options": ["get()", "keys()", "index()", "values()"],
    "answer": "index()"
  },
  {
    "question": "What is the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\ndict1['c'] = 3\nprint(dict1)",
    "options": ["{'a': 1, 'b': 2, 'c': 3}", "{'a': 1, 'b': 2}", "{'c': 3}", "{'a': 1, 'c': 3}"],
    "answer": "{'a': 1, 'b': 2, 'c': 3}"
  },
  {
    "question": "What will be the result of the following code?\n\ndict1 = {'a': 1, 'b': 2}\ndict2 = dict1\nprint(dict2)",
    "options": ["{'a': 1, 'b': 2}", "{'a': 1, 'b': 2, 'c': 3}", "Error", "None"],
    "answer": "{'a': 1, 'b': 2}"
  },
  {
    "question": "Can a dictionary have duplicate keys?",
    "options": ["Yes", "No", "Only if values are the same", "Only if keys are strings"],
    "answer": "No"
  },
  {
    "question": "Which of the following methods can be used to convert a dictionary to a list?",
    "options": ["list()", "dict()", "to_list()", "convert()"],
    "answer": "list()"
  },
  {
    "question": "What is the output of the following code?\n\ndict1 = {'a': 1, 'b': 2}\ndict1.pop('b')\nprint(dict1)",
    "options": ["{'a': 1}", "Error", "{'a': 2}", "{}"],
    "answer": "{'a': 1}"
  },
  {
    "question": "Which of the following is used to remove all key-value pairs from a dictionary?",
    "options": ["clear()", "pop()", "remove()", "del()"],
    "answer": "clear()"
  },
  {
    "question": "Which of the following is the correct way to define a set in Python?",
    "options": ["{1, 2, 3}", "[1, 2, 3]", "(1, 2, 3)", "set{1, 2, 3}"],
    "answer": "{1, 2, 3}"
  },
  {
    "question": "What is the output of the following code?\n\nset1 = {1, 2, 3}\nprint(len(set1))",
    "options": ["1", "2", "3", "None"],
    "answer": "3"
  },
  {
    "question": "Which method is used to add an element to a set?",
    "options": ["add()", "append()", "insert()", "extend()"],
    "answer": "add()"
  },
  {
    "question": "What will be the result of the following code?\n\nset1 = {1, 2, 3}\nset1.add(4)\nprint(set1)",
    "options": ["{1, 2, 3, 4}", "{1, 4}", "{4, 3, 2, 1}", "Error"],
    "answer": "{1, 2, 3, 4}"
  },
  {
    "question": "What is the output of the following code?\n\nset1 = {1, 2, 3}\nprint(2 in set1)",
    "options": ["True", "False", "Error", "None"],
    "answer": "True"
  },
  {
    "question": "Which method is used to remove a specific element from a set?",
    "options": ["remove()", "delete()", "discard()", "clear()"],
    "answer": "remove()"
  },
  {
    "question": "What will be the output of the following code?\n\nset1 = {1, 2, 3}\nset1.remove(2)\nprint(set1)",
    "options": ["{1, 3}", "{2, 3}", "{1, 2}", "Error"],
    "answer": "{1, 3}"
  },
  {
    "question": "What will be the result of the following code?\n\nset1 = {1, 2, 3}\nset1.discard(3)\nprint(set1)",
    "options": ["{1, 2}", "{2, 3}", "{1, 3}", "None"],
    "answer": "{1, 2}"
  },
  {
    "question": "What will be the output of the following code?\n\nset1 = {1, 2, 3}\nset1.clear()\nprint(set1)",
    "options": ["{}", "None", "Error", "Empty set"],
    "answer": "{}"
  },
  {
    "question": "What method is used to return a new set with the elements of another set added?",
    "options": ["union()", "add()", "update()", "extend()"],
    "answer": "union()"
  },
  {
    "question": "What is the output of the following code?\n\nset1 = {1, 2, 3}\nset2 = {2, 3, 4}\nset3 = set1.union(set2)\nprint(set3)",
    "options": ["{1, 2, 3, 4}", "{2, 3}", "{1, 4}", "{1, 2, 3}"],
    "answer": "{1, 2, 3, 4}"
  },
  {
    "question": "Which method is used to return the intersection of two sets?",
    "options": ["union()", "intersection()", "add()", "update()"],
    "answer": "intersection()"
  },
  {
    "question": "What will be the output of the following code?\n\nset1 = {1, 2, 3}\nset2 = {2, 3, 4}\nset3 = set1.intersection(set2)\nprint(set3)",
    "options": ["{2, 3}", "{1, 2, 3, 4}", "{1, 4}", "{2, 3, 4}"],
    "answer": "{2, 3}"
  },
  {
    "question": "Which of the following is used to find the difference between two sets?",
    "options": ["difference()", "subtract()", "remove()", "clear()"],
    "answer": "difference()"
  },
  {
    "question": "What will be the output of the following code?\n\nset1 = {1, 2, 3}\nset2 = {2, 3, 4}\nset3 = set1.difference(set2)\nprint(set3)",
    "options": ["{1}", "{2, 3}", "{4}", "{}"],
    "answer": "{1}"
  },
  {
    "question": "Which method is used to remove the elements present in another set from the current set?",
    "options": ["difference_update()", "remove()", "discard()", "clear()"],
    "answer": "difference_update()"
  },
  {
    "question": "What will be the output of the following code?\n\nset1 = {1, 2, 3}\nset2 = {2, 3, 4}\nset1.difference_update(set2)\nprint(set1)",
    "options": ["{1}", "{2, 3}", "{4}", "{}"],
    "answer": "{1}"
  },
  {
    "question": "What is the result of the following code?\n\nset1 = {1, 2, 3}\nset2 = {2, 3, 4}\nprint(set1.symmetric_difference(set2))",
    "options": ["{1, 4}", "{2, 3}", "{1, 2, 3, 4}", "{1, 4, 2}"],
    "answer": "{1, 4}"
  },
  {
    "question": "Which method returns the symmetric difference of two sets?",
    "options": ["symmetric_difference()", "union()", "difference()", "intersection()"],
    "answer": "symmetric_difference()"
  },
  {
    "question": "What will be the output of the following code?\n\nset1 = {1, 2, 3}\nset2 = {3, 4, 5}\nprint(set1.isdisjoint(set2))",
    "options": ["True", "False", "None", "Error"],
    "answer": "False"
  },
  {
    "question": "Which method checks whether two sets have no common elements?",
    "options": ["isdisjoint()", "isunion()", "disjoint()", "common()"],
    "answer": "isdisjoint()"
  },
  {
    "question": "What is the result of the following code?\n\nset1 = {1, 2, 3}\nset2 = {1, 2, 3}\nprint(set1 == set2)",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "Which method checks whether a set is a subset of another set?",
    "options": ["issubset()", "issuperset()", "sub()", "subset()"],
    "answer": "issubset()"
  },
  {
    "question": "What will be the output of the following code?\n\nset1 = {1, 2, 3}\nset2 = {1, 2, 3, 4}\nprint(set1.issubset(set2))",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "What is the result of the following code?\n\nset1 = {1, 2, 3}\nset2 = {1, 2}\nprint(set1.issuperset(set2))",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "Which of the following methods returns the union of two sets?",
    "options": ["union()", "intersection()", "difference()", "symmetric_difference()"],
    "answer": "union()"
  },
  {
    "question": "What is the output of the following code?\n\nset1 = {1, 2, 3}\nset2 = {2, 3, 4}\nprint(set1 | set2)",
    "options": ["{1, 2, 3, 4}", "{2, 3}", "{1, 4}", "{}"],
    "answer": "{1, 2, 3, 4}"
  },
  {
    "question": "Which of the following methods is used to remove an arbitrary element from a set?",
    "options": ["pop()", "remove()", "discard()", "clear()"],
    "answer": "pop()"
  },
  {
    "question": "What will be the result of the following code?\n\nset1 = {1, 2, 3}\nset1.pop()\nprint(set1)",
    "options": ["{2, 3}", "{1, 3}", "{2}", "None"],
    "answer": "{2, 3}"
  },
  {
    "question": "Which of the following operations can be performed on sets in Python?",
    "options": ["Union", "Intersection", "Difference", "All of the above"],
    "answer": "All of the above"
  },
  {
    "question": "What is the output of the following code?\n\nset1 = {1, 2, 3}\nset2 = {2, 3, 4}\nprint(set1 & set2)",
    "options": ["{2, 3}", "{1, 2, 3, 4}", "{1, 4}", "{2, 3, 4}"],
    "answer": "{2, 3}"
  },
  {
    "question": "What will be the output of the following code?\n\nset1 = {1, 2, 3}\nset1.add(3)\nprint(set1)",
    "options": ["{1, 2, 3}", "{1, 3}", "{2, 3}", "{1, 2}"],
    "answer": "{1, 2, 3}"
  },
  {
    "question": "Which of the following data types cannot be used as elements of a set?",
    "options": ["Integer", "List", "String", "Tuple"],
    "answer": "List"
  },
  {
    "question": "What will be the result of the following code?\n\nset1 = {1, 2, 3}\nset1.add([4, 5])\nprint(set1)",
    "options": ["Error", "{1, 2, 3, [4, 5]}", "{1, 2, 3}", "{4, 5}"],
    "answer": "Error"
  },
  {
    "question": "Which method is used to return the intersection of two sets?",
    "options": ["intersection()", "union()", "difference()", "symmetric_difference()"],
    "answer": "intersection()"
  },
  {
    "question": "What is the result of the following code?\n\nset1 = {1, 2, 3}\nset2 = {3, 4, 5}\nprint(set1 | set2)",
    "options": ["{1, 2, 3, 4, 5}", "{1, 2, 3}", "{4, 5}", "{2, 3, 4}"],
    "answer": "{1, 2, 3, 4, 5}"
  },
  {
    "question": "Which of the following statements is true about sets?",
    "options": ["Sets are ordered", "Sets allow duplicate elements", "Sets are mutable", "Sets allow index access"],
    "answer": "Sets are mutable"
  },
  {
    "question": "What will be the result of the following code?\n\nset1 = {1, 2, 3}\nset2 = set1.copy()\nprint(set2)",
    "options": ["{1, 2, 3}", "{2, 3}", "{1}", "{}"],
    "answer": "{1, 2, 3}"
  },
  
  {
    "question": "What is the correct way to import a module in Python?",
    "options": ["import module", "import(module)", "module import", "from module import"],
    "answer": "import module"
  },
  {
    "question": "Which of the following functions is used to get the name of a module in Python?",
    "options": ["module.name()", "module.get()", "module.__name__", "module.get_name()"],
    "answer": "module.__name__"
  },
  {
    "question": "How can you import specific functions from a module?",
    "options": ["import module.function", "from module import function", "import module as function", "from function import module"],
    "answer": "from module import function"
  },
  {
    "question": "Which of the following statements is used to import all functions from a module?",
    "options": ["import * from module", "from module import *", "import all from module", "None of the above"],
    "answer": "from module import *"
  },
  {
    "question": "Which function is used to display all available functions in a module?",
    "options": ["dir()", "functions()", "help()", "list()"],
    "answer": "dir()"
  },
  {
    "question": "How can you create a function in Python?",
    "options": ["def function_name():", "function function_name():", "create function_name():", "def function_name[]:"],
    "answer": "def function_name():"
  },
  {
    "question": "Which of the following is the correct syntax for a function that returns a value?",
    "options": ["def function_name(): return value", "def function_name return value", "function_name(): return value", "function_name: return value"],
    "answer": "def function_name(): return value"
  },
  {
    "question": "What does the 'return' keyword do in a function?",
    "options": ["Ends the function", "Returns a value to the caller", "Repeats the function", "None of the above"],
    "answer": "Returns a value to the caller"
  },
  {
    "question": "What is the output of the following code?\n\nimport math\nprint(math.sqrt(16))",
    "options": ["4", "16", "2", "None of the above"],
    "answer": "4"
  },
  {
    "question": "What is the purpose of the 'import' keyword in Python?",
    "options": ["To include functions and variables from another file", "To define a function", "To execute a script", "None of the above"],
    "answer": "To include functions and variables from another file"
  },
  {
    "question": "What will be the output of the following code?\n\nimport random\nprint(random.randint(1, 10))",
    "options": ["A random integer between 1 and 10", "1", "10", "None of the above"],
    "answer": "A random integer between 1 and 10"
  },
  {
    "question": "Which of the following is NOT a standard Python module?",
    "options": ["math", "sys", "random", "input"],
    "answer": "input"
  },
  {
    "question": "What does the 'def' keyword do in Python?",
    "options": ["It defines a function", "It returns a value", "It initializes a variable", "It imports a module"],
    "answer": "It defines a function"
  },
  {
    "question": "How do you call a function in Python?",
    "options": ["function_name()", "call function_name()", "function_name[]", "None of the above"],
    "answer": "function_name()"
  },
  {
    "question": "Which function is used to display a list of modules in the current environment?",
    "options": ["help()", "dir()", "list_modules()", "modules()"],
    "answer": "dir()"
  },
  {
    "question": "Which of the following is the correct way to use the 'math' module?",
    "options": ["import math", "from math import *", "import math as m", "All of the above"],
    "answer": "All of the above"
  },
  {
    "question": "What will be the output of the following code?\n\nimport os\nprint(os.getcwd())",
    "options": ["Current working directory", "os module", "None", "Error"],
    "answer": "Current working directory"
  },
  {
    "question": "What is the purpose of the 'global' keyword in Python?",
    "options": ["To declare a global variable", "To declare a local variable", "To exit a function", "To import a module"],
    "answer": "To declare a global variable"
  },
  {
    "question": "What is the correct syntax for passing arguments to a function?",
    "options": ["function(arg1, arg2)", "function[arg1, arg2]", "function{arg1, arg2}", "function(arg1 and arg2)"],
    "answer": "function(arg1, arg2)"
  },
  {
    "question": "Which of the following is the correct way to call a function that takes two arguments?",
    "options": ["function(arg1, arg2)", "function(arg1 and arg2)", "function{arg1, arg2}", "function: arg1, arg2"],
    "answer": "function(arg1, arg2)"
  },
  {
    "question": "What does the 'help()' function do in Python?",
    "options": ["Displays help documentation for a module", "Runs the code", "Prints output to the console", "None of the above"],
    "answer": "Displays help documentation for a module"
  },
  {
    "question": "What is the result of the following code?\n\ndef test():\n    return 5\nprint(test())",
    "options": ["5", "None", "Error", "test"],
    "answer": "5"
  },
  {
    "question": "What is the purpose of the 'lambda' keyword in Python?",
    "options": ["To define an anonymous function", "To define a variable", "To define a class", "To import a module"],
    "answer": "To define an anonymous function"
  },
  {
    "question": "How do you pass a default value for a parameter in a function?",
    "options": ["def function(param=default_value)", "def function(param=default_value):", "function(param=default_value)", "None of the above"],
    "answer": "def function(param=default_value)"
  },
  {
    "question": "Which of the following is used to read the contents of a file in Python?",
    "options": ["open()", "read()", "file()", "open_file()"],
    "answer": "open()"
  },
  {
    "question": "What will be the output of the following code?\n\ndef test(a, b=2):\n    return a + b\nprint(test(3))",
    "options": ["5", "3", "None", "Error"],
    "answer": "5"
  },
  {
    "question": "Which of the following is true about functions in Python?",
    "options": ["A function can return multiple values", "A function must always return a value", "Functions cannot be nested", "None of the above"],
    "answer": "A function can return multiple values"
  },
  {
    "question": "What is the correct way to call a function from a module?",
    "options": ["module.function()", "function.module()", "call function()", "None of the above"],
    "answer": "module.function()"
  },
  {
    "question": "What will be the output of the following code?\n\nimport math\nprint(math.pow(2, 3))",
    "options": ["8.0", "8", "2", "None of the above"],
    "answer": "8.0"
  },
  {
    "question": "How do you import a module and give it an alias?",
    "options": ["import module as alias", "from module import alias", "import alias as module", "None of the above"],
    "answer": "import module as alias"
  },
  {
    "question": "What will be the result of the following code?\n\nimport datetime\nprint(datetime.date.today())",
    "options": ["Current date", "Current time", "Date and time", "None of the above"],
    "answer": "Current date"
  },
  {
    "question": "What is the purpose of the 'args' and 'kwargs' in Python functions?",
    "options": ["To pass a variable number of arguments", "To define the default value", "To return multiple values", "None of the above"],
    "answer": "To pass a variable number of arguments"
  },
  {
    "question": "What will be the result of the following code?\n\ndef func(*args):\n    return sum(args)\nprint(func(1, 2, 3))",
    "options": ["6", "None", "1", "3"],
    "answer": "6"
  },
  {
    "question": "Which of the following functions is used to call a function from another file in Python?",
    "options": ["import function", "import module", "call() function", "None of the above"],
    "answer": "import module"
  },
  {
    "question": "How do you handle errors in Python?",
    "options": ["try...except", "error...handle", "throw...catch", "None of the above"],
    "answer": "try...except"
  },
  {
    "question": "Which module is used for working with regular expressions in Python?",
    "options": ["re", "regex", "re.match", "None of the above"],
    "answer": "re"
  },
  {
    "question": "What is the purpose of the 'yield' keyword in Python?",
    "options": ["To define a generator", "To return a value", "To define a function", "None of the above"],
    "answer": "To define a generator"
  },
  {
    "question": "What is the correct way to call a function with keyword arguments?",
    "options": ["function(arg1=value1, arg2=value2)", "function(arg1, arg2)", "function(arg1=value1)", "None of the above"],
    "answer": "function(arg1=value1, arg2=value2)"
  },
  {
    "question": "What will be the result of the following code?\n\ndef add(a, b=3):\n    return a + b\nprint(add(2))",
    "options": ["5", "2", "None", "Error"],
    "answer": "5"
  },
  {
    "question": "How do you execute a Python script from another script?",
    "options": ["import script", "run script", "exec() script", "None of the above"],
    "answer": "import script"
  },
  {
    "question": "Which of the following is used to handle exceptions in Python?",
    "options": ["try...except", "try...catch", "catch...finally", "None of the above"],
    "answer": "try...except"
  },
  {
    "question": "What is the correct syntax for defining a recursive function?",
    "options": ["def function_name(): function_name()", "function_name() = function_name()", "function_name = function_name()", "None of the above"],
    "answer": "def function_name(): function_name()"
  },
  {
    "question": "Which of the following is a built-in function in Python?",
    "options": ["print()", "input()", "abs()", "All of the above"],
    "answer": "All of the above"
  },
  {
    "question": "How do you define a function with variable arguments in Python?",
    "options": ["def function(*args)", "def function(...args)", "def function(args*)", "def function(*args, **kwargs)"],
    "answer": "def function(*args)"
  },
  {
    "question": "What will be the result of the following code?\n\ndef multiply(a, b=2):\n    return a * b\nprint(multiply(3))",
    "options": ["6", "3", "None", "Error"],
    "answer": "6"
  },
  {
    "question": "What is an exception in Python?",
    "options": ["An error that occurs during the execution of a program", "A function that returns an error", "A variable that stores error messages", "None of the above"],
    "answer": "An error that occurs during the execution of a program"
  },
  {
    "question": "Which of the following is used to handle exceptions in Python?",
    "options": ["try...except", "throw...catch", "if...else", "None of the above"],
    "answer": "try...except"
  },
  {
    "question": "What will happen if an exception is not handled in Python?",
    "options": ["The program will continue running", "The program will terminate abruptly", "The program will ask the user for input", "None of the above"],
    "answer": "The program will terminate abruptly"
  },
  {
    "question": "What is the purpose of the 'except' block?",
    "options": ["To specify the code that handles the exception", "To define a function", "To terminate the program", "To initialize variables"],
    "answer": "To specify the code that handles the exception"
  },
  {
    "question": "What does the 'finally' block do in exception handling?",
    "options": ["Executes code regardless of whether an exception occurred or not", "Executes code only if an exception occurred", "Defines a function", "None of the above"],
    "answer": "Executes code regardless of whether an exception occurred or not"
  },
  {
    "question": "Which block is optional in exception handling?",
    "options": ["finally", "except", "try", "None of the above"],
    "answer": "finally"
  },
  {
    "question": "What is the correct syntax for handling an exception in Python?",
    "options": ["try: ... except: ...", "try: ... catch: ...", "throw: ... catch: ...", "None of the above"],
    "answer": "try: ... except: ..."
  },
  {
    "question": "Which exception is raised when you try to divide by zero?",
    "options": ["ZeroDivisionError", "TypeError", "ValueError", "IndexError"],
    "answer": "ZeroDivisionError"
  },
  {
    "question": "What type of exception is raised when an invalid value is provided to a function?",
    "options": ["ValueError", "TypeError", "IndexError", "FileNotFoundError"],
    "answer": "ValueError"
  },
  {
    "question": "What will be the result of the following code?\n\ntry:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Zero Division Error')\nelse:\n    print('No error')",
    "options": ["Zero Division Error", "No error", "Error", "None of the above"],
    "answer": "Zero Division Error"
  },
  {
    "question": "Which keyword is used to raise an exception in Python?",
    "options": ["throw", "raise", "exception", "error"],
    "answer": "raise"
  },
  {
    "question": "What is the correct way to handle multiple exceptions?",
    "options": ["try...except...except", "try...except...finally", "try...except: (ExceptionType1, ExceptionType2)", "None of the above"],
    "answer": "try...except...except"
  },
  {
    "question": "Which of the following will cause an exception?",
    "options": ["1 / 0", "a = int('a')", "open('file.txt')", "All of the above"],
    "answer": "All of the above"
  },
  {
    "question": "Which exception is raised when a file is not found?",
    "options": ["FileNotFoundError", "ValueError", "IndexError", "KeyError"],
    "answer": "FileNotFoundError"
  },
  {
    "question": "Which of the following is used to get more information about an exception?",
    "options": ["e.args", "e.message", "e.traceback", "None of the above"],
    "answer": "e.args"
  },
  {
    "question": "What is the purpose of the 'else' block in exception handling?",
    "options": ["To execute code if no exception occurs", "To catch specific exceptions", "To re-raise an exception", "None of the above"],
    "answer": "To execute code if no exception occurs"
  },
  {
    "question": "Which of the following is NOT a valid exception in Python?",
    "options": ["ZeroDivisionError", "FileNotFoundError", "MemoryError", "EndOfFileError"],
    "answer": "EndOfFileError"
  },
  {
    "question": "How can you handle multiple exceptions in a single 'except' block?",
    "options": ["except (Exception1, Exception2):", "except Exception1, Exception2:", "except Exception1, Exception2 as e:", "None of the above"],
    "answer": "except (Exception1, Exception2):"
  },
  {
    "question": "What does the 'try' block do in exception handling?",
    "options": ["Contains code that might raise an exception", "Handles the exception", "Contains the code that executes if no exception occurs", "None of the above"],
    "answer": "Contains code that might raise an exception"
  },
  {
    "question": "What is the purpose of the 'raise' keyword in Python?",
    "options": ["To manually raise an exception", "To stop the program", "To handle exceptions", "None of the above"],
    "answer": "To manually raise an exception"
  },
  {
    "question": "What will the following code print?\n\ntry:\n    a = 5 / 0\nexcept ZeroDivisionError:\n    print('Divide by zero error')\nexcept:\n    print('General error')",
    "options": ["Divide by zero error", "General error", "None", "Error"],
    "answer": "Divide by zero error"
  },
  {
    "question": "Which exception is raised when trying to access an index outside the range of a list?",
    "options": ["IndexError", "KeyError", "ValueError", "TypeError"],
    "answer": "IndexError"
  },
  {
    "question": "What will be the result of the following code?\n\ntry:\n    x = 'abc'\n    y = int(x)\nexcept ValueError:\n    print('Invalid literal')\nexcept:\n    print('General error')",
    "options": ["Invalid literal", "General error", "Error", "None of the above"],
    "answer": "Invalid literal"
  },
  {
    "question": "Which exception is raised when a function is passed an object of an inappropriate type?",
    "options": ["TypeError", "ValueError", "IndexError", "AttributeError"],
    "answer": "TypeError"
  },
  {
    "question": "How do you catch an exception and store it in a variable?",
    "options": ["except Exception as e:", "except e:", "try: e except:", "None of the above"],
    "answer": "except Exception as e:"
  },
  {
    "question": "What is the purpose of the 'try' and 'except' block?",
    "options": ["To catch and handle exceptions", "To terminate the program", "To create functions", "None of the above"],
    "answer": "To catch and handle exceptions"
  },
  {
    "question": "Which exception is raised when an invalid operation is performed on a non-numeric value?",
    "options": ["ValueError", "TypeError", "ZeroDivisionError", "IndexError"],
    "answer": "ValueError"
  },
  {
    "question": "What is the syntax for raising an exception manually?",
    "options": ["raise Exception('Error message')", "raise 'Error message'", "throw Exception('Error message')", "None of the above"],
    "answer": "raise Exception('Error message')"
  },
  {
    "question": "Which of the following can be used inside an 'except' block?",
    "options": ["pass", "print", "continue", "all of the above"],
    "answer": "all of the above"
  },
  {
    "question": "Which exception is raised when a function is called with incorrect arguments?",
    "options": ["TypeError", "ValueError", "ArgumentError", "AttributeError"],
    "answer": "TypeError"
  },
  {
    "question": "What is the default behavior if an exception is not caught in a Python program?",
    "options": ["The program will terminate", "The program will display an error message", "The program will continue execution", "None of the above"],
    "answer": "The program will terminate"
  },
  {
    "question": "What will the following code print?\n\ntry:\n    a = [1, 2, 3]\n    print(a[3])\nexcept IndexError:\n    print('Index out of range')\nelse:\n    print('No error')",
    "options": ["Index out of range", "No error", "Error", "None of the above"],
    "answer": "Index out of range"
  },
  {
    "question": "Which of the following is used to catch all exceptions?",
    "options": ["except Exception as e:", "except:", "try...except", "None of the above"],
    "answer": "except:"
  },
  {
    "question": "What will be the output of the following code?\n\ntry:\n    a = 5 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')\nfinally:\n    print('Execution completed')",
    "options": ["Cannot divide by zero\nExecution completed", "Execution completed", "Cannot divide by zero", "Error"],
    "answer": "Cannot divide by zero\nExecution completed"
  },
  {
    "question": "What will happen when an exception is raised in the 'finally' block?",
    "options": ["It will be handled", "The program will terminate", "The 'finally' block will be skipped", "None of the above"],
    "answer": "The program will terminate"
  },
  {
    "question": "Which of the following will raise an exception in Python?",
    "options": ["a = 'abc'\nint(a)", "open('non_existent_file.txt')", "1 / 0", "All of the above"],
    "answer": "All of the above"
  },
  {
    "question": "What will happen when an exception is raised in the 'else' block?",
    "options": ["The exception will be caught by the 'except' block", "The program will terminate", "The 'else' block will be skipped", "None of the above"],
    "answer": "The exception will be caught by the 'except' block"
  },
  {
    "question": "Which of the following is the correct way to define a custom exception class in Python?",
    "options": ["class MyException(Exception):", "def MyException(Exception):", "MyException = Exception", "None of the above"],
    "answer": "class MyException(Exception):"
  },
  {
    "question": "Which of the following statements about exception handling is true?",
    "options": ["Exceptions can be raised manually", "Exception handling improves program performance", "Exceptions are only used in debugging", "None of the above"],
    "answer": "Exceptions can be raised manually"
  },
  {
    "question": "Which of the following is a valid exception in Python?",
    "options": ["FileNotFoundError", "DivisionByZeroError", "OutOfRangeError", "None of the above"],
    "answer": "FileNotFoundError"
  },
  {
    "question": "What is the best way to handle an exception that is not foreseen?",
    "options": ["Use a generic 'except' block", "Use specific exception types", "Do nothing", "None of the above"],
    "answer": "Use a generic 'except' block"
  },
  {
    "question": "Which method can be used to access the error message of an exception?",
    "options": ["e.args", "e.message", "e.print()", "None of the above"],
    "answer": "e.args"
  },
  
  {
    "question": "What is the function used to open a file in Python?",
    "options": ["open()", "file()", "read()", "write()"],
    "answer": "open()"
  },
  {
    "question": "What is the default mode for opening a file in Python?",
    "options": ["r", "w", "a", "rb"],
    "answer": "r"
  },
  {
    "question": "Which mode is used to open a file for reading and writing in Python?",
    "options": ["r+", "w+", "a+", "rb"],
    "answer": "r+"
  },
  {
    "question": "Which of the following modes opens a file in binary format?",
    "options": ["rb", "wb", "r", "w"],
    "answer": "rb"
  },
  {
    "question": "Which function is used to read the content of a file?",
    "options": ["read()", "write()", "open()", "close()"],
    "answer": "read()"
  },
  {
    "question": "Which function is used to write to a file?",
    "options": ["write()", "read()", "open()", "close()"],
    "answer": "write()"
  },
  {
    "question": "What does 'r' mode do when opening a file in Python?",
    "options": ["Opens a file for reading", "Opens a file for writing", "Opens a file for appending", "Opens a file for binary reading"],
    "answer": "Opens a file for reading"
  },
  {
    "question": "What will happen if you try to open a file in 'w' mode and the file doesn't exist?",
    "options": ["A new file will be created", "An error will occur", "Nothing will happen", "The file will be read"],
    "answer": "A new file will be created"
  },
  {
    "question": "What happens if you open a file in 'a' mode?",
    "options": ["The file will be opened for appending", "The file will be overwritten", "The file will be opened for reading", "None of the above"],
    "answer": "The file will be opened for appending"
  },
  {
    "question": "Which function is used to close a file in Python?",
    "options": ["close()", "end()", "finish()", "stop()"],
    "answer": "close()"
  },
  {
    "question": "Which function is used to check if a file exists in Python?",
    "options": ["os.exists()", "os.path.exists()", "file.exists()", "open.exists()"],
    "answer": "os.path.exists()"
  },
  {
    "question": "Which function is used to delete a file in Python?",
    "options": ["os.remove()", "os.delete()", "remove()", "file.remove()"],
    "answer": "os.remove()"
  },
  {
    "question": "What will happen if you open a file in 'w' mode and the file already exists?",
    "options": ["The file will be overwritten", "The file will be appended", "An error will occur", "The file will remain unchanged"],
    "answer": "The file will be overwritten"
  },
  {
    "question": "How can you read the entire content of a file into a string in Python?",
    "options": ["file.read()", "file.readlines()", "file.read(0)", "file.close()"],
    "answer": "file.read()"
  },
  {
    "question": "Which function is used to read a single line from a file in Python?",
    "options": ["readline()", "read()", "line()", "get()"],
    "answer": "readline()"
  },
  {
    "question": "How do you read all lines from a file into a list in Python?",
    "options": ["file.readlines()", "file.read()", "file.getlines()", "file.splitlines()"],
    "answer": "file.readlines()"
  },
  {
    "question": "Which of the following modes will open a file for both reading and writing?",
    "options": ["r+", "rw", "a+", "rb"],
    "answer": "r+"
  },
  {
    "question": "What happens when you open a file with 'rb' mode?",
    "options": ["The file is opened in binary format for reading", "The file is opened in text format for reading", "The file is opened in binary format for writing", "None of the above"],
    "answer": "The file is opened in binary format for reading"
  },
  {
    "question": "What does the 'a' mode do when opening a file?",
    "options": ["Opens the file for appending", "Opens the file for reading", "Opens the file for writing", "None of the above"],
    "answer": "Opens the file for appending"
  },
  {
    "question": "How do you open a file for writing only in Python?",
    "options": ["open('file.txt', 'w')", "open('file.txt', 'r')", "open('file.txt', 'a')", "open('file.txt', 'rb')"],
    "answer": "open('file.txt', 'w')"
  },
  {
    "question": "What will happen if you try to read a file opened in 'w' mode?",
    "options": ["It will raise an error", "It will return an empty string", "It will return the file content", "None of the above"],
    "answer": "It will raise an error"
  },
  {
    "question": "Which function is used to move the file pointer to a specific location in a file?",
    "options": ["seek()", "move()", "tell()", "position()"],
    "answer": "seek()"
  },
  {
    "question": "What is the function used to get the current position of the file pointer?",
    "options": ["tell()", "seek()", "position()", "getpos()"],
    "answer": "tell()"
  },
  {
    "question": "What is the result of the following code?\n\nwith open('file.txt', 'w') as f:\n    f.write('Hello')\n\nwith open('file.txt', 'r') as f:\n    print(f.read())",
    "options": ["Hello", "file.txt", "None of the above", "Error"],
    "answer": "Hello"
  },
  {
    "question": "What does the 'with' keyword do when opening a file?",
    "options": ["It ensures the file is closed automatically after the block of code is executed", "It opens the file for writing", "It opens the file for reading", "None of the above"],
    "answer": "It ensures the file is closed automatically after the block of code is executed"
  },
  {
    "question": "How can you read a file in binary mode in Python?",
    "options": ["open('file.txt', 'rb')", "open('file.txt', 'b')", "open('file.txt', 'rw')", "None of the above"],
    "answer": "open('file.txt', 'rb')"
  },
  {
    "question": "Which method is used to write a string to a file in Python?",
    "options": ["write()", "writelines()", "append()", "None of the above"],
    "answer": "write()"
  },
  {
    "question": "How do you write multiple lines to a file in Python?",
    "options": ["write()", "writelines()", "append()", "None of the above"],
    "answer": "writelines()"
  },
  {
    "question": "Which function is used to read a file in chunks?",
    "options": ["read(size)", "readline(size)", "readchunk()", "None of the above"],
    "answer": "read(size)"
  },
  {
    "question": "What will the following code do?\n\nf = open('file.txt', 'w')\nf.write('Hello, World!')\nf.close()\n\nopen('file.txt', 'r')",
    "options": ["It will write 'Hello, World!' to 'file.txt'", "It will throw an error", "It will read 'Hello, World!' from 'file.txt'", "None of the above"],
    "answer": "It will write 'Hello, World!' to 'file.txt'"
  },
  {
    "question": "What is the function used to check if a file is closed in Python?",
    "options": ["file.closed", "file.isclosed()", "file.status", "None of the above"],
    "answer": "file.closed"
  },
  {
    "question": "How can you open a file in 'read' mode and display its content in Python?",
    "options": ["open('file.txt', 'r')", "open('file.txt', 'w')", "open('file.txt', 'a')", "None of the above"],
    "answer": "open('file.txt', 'r')"
  },
  {
    "question": "What will happen if you try to read from a file opened in 'write' mode?",
    "options": ["An error will occur", "The file will be written to", "The file will be read", "None of the above"],
    "answer": "An error will occur"
  },
  {
    "question": "Which method allows you to remove whitespace characters from the beginning and end of a string read from a file?",
    "options": ["strip()", "striplines()", "remove()", "rtrim()"],
    "answer": "strip()"
  },
  {
    "question": "Which of the following statements is true about file handling in Python?",
    "options": ["A file should be closed after its use", "Files cannot be opened in 'append' mode", "Files can only be opened in text mode", "None of the above"],
    "answer": "A file should be closed after its use"
  },
  {
    "question": "Which of the following modes will allow you to read and append data to a file?",
    "options": ["a+", "r+", "w+", "rb"],
    "answer": "a+"
  },
  {
    "question": "How do you append data to a file without overwriting its current content?",
    "options": ["open('file.txt', 'a')", "open('file.txt', 'w')", "open('file.txt', 'r')", "open('file.txt', 'wb')"],
    "answer": "open('file.txt', 'a')"
  },
  {
    "question": "Which of the following methods can be used to handle the EOF (End Of File) while reading a file?",
    "options": ["read()", "readline()", "readlines()", "All of the above"],
    "answer": "All of the above"
  },
  {
    "question": "What does the following code do?\n\nwith open('file.txt', 'r') as f:\n    print(f.read())",
    "options": ["It reads the entire content of 'file.txt'", "It writes to 'file.txt'", "It appends to 'file.txt'", "None of the above"],
    "answer": "It reads the entire content of 'file.txt'"
  },
  {
    "question": "What will the following code print?\n\nwith open('file.txt', 'r') as f:\n    print(f.readline())",
    "options": ["The first line of the file", "All lines in the file", "The last line of the file", "None of the above"],
    "answer": "The first line of the file"
  },
  {
    "question": "How do you delete a file in Python?",
    "options": ["os.remove()", "os.delete()", "os.rmdir()", "os.removefile()"],
    "answer": "os.remove()"
  },
  {
    "question": "Which of the following methods will give the length of the content of a file?",
    "options": ["len(f.read())", "f.length()", "len(f)", "None of the above"],
    "answer": "len(f.read())"
  },
  {
    "question": "What is the function used to rename a file in Python?",
    "options": ["os.rename()", "os.move()", "os.change()", "os.modify()"],
    "answer": "os.rename()"
  },
  {
    "question": "What does the 'flush()' method do in file handling?",
    "options": ["Flushes the data in the file to disk", "Closes the file", "Reads the file", "None of the above"],
    "answer": "Flushes the data in the file to disk"
  },
  {
    "question": "What will the following code do?\n\nfile = open('file.txt', 'w')\nfile.write('Hello')\nfile.flush()\nfile.close()",
    "options": ["Flush the content of 'file.txt' to disk", "Write 'Hello' to 'file.txt'", "Write 'Hello' to 'file.txt' and keep it open", "None of the above"],
    "answer": "Write 'Hello' to 'file.txt' and keep it open"
  }

]

]

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
