import spacy
from spacy.matcher import Matcher

# Cargar el modelo de spaCy para inglés
nlp = spacy.load("es_core_news_sm")

# Crear el matcher
matcher = Matcher(nlp.vocab)

# Definir el patrón con el operador "*"
patron_sustantivo_adjetivo = [{"POS": "NOUN"}, {"POS": "ADJ", "OP": "*"}]

# Añadir el patrón al matcher
matcher.add("SUSTANTIVO_ADJETIVO", [patron_sustantivo_adjetivo])

# Texto de ejemplo
texto = "El perro rápido corre velozmente por el hermoso parque."

# Procesar el texto con spaCy
doc = nlp(texto)

# Encontrar coincidencias con el matcher
coincidencias = matcher(doc)

# Imprimir los resultados
for match_id, start, end in coincidencias:
    print(f"Caso encontrado: {doc[start:end].text}")
