import spacy

nlp = spacy.load("es_core_news_sm")

def detectar_conectores_spacy(oracion):
    doc = nlp(oracion)
    conectores = []

    for token in doc:

        if token.pos_ in {"SCONJ", "CCONJ", "ADV"} and token.dep_ in {
            "mark", "cc", "advmod", "discourse", "conj"
        }:
            conectores.append((token.text, token.pos_, token.dep_))

    return conectores

oracion = "Estudié mucho, pero estaba cansado. Además, tenía sueño. Aunque llovía, salimos igual."
conectores = detectar_conectores_spacy(oracion)

for texto, pos, dep in conectores:
    print(f"'{texto}': POS={pos}, DEP={dep}")
