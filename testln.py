from posixpath import split


text="I am groot, I am groot!, I am groot. I am groot?"
text_fmt=text.replace('.','').replace(',','').replace('!','').replace('?','')
print(text_fmt.upper())
split_fmt=text_fmt.split()
print(split_fmt)
splitset=set(split_fmt)
print(splitset)
for unique in splitset:
    print(unique)
    print(split_fmt.count(unique))
##############################################################################
# dictionary parameters
keys = ['a', 'b', 'c']
values = [1, 2, 3]
# create dictionary func.
def create_dictionary(keys, values):
    result = {} # empty dictionary
    for key, value in zip(keys, values):
        result[key] = value
    return result
# use create_dictionary func.
print(create_dictionary(keys=keys, values=values))