import spacy

nlp = spacy.load("es_core_news_sm")

def detectar_tiempos_y_inconsistencias(oracion):
    doc = nlp(oracion)
    tiempos_detectados = set()
    resultados = []

    tokens = list(doc)

    for i, token in enumerate(tokens):
        # ---- PRESENTE SIMPLE ----
        if token.pos_ == "VERB" and "Tense=Pres" in token.morph and token.morph.get("Mood") in [["Ind"], ["Sub"]]:
            tiempos_detectados.add("presente")
            resultados.append(f"Presente {'subjuntivo' if 'Mood=Sub' in token.morph else 'indicativo'}: '{token.text}'")

        # ---- PRESENTE PROGRESIVO ----
        if token.lemma_ == "estar" and token.text.lower() in ["estoy", "estás", "está", "estamos", "estáis", "están"]:
            if i + 1 < len(tokens) and tokens[i + 1].tag_.startswith("VMG"):
                tiempos_detectados.add("presente")
                resultados.append(f"Presente progresivo: '{token.text} {tokens[i+1].text}'")

        # ---- PRETÉRITO PERFECTO COMPUESTO (he + participio) ----
        if token.lemma_ == "haber" and token.text.lower() in ["he", "has", "ha", "hemos", "habéis", "han"]:
            if i + 1 < len(tokens) and tokens[i + 1].tag_.startswith("VMP"):
                tiempos_detectados.add("presente")
                resultados.append(f"Pretérito perfecto compuesto: '{token.text} {tokens[i+1].text}'")

        # ---- FUTURO SIMPLE ----
        if "Tense=Fut" in token.morph:
            tiempos_detectados.add("futuro")
            resultados.append(f"Futuro simple: '{token.text}'")

        # ---- FUTURO PERIFRÁSTICO (ir a + infinitivo) ----
        if token.lemma_ == "ir" and token.pos_ == "VERB":
            a_children = [child for child in token.children if child.text.lower() == "a"]
            for a in a_children:
                inf_verbs = [child for child in a.children if child.pos_ == "VERB" and "VerbForm=Inf" in child.morph]
                if inf_verbs:
                    tiempos_detectados.add("futuro")
                    resultados.append(f"Futuro perifrástico: '{token.text} a {inf_verbs[0].text}'")

        # ---- FUTURO COMPUESTO (haber + participio en futuro) ----
        if token.lemma_ == "haber" and "Tense=Fut" in token.morph:
            participios = [child for child in token.children if "VerbForm=Part" in child.morph]
            if participios:
                tiempos_detectados.add("futuro")
                resultados.append(f"Futuro compuesto: '{token.text} {participios[0].text}'")

    # ---- CONSISTENCIA ----
    if "presente" in tiempos_detectados and "futuro" in tiempos_detectados:
        resultados.append("⚠️ Inconsistencia temporal: mezcla de presente y futuro")

    return resultados


# Ejemplos de prueba
oraciones = [
    "Estudio todos los días.",
    "Estaré en casa mañana.",
    "Voy a salir esta noche.",
    "Estoy comiendo mientras tú leerás.",
    "He terminado pero viajaré pronto.",
    "Mañana estaré enfermo, así que me quedo en casa.",
    "Cantamos mientras ellos cantarán.",
    "Ha dicho que vendrá.",
    "Digo que diré la verdad.",
]

for oracion in oraciones:
    print(f"Oración: '{oracion}'")
    resultado = detectar_tiempos_y_inconsistencias(oracion)
    if resultado:
        print("  - " + "\n  - ".join(resultado))
    else:
        print("  - No se detectó presente ni futuro")
    print("---")
