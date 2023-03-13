from sklearn.feature_extraction.text import CountVectorizer
# El input va dentro de un arreglo en la variable text
text = ["I love NLP and I will learn NLP in 2month "]
#generamos un vector con la cantidad de ocurrencias de las palabras
vectorizer = CountVectorizer(ngram_range=(2,2))
#entrenamos
vectorizer.fit(text)
#pasamos el texto por el vectorizador
vector = vectorizer.transform(text)
print("Bigramas encontrados")
print(vectorizer.vocabulary_)
#print(vector.toarray())