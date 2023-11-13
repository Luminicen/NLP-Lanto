from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
Text = ["The quick brown fox jumped over the lazy dog.",
"The dog.",
"The fox"]
#Create the transform
# Crear una instancia del transformador CountVectorizer para calcular TF
tf_vectorizer = CountVectorizer()
tf_vectorizer.fit(Text)

# Calcular los valores de TF para los documentos
tf_matrix = tf_vectorizer.transform(Text)

vectorizer = TfidfVectorizer()
#Tokenize and build vocab
vectorizer.fit(Text)
#Summarize
feature_names = vectorizer.get_feature_names_out()
# Calcular los valores TF-IDF para los documentos de entrenamiento
tfidf_matrix = vectorizer.transform(Text)
# Extraer los valores de TF-IDF en una matriz densa
tfidf_dense = tfidf_matrix.toarray()
print("-----------------TF DEL PRIMER DOCUMENTO---------------------")
for i, word in enumerate(feature_names):
    tf_score = tf_matrix[0, i]  # Muestra los valores de TF para el primer documento
    print(f"{word}: {tf_score}")
print("-----------------TF DEL SEGUNDO DOCUMENTO---------------------")
for i, word in enumerate(feature_names):
    tf_score = tf_matrix[1, i]  # Muestra los valores de TF para el segundo documento
    print(f"{word}: {tf_score}")
print("-----------------TF DEL TERCER DOCUMENTO---------------------")
for i, word in enumerate(feature_names):
    tf_score = tf_matrix[2, i]  # Muestra los valores de TF para el tercer documento
    print(f"{word}: {tf_score}")
print("-----------------IDF--------------------")
for word, idf_value in zip(feature_names, vectorizer.idf_):
    print(f'{word}: {idf_value}')
print("-----------------TF-IDF-----------------")
for i, document in enumerate(Text):
    print(f"Documento {i + 1}:")
    for j, word in enumerate(feature_names):
        tfidf_score = tfidf_dense[i][j]
        print(f"{word}: {tfidf_score}")