"to get all the punctuations "
import string
punc_list = string.punctuation
with open('puncfile.txt','w') as file1:
    file1.write(punc_list)