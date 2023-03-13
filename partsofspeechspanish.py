import spacy
from spacy import displacy
nlp_español = spacy.load("es_dep_news_trf")
# El input se le pasa como parametro al objeto nlp. Ej nlp_español(input)
print("Ejemplos en Español")
texto = "La inteligencia artificial es el conjunto de sistemas o combinación de algoritmos, cuyo propósito es crear máquinas que imitan la inteligencia humana para realizar tareas y pueden mejorar conforme la información que recopilan."
doc = nlp_español(texto)
print("Se imprimira en el siguiente orden: el texto, el parts of speech y dependencia")
for i in doc:
    print(i.text, i.pos_, i.dep_)
print("para visualizarlo en el grafico abrir un navegador web y ir a la direccion 127.0.0.1:5000")
displacy.serve(doc, style="dep")