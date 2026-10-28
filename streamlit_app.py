import streamlit as st

st.title("Math Learners")
st.write("Math Learners is a website where 7th graders can exectively learn how to study and practice 7th grade math.")
st.write("All study methods have been used by me a 7th grader and all topics are going to be based on Georgia standards.")
st.write("All of the features that are featured in this app have been coded by me. Also, all units and math knowlegde has been")
st.write("learned at Amana Academy West Atlanta, and this website will only contain knowlegde from unit one since it is the only")
st.write("unit that my 7th grade class has finished so far.")



st.title("Unit 1")

st.write("Learning Target: I can successfully show that a number and its opposite have a sum of 0 (are additive inverses) and can Describe situations in which opposite Quantities combined make 0.")
st.write("Zero Pair-A pair of numbers (like 1 and -1) that together equal zero")
st.write("Rule summary-For any number and its additive inverse they both will equal zero")
st.write("Additive inverses/Opposites-These are numbers that when added will equal zero and only zero, they are the same number but only one is positive and one is negative.")
st.write("Scenarios when adding/subtracting rational numbers:")
st.write("1.When your numbers have the same sign your sum will have the same sign as the numbers you are adding and just add the numbers normally.")
st.write("2.If the numbers have different signs you will keep the sign of the number with the greater absolute value and subtract the two numbers.")
st.write("3.When you have two subtraction signs touching each other they will turn into an addition sign and continue  the equation with the new addition sign.")
st.write("Learning Target: I can subtract rational numbers and explain why subtraction is the same as adding opposites.")
st.write("When I subtract opposites it is the same as adding opposites because the only thing you are doing is flipping the opposites and using the negative sign as your subtraction sign.")
st.write("Learning Target: I can multiply and divide rational numbers (integers, Fractions, and decimals).")
st.write("Multiplying decimals: When you multiply rational numbers you will remove the decimal points, count how many places are behind the decimal of both numbers, then multiply them both normally, and lastly add the decimal places back to finish.")
st.write("Dividing decimals: When you divide decimals you look at the first number as you dividend and your second as you divisor, you will set them up on the division house, if your divisor is a decimal you will multiply it 10/100/1,000 based how many times needed to turn it into a complete whole number, then multiply normal to finish.")
st.write("Multiply fractions: Use the butterfly method by dividing across like diagonally with numbers with the same factors to simplify then multiply across.")
st.write("Dividing fractions: Use keep, change, flip to solve fractions while dividing them first you keep the first fraction the same, then change the division to multiplication, and flip the numerator and denominator of the last fraction then multiply to finish.")
st.write("Learning Target: I can apply the same rules for signs to determine if a product or quotient is positive or negative.")
st.write("Multiplying/dividing positive and negative numbers: If both numbers are positive/negative when dividing/multiplying the answer will be positive, but when one number is positive and the other is negative in an equation then the answer will be negative.")
st.write("Converting fractions to decimals: First take the numerator as the dividend and the denominator as the divisor, divide normally, and then add a decimal point in front of your quotient.")
st.write("Converting decimals to fraction: First you look for many places that are behind the decimal point, then based on that your denominator will have as many zeros as decimal places, only add the numbers behind the decimal.")
st.write("Converting decimals to percent: You take your decimal and multiply it by 100x then and the percent sign to finish converting.")
st.write("Finding percent: when you need to find the percent you will have one out of a hundred so like 20/100 and another fraction is can be any fraction but one of the fractions will be missing a part and you will multiply the two number that are crossed to each other and then divide.")

         
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
