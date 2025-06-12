import spacy

nlp = spacy.load("es_core_news_sm")

def detectar_perifrasis_modales(oracion):
    doc = nlp(oracion)
    resultados = []

    for i, token in enumerate(doc):
        # Casos como "Tener que", "Haber de", "Haber que", etc.
        if token.lemma_ in ["tener", "haber", "deber", "poder", "venir", "estar"]:
            siguiente = doc[i + 1] if i + 1 < len(doc) else None
            if siguiente and siguiente.text.lower() in {"que", "de", "para", "a", "por"}:
                resultados.append(f"{token.text} {siguiente.text}")
            elif token.lemma_ in ["deber", "poder"] and token.pos_ == "AUX":
                resultados.append(f"{token.text}")
        
        # Casos como "Hay que"
        if token.text.lower() == "hay":
            siguiente = doc[i + 1] if i + 1 < len(doc) else None
            if siguiente and siguiente.text.lower() == "que":
                resultados.append(f"{token.text} {siguiente.text}")
        
        # Casos como "Es necesario que"
        if token.text.lower() == "es":
            for child in token.children:
                if child.pos_ == "ADJ" and child.text.lower() in {"necesario", "urgente", "importante", "claro"}:
                    resultados.append(f"{token.text} {child.text}")
    
    return resultados

# Lista de oraciones para prueba
oraciones = [
    "Tienes que venir ahora.",
    "Hay que estudiar para el examen.",
    "Debes estudiar más.",
    "Debe de haber un error.",
    "Puedes comer lo que quieras.",
    "Viene a costar veinte euros.",
    "Es urgente que lo hagas.",
    "Está claro que no vendrá.",
    "Tengo una idea.",
    "Corremos todos los días."
]

# Ejecutar la detección
resultados_deteccion = []
for oracion in oraciones:
    resultados = detectar_perifrasis_modales(oracion)
    resultados_deteccion.append((oracion, resultados))

resultados_deteccion
