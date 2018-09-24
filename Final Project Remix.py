
# coding: utf-8

# In[39]:


import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

import random
from textblob import TextBlob

# This looks for a file called "Apple One" 
# in the same directory as my python notebook or script.
# Replace "Apple One" with your file's name.
# The text file's contents are stored in the variable "text"
with open('Apple One', 'r') as file:
    text = file.read()

# This parses the text file contents into a TextBlob oject called "blob"
blob = TextBlob(text)

# Create two empty lists for storing adjectives and nouns
adjectives = []
nouns = []
verbs= []

# TextBlob parses the words and labels them with a part-of-speech tag.
# This code loops through the whole text, checks for adjectives and nouns
# and adds them to the appropriate list.
for word,pos in blob.tags:
    # print(word,pos)
    if (pos == 'JJ'):
        adjectives.append(word)
    if (pos == 'NN'):
        nouns.append(word)

# This generates an eight-line poem by pairing a random adjective 
# with a random noun eight times and printing the pairs.
for i in range(4):
    a = random.choice(adjectives)
    n = random.choice(nouns)
    print(a,n)

