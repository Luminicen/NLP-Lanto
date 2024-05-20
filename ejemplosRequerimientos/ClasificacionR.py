from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.utils import to_categorical
from keras.layers import Dense, Input, LSTM, Embedding,Dropout, Activation
from keras.layers import Bidirectional, GlobalMaxPool1D,Conv1D, SimpleRNN
from keras.models import Model
from keras.models import Sequential
from keras import initializers, regularizers, constraints,optimizers, layers
from keras.layers import Dense, Input, Flatten, Dropout,BatchNormalization
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Sequential
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics import classification_report as result
import pandas as pd
import numpy as np
import re
file_content = pd.read_excel("req.xlsx")
stop = stopwords.words('english')
file_content['Req'] = file_content['Req'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
Req_Data = file_content[['Target', 'Req']]
Req_Data = Req_Data.rename(columns={"Target":"Target", "Req":"Req"})
Req_Data['Req'] = Req_Data['Req'].apply(lambda x:re.sub('[!@#$:).;,?&]', '', x.lower()))
Req_Data['Req'] = Req_Data['Req'].apply(lambda x:re.sub(' ', ' ', x))
print("----------------DATOS--------------------")
print(Req_Data['Req'].head(5)) 
#identifico los datos, las clases = labels
list_sentences_rawdata = Req_Data["Req"].fillna("_na_").values
list_classes = ["Target"]
target = Req_Data[list_classes].values
To_Process=Req_Data[['Req', 'Target']]
#separo datos en datos de entrenamiento y datos de testeo
train, test = train_test_split(To_Process, test_size=0.2)
MAX_SEQUENCE_LENGTH = 300
# Top 20000 frequently occurring words
MAX_NB_WORDS = 20000
# Obtengo las frequently occurring words
tokenizer = Tokenizer(num_words=MAX_NB_WORDS)
tokenizer.fit_on_texts(train.Req)
train_sequences = tokenizer.texts_to_sequences(train.Req)
test_sequences = tokenizer.texts_to_sequences(test.Req)
# hago un diccionario
word_index = tokenizer.word_index
# cantidad de palabras en el diccionario
print('Cantidad encontrada:  %s' % len(word_index))
train_data = pad_sequences(train_sequences, maxlen=MAX_SEQUENCE_LENGTH)
# obtenemos las palabras mnas frecuentes para el test
test_data = pad_sequences(test_sequences, maxlen=MAX_SEQUENCE_LENGTH)
train_labels = train['Target']
test_labels = test['Target']
#convierto los labels de texto a numero
le = LabelEncoder()
le.fit(train_labels)
train_labels = le.transform(train_labels)
test_labels = le.transform(test_labels)
print("clases a usar")
print(le.classes_)
#print(np.unique(train_labels, return_counts=True))
#print(np.unique(test_labels, return_counts=True))
labels_train = to_categorical(np.asarray(train_labels))
labels_test = to_categorical(np.asarray(test_labels))
EMBEDDING_DIM = 100
model = Sequential()
model.add(Embedding(MAX_NB_WORDS,EMBEDDING_DIM,input_length=MAX_SEQUENCE_LENGTH))
model.add(LSTM(16, activation='relu', recurrent_activation='hard_sigmoid',return_sequences=True))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(Flatten())
model.add(Dense(2,activation='softmax'))
model.compile(loss = 'binary_crossentropy',
optimizer='adam',metrics = ['accuracy'])
model.fit(train_data, labels_train,batch_size=16,epochs=20,validation_data=(test_data, labels_test))
predicted_lstm=model.predict(test_data)
precision, recall, fscore, support = score(labels_test,predicted_lstm.round())
print("precision: indica que tan preciso es el modelo. Mide calidad, y la viabilidad de la respuesta")
print("recall: Nos informa sobre la cantidad de casos que es capas de identificar")
print("fscore: Convina las medidas de precision y recal en un solo valor. Sirve para comparar rendimiento")
print("support: Es el numero de occurencias de cada clase acertada ")
print('precision: {}'.format(precision))
print('recall: {}'.format(recall))
print('fscore: {}'.format(fscore))
print('support: {}'.format(support))   
print("############################")
print(result(labels_test,predicted_lstm.round()))
#prediccion
predict_msg = ["""The system must have a disaster recovery plan in place, ensuring that it can be restored within 4 hours in the event of a major failure.."""]
def predict_spam(predict_msg):
  new_seq = tokenizer.texts_to_sequences(predict_msg)
  padded = pad_sequences(new_seq,maxlen=MAX_SEQUENCE_LENGTH)
  return(model.predict(padded))
pred = predict_spam(predict_msg)
print("salida")
print("la siguiente matriz reeprecenta a la etiqueta predecida")
print(pred)
labels = ['Functional Requirements','Non-Functional Requirements']
print("salida traducida")
print( labels[np.argmax(labels_train[np.argmax(pred)])])