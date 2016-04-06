'''
Created on Mar 29, 2014

@author: soumyasreekumar
'''
import urllib
from urllib.request import urlopen 
import re
import time
import random
from bs4 import BeautifulSoup
from bs4.element import SoupStrainer



def main():
    i=0 
    
    f = open('input.txt','r')
    myList =[]
    for line in f.readlines() : 
        myList.append(line)  
    f.close()  
    print(myList)
    
    f = open('index.txt','w').close()
     
    while i <len(myList):
        url = myList[i]   
        htmlfile = urllib.request.urlopen(url)  
        htmltext = htmlfile.read()                                   
        #links = re.findall(b'<link.*?href="(.*?)"',htmltext)   
        #links = re.findall(b'"((http|ftp)s?://.*?)"',htmltext)
        soup = BeautifulSoup(htmltext)
        print(htmltext)
       # myList.append(links)
        #random.shuffle(links)
        #random.randint
        #print(links) 
        #time.sleep(5)
        #new_file = str(i) + '.html'
        #with open(new_file,'wb') as myfile:
            #myfile.write(htmltext) 
            #with open('index.txt','a') as storeFileName :
             #   storeFileName.write(new_file + "  " + url)
              #  htmlfile.close()
               # i+=1
                #print (myList)
       
            
 
if __name__ == "__main__" :   
    main() 
