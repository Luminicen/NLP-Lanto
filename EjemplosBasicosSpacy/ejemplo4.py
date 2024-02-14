import spacy
from spacy import displacy

nlp = spacy.load("es_core_news_sm")

texto = "El presidente de Estados Unidos, Joe Biden, visitará Berlín el próximo mes."

doc = nlp(texto)

for en in doc.ents:
    print(f"Entidad encontrada:  {en}")

# Visualizar las entidades con displacy
options = {"compact": True, "color": "blue"}
displacy.serve(doc, style="ent", options=options)