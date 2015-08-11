#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou:
#   - # of words that use all aeiouy:
##############################################################################
# Imports

# Body
def uses_all(word, letters):
    for letter in letters:
        if letter not in word:
            return False
        else:
            continue
    return True

def read_from_file():
    
    count1 = 0
    count2 = 0
#     list_ =[]
    fin = open("words.txt", "r")
    for line in fin:
        words = line.split()    #get each line of file
        for word in words:      #get each word of each line
            res = uses_all(word, "aeiou")   # check if word has an 'e' or not
            if res == True:
                count1 += 1
            
            res = uses_all(word, "aeiouy")   # check if word has an 'e' or not
            if res == True:
                count2 += 1
     
    print "# of words that use all aeiou: {0}" .format(count1)
    print "# of words that use all aeiouy: {0}" .format(count2)
    
    
    
                    
    # of words that use all aeiouy
#     for word in list_:
        
    
    
##############################################################################
def main():
    print uses_all("hello", "el")
    print uses_all("hi my name is pooja jain", "pxz")
    print uses_all("banana", "ANZ")
    print uses_all("Berkeley", "ey")
    print uses_all("cryptography", "c ")
    print
    read_from_file()
    

if __name__ == '__main__':
    main()
