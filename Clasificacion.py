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
file_content = pd.read_csv('spam.csv', encoding = "ISO-8859-1")
#limpieza
stop = stopwords.words('english')
file_content['text'] = file_content['text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
Email_Data = file_content[['label', 'text']]
Email_Data = Email_Data.rename(columns={"label":"Target", "text":"Email"})
Email_Data['Email'] = Email_Data['Email'].apply(lambda x:re.sub('[!@#$:).;,?&]', '', x.lower()))
Email_Data['Email'] = Email_Data['Email'].apply(lambda x:re.sub(' ', ' ', x))
print("----------------DATOS--------------------")
print(Email_Data['Email'].head(5))# <--- descomentar para ver como se compone el .csv
#identifico los datos, las clases = labels
list_sentences_rawdata = Email_Data["Email"].fillna("_na_").values
list_classes = ["Target"]
target = Email_Data[list_classes].values
To_Process=Email_Data[['Email', 'Target']]
#separo datos en datos de entrenamiento y datos de testeo
train, test = train_test_split(To_Process, test_size=0.2)
MAX_SEQUENCE_LENGTH = 300
# Top 20000 frequently occurring words
MAX_NB_WORDS = 20000
# Obtengo las frequently occurring words
tokenizer = Tokenizer(num_words=MAX_NB_WORDS)
tokenizer.fit_on_texts(train.Email)
train_sequences = tokenizer.texts_to_sequences(train.Email)
test_sequences = tokenizer.texts_to_sequences(test.Email)
# hago un diccionario
word_index = tokenizer.word_index
# cantidad de palabras en el diccionario
print('Cantidad encontrada:  %s' % len(word_index))
train_data = pad_sequences(train_sequences, maxlen=MAX_SEQUENCE_LENGTH)
# obtenemos las palabras mnas frecuentes para el test
test_data = pad_sequences(test_sequences, maxlen=MAX_SEQUENCE_LENGTH)
#print(train_data.shape)
#print(test_data.shape)
train_labels = train['Target']
test_labels = test['Target']
#convierto los labels de texto a numero
le = LabelEncoder()
le.fit(train_labels)
train_labels = le.transform(train_labels)
test_labels = le.transform(test_labels)
print(le.classes_)
print(np.unique(train_labels, return_counts=True))
#print(np.unique(test_labels, return_counts=True))
labels_train = to_categorical(np.asarray(train_labels))
labels_test = to_categorical(np.asarray(test_labels))
#print('Shape of data tensor:', train_data.shape)
#print('Shape of label tensor:', labels_train.shape)
#print('Shape of label tensor:', labels_test.shape)
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
model.fit(train_data, labels_train,batch_size=16,epochs=5,validation_data=(test_data, labels_test))
predicted_lstm=model.predict(test_data)
precision, recall, fscore, support = score(labels_test,predicted_lstm.round())
print('precision: {}'.format(precision))
print('recall: {}'.format(recall))
print('fscore: {}'.format(fscore))
print('support: {}'.format(support))   
print("############################")
print(result(labels_test,predicted_lstm.round()))
#prediccion
predict_msg = ["""Hey judy, i have the work for tomorrow.""",
               "Call me"]
def predict_spam(predict_msg):
  new_seq = tokenizer.texts_to_sequences(predict_msg)
  padded = pad_sequences(new_seq,maxlen=MAX_SEQUENCE_LENGTH)
  return(model.predict(padded))
pred = predict_spam(predict_msg)
print("salida")
print(pred)
labels = ['ham','spam']
print("salida traducida")
print(pred, labels[np.argmax(labels_train[np.argmax(pred)])])