from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
import json
import pandas as pd
from gensim import corpora
import os
# El input debe estar en formato array y se lo deben pasar a la funcion identificarTopicos. Ej identificarTopicos(input)
def clean(doc,stop,exclude,lemma):
    #limpieza de palabras o caracteres que no suman informacion
    stop_free = " ".join([i for i in doc.lower().split()if i not in stop])
    punc_free = "".join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized
def format_topics_sentences(ldamodel,corpus):
    # Init output
    sent_topics_df = pd.DataFrame()
    # Get main topic in each document
    for i, row in enumerate(ldamodel[corpus]):
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = ", ".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num), round(prop_topic,4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']
    return sent_topics_df
def identificarTopicos(doc_complete) :
    stop = set(stopwords.words('english'))
    #stop = set(stopwords.words('spanish')) PARA ANALISAR TEXTO EN ESPAÑOL DESCOMENTAR ESTA Y COMENTAR LA DE ARRIBA
    exclude = set(string.punctuation)
    lemma = WordNetLemmatizer()
    doc_clean = [clean(doc,stop,exclude,lemma).split() for doc in doc_complete]
    #preprocesamiento terminado
    #creo un diccionario de terminos unicos (no se repten)
    dictionary = corpora.Dictionary(doc_clean)
    #convierto la lista en una matrix doc - termino
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    # Creo el LDA
    Lda = gensim.models.ldamodel.LdaModel
    # Entreno el modelo
    #Establesco el numero de topicos
    ldamodel = Lda(doc_term_matrix, num_topics=3, id2word =
    dictionary, passes=50)
    topicos = ldamodel.show_topics(formatted=False)
    print("-----------------Topicos encontrados con sus '%' de valoracion y peso en el documento-------------- ")
    print(topicos[0][1])
    result = format_topics_sentences(ldamodel,doc_term_matrix)
    print("----------------- Elije las mas repecentativas, aquellas de mayor numero de valoracion -------------- ")
    print(result)
    return result
import json
datos = None
# Define el directorio y el nombre del archivo
directorio = './'  # Puedes cambiar esto al directorio donde está tu archivo
nombre_archivo = 'Githubissues.json'

# Construye la ruta completa del archivo y la convierte en absoluta
ruta_archivo = os.path.join(directorio, nombre_archivo)
ruta_absoluta = os.path.abspath(ruta_archivo)
try:
    with open(ruta_absoluta, 'r') as archivo:
        datos = json.load(archivo)
except FileNotFoundError:
    print("El archivo no se encontró.")
except json.JSONDecodeError:
    print("Error al decodificar el archivo JSON.")
doc = []
for i in range (10):
    doc.append(datos[i]["body"])

print(doc)
doc_complete = doc
identificarTopicos(doc_complete)