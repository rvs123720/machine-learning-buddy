
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-flash-latest")

# Page Configuration
st.set_page_config(
    page_title="Machine Learning Buddy",
    page_icon="🤖"
)

st.title("🤖 Machine Learning Buddy")
st.write("Learn Machine Learning concepts with the help of Gemini AI!")

# Topic Input
topic = st.text_input(
    "Enter a Machine Learning Topic",
    placeholder="Example: Supervised Learning, Decision Trees, Neural Networks"
)

# Activity Selection
option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything",
        "Evaluate My Answer"
    ]
)

# Student answer (only for evaluation)
student_answer = ""

if option == "Evaluate My Answer":
    student_answer = st.text_area(
        "Enter your answer here"
    )

# Generate Button
if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a Machine Learning topic.")

    else:

        if option == "Explain Concept":
            prompt = f"""
            Explain the Machine Learning topic '{topic}' in simple language for a beginner.

            Include:
            - Definition
            - Why it is important
            - Simple explanation
            - Key points
            """

        elif option == "Real-Life Example":
            prompt = f"""
            Give one simple real-life example of the Machine Learning topic '{topic}'.
            Explain why it is a good example.
            """

        elif option == "Generate Quiz":
            prompt = f"""
            Create 5 multiple-choice questions on '{topic}'.

            For each question provide:
            - Four options (A, B, C, D)
            - Correct answer
            - One-line explanation
            """

        elif option == "Ask Anything":
            prompt = topic

        else:
            prompt = f"""
            You are a Machine Learning teacher.

            Topic:
            {topic}

            Student's Answer:
            {student_answer}

            Evaluate the answer.

            Mention:
            - What is correct
            - What is incorrect
            - Suggestions for improvement
            - Score out of 10
            """

        with st.spinner("Generating response..."):
            response = model.generate_content(prompt)

        st.success("Done!")
        st.write(response.text)
