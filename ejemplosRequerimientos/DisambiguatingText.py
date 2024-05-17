from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer
from itertools import chain
from pywsd.lesk import simple_lesk
# El input va dentro de un arreglo
# En la funcion simple_lesk hay que especificar la palabra a la cual queremos desambiguar
# Sentencias
bank_sents = ['The professor outlined the course requirements that students needed to fulfill by the end of the semester.',
'The requirements of the machine were beyond what the current electrical system could support.']
# llamamos a la funcion lesk e imprimimos los resultados
print ("Contexto-1:", bank_sents[0])
answer = simple_lesk(bank_sents[0],'requirements')
print ("Sentido detectado:", answer)
print ("Definicion : ", answer.definition())
print ("Contexto-2:", bank_sents[1])
answer = simple_lesk(bank_sents[1],'requirements','n')
print ("Sentido detectado:", answer)
print ("Definicion : ", answer.definition())