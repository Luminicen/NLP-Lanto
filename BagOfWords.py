from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
sentences = [['I', 'love', 'nlp'],
 ['I', 'will', 'learn', 'nlp', 'in', '2','months'],
 ['nlp', 'is', 'future'],
 ['nlp', 'saves', 'time', 'and', 'solves', 
'lot', 'of', 'industry', 'problems'],
 ['nlp', 'uses', 'machine', 'learning']]
#creo el modelo y lo configuro
cbow = Word2Vec(sentences, vector_size =50, window = 3, min_count=1,sg = 1)
cbow.save('cbow.bin')
cbow = Word2Vec.load('cbow.bin')
X = cbow.wv[cbow.wv.index_to_key]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
#configuraciones para crear el plot
pyplot.scatter(result[:, 0], result[:, 1])
words = list(cbow.wv.index_to_key)
print("cuanto mas juntas esten las palabras en el grafico mas relacionadas estan en el contexto del documento")
for i, word in enumerate(words):
 pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()