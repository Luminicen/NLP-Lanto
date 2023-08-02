from sklearn.feature_extraction.text import TfidfVectorizer
Text = ["The quick brown fox jumped over the lazy dog.",
"The dog.",
"The fox"]
#Create the transform
vectorizer = TfidfVectorizer()
#Tokenize and build vocab
vectorizer.fit(Text)
#Summarize
print(vectorizer.vocabulary_)
print(vectorizer.idf_)
