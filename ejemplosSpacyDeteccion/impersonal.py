import spacy

nlp = spacy.load("es_core_news_sm")

def es_impersonal(doc):
    for sent in doc.sents:
        has_subject = any(tok.dep_ == "nsubj" for tok in sent)
        has_se = any(tok.text.lower() == "se" for tok in sent)
        verb_sing_3rd = any(tok.pos_ == "VERB" and "Number=Sing" in tok.morph and "Person=3" in tok.morph for tok in sent)

        for token in sent:
            # Casos con "haber" impersonal
            if token.lemma_ == "haber" and token.pos_ == "VERB" and "Person=3" in token.morph:
                return True
            # Meteorológicos o verbos típicamente impersonales
            if token.lemma_ in {"llover", "nevar", "granizar", "hacer", "ser"} and token.pos_ == "VERB":
                if not has_subject:
                    return True
        
        # Casos con "se" + verbo sin sujeto
        if has_se and verb_sing_3rd and not has_subject:
            return True

    return False

oraciones = [
    "Se vive bien aquí.",
    "Llueve mucho en primavera.",
    "Hace calor hoy.",
    "Hay mucha gente en la sala.",
    "Se duerme mejor con la ventana abierta.",
    "Ella se duerme temprano.",
    "Nosotros nos duchamos.",
    "Se dice que vendrá.",
    "El niño se cayó.",
    "Se rompió el vaso.",
]

for oracion in oraciones:
    doc = nlp(oracion)
    print(f"'{oracion}' → {'✅ Impersonal' if es_impersonal(doc) else '❌ No impersonal'}")
