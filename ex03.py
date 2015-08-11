
#body
def read_from_file():
    
    count = 0
    list_ =[]
    fin = open("roster.txt", "r")
    for line in fin:
        word  = line.strip()
        if 'e' in word or 'E' in word:
            list_.append(word)
            count += 1 
    print ("count = {0}" .format(count))
    for word in list_:
        print word
            

#     

def main():
    read_from_file()
    
#     fin = open("file.txt", "r")
#     for line in fin:
#         print line    
    
    
if __name__ == '__main__':

    main()