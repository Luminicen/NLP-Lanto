from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer
from itertools import chain
from pywsd.lesk import simple_lesk
# El input va dentro de un arreglo
# En la funcion simple_lesk hay que especificar la palabra a la cual queremos desambiguar
# Sentencias
bank_sents = ['I went to the bank to deposit my money',
'The river bank was full of dead fishes']
# llamamos a la funcion lesk e imprimimos los resultados
print ("Contexto-1:", bank_sents[0])
answer = simple_lesk(bank_sents[0],'bank')
print ("Sentido detectado:", answer)
print ("Definicion : ", answer.definition())
print ("Contexto-2:", bank_sents[1])
answer = simple_lesk(bank_sents[1],'bank','n')
print ("Sentido detectado:", answer)
print ("Definicion : ", answer.definition())