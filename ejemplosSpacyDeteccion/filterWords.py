import spacy

nlp = spacy.load("es_core_news_sm")

def detectar_filter_words_pos_dep(texto):
    doc = nlp(texto)
    resultados = []

    for token in doc:
        # Verbo en primera persona singular (por morfología)
        if token.pos_ == "VERB" and "Person=1" in token.morph and "Number=Sing" in token.morph:
            # Si tiene dependencia de raíz o complement clause
            if token.dep_ in {"ROOT", "ccomp"}:
                resultados.append((token.text, token.pos_, token.dep_, token.sent.text))
    
    return resultados

# Ejemplo
oraciones = [
    "Creo que es una buena idea.",
    "Pienso que deberíamos irnos.",
    "Él cree que tiene razón.",  # tercera persona, debería no detectar
    "Sentí que me miraban.",
    "Nos parece bien la propuesta.",  # primera persona del plural
]

for oracion in oraciones:
    print(f"Oración: {oracion}")
    encontrados = detectar_filter_words_pos_dep(oracion)
    if encontrados:
        for palabra, pos, dep, sent in encontrados:
            print(f"  - Filter word detectada: '{palabra}' (POS={pos}, DEP={dep})")
    else:
        print("  - No se detectaron filter words (por POS/DEP)")
