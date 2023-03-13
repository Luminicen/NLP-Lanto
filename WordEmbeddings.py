import gensim
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
# El input se pone en la variable sentence y tiene que separarse las palabras ya que no se una un tokenizer jeje.
sentences = [['I', 'love', 'nlp'],
 ['I', 'will', 'learn', 'nlp', 'in', '2','months'],
 ['nlp', 'is', 'future'],
 ['nlp', 'saves', 'time', 'and', 'solves', 
'lot', 'of', 'industry', 'problems'],
 ['nlp', 'uses', 'machine', 'learning']]
# entrenamos el modelo
skipgram = Word2Vec(sentences, vector_size =50, window = 3, min_count=1,
sg = 1)
#print(skipgram)
# accedemos al vector
print("-----------------REPRECENTACION DE LA PALABRA 'NLP' EN EL MODELO ------------------")
print(skipgram.wv['nlp'])
skipgram.save('skipgram.bin')
skipgram = Word2Vec.load('skipgram.bin')
X = skipgram.wv[skipgram.wv.index_to_key]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# creamos el grafico
pyplot.scatter(result[:, 0], result[:, 1])
words = list(skipgram.wv.index_to_key)
print("cuanto mas cerca esten los puntos, mas relacionadas van a estar las palabras")
for i, word in enumerate(words):
 pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()