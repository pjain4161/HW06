#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
def has_no_e(s):
    
    if ('e' not in s) and ('E' not in s):
        return True
    else:
        return False
    
  
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports


# Body
def read_from_file():
    
    count_total = 0.0
    count_without_e = 0.0
    list_ =[]
    fin = open("words.txt", "r")
    for line in fin:
        words = line.split()    #get each line of file
        for word in words:      #get each word of each line
            count_total += 1
            res = has_no_e(word)   # check if word has an 'e' or not
            if res == True:
                count_without_e += 1
                list_.append(word)
                 
    for word in list_:
        print word + "%"
                 
    print "total words = {0}" .format(int(count_total))  
    print "total words without e = {0} " .format(int(count_without_e))  
    try:
        percentage = (count_without_e/count_total)*100
    except:
        print "No word in file"
    else:
        print "percentage = {0}" .format(percentage)        

##############################################################################
def main():
    print has_no_e("hate")
    print has_no_e("hatE")
    print has_no_e("banana")
    print " words that have no 'e' in 'words.text' are :"
    read_from_file()

if __name__ == '__main__':
    main()
