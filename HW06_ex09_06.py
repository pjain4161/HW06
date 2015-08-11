#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports

# Body
def is_abecedarian(word):
    i = 0
    j = 1
    for i in range(len(word)-1):
        if word[i].lower() <= word[j].lower() :
            j += 1
            continue
        else:
            return False
    return True
            
def read_from_file():
    
    count = 0
    fin = open("words.txt", "r")
    for line in fin:
        words = line.split()    #get each line of file
        for word in words:      #get each word of each line
            res = is_abecedarian(word)   # check if word has an 'e' or not
            if res == True:
                count += 1
    
    print "# number of abecedarian words: {0}" .format(count)
            

##############################################################################
def main():
    print is_abecedarian("DeFAA")
    print is_abecedarian("AADeyZ")
    read_from_file()

if __name__ == '__main__':
    main()
