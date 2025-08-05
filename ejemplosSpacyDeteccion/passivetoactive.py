import spacy

nlp = spacy.load("es_core_news_sm")

def convertir_pasiva_a_activa(texto: str) -> str:
    doc = nlp(texto)

    for token in doc:
        # 1) Verbo en participio
        if not (token.pos_ == "VERB" and "Part" in token.morph.get("VerbForm")):
            continue

        # 2) Auxiliar hijo (ser/estar en pasado)
        aux = next(
            (c for c in token.children
             if c.dep_ == "aux" and c.lemma_ in {"ser", "estar"}),
            None
        )
        if not aux:
            continue

        # 3) Sujeto paciente (hijo con dep_ nsubj)
        subj = next(
            (c for c in token.children
             if c.dep_ == "nsubj"),
            None
        )
        if not subj:
            continue

        # 4) Complemento agente: "por" es marcador case
        por = next(
            (t for t in doc
             if t.dep_ == "case" and t.lemma_ == "por"),
            None
        )
        if not por:
            continue

        # 5) El head de "por" es el sustantivo agente
        agente_nodo = por.head
        # extraemos todo su subtree excepto el marcador "por"
        agentes = [t.text for t in agente_nodo.subtree if not (t.dep_ == "case" and t.lemma_ == "por")]
        agente = " ".join(agentes).strip()
        if not agente:
            continue

        # 6) Reconstruimos la activa (verbo en lemma = infinitivo)
        return f"{agente.capitalize()} {token.lemma_} {subj.text.lower()}."

    # Si no hay pasiva explícita, devolvemos el original
    return texto


if __name__ == "__main__":
    ejemplos = [
        "La carta fue escrita por Juan.",
        "El informe fue redactado por la secretaria.",
        "Los libros fueron leídos por los estudiantes.",
        "El auto fue vendido por el concesionario.",
        "Se construyó un puente en el río.",
        "María come una manzana."
    ]
    for o in ejemplos:
        print(f"Original: {o}")
        print(f"Activa:   {convertir_pasiva_a_activa(o)}")
        print("-" * 50)
