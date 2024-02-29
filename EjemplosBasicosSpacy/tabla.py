import spacy
from spacy.matcher import DependencyMatcher
def extraerPalabritas(coincidencias):
    palabra= ""
    for _ , token_ids in coincidencias:
        for token_id in token_ids:
            token = doc[token_id]
            palabra = palabra + token.text + " "
    return palabra

nlp = spacy.load("es_core_news_sm")
matcher = DependencyMatcher(nlp.vocab)
# Define los nodos de anclaje
matcher.add("juez", [
        [
            #extraigo juez
            {'RIGHT_ID': 'juez', 'RIGHT_ATTRS':  {"lower": "juez"}},
            {'LEFT_ID': 'juez', 'REL_OP': '>', 'RIGHT_ID': 'juzgado', 'RIGHT_ATTRS':  {"DEP": "nmod"}},
            {'LEFT_ID': 'juzgado', 'REL_OP': '.', 'RIGHT_ID': 'federal', 'RIGHT_ATTRS':  {"DEP": "flat"}},   
        ]
])
# Texto de ejemplo
texto = " Que el juez a cargo del Juzgado Federal de Oberá  declaró procedente la extradición de César Elías Fucks a la  República Federativa del Brasil para someterlo a proceso por el  delito de robo seguido de muerte."

doc = nlp(texto)
#displacy.serve(doc)
coincidencias = matcher(doc)
quien=extraerPalabritas(coincidencias)
matcher.remove("juez")
matcher.add("criminal", [
        [
            #extraigo criminal
            {'RIGHT_ID': 'crim', 'RIGHT_ATTRS':  {"lower": "declaró"}},
            {'LEFT_ID': 'crim', 'REL_OP': '>', 'RIGHT_ID': 'extradicion', 'RIGHT_ATTRS':  {"DEP": "obj"}},
            {'LEFT_ID': 'extradicion', 'REL_OP': '>', 'RIGHT_ID': 'nombre', 'RIGHT_ATTRS':  {"DEP": "nmod"}},
            {'LEFT_ID': 'nombre', 'REL_OP': '.', 'RIGHT_ID': 'nombre2', 'RIGHT_ATTRS':  {"DEP": "flat"}},
            {'LEFT_ID': 'nombre2', 'REL_OP': '.', 'RIGHT_ID': 'apellido', 'RIGHT_ATTRS':  {"DEP": "flat"}},
              
        ]
])
coincidencias = matcher(doc)
criminal = extraerPalabritas(coincidencias)
matcher.remove("criminal")
matcher.add("destino", [
        [
            #extraigo destino
            {'RIGHT_ID': 'crim', 'RIGHT_ATTRS':  {"lower": "declaró"}},
            {'LEFT_ID': 'crim', 'REL_OP': '>', 'RIGHT_ID': 'extradicion', 'RIGHT_ATTRS':  {"DEP": "obj"}},
            {'LEFT_ID': 'extradicion', 'REL_OP': '>', 'RIGHT_ID': 'destino', 'RIGHT_ATTRS':  {"DEP": "nmod"}},
            {'LEFT_ID': 'destino', 'REL_OP': '>', 'RIGHT_ID': 'fed', 'RIGHT_ATTRS':  {"DEP": "flat"}},
            {'LEFT_ID': 'fed', 'REL_OP': '.', 'RIGHT_ID': 'aladito', 'RIGHT_ATTRS':  {"POS": "ADP"}},
            {'LEFT_ID': 'aladito', 'REL_OP': '.', 'RIGHT_ID': 'aladito2', 'RIGHT_ATTRS':  {"POS": "PROPN"}},
            
            

        ]
])
coincidencias = matcher(doc)
destino = extraerPalabritas(coincidencias)
matcher.remove("destino")
matcher.add("crimen", [
        [
            #extraigo crimen
            {'RIGHT_ID': 'crim', 'RIGHT_ATTRS':  {"lower": "declaró"}},
            {'LEFT_ID': 'crim', 'REL_OP': '>>', 'RIGHT_ID': 'delito', 'RIGHT_ATTRS':  {"DEP": "obl"}},
            {'LEFT_ID': 'delito', 'REL_OP': '>', 'RIGHT_ID': 'robo', 'RIGHT_ATTRS':  {"DEP": "nmod"}},
            {'LEFT_ID': 'robo', 'REL_OP': '.', 'RIGHT_ID': 'seguido', 'RIGHT_ATTRS':  {"DEP": "amod"}},
            {'LEFT_ID': 'seguido', 'REL_OP': '.', 'RIGHT_ID': 'de', 'RIGHT_ATTRS':  {}},
            {'LEFT_ID': 'de', 'REL_OP': '.', 'RIGHT_ID': 'muertesita', 'RIGHT_ATTRS':  {}},
                 
        ]
])
coincidencias = matcher(doc)
delito = extraerPalabritas(coincidencias)
print(f'Juez: {quien}')
print(f'Criminal: {criminal}')
print(f'Destino: {destino}')
print(f'Delito: {delito}')

