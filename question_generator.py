import nltk
nltk.download('punkt')

def generate_questions(text, num_questions=5):
    sentences = nltk.sent_tokenize(text)
    questions = []

    for sent in sentences:
        sent = sent.strip()

        if len(sent) > 20:

            # Basic patterns
            if " is " in sent:
                subject = sent.split(" is ")[0]
                q = f"What is {subject}?"

            elif " are " in sent:
                subject = sent.split(" are ")[0]
                q = f"What are {subject}?"

            elif " consists of " in sent:
                subject = sent.split(" consists of ")[0]
                q = f"What does {subject} consist of?"

            elif " uses " in sent:
                subject = sent.split(" uses ")[0]
                q = f"What does {subject} use?"

            else:
                q = f"Explain: {sent[:40]}?"

            questions.append(q)

            if len(questions) >= num_questions:
                break

    return questions