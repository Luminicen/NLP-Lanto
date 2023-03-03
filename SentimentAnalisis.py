import re
import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from textblob import Word
from nltk.util import ngrams
import re
from textblob import Word
from textblob import TextBlob
#from wordcloud import WordCloud, STOPWORDS
from nltk.tokenize import word_tokenize
review = "I like this phone. screen quality and camera clarity is really good."
review2 = "This tv is not good. Bad quality, no clarity, worst experience. A piece of trash."
#limpieza
def processRow(row):
    string = row
    #pongo todo en minuscuka
    string.lower()
    #saco espacios adicionales
    string = re.sub('[\s]+', ' ', string)
    string = re.sub('[\n]+', ' ', string)
    #saco caracteres no alfanumericos
    string = re.sub(r'[^\w]', ' ', string)
    #saco #
    string = re.sub(r'#([^\s]+)', r'\1', string)
    #cambio #palabra por palabra
    string = re.sub(r'#([^\s]+)', r'\1', string)
    #Sacp :( or :)
    string = string.replace(':)','')
    string = string.replace(':(','')
    #Saco numeros
    string = ''.join([i for i in string if not i.isdigit()])
    #si hay multiples ! los saco
    string = re.sub(r"(\!)\1+", ' ', string)
    #si hay multiples ? los saco
    string = re.sub(r"(\?)\1+", ' ', string)
    #saco ...
    string = re.sub(r"(\.)\1+", ' ', string)
    #lemma
    string =" ".join([Word(word).lemmatize() for word in string.split()])
    #stemmer
    #st = PorterStemmer()
    #string=" ".join([st.stem(word) for word in string.split()])
    #trim
    string = string.strip('\'"')
    row = string
    return row
review_limpio = processRow(review)
review2_limpio = processRow(review2)
#TextBlob tiene un modelo preentrenado para analisis de sentimientos
blob = TextBlob(review_limpio)
print("REVIEW 1")
print(blob.sentiment)
#now lets look at the sentiment of review2
print("REVIEW 2")
blob = TextBlob(review2_limpio)
print(blob.sentiment)
#cuanto mas se acerque a 1 es mas positiva y cuanto mas se acerque a -1 es negativa
