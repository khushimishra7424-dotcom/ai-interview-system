import streamlit as st
import pdfplumber
import random
import speech_recognition as sr

st.set_page_config(page_title="AI Interview Preparation System", layout="wide")

st.title("🤖 AI Interview Preparation System")
st.write("Upload your resume and practice interview questions based on your skills")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

resume_text = ""
skills = []
questions = []

# -----------------------------
# Resume Processing
# -----------------------------

if uploaded_file is not None:

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            resume_text += page.extract_text()

    st.subheader("📄 Resume Preview")
    st.write(resume_text[:800])

# -----------------------------
# ATS Score
# -----------------------------

keywords = [
"python","machine learning","deep learning","numpy",
"pandas","scikit-learn","streamlit","sql",
"data analysis","nlp","marketing","finance","hr","html","css","javascript"
]

score = 0

for k in keywords:
    if k in resume_text.lower():
        score += 10
        skills.append(k)

if resume_text != "":
    st.subheader("📊 Resume ATS Score")
    st.progress(min(score,100))
    st.write(f"ATS Score: {min(score,100)}/100")

# -----------------------------
# Detected Skills
# -----------------------------

if skills:
    st.subheader("🧠 Detected Skills")
    st.write(list(set(skills)))

# -----------------------------
# Question Bank
# -----------------------------

question_bank = {

"python":[
"What is Python?",
"Explain list vs tuple",
"What are Python libraries?"
],

"machine learning":[
"What is supervised learning?",
"Explain overfitting vs underfitting",
"What is bias vs variance?"
],

"data analysis":[
"What is data analysis?",
"What is the role of Excel in data analysis?",
"Explain data cleaning"
],

"marketing":[
"What is digital marketing?",
"Explain SEO",
"What is social media marketing?"
],

"finance":[
"What is financial analysis?",
"Explain ROI",
"What is risk management?"
],

"hr":[
"What is recruitment process?",
"Explain employee engagement",
"What is HR management?"
],

"html":[
"What is HTML?",
"What are HTML tags?"
],

"css":[
"What is CSS?",
"What is responsive design?"
],

"javascript":[
"What is JavaScript?",
"What is DOM?"
]

}

# -----------------------------
# Generate Questions
# -----------------------------

if uploaded_file is not None:

    st.subheader("🎯 Interview Questions Based on Your Skills")

    for skill in skills:

        skill = skill.lower()

        if skill in question_bank:
            questions.extend(question_bank[skill])

    if len(questions) == 0:

        questions = [
        "Tell me about yourself",
        "What are your strengths?",
        "Why should we hire you?",
        "Where do you see yourself in 5 years?",
        "What motivates you?"
        ]

    questions = random.sample(questions, min(5,len(questions)))

    answers = []

    for i,q in enumerate(questions):

        st.write(f"Question {i+1}: {q}")

        ans = st.text_area("Type your answer", key=f"ans_{i}")

        answers.append(ans)

# -----------------------------
# Voice Interview
# -----------------------------

st.subheader("🎤 Voice Interview (Optional)")

if st.button("Start Voice Answer"):

    r = sr.Recognizer()

    with sr.Microphone() as source:

        st.write("Speak now...")

        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            st.write("You said:", text)

        except:
            st.write("Voice not detected")

# -----------------------------
# Evaluation
# -----------------------------

if uploaded_file is not None:

    if st.button("Submit Interview"):

        st.subheader("📊 AI Feedback")

        score = 0

        for i,ans in enumerate(answers):

            words = len(ans.split())

            if words > 40:
                feedback = "✅ Strong Answer"
                score += 1

            elif words > 15:
                feedback = "⚠️ Good but add more explanation"

            else:
                feedback = "❌ Too short"

            st.write(f"Question {i+1}: {feedback}")

        accuracy = (score/5)*100

        st.subheader(f"🎯 Interview Accuracy: {accuracy}%")

        if accuracy > 80:
            st.success("Excellent Interview Performance 🚀")

        elif accuracy > 50:
            st.warning("Good but practice more")

        else:
            st.error("You need more preparation")