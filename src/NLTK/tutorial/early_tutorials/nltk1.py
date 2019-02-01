from nltk.tokenize import sent_tokenize, word_tokenize

# tokenizers - word and scentence
# lexicon - words and their meanings
# corpora - bodies of text
# investor-speak vs english-speak differ

example_text = "Hello Mr. Smith, how are you doing today? The weather is great and python is awesome. The sky is pinkish blue and you should not eat cardboard."
#print(sent_tokenize(example_text))
#print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)