from textblob import TextBlob
# El input se pasa como parametro a la funcion TextBlob. Ej TextBlob(input)
print("CASO A")
blob = TextBlob("John is learning natural language processing")
for np in blob.noun_phrases:
    print(np)
#Ejemplo mas largo
print("CASO B")
with open('./Datos/Agricultura.txt',"r",encoding='utf-8') as f:
    contents = f.read()
    #print(contents)
    agriculture = TextBlob(contents)
    for np in agriculture.noun_phrases:
        print(np)