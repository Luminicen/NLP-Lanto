import spacy
from spacy.matcher import DependencyMatcher
from spacy import displacy

nlp = spacy.load("es_core_news_sm")
matcher = DependencyMatcher(nlp.vocab)
# Define los nodos de anclaje
matcher.add("mi_patron", [
        [
            {'RIGHT_ID': 'programa', 'RIGHT_ATTRS': {"LOWER": "programa"}},
            {'LEFT_ID': 'programa', 'REL_OP': '>', 'RIGHT_ID': 'nombre', 'RIGHT_ATTRS':  {"DEP": "nsubj"}},
            {'LEFT_ID': 'programa', 'REL_OP': '>', 'RIGHT_ID': 'de_que', 'RIGHT_ATTRS': {"DEP": "nmod"}} ,
            {'LEFT_ID': 'de_que', 'REL_OP': '>', 'RIGHT_ID': 'elem', 'RIGHT_ATTRS': {"DEP": "nmod"}} ,
            {'LEFT_ID': 'elem', 'REL_OP': '>', 'RIGHT_ID': 'control', 'RIGHT_ATTRS': {"DEP": "amod"}} ,
            {'LEFT_ID': 'control', 'REL_OP': '>', 'RIGHT_ID': 'controlobj', 'RIGHT_ATTRS': {"DEP": "obj"}} ,
            {'LEFT_ID': 'controlobj', 'REL_OP': '>', 'RIGHT_ID': 'rem', 'RIGHT_ATTRS': {"DEP": "amod"}} ,
           

        ]
])

# Texto de ejemplo
texto = "BattleBots es un programa de televisión acerca de combates de robots controlados por control remoto.BattleBots Inc.  tiene su sede en Vallejo, California y cuenta con la mayoría de sus competencias en San Francisco."

doc = nlp(texto)
#displacy.serve(doc)
coincidencias = matcher(doc)
print(coincidencias)
i = 0
for match_id, token_ids in coincidencias:
    palabra= []
    for token_id in sorted(token_ids):
        token = doc[token_id]
        palabra.append(token.text)
    print(nlp.vocab.strings[match_id], ' '.join(palabra))

