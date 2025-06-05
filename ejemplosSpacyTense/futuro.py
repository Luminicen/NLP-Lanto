import spacy

nlp = spacy.load("es_core_news_sm")

def detectar_futuro(oracion):
    doc = nlp(oracion)
    resultados = []
    
    for token in doc:
        # Futuro simple
        if "Tense=Fut" in token.morph and token.pos_ == "VERB":
            resultados.append(f"Futuro simple: '{token.text}'")
        
        # Condicional
        if "Mood=Cnd" in token.morph and token.pos_ == "VERB":
            resultados.append(f"Condicional (futuro hipotético): '{token.text}'")
        
        # Futuro compuesto
        if token.lemma_ == "haber" and "Tense=Fut" in token.morph:
            participios = [child for child in token.children if "VerbForm=Part" in child.morph]
            if participios:
                resultados.append(f"Futuro compuesto: '{token.text} {participios[0].text}'")

    # Detección de 'ir a + infinitivo' como secuencia
    for i in range(len(doc) - 2):
        if doc[i].lemma_ == "ir" and doc[i+1].text == "a" and doc[i+2].pos_ == "VERB" and "VerbForm=Inf" in doc[i+2].morph:
            resultados.append(f"Futuro perifrástico: '{doc[i].text} a {doc[i+2].text}'")

    return resultados


# Ejemplos
oraciones = [
    "Mañana comeré sushi.",
    "Voy a estudiar español.",
    "Para diciembre habré terminado el proyecto.",
    "Ellos viajarán a Japón.",
    "Está lloviendo fuerte.",
    "Deberías venir mañana",
    "Iba a comprar pan"
]

for oracion in oraciones:
    print(f"Oración: '{oracion}'")
    resultado = detectar_futuro(oracion)
    if resultado:
        print("  - " + "\n  - ".join(resultado))
    else:
        print("  - No se detectó futuro")
    print("---")
