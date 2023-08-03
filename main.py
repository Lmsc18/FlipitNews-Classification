import pickle
import nltk 
import re 
import numpy as np
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from fastapi import FastAPI


app=FastAPI()
lm=WordNetLemmatizer()
stop_words=set(stopwords.words('english'))

def clean_text(text):
    text=re.sub('[%s]' % re.escape(string.punctuation), '' , text)
    text=re.sub(r"\d+", "", text)
    text=text.lower()
    words=nltk.word_tokenize(text)
    words=[lm.lemmatize(x) for x in words]
    words=" ".join([x if x not in stop_words else'' for x in words])
    return words

mod=open('./nb_model.pkl','rb')
model=pickle.load(mod)

vct=open('./tfidf.pkl','rb')
vect=pickle.load(vct)

enc=open('./encoder.pkl','rb')
encoder=pickle.load(enc)

@app.get("/")
def read_root():
    return {"message": "Hello World"}



@app.post("/predict")
def prediction(article :str):
    text=clean_text(article)
    vt=vect.transform([text]).toarray()
    pred=model.predict(vt)
    ans=encoder.inverse_transform(pred)
    return ans.tolist()
    