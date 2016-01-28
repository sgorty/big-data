#!/usr/bin/env python3
from random import randint

index = {}

def create_index(index_file):
    global index
    with open(index_file,"r") as file:
        for line in file:
            (count,ngram) = line.strip().split("\t")
            count = int(count)-10000
            words = ngram.split("~")
            key = "~".join(words[0:-1])
            nextword = words[-1]
            #print(count,ngram,words,key,nextword)
            if key in index:
                index[key].append((nextword,count))
            else:
                index[key] = [(nextword,count)]

def next_word2(words):
    key = "~".join(words)
    if key in index:
        print(index[key])
        sum = 0
        for word,count in index[key]:
            print(word,count)
            sum += count
        return index[key][0][0]
    
def next_word(words):
    key = "~".join(words)
    if key in index:
        print(index[key])
        sum = 0
        for word,count in index[key]:
            print(word,count)
            sum += count
        n = randint(1,sum)
        for word,count in index[key]:
            print(word,count)
            sum += count
            if sum >= n:
                return word
        return "<ERROR>"
 
create_index("ngrams.3.list.txt")
words = ['was','nothing']
for i in range(0,1000):
    print(words[-2:])
    words.append(next_word(words[-2:]))
print(" ".join(words).replace("###","\n"))


