import pickle
filename = "finalized_model.sav"
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict([[6,148,72,35,0,33.6,0.627,50]])
print(result)
