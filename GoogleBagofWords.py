#descargar el modelo: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g
#descomprimirlo en esta carpeta
import gensim
from sklearn.decomposition import PCA
from matplotlib import pyplot
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
print (model.similarity('this', 'is'))
print (model.similarity('post', 'book'))
# Finding the odd one out.
print(model.doesnt_match('breakfast cereal dinner lunch'.split()))
print(model.most_similar(positive=['woman', 'king'], negative=['man']))