from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# El input se pone en un arreglo o tupla y se lo pasa a tfidf_matrix
documents = (
"The system must allow users to log in using a username and password.",
"The system must allow users to authenticate using email and password.",
"The system must be compatible with the latest versions of major web browsers, including Chrome, Firefox, Safari, and Edge.",
"The system must allow administrators to update information of existing products in the catalog.",
"The system must allow users to search for products by name."
)
#Hacemos  feature engineering
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
#print(tfidf_matrix.shape)
#hacemos el computo de similaridad
print("Se compara la palabra con si misma y con el resto. El resultado queda en la posicion de la palabra. Cuanto mayor sea el numero mas parecido es. Si es 1 es porque es igual. Compara el primer valor con el resto!")
print("EJEMPLO 1")
print(cosine_similarity(tfidf_matrix[0:1],tfidf_matrix))
#------------------------------JACCARD INDEX-----------------------------------------
print("-----------JACCARD SIMILARITY--------------")
# Función para calcular el índice de Jaccard entre dos textos
def jaccard_index(text1, text2):
    # Tokeniza los textos en palabras individuales
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    
    # Calcula la intersección de los conjuntos de palabras
    intersection = len(words1.intersection(words2))
    
    # Calcula la unión de los conjuntos de palabras
    union = len(words1.union(words2))
    
    # Calcula el índice de Jaccard
    jaccard = intersection / union if union > 0 else 0.0
    
    return jaccard

# Ejemplo de uso, Cuando mas cercano sea a 1 mas similar es
texto1 = "The system must allow users to authenticate using email and password"
texto2 = "The system must send an order confirmation email to users once the payment has been successfully processed."
resultado = jaccard_index(texto1, texto2)

print("Índice de Jaccard:", resultado)
print("Distancia Jaccard:",1-resultado)