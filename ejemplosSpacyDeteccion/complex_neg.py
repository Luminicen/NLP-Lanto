import spacy

nlp = spacy.load("es_core_news_sm")

negaciones = {"no", "nunca", "jamás", "nadie", "ninguno", "nada", "ni"}

def detectar_fraseo_negativo_complejo(oracion):
    doc = nlp(oracion.lower())
    neg_count = sum(1 for token in doc if token.text in negaciones)
    
    if neg_count > 1:
        return True, [token.text for token in doc if token.text in negaciones]
    return False, []

# Ejemplos
oraciones = [
    "No creo que no venga.",
    "No es raro no sentirse bien en esta situación.",
    "No diría que no estuvo mal.",
    "Nunca nadie me dijo nada.",
    "No me gusta el café."
]

for oracion in oraciones:
    complejo, negs = detectar_fraseo_negativo_complejo(oracion)
    print(f"'{oracion}' → {'⚠️ Complejo' if complejo else '✔️ Claro'} | Negaciones: {negs}")
