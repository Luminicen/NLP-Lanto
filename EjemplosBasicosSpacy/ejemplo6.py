import spacy
from spacy.matcher import Matcher

# Cargar el modelo de spaCy para español
nlp = spacy.load("es_core_news_sm")

# Crear el matcher
matcher = Matcher(nlp.vocab)

# Imagina un patrón que te gustaría buscar
# Ejemplo: Patrón para encontrar fechas en formato dd/mm/yyyy
patron_imaginado = [{"SHAPE": "dd/dd/dddd"}]

# Añadir el patrón al matcher
matcher.add("PATRON_IMAGINADO", [patron_imaginado])

# Texto para analizar
texto = "El informe del 12/05/2023 muestra un aumento en las ventas. La próxima reunión será el 20/06/2023."

# Procesar el texto con spaCy
doc = nlp(texto)

# Encontrar coincidencias con el matcher
coincidencias = matcher(doc)

# Imprimir los resultados
print("Coincidencias encontradas:")
for match_id, start, end in coincidencias:
    print(f"{matcher.vocab.strings[match_id]}: {doc[start:end].text}")
