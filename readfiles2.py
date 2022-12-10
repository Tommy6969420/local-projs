'''using with to use it more pytohnically and more systematically'''
with open('abcd','r') as file1:
    file_data=file1.read()
    print(file1)
print(file1.closed)
print(file_data)
'''to send unpunctuated data to another file '''
file_fmt=file_data.capitalize().strip().replace('!','').replace('?','').replace('.','').replace(',','').replace(' ','')
with open('newfile1.txt','w') as filedata:
    filedata.write(file_fmt)
