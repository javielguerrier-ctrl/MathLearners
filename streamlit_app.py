import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

st.title("Simple Python Calculator")

# Dropdown for operations
operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Inputs
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Calculation logic
if st.button("Calculate"):
    if operation == "Add":
        st.success(f"Result: {num1 + num2}")
    elif operation == "Subtract":
        st.success(f"Result: {num1 - num2}")
    elif operation == "Multiply":
        st.success(f"Result: {num1 * num2}")
    elif operation == "Divide":
        if num2 == 0:
            st.error("Error! Division by zero is not allowed.")
        else:
            st.success(f"Result: {num1 / num2}")
