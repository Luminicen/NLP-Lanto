from sklearn.feature_extraction.text import TfidfVectorizer
Text = ["The quick brown fox jumped over the lazy dog.",
"The dog.",
"The fox"]
#Create the transform
vectorizer = TfidfVectorizer()
#Tokenize and build vocab
vectorizer.fit(Text)
#Summarize
feature_names = vectorizer.get_feature_names_out()
print(vectorizer.vocabulary_)
print(vectorizer.idf_)
for word, idf_value in zip(feature_names, vectorizer.idf_):
    print(f'{word}: {idf_value}')