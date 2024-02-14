import spacy

# Cargar el modelo de spaCy para inglés
nlp = spacy.load("es_core_news_sm")

# Ejemplo de texto (puedes usar cualquiera de los ejemplos anteriores)
texto = "En el estudio de las ciencias sociales, los investigadores examinan cómo los patrones de migración afectan las dinámicas familiares. El análisis detallado de estos patrones revela tendencias que sugieren cambios en la estructura social."

# Procesar el texto con spaCy
doc = nlp(texto)

# Extraer objetos directos
objetos_directos = []

for token in doc:
    if "obj" in token.dep_:
        objetos_directos.append(token.text)

# Imprimir los objetos directos
print("Objetos Directos encontrados:")
print(objetos_directos)
