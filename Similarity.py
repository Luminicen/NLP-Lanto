from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
documents = (
"I like NLP",
"I am exploring NLP",
"I am a beginner in NLP",
"I want to learn NLP",
"I like advanced NLP"
)
#Hacemos  feature engineering
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
#print(tfidf_matrix.shape)
#hacemos el computo de similaridad
print("EJEMPLO 1")
print(cosine_similarity(tfidf_matrix[0:1],tfidf_matrix))
#cuanto mas alto sea el numerito mas similar es.
#ejemplos
f1 = open('./Datos/Agricultura.txt',"r",encoding='utf-8')
doc = f1.read()
f1.close()
f2 = open('./Datos/Tomato.txt',"r",encoding='utf-8')
doc2 = f2.read()
f2.close()
f3 = open('./Datos/TomatoCherry.txt',"r",encoding='utf-8')
doc3 = f3.read()
f3.close()
documentos = [doc2,doc,doc3]
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documentos)
print("EJEMPLO 2")
print(cosine_similarity(tfidf_matrix[0:1],tfidf_matrix))
print("EJEMPLO EN ESPAÑOL")
documentos = ["Me interesa aprender NLP",
              "Estoy explorando NLP",
              "Mi hermana conoce en profundidad algunos temas relacionados a NLP",
              "NLP es imperativo para requerimientos",
              "Necesito aprender NLP mas avanzado"
              ]
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documentos)
print(cosine_similarity(tfidf_matrix[0:1],tfidf_matrix))