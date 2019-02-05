from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
'''
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
'''
#default pos="n"(noun)
#"a" = adjective, "v" = verb
#lemmas give back actual words, usually better then stemmers
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run", pos="v"))
print(lemmatizer.lemmatize("run"))

