import spacy
from spacy.matcher import DependencyMatcher

nlp = spacy.load("es_core_news_sm")
matcher = DependencyMatcher(nlp.vocab)

# Define los nodos de anclaje
matcher.add("mi_patron", [
    [
        {
            "RIGHT_ID": "patron1",
            "RIGHT_ATTRS": {"LOWER": "ejemplo"}
        },
        {
            "LEFT_ID": "patron1",
            "REL_OP": ">",
            "RIGHT_ID": "patron2",
            "RIGHT_ATTRS": {"DEP": "nmod"}
        },
    ],
])

# Texto de ejemplo
texto = "Esto es un ejemplo de spaCy."

doc = nlp(texto)
coincidencias = matcher(doc)

for _, token_ids in coincidencias:
    token_a = doc[token_ids[0]]
    token_b = doc[token_ids[1]]
    print(f"Encontrado: '{token_a.text}' y '{token_b.text}'")
