with open('abcd','r') as file1:
    file_data=file1.read()
file_data=file_data.lower()
requirement="abcdefghijklmnopqrstuvwxyz"
analysed=''
for char in file_data:
    if char not in requirement:
        analysed=analysed+char
analysed.replace('  ','')

print(analysed)
with open('puncfile.txt','w') as file_write:
    file_write.write(analysed)
'''this much is for text analysis and reading with writing code in python'''
'''now we will start to use actually analyse and remove punctuations from the files the file name is 
readfilesprogram2.py'''
