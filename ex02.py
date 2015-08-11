#imports
from random import randint

def write_to_file():
    fout = open("file.txt", "w")
    x = 0
    while(x<10):
        y = randint(0,9)
        
        fout.write(str(y))
        fout.write("\r\n")
        x += 1
    fout.close()
    


def main():
    write_to_file()
    
#     fin = open("file.txt", "r")
#     for line in fin:
#         print line    
    
    
if __name__ == '__main__':

    main()