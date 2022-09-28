"""### Text cleanup
In this section we would:

- Define a contraction hashmap
- Define a function preprocess(text) and call it
- Create a dataframe to contain text and summary, and remove those empty strings both from summary and the text column
"""

# Defining a contraction hashmap
contraction_map = {"ain't": "is not", "aren't": "are not","can't": "cannot", "'cause": "because", "could've": "could have", "couldn't": "could not",

                           "didn't": "did not", "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not",

                           "he'd": "he would","he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is",

                           "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have","I'm": "I am", "I've": "I have", "i'd": "i would",

                           "i'd've": "i would have", "i'll": "i will",  "i'll've": "i will have","i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would",

                           "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have","it's": "it is", "let's": "let us", "ma'am": "madam",

                           "mayn't": "may not", "might've": "might have","mightn't": "might not","mightn't've": "might not have", "must've": "must have",

                           "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock",

                           "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have",

                           "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is",

                           "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have","so's": "so as",

                           "this's": "this is","that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would",

                           "there'd've": "there would have", "there's": "there is", "here's": "here is","they'd": "they would", "they'd've": "they would have",

                           "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have",

                           "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are",

                           "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are",

                           "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is",

                           "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have",

                           "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have",

                           "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all",

                           "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have",

                           "you'd": "you would", "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have",

                           "you're": "you are", "you've": "you have"}

import nltk
nltk.__version__

nltk.download('stopwords') # Downloading stopwards(just in case they are not already available)

import re 
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

#defining the preprocess function
def preprocess(text):
    text = text.lower() # convert text tlowercase
    text = text.split() 
    for i in range(len(text)):
        word = text[i]
        if word in contraction_map: 
            text[i] = contraction_map[word] #apply the contraction hashmap
    text = " ".join(text)
    text = text.split()
    newtext = []
    for word in text:
        if word not in stop_words:
            newtext.append(word)
    text = " ".join(newtext)
    text = text.replace("'s",'') # remove 's e.g convert your's -> your
    text = re.sub(r'\(.*\)','',text) # remove parenthesis outside a word e.g (word) -> word
    text = re.sub(r'[^a-zA-Z0-9. ]','',text) # remove punctuations
    text = re.sub(r'\.',' . ',text) # add a space character before and after the full stop
    return text

X = []
Y = []
for d_text in dataset:
    prep_dataset = preprocess(d_text)
    X.append(prep_dataset)
for t_text in target:
    prep_target = preprocess(t_text)
    Y.append(prep_target)

print(len(X), len(Y))

# Reduce dataset size
max_len_text = 600
max_len_target = 30

short_text=[]
short_summary=[]

for i in range(len(dataset)):
    if(len(target[i].split())<=max_len_target and len(dataset[i].split())<=max_len_text):
        short_text.append(dataset[i])
        short_summary.append(target[i])

temp_df = pd.DataFrame({'text':short_text,'summary':short_summary})

temp_df.head()

# remove those empty strings both from summary and the text column
newdf = temp_df[temp_df['summary'].str.strip().astype(bool)]
df = newdf[newdf['text'].str.strip().astype(bool)]

df.head()
