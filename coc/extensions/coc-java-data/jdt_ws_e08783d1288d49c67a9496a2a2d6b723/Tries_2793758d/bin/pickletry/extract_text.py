import pickle
vectorizer = pickle.load(open('text.sav','rb'))
text_vector = vectorizer.transform(['abilities'])
text_vector = text_vector.toarray()
print(text_vector)
