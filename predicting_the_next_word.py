import numpy as np
import random
import pandas as pd
import sys
import os
import time
import codecs
import collections
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from nltk.tokenize import sent_tokenize, word_tokenize
import scipy
from scipy import spatial
from nltk.tokenize.toktok import ToktokTokenizer
import re
from collections.abc import Iterable
# leemos un dataset
file_content = pd.read_csv('spam.csv', encoding = "ISO-8859-1")
Email_Data = file_content[[ 'text']]
list_data = Email_Data.values.tolist()
#print(list_data)# DATOS
def flatten(items):
    """Yield items from any nested iterable"""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
            else:
                yield x
#convierto la lista en STRINGS
TextData=list(flatten(list_data))
texto =''
for i in TextData:
    texto +=i[0]

TextData =texto
#preprocesamos el texto sacandole por ej lineas nuevas, convirtiendo en minusculas entre otras...
TextData = TextData.replace('\n','')
TextData = TextData.lower()
pattern = r'[^a-zA-z0-9\s]'
TextData = re.sub(pattern, '', ''.join(TextData))
#realizamos la tokenizacion
tokenizer = ToktokTokenizer()
tokens = tokenizer.tokenize(TextData)
tokens = [token.strip() for token in tokens]
#obtenemos las palabritas y las ordenamos
word_counts = collections.Counter(tokens)
word_c = len(word_counts)
print(word_c)
distinct_words = [x[0] for x in word_counts.most_common()]
distinct_words_sorted = list(sorted(distinct_words))
#generamos un indice para todas las palabritas
word_index = {x: i for i, x in enumerate(distinct_words_sorted)}
#largo de la ORACION
sentence_length = 25
#preparammos los datos para el modelo
#vamos a generar secuencias de palabras
#input = oraciones de entrada con indice
#output = oraciones de salida con indice
InputData = []
OutputData = []
for i in range(0, word_c - sentence_length, 1):
    X = tokens[i:i + sentence_length]
    Y = tokens[i + sentence_length]
    InputData.append([word_index[char] for char in X])
    OutputData.append(word_index[Y])
print (InputData[:1])
print ("\n")
print(OutputData[:1])
#generamos X
X = numpy.reshape(InputData, (len(InputData), sentence_length, 1))
#hacemos el one hot encode de la variable de salida
# One hot encode the output variable
Y = np_utils.to_categorical(OutputData)
#Vamos a definir el modelos LSTM con 256 unidades de memoria
#definimos el modelo:
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(Y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
#definimos un 'checkpoint'
file_name_path="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(file_name_path, monitor='loss', 
verbose=1, save_best_only=True, mode='min')
callbacks = [checkpoint]
#VARIABLES
EPOCH = 5
BATCH_SIZE = 128
#entrenamos el modelo
model.fit(X, Y, epochs=EPOCH, batch_size=BATCH_SIZE, callbacks=callbacks)
#esto nos  genero unos archivitos que los vamos a cargar para usar. Estos son los weights de la red neuronal
file_name = "weights-improvement-05-7.2197.hdf5"
model.load_weights(file_name)
model.compile(loss='categorical_crossentropy', optimizer='adam')
###############PRUEBA####################
#genero secuencias random
start = numpy.random.randint(0, len(InputData))
input_sent = InputData[start]
#generamos el indice de la siguiente palabrita del mail (Lo que vamos a predecir)
X = numpy.reshape(input_sent, (1, len(input_sent), 1))
predict_word = model.predict(X, verbose=0)
index = numpy.argmax(predict_word)
print(input_sent)
print ("\n")
print(index)
#traducimos la salida
word_index_rev = dict((i, c) for i, c in enumerate(tokens))
result = word_index_rev[index]
sent_in = [word_index_rev[value] for value in input_sent]
print(sent_in)
print ("\n")
print(result)
