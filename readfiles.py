# file=open('abcd','w')
# print(file)
# print(file.name)
# print(file.mode)
# file.close()
'''using with to use it more pytohnically and more systematically'''
with open('abcd','r') as file1:
    file_data=file1.read()
    print(file1)
print(file1.closed)
print(file_data)
file_fmt=file_data.upper().strip()
with open('abcd','w') as filedata:
    filedata.write(file_fmt)
