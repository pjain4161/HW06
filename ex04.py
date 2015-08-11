def read_write():
    
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
    fin.close()
    
    
    with open("new_roster.txt", "w") as f:
        for word in list_:
            f.write(word)
            f.write("\r\n")
    
#     

def main():
    read_write()
    
#     fin = open("file.txt", "r")
#     for line in fin:
#         print line    
    
    
if __name__ == '__main__':

    main()