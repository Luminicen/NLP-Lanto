#descargar el modelo: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g
#descomprimirlo en esta carpeta
import gensim
from sklearn.decomposition import PCA
from matplotlib import pyplot
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
print("SIMILARIDADES")
print()
print("Entre 'this' y 'is' ")
print (model.similarity('this', 'is'))
data = round(model.similarity('this', 'is') * 100,2)
print("Es decir se parecen en un {}%".format(data))
print("Entre 'post' y 'book' ")
print (model.similarity('post', 'book'))
data = round(model.similarity('post', 'book') * 100,2)
print("Es decir se parecen en un {}%".format(data))
print("NO MATCHEA")
print("¿Cual es la palabra que no matchea con el resto? breakfast cereal dinner lunch")
print(model.doesnt_match('breakfast cereal dinner lunch'.split()))
print("Operemos con terminos")
print("WOMAN + KING - MAN")
print(model.most_similar(positive=['woman', 'king'], negative=['man']))
print("La respuesta es aquella que tiene el valor mas alto!")
