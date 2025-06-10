import spacy

nlp = spacy.load("es_core_news_sm")

def detectar_fraseo_negativo_complejo_por_pos(oracion):
    doc = nlp(oracion)
    negaciones = []

    for token in doc:
        # Detectamos palabras de negación como adverbios (ADV) y pronombres indefinidos negativos
        if token.pos_ in {"ADV", "PRON", "DET"} and token.dep_ == "neg":
            negaciones.append(token.text)
        
        # También podemos considerar adverbios de negación frecuentes por POS
        if token.pos_ == "ADV" and token.lemma_ in {"no", "nunca", "jamás"}:
            negaciones.append(token.text)

    return negaciones if len(negaciones) > 1 else []

# Ejemplos
oraciones = [
    "No creo que no venga.",
    "No es raro no sentirse bien en esta situación.",
    "Nunca nadie me dijo nada.",
    "No diría que no estuvo mal",
    "No tengo nada que decir."
]

for oracion in oraciones:
    resultado = detectar_fraseo_negativo_complejo_por_pos(oracion)
    if resultado:
        print(f"⚠️ Complejo → '{oracion}' | Negaciones detectadas: {resultado}")
    else:
        print(f"✔️ Claro → '{oracion}'")
