import spacy

# Cargar el modelo para español
nlp = spacy.load("es_core_news_sm")

# Texto de ejemplo
texto = "El gato está durmiendo pacíficamente en la alfombra."

# Procesar el texto con spaCy
doc = nlp(texto)

# Imprimir el POS tagging de cada palabra
for token in doc:
    print(f"{token.text}: {token.pos_}")
