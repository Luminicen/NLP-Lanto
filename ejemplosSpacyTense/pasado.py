import spacy

# Cargamos el modelo de spaCy para español
nlp = spacy.load("es_core_news_sm")

def detectar_pasado(oracion):
    """
    Detecta distintos tiempos verbales pasados en una oración en español.
    Devuelve una lista de descripciones del tiempo y la forma encontrada.
    """
    doc = nlp(oracion)
    resultados = []

    # Primero recorremos token a token para tiempos simples y compuestos
    for i, token in enumerate(doc):
        # 1) Pretérito perfecto simple (comí, viajé, fui, cené...)
        if token.pos_ == "VERB" and "Tense=Past" in token.morph and "VerbForm=Fin" in token.morph:
            resultados.append(f"Pretérito perfecto simple: '{token.text}'")

        # 2) Pretérito imperfecto (comía, jugaba, era, iba...)
        elif token.pos_ == "VERB" and "Tense=Imp" in token.morph and "VerbForm=Fin" in token.morph:
            resultados.append(f"Pretérito imperfecto: '{token.text}'")

        # 3) Pretérito perfecto compuesto (he comido, has dicho, ha salido...)
        #     Se detecta como: token = "he"/"has"/"ha"/"hemos"/... (auxiliar "haber" en presente)
        #     y siguiente token en doc es participio
        if token.lemma_ == "haber" and "Tense=Pres" in token.morph:
            if i + 1 < len(doc):
                siguiente = doc[i + 1]
                if siguiente.pos_ == "VERB" and "VerbForm=Part" in siguiente.morph:
                    resultados.append(f"Pretérito perfecto compuesto: '{token.text} {siguiente.text}'")

        # 4) Pretérito pluscuamperfecto (había comido, habías salido...)
        #     token = "había"/"habías"/"habíamos"/... (haber en imperfecto) + siguiente participio
        if token.lemma_ == "haber" and "Tense=Imp" in token.morph:
            if i + 1 < len(doc):
                siguiente = doc[i + 1]
                if siguiente.pos_ == "VERB" and "VerbForm=Part" in siguiente.morph:
                    resultados.append(f"Pretérito pluscuamperfecto: '{token.text} {siguiente.text}'")

        # 5) Pretérito anterior (hube comido, hubiste salido...) — poco común
        #     token = "hube"/"hubiste"/... (haber en pretérito) + siguiente participio
        if token.lemma_ == "haber" and "Tense=Past" in token.morph:
            if i + 1 < len(doc):
                siguiente = doc[i + 1]
                if siguiente.pos_ == "VERB" and "VerbForm=Part" in siguiente.morph:
                    resultados.append(f"Pretérito anterior: '{token.text} {siguiente.text}'")

    # 6) Pasado progresivo (estaba comiendo, estaba durmiendo...)
    #    Buscamos secuencias token = "estar" en pretérito/imperfecto + siguiente gerundio
    for i in range(len(doc) - 1):
        tok = doc[i]
        siguiente = doc[i + 1]
        if tok.lemma_ == "estar" and "Tense=Imp" in tok.morph:
            if siguiente.pos_ == "VERB" and "VerbForm=Ger" in siguiente.morph:
                resultados.append(f"Pasado progresivo: '{tok.text} {siguiente.text}'")

    return resultados


# --- Ejemplos de prueba ---
oraciones = [
    "Ayer comí pizza.",
    "Cuando era niño, jugaba mucho.",
    "He visitado Madrid este año.",
    "Había leído ese libro antes.",
    "Hube terminado cuando llegaste.",
    "Estaba cocinando cuando llamaste.",
    "Fui al cine y después cené.",
    "Iba caminando por el parque.",
    "Has dicho la verdad.",
    "Habíamos salido temprano.",
    "Hubo terminado antes de las siete."
]

for oracion in oraciones:
    print(f"Oración: '{oracion}'")
    resultado = detectar_pasado(oracion)
    if resultado:
        print("  - " + "\n  - ".join(resultado))
    else:
        print("  - No se detectó pasado")
    print("---")
