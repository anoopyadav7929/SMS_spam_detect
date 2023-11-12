import streamlit as st
import string, pickle, nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)

    # stemming the words 
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
        
    return " ".join(y)

st.title("Email/SMS spam classifier")
input_sms = st.text_input("Enter message")
# ...

if st.button("Predict"):
    # 1. Preprocess the message 
    transform_sms = transform_text(input_sms)

    # 2. Vectorize
    vectorized_sms = tfidf.transform([transform_sms]).toarray()  # Convert to dense array

    # 3. Predict using the model's predict_proba method
    proba = model.predict_proba(vectorized_sms)[0]

    # Threshold the probabilities (adjust the threshold as needed)
    threshold = 0.5
    result = 1 if proba[1] > threshold else 0

    # Display the result
    if result == 1:
        st.header("spam")
    else:
        st.header("not spam")



