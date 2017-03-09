
# coding: utf-8

# In[65]:

import string


# In[68]:

'''printing function'''

def dict_printer(d):
    output = ""
    for k in d.keys():
        output += k + ',' + str(d[k]) + "\n"
    return output

'''
input - text file
output - dictionary with word and number of occurences
description - the function splits each line in a text file and 
counts the number of distinct words in each line and puts them in a dictionary'''

def count(file_name):
    file = open(file_name,'r') 
    dic1 = {}
    for line in file:
        line = line.lower() #lower case
        replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
        line = line.translate(replace_punctuation) #removes all punctuation and replaces by white space
        a = line.split() #tokenizes line by space 
        for i in range(0,len(a)):
            if a[i] not in dic1:
                dic1[a[i]] = 1
            else:
                dic1[a[i]]+=1
    return dict_printer(dic1)


# In[72]:

text_file = open("output.txt", "w")
text_file.write(count('alice30.txt'))
text_file.close()

