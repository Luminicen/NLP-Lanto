import nltk
#nltk.download('omw-1.4')  # WordNet multilingüe
#nltk.download('wordnet')  # WordNet base
from nltk.corpus import wordnet as wn

def es_abstracto(palabra, lang='spa'):
    synsets = wn.synsets(palabra, lang=lang, pos=wn.NOUN)
    for s in synsets:
        # Traducimos al synset en inglés para acceder a la jerarquía
        for lemma in s.lemma_names('eng'):
            eng_synset = wn.synsets(lemma, pos=wn.NOUN)
            for eng_s in eng_synset:
                hypernyms = [h.name() for h in eng_s.hypernyms()]
                # Buscamos si tiene un hiperónimo abstracto
                if any("abstraction" in h or "attribute" in h for h in hypernyms):
                    return True
    return False

palabras = ["cosa", "mesa", "aspecto", "idea", "manzana", "realidad", "concepto"]

for p in palabras:
    print(f"{p}: {'abstracto' if es_abstracto(p) else 'concreto'}")

