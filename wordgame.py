import itertools
import random
from collections import Counter
from random import shuffle
from itertools import groupby

word=open("words.txt", "r")
user_input_low, user_input_high= input("Enter the range of word lengths (low,high): ").split(",")
user_input_low= int(user_input_low.replace("(",""))
user_input_high= int(user_input_high.replace(")",""))
word_list=[]
for words in word:  
    words=words.strip()
    if len(words) >= user_input_low and len(words) <= user_input_high: 
        word_list.append(words)
words_list_high=[]
words_list_high = [high for high in word_list if len(high) == user_input_high ]
random_word=random.choice(words_list_high) 
random_word = list(random_word)
letters_count = Counter(random_word)
anagrams = set()
for wordss in word_list:
    if not set(wordss) - set(random_word):
        check_word = set()
        for k, v in Counter(wordss).items():
            if v <= letters_count[k]:
                check_word.add(k)
        if check_word == set(wordss):
            anagrams.add(wordss)
words_list=[]
for h in anagrams:
    words_list.append(h)
words_list.sort(key=len)
hidden_list=[]
for t in words_list:
    for letter in t:
        if letter != " ":
            hide = "-" * len(t)
    hidden_list.append(hide)
final_list=[list(g) for k, g in groupby(words_list, key=len)]
b=set(itertools.chain(*final_list))
guessed_list=[]
def display():
    hidden_list.sort()
    hidden_list.sort(key=len)
    final_hidden_list=[list(g) for k, g in groupby(hidden_list, key=len)]
    shuffle(random_word)
    random_word_shuffled= ''.join(random_word)
    print(random_word_shuffled+':\n')         
    for h in final_hidden_list:
        print(h)
    print('')
display()         
while True:    
    guess = input("Enter a guess: ")
    guess_hidden= "-" * len(guess)
    if guess in guessed_list:
        print("you have already guessed that")
        display() 
    elif guess in b:
        hidden_list.remove(guess_hidden)
        hidden_list.append(guess)
        guessed_list.append(guess)
        print('Correct!','\n')        
        display()   
    elif guess == 'q':
        words_list.sort()
        words_list.sort(key=len)
        print(words_list)
        break
    elif guess not in b:
          print('Sorry. Try again','\n')        
          display()      
    if len(guessed_list) == len(words_list):
        print("Contrats you Won!")
        break 