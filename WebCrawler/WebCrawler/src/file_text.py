'''
Created on Mar 24, 2014

@author: soumyasreekumar
'''

import urllib
from urllib.request import urlopen 
from html.parser import HTMLParser
import re
import time
import random



def main():
    i=0 
    
    f = open('input.txt','r')
    myList =[]
    for line in f.readlines() : 
        myList.append(line)  
    f.close()  
    print(myList)
    
    f = open('index.txt','w').close()
     
    while i < 100 and len(myList) > 0:
        url = myList[i]   
        htmlfile = urllib.request.urlopen(url)  
        htmltext = htmlfile.read()                                   
        #links = re.findall(b'<link.*?href="(.*?)"',htmltext)   
        links = re.findall(b'"((http)s?://.*?)"',htmltext)
        
        #print (links)
                             
        for link in range (0 ,len(links)):       
            myList.append(link)
            if link == 50:                                 
                break            
            
            myList.pop(0)
                   
            random.shuffle(myList)
            
            print(myList) 
            time.sleep(5)
            
            new_file = str(i) + '.html'
            
            with open(new_file,'wb') as myfile:
                myfile.write(link) 
                with open('index.txt','a') as storeFileName :
                    storeFileName.write(new_file + "  " + url)
                    htmlfile.close() 
                    i+=1
                    print (myList)
       
                
            
           
             
            
                                  
        
 
 
if __name__ == "__main__" :   
    main() 
    

 

           
    
      
      
