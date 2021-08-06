import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
dataframe = pd.read_csv('essays.csv', encoding = 'latin-1')
data = dataframe[['essay_set','essay','domain1_score']].copy()

vectorizer = CountVectorizer(max_features = 10000, ngram_range=(1, 3), stop_words='english')
count_vectors = vectorizer.fit_transform(data[data['essay_set'] == 1]['essay'])
# pickle.dump(vectorizer,open('text.sav','wb'))
text_vector= vectorizer.transform(['abilities'])
text_vector = text_vector.toarray()
print(text_vector)

