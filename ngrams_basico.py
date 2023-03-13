from textblob import TextBlob
# El input es la variable text
Text = "I am learning NLP"
# n=1 unigrama
print("obtenemos unigramas! es decir n=1")
print(TextBlob(Text).ngrams(1))
#n=2 bigrama
print("obtenemos bigramas! es decir n=2")
print(TextBlob(Text).ngrams(2))