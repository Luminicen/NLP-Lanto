from textblob import TextBlob
Text = "I am learning NLP"
# n=1 unigrama
print("n=1")
print(TextBlob(Text).ngrams(1))
#n=2 bigrama
print("n=2")
print(TextBlob(Text).ngrams(2))