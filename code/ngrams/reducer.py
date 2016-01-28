#!/usr/bin/env python3

import sys

current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t',1)
    try:
        count = int(count)
    except ValueError:
        continue
    if word == current_word:
        current_count = current_count + count
    else:
        if current_word:
            print("%s\t%s" % (current_count+10000,current_word))
        current_word = word
        current_count = count
    
if current_word == word:
    print("%s\t%s" % (current_count+10000,current_word))
    

