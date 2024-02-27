import spacy
from spacy.matcher import DependencyMatcher
from spacy import displacy

nlp = spacy.load("es_core_news_sm")
matcher = DependencyMatcher(nlp.vocab)
# Define los nodos de anclaje
matcher.add("mi_patron", [
    [
        {
            "RIGHT_ID": "patron1",
            "RIGHT_ATTRS": {"LOWER": "programa"}
        },
        {
            "LEFT_ID": "patron1",
            "REL_OP": ">",
            "RIGHT_ID": "patron2",
            "RIGHT_ATTRS": {"DEP": "nsubj"}
        },
        {
            "LEFT_ID": "patron1",
            "REL_OP": ">",
            "RIGHT_ID": "patron3",
            "RIGHT_ATTRS": {"DEP": "nmod"}
        },
        {
            "LEFT_ID": "patron3",
            "REL_OP": ">",
            "RIGHT_ID": "patron4",
            "RIGHT_ATTRS": {"DEP": "nmod"}
        },
         
        
    ],
])

# Texto de ejemplo
texto = "BattleBots es un programa de televisión acerca de combates de robots controlados por control remoto.BattleBots Inc.  tiene su sede en Vallejo, California y cuenta con la mayoría de sus competencias en San Francisco."

doc = nlp(texto)
#displacy.serve(doc)
coincidencias = matcher(doc)
print(coincidencias)
i = 0
for _, token_ids in coincidencias:
    token_a = doc[token_ids[i]]
    print(token_a)
    i = i + 1
    

