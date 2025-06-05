import spacy

nlp = spacy.load("es_core_news_sm")

def detectar_tiempos(oracion):
    doc = nlp(oracion)
    resultados = []

    tokens = list(doc)

    for i, token in enumerate(tokens):
        # PRESENTE SIMPLE
        if token.pos_ == "VERB" and "Tense=Pres" in token.morph and token.morph.get("Mood") in [["Ind"], ["Sub"]]:
            resultados.append(f"Presente {'subjuntivo' if 'Mood=Sub' in token.morph else 'indicativo'}: '{token.text}'")

        # PRESENTE PROGRESIVO: estoy + gerundio
        elif token.lemma_ == "estar" and token.text.lower() in ["estoy", "estás", "está", "estamos", "estáis", "están"]:
            if i + 1 < len(tokens) and tokens[i + 1].tag_.startswith("VMG"):
                resultados.append(f"Presente progresivo: '{token.text} {tokens[i+1].text}'")

        # PRETÉRITO PERFECTO COMPUESTO (presente perfecto): he + participio
        elif token.lemma_ == "haber" and token.text.lower() in ["he", "has", "ha", "hemos", "habéis", "han"]:
            if i + 1 < len(tokens) and tokens[i + 1].tag_.startswith("VMP"):
                resultados.append(f"Pretérito perfecto compuesto: '{token.text} {tokens[i+1].text}'")

    return resultados


# Ejemplos de prueba
oraciones = [
    "Estudio todos los días.",
    "Estoy comiendo ahora.",
    "He terminado mi tarea.",
    "Ojalá venga pronto.",
    "Estás leyendo un libro.",
    "Han dicho la verdad.",
    "Cantamos en el coro.",
    "Sea lo que sea, estaré contigo.",
    "Va al gimnasio cada semana."
]

for oracion in oraciones:
    print(f"Oración: '{oracion}'")
    resultado = detectar_tiempos(oracion)
    if resultado:
        print("  - " + "\n  - ".join(resultado))
    else:
        print("  - No se detectó presente")
    print("---")
