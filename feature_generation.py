SOS_token = 0
EOS_token = 1


class Lang:
    def __init__(self, name):
        self.name = name
        self.word2index = {} 
        self.word2count = {} 
        self.index2word = {0: "SOS", 1: "EOS"}
        self.n_words = 2  # SOS and EOS already indexed 0 annd 1, so the first new word starts at 2 
        
    def addSentence(self, sentence):
        for word in sentence.split(' '): #get every word from the sentence and pas it into the addword function
            self.addWord(word)
            
    #updating word2index, index2word and word2count hashmaps
    def addWord(self, word):
        if word not in self.word2index: 
            self.word2index[word] = self.n_words 
            self.word2count[word] = 1
            self.index2word[self.n_words] = word
            self.n_words += 1
        else:
            self.word2count[word] += 1

"""### Make the features ready for the model"""

def readData(text, summary):
    pairs = [[text[i],summary[i]] for i in range(len(text))] # Put text and summary in pairs 
    input_lang = Lang(text) #create input object
    output_lang = Lang(summary) #create output object 
    return input_lang, output_lang, pairs 

def prepareData(X, Y):
    input_lang, output_lang, pairs = readData(X,Y)
    
    for pair in pairs:
        input_lang.addSentence(pair[0])
        output_lang.addSentence(pair[1])
        
    return input_lang, output_lang, pairs

input_lang, output_lang, pairs = prepareData(X,Y)

print(pairs)

