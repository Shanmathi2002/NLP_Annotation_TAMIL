from tamil import utf8
class Ta2EnTransliterate:
    def __init__(self,tdict=None):
        if tdict:
            self.tdict = tdict
        else:
            self.tdict=dict()
        self.addPuncAndSpaceToDict()
    
    def formDictFromCommaSepTxt(self,data):
        for t in data.split('\n'):
            if ',' in t:
                key=t.strip().split(',')[0]
                val=t.strip().split(',')[1]
                self.tdict[key]=val
    
    def addPuncAndSpaceToDict(self):
        self.tdict[' ']=' '
        puncs = ''',.!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for punc in puncs:
            self.tdict[punc]=punc
        eng_let = "abcdefghiklmnopqrstuvwxyz0123456789"
        for ch in eng_let:
            self.tdict[ch]=ch
    
    def transliterate(self,line):
        tline = ''
        n = len(line)
        i=0
        dchars = ['க்','ங்','ச்','ஞ்','ட்','ண்','த்','ந்','ப்','ம்','ய்','ர்','ல்','வ்','ழ்','ள்','ற்','ன்','ஜ்','ஶ்','ஷ்','ஸ்','ஹ்','க்ஷ்']
        letters = utf8.get_letters(line)
        transf = ['']*len(letters)
#         print(letters)
        
        for i in range(len(letters)):
            letters[i] = letters[i].lower()
            if letters[i] in dchars:
                transf[i] = self.tdict[letters[i]]
#         print(transf)
        for i in range(len(letters)):
            if transf[i]=='':
                ans=''
                for curch in letters[i]:
                    if curch in self.tdict:
                        ans = ans[:-1] +  self.tdict[curch]
                    else:
                        ans+=''
                transf[i] = ans   
#         print(letters)
#         print(transf)
#         print()
        return "".join(transf)
