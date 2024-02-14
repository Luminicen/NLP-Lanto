import spacy
from spacy.matcher import Matcher

# Cargar el modelo para español
nlp = spacy.load("es_core_news_sm")

# Crear el matcher
matcher = Matcher(nlp.vocab)

# Definir el patrón: DET seguido de NOUN
patron = [{"POS": "DET"}, {"POS": "NOUN"}]

# Añadir el patrón al matcher
matcher.add("DET_NOUN_PATTERN", [patron])

# Texto de ejemplo
texto = "El cuadro esta muy bonito. Cada vez que miro el horizonte me trae recuerdos. Limpio el cuadro. La casa esta de maravilla"

# Procesar el texto con spaCy
doc = nlp(texto)

# Encontrar coincidencias con el matcher
coincidencias = matcher(doc)

# Imprimir los resultados
for match_id, start, end in coincidencias:
    print(f"Caso encontrado: {doc[start:end].text}")
