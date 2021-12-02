from itertools import accumulate
from nltk import bigrams, trigrams
import nltk
import random 
from collections import Counter, defaultdict
from numpy import random

# placeholder value 
model = defaultdict(lambda: defaultdict(lambda: 0))

# sheldon
text = (open("/Users/gracezhang/ling242Project/all_sheldon.txt").read())

most_occur_start_word = ['I', 'Oh', 'where', 'You', "I'm", "No,", "It's'", "All", 
              "And", "Yeah", "What", "That's", "Yes."
              "You're", "No.", "Yes,", "It", "The", "Thank", "But"]

most_occur_starting_words = ['I don’t', 'All right,', 'Well, I', 'Thank you.', 'Oh, I', 'All right.' ,
                             'Are you', 'You know,' , 'This is', 'Do you', 'I have', 'I’m not',
                             'I was', 'No, I', 'You know', 'I can’t', 'Of course', 'I think',
                             'I’m sorry,', "No, no,"]

## tokenize 
nltk_tokens = nltk.word_tokenize(text)
#print(nltk_tokens)

## ********** Tri-gram Model 
# make sentences into a list, appends each sentence by the "\n"
for sentence in text.split("\n"):
    
    # make each sentence into a list of words split by the " "
    sentence = sentence.split(" ")
    
    # since trigram use w1, w2, and w3
    # trigram() from nltk divides each sentence into [(w1, w2, w3), (w2, w3, w4) ...]
    # counts the occurance of (w1, w2) and w3
    # padding tokens with pad_right, pad_left 
    for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
        
        # finds the value of the key pair (w1, w2)
        # finds the value with w3
        # adds 1 if this is found
        model[(w1, w2)][w3] += 1

# transform counts to probability 
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count
        
## ********************* Bigram Model
# make sentences into a list, appends each sentence by the "\n"
for sentence in text.split("\n"):
    
    # make each sentence into a list of words split by the " "
    sentence = sentence.split(" ")
    
    # since bigram use w1, w2
    # bigram() from nltk divides each sentence into [(w1, w2), (w2, w3), (w3, w4) ...]
    # counts the occurance of w1 and w2
    # padding tokens with pad_right, pad_left 
    for w1, w2, in bigrams(sentence, pad_right=True, pad_left=True):
        
        # finds the value of the key pair (w1, w2)
        # finds the value with w3
        # adds 1 if this is found
        model[w1][w2] += 1

# transform counts to probability 
for w1 in model:
    total_count = float(sum(model[w1].values()))
    for w2 in model[w1]:
        model[w1][w2] /= total_count


def bigram_not_finished(input_text):
    
    sentence_not_finished = True
    iteration_num = 0
    
    while sentence_not_finished:
    # selecting a random probability threshold 
    
        r = random.random()
        x = random.randint(19)
        iteration_num += 1
    
        # sets an accumulator value 
        accumulator = .0
    
        # obtain a list of keys from the text
        # tuple makes a list 
        for word in model[tuple(input_text[-1:])].keys():
        
            accumulator += model[tuple(input_text[-1:])][word]
        
            # when accumulator is greater than the random probability selected
            # choses word with highest proabability to append to the list
            if accumulator >= r:
                input_text.append(word)
                break
        
        ## when number of iterations has been reached (as no words are found)
        ## clear the input, and try and use
        if iteration_num == 20:
            input_text = []
            input_text.append(most_occur_start_word[x])
        
         ## if there is nothing left, end the loop 
        if input_text[-1:] == [None] or iteration_num == 100:
            print("Sorry, I can't respond to that!")
            sentence_not_finished = False
            break
        
    
    print(" ".join(t for t in input_text if t))


# ************************ Predicting the next word 
input_text = ["the", "news"]

sentence_not_finished = True
iteration_num = 0

while sentence_not_finished:
    # selecting a random probability threshold 
    r = random.random()

    iteration_num += 1
    
    # sets an accumulator value 
    accumulator = .0
    
    # obtain a list of keys from the text
    # tuple makes a list 
    for word in model[tuple(input_text[-2:])].keys():
        
        accumulator += model[tuple(input_text[-2:])][word]
        
        # when accumulator is greater than the random probability selected
        # choses word with highest proabability to append to the list
        if accumulator >= r:
            input_text.append(word)
            break
    
    ## when number of iterations are reached, pass it into the bigram model  
    if iteration_num == 20:
        bigram_not_finished(input_text)
        
        
    ## if there is nothing left, end the loop 
    if input_text[-2:] ==[None, None]:
        sentence_not_finished = False


# join each word together by a " "
print(" ".join(t for t in input_text if t))
    
            
    