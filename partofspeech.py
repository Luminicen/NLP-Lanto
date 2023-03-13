import spacy
from spacy import displacy
# El input se le pasa como parametro al objeto nlp. Ej nlp_ingles(input)
nlp_ingles = spacy.load("en_core_web_trf")
print("Ejemplos en ingles")
texto = "Feature engineering is a process of extracting meaningful information from the raw data to make it usable for machine learning models."
doc = nlp_ingles(texto)
print("Se imprimira en el siguiente orden: el texto, el parts of speech y dependencia")
for i in doc:
    print(i.text, i.pos_, i.dep_)
print("para visualizarlo en el grafico abrir un navegador web y ir a la direccion 127.0.0.1:5000")
displacy.serve(doc, style="dep")