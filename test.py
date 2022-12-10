class analysedText(object):
    
    def __init__ (self, text):
        self.text=text
        text_fmt=text.replace('.','').replace(',','').replace('!','').replace('?','')
        fmtText=text.lower()
        return text_fmt,fmtText
        # TODO: Remove the punctuation from <text> and make it lower case.
        # TODO: Assign the formatted text to a new attribute called "fmtText"

    def freqAll(self):
        splitText=self.fmtText.split()
        txtSet= set(splitText)
        for unique in txtSet:
            uniqueTxt=txtSet.unique()
            uniqueCnt=splitText.count(unique)
        dict1={}
        for uniquetx, uniqueno in zip(uniqueTxt,uniqueCnt):
                dict1[uniquetx]=uniqueno
        return dict1

        
        # TODO: Split the text into a list of words  
        # TODO: Create a dictionary with the unique words in the text as keys
        # and the number of times they occur in the text as values
      
        # return the created dictionary
    
    def freqOf(self, word):
        for word in txtset:
            uniqueTxt=txtSet.unique()
            uniqueCnt=splitText.count(unique)
        return print(uniqueTxt,":",uniqueCnt)
            
        
        # TODO: return the number of occurrences of <word> in <fmtText>
sample=analysedText("i am groot ai am an gororo tasdf")
sample.freqAll
