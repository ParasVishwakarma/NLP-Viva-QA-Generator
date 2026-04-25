import streamlit as st
from pdf_reader import extract_text_from_pdf
from question_generator import generate_questions
from answer_generator import generate_answers

st.title("Automated Viva Question & Answer Generator")

option = st.radio("Choose Input Type", ["Text", "PDF"])

num_q = st.slider("Number of Questions", 1, 50, 5)

text = ""

if option == "Text":
    text = st.text_area("Enter Notes Here", height=200)

elif option == "PDF":
    file = st.file_uploader("Upload PDF", type="pdf")
    if file:
        text = extract_text_from_pdf(file)

if st.button("Generate"):

    if text:
        questions = generate_questions(text, num_q)
        answers = generate_answers(text, questions)

        st.subheader("📌 Generated Q&A")

        for i, q in enumerate(questions):
            st.write(f"Q{i+1}: {q}")
            st.write(f"A{i+1}: {answers.get(q, 'Not found')}")
            st.write("---")