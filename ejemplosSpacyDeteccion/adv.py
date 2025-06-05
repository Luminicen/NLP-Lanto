import spacy

nlp = spacy.load("es_core_news_sm")

def detectar_adverbios(oracion):
    doc = nlp(oracion)
    adverbios = [(token.text, token.pos_, token.dep_) for token in doc if token.pos_ == "ADV"]
    return adverbios

# Lista de oraciones para probar
oraciones = [
    "Rápidamente salió corriendo, pero luego volvió tranquilamente.",
    "Hoy comimos muy temprano.",
    "Casi nunca llega tarde.",
    "Aquí empieza la historia.",
    "Seguramente lo lograrás.",
    "A veces me siento confundido.",
    "Allí estaba esperando con paciencia.",
    "Jamás lo había visto tan feliz.",
    "Quizás mañana tengamos suerte.",
    "Realmente aprecio tu ayuda."
]

# Evaluar cada oración
for oracion in oraciones:
    print(f"Oración: '{oracion}'")
    adverbios = detectar_adverbios(oracion)
    if adverbios:
        for texto, pos, dep in adverbios:
            print(f"  - '{texto}': POS={pos}, DEP={dep}")
    else:
        print("  - No se detectaron adverbios.")
    print("---")
