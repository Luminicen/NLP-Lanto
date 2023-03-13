import spacy
from spacy import displacy
# El texto de input se pone en el objeto nlp. Ej nlp(input)
nlp = spacy.load("en_core_web_trf")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
print("La siguiente lista se interpreta de la siguiente forma: texto, caracter de inicio, caracter de fin, etiqueta")
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
print("para visualizarlo en el grafico abrir un navegador web y ir a la direccion 127.0.0.1:5000")
displacy.serve(doc, style="ent")