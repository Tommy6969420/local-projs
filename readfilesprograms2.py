with open('abcd','r') as file1:
    file_data=file1.read()
with open('puncfile.txt','r') as file2:
    punc_data=file2.read()
analysed=''
for char in file_data:
    if char not in punc_data:
        analysed=analysed + char
print(analysed)
'''this program gives the analysed text or texts without punctuations'''