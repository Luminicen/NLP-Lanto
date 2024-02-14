import spacy
from spacy import displacy

# Cargar el modelo de spaCy para español
nlp_es = spacy.load("es_core_news_sm")

# Texto traducido al español
texto_espanol = "Apple está considerando la compra de una startup en el Reino Unido por $1 mil millones"

# Procesar el texto en español con spaCy
doc_espanol = nlp_es(texto_espanol)

displacy.serve(doc_espanol)
