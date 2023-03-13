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
# El input: Se manda el texto como parametro a la funcion de TextBlob. Ej TextBlob(input).
# Nota: Preprocesar siempre el texto antes de pasarlo como parametro a TextBlob con la funcion processRow.
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
print("REVIEW 2")
blob = TextBlob(review2_limpio)
print("Polaridad: Cuanto mas se acerque a 1 mas positivo es la review, si es 0 es neutral la review y cuanto mas cercana a -1 este mas negativa es la review")
print(blob.sentiment)
#cuanto mas se acerque a 1 es mas positiva y cuanto mas se acerque a -1 es negativa
#ejemplos mas largos
review_larga_positiva="""Total War: Warhammer 3 is the perfect example of a sequel done well. All the elements of both Total War and Warhammer universe fused into a game of epic proportions.
 Some innovation in the variety of missions as well bring a bit more freshness in the gameplay. 
 Graphics as usual stunning, with scenery that looks like fresh."""
review_larga_neutral="""Warhammer 3 opens strongly. The narrative hook of the prologue sinks deep and the raft of tweaks to the strategic layer and tactical battles are all welcome. But it can't sustain the early momentum. The endgame objectives feel like a distraction, even though they're the main point, and serve only to diminish the entire campaign. The factions all have different reasons for wanting the endgame MacGuffin, but none of those motivations make a difference to how the campaign plays out. They're all trapped in the same Chaos Realm, going through the same motions, in pursuit of the same unsatisfying win conditions. In the end, Total War: Warhammer 3 is a good game--there just isn't a good reason to see it through to the bitter end."""
review_larga_negativa=""
with open('./Datos/review_negativa.txt',"r",encoding='utf-8') as f:
    contents = f.read()
    review_larga_negativa=contents
positiva = processRow(review_larga_positiva)
neutral = processRow(review_larga_neutral)
negativa = processRow(review_larga_negativa)
blob = TextBlob(positiva)
print("REVIEW POSITIVA")
print(blob.sentiment)
blob = TextBlob(neutral)
print("REVIEW NEUTRAL")
print(blob.sentiment)
blob = TextBlob(negativa)
print("REVIEW NEGATIVA")
print(blob.sentiment)

