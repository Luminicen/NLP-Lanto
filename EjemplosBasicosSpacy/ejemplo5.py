import spacy
from spacy.matcher import Matcher


nlp = spacy.load("es_core_news_sm")

# Crear el matcher
matcher = Matcher(nlp.vocab)

# Definir patrones
patron_minuscula = [{"is_lower": True}]  # Busca palabras en minúscula
patron_mayuscula = [{"is_upper": True}]  # Busca palabras en mayúscula
patron_entidad = [{"ent_type": {"in": ["ORG", "PERSON"]}}]  # Busca entidades de tipo ORG o PERSON
patron_palabra_particular = [{"lower": "ejemplo"}]  # Busca la palabra "ejemplo"

# Añadir patrones al matcher
matcher.add("MINUSCULA_PATTERN", [patron_minuscula])
matcher.add("MAYUSCULA_PATTERN", [patron_mayuscula])
matcher.add("ENTIDAD_PATTERN", [patron_entidad])
matcher.add("PALABRA_PARTICULAR_PATTERN", [patron_palabra_particular])

# Texto de ejemplo
texto = "Este es un Ejemplo de Matcher en spaCy. Aquí está UNA entidad llamada USA."

# Procesar el texto con spaCy
doc = nlp(texto)

# Encontrar coincidencias con el matcher
coincidencias = matcher(doc)

# Imprimir los resultados
for match_id, start, end in coincidencias:
    print(f"Caso encontrado: {doc[start:end].text}")
