'''
Created on Mar 29, 2014

@author: soumyasreekumar
'''
import urllib
from urllib.request import urlopen 
import re
import os
import time
import random

def main():
    i=0 

    f = open('input.txt','r')
    myList =[]
    for line in f.readlines() : 
        myList.append(line)  
    f.close()  
    
    index_file = open('index.txt','w')
    
    if len(myList) > 0:
        data_folder_path = os.path.join(os.getcwd(), 'data')
        if not os.path.exists(data_folder_path):
            os.makedirs(data_folder_path)
        
    while i < 10 and len(myList) > 0:
        print('---------------'+str(i)+'----------------------')
        for link in myList:
            print(link)
        url = myList.pop(0)

        if url[0:3] == "www":
            url = "http://"+url
        print('requesting url... ' +url)
        htmlfile = urllib.request.urlopen(url)  
        htmltext = htmlfile.read()
        i+=1
        data_filename = str(i) + '.html'
        data_file_path = os.path.join(data_folder_path, data_filename)
        with open(data_file_path,'wb') as myfile:
            print(data_file_path)
            myfile.write(htmltext)
            myfile.close()
        index_file.write(data_filename + "  " + url+"\n")
        
        links = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(htmltext))
        for link in links:
            myList.append(link)

        random.shuffle(myList)
        time.sleep(3) 
          
    index_file.close();
    
    
if __name__ == "__main__" :   
    
    main() 