# NLP-Viva-QA-Generator-
Built an NLP-based system to automatically generate viva questions and answers from input text using preprocessing, keyword extraction, and rule-based techniques for smart exam preparation.

# 📚 Automated Viva Question & Answer Generator using NLP

## 🔍 Overview
This project is an NLP-based application that automatically generates viva questions and answers from lecture notes or PDF documents. It helps students prepare for oral exams by converting study material into structured Q&A format.

---

## 🚀 Features
- 📄 Accepts **Text and PDF input**
- ❓ Generates **viva questions automatically**
- 💡 Provides **relevant answers**
- 🔢 Allows user to select **number of questions**
- 🌐 Simple **web interface using Streamlit**
- ⚡ Fast and lightweight (no heavy AI models required)

---

## 🛠️ Technologies Used
- **Python** – Core programming language  
- **NLTK** – Text processing and tokenization  
- **Scikit-learn** – TF-IDF and cosine similarity  
- **Streamlit** – Web application UI  
- **PyPDF2** – PDF text extraction  

---

## ⚙️ How It Works

1. User inputs lecture notes or uploads a PDF  
2. Text is split into sentences using NLP  
3. Questions are generated using rule-based patterns  
4. TF-IDF vectorization converts text into numerical form  
5. Cosine similarity finds the most relevant answer  
6. Questions and answers are displayed on the screen  

---

## 🧪 Example

### Input:
Deep learning is a subset of machine learning.
It is used in computer vision.


### Output:
Q1: What is deep learning?
A1: Deep learning is a subset of machine learning.

Q2: Where is deep learning used?
A2: It is used in computer vision.


---

## ▶️ How to Run

### Step 1: Navigate to project folder
cd NLP_project

### Step 2: Activate virtual environment
.venv\Scripts\activate

### Step 3: Install dependencies
pip install streamlit nltk scikit-learn PyPDF2

### Step 4: Run application
python -m streamlit run app.py

### Step 5: Open in browser
http://localhost:8501


---

## 📌 Advantages
- Easy to use  
- Works offline  
- Saves time for students  
- Lightweight and fast  

---

## ⚠️ Limitations
- Limited understanding of context  
- Rule-based question generation  
- Accuracy depends on input quality  

---

## 🔮 Future Enhancements
- Integration with deep learning models (BERT, T5)  
- Improved grammar and question quality  
- MCQ generation  
- Voice input support  

---

## 👨‍💻 Contributors
- Paras Vishwakarma
- Rushikesh Jadhav  
- Shivtej Karle 
- Yash Marne  
- Mithali Thakur
   

---

## 📚 Use Case
This project can be used in:
- E-learning platforms  
- Viva preparation tools  
- Academic assistance systems  

---

## ⭐ Conclusion
This system demonstrates how NLP techniques can be used to automate question-answer generation, making learning faster and more efficient.

