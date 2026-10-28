import streamlit as st

st.title("Math Learners")
st.write("Math Learners is a website where 7th graders can exectively learn how to study and practice 7th grade math.")
st.write("All study methods have been used by me a 7th grader and all topics are going to be based on Georgia standards.")
st.write("All of the features that are featured in this app have been coded by me. Also, all units and math knowlegde has been")
st.write("learned at Amana Academy West Atlanta")


st.title("Math Calculator")

operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

rounded_result = round(result, 3)

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
