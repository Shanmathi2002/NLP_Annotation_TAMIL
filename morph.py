import re

def is_roman_numeral(s):
    # Define a regular expression pattern to match Roman numerals
    pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    
    # Use re.match to check if the string matches the Roman numeral pattern
    return bool(re.match(pattern, s))


s1= ('kiṟatu','kiṉṟatu','kiṟēṉ','kiṟāṉ','kiṟāḷ','kiṉṟāṉ','kiṉṟēṉ','kiṉṟār','kiṉṟāḷ','vatu','tuk','kiṟōm','ka','patu',
    'kap','ataṟku','kiṉṟaṉar','kavē','kat','ataṟkuk','kiṉṟaṉa','kiṟārkaḷ','kiṉṟārkaḷ','kiṟōm','kiṟīrkaḷ','kiṉṟīrkaḷ','kiṟaṉa','ra'
    ,'pavar','pavaḷ','pavaṉ','pavarkaḷ','kiṉṟavar','kiṉṟavaṉ','kiṉṟavaḷ','kiṟavar','kiṟavaṉ','kiṟavaḷ','ru','kiṟay','ṭu','illai','ḷaṉa','ātu',
     'ḷatu','kiṟār','kiṟīr','kiṉṟīr')
s2= ('tatu','taṉar','tār','tāṉ','tāḷ','tāl','ta','ataṟkāka','vāṟē','tu','tup','tuc','tōm','tāka','atum','tēṉ','pēṉ','tāy','tum','tārkaḷ'
     ,'tap','avai','tavar','tavaḷ','tavaṉ','tavarkaḷ','taṉa','rēṉ','ṉār','ṉāṉ','ṉāḷ','ṉārkaḷ','tārkaḷ','ṉar','ṭīrkaḷ')
s3= ('uṅkaḷ','kum','pōm','alām','kaṟōm','vēṉ','pēṉ','vāḷ','atāl','vār','vāṉ','pāḷ','pār','pāṉ','vōm','vārkaḷ','atai','vaṉa','paṉa','vāy')
P1= ('nāṉ','eṉ','eṉakku','eṉṉai','eṉṉāl','eṉatu','Eṉṉiṭam','nāṅkaḷ','nām','eṉṉōṭu','namatu','namakku','nam\'māl','nam\'mai','nam\'miṭam','eṅkaḷ','eṅkaḷāl',
     'eṅkaḷai','eṅkaḷukku','eṅkaḷiliṭam','emakku','em\'mai','ematu','eṅkaḷiṉ','nam\'mil','nam\'miṉ','eṉṉil','eṅkaḷil')
P2= ('nī','uṉ','uṉakku','uṉṉai','uṉṉāl','uṉatu','uṉṉiṭam','nīṅkaḷ','niṉatu','uṉṉōṭu','uṅkaḷatu','niṉakku','uṅkaḷ','uṅkaḷai','uṅkaḷāl','uṅkaḷukku','uṅkaḷiliṭam','umakku',
     'um\'mai','umatu','uṅkaḷiṉ','niṉakku','uṅkaḷil','uṉṉil')
Pe1=('ēṉ','ōm')
Pe2=('īrkaḷ','īr')
po1=('illai','iṉṟi','illi','illāta','villai','il','illāmaṟ','illa','alla')
n=('ātu','āmal')
k='kaḷ'
t='ṉar'
case1='kku'
case2='ai'
case3='il'
case4='iṭam'
case5='iṉ'
case6='āl'
case7='atu'
case8='kāka'
case9='uṭaṉ'
case10='ōṭu'
case11='iruntu'
punctuations = {
    '.': 'Peri',
    ',': 'Comm',
    '(': 'Brck',
    ')': 'Brck',
    '“': 'Quot',
    '”': 'Quot',
    '‘': 'Quot',
    '’': 'Quot',
    '?': 'Qest',
    '-': 'Dash',
    '!': 'Excl',
    ':': 'Colo',
    ';': 'Semi'  
}

def get_punctType(pos, word):
    return punctuations.get(word, None)

def morph(pos,word):
  morph=[]
  if pos=='ADJ' or pos=='ADV' or pos=='PART' or pos=='SCONJ' or pos=='CCONJ' or pos=='INTJ' or pos=='UNKNOWN' or pos=='X':
          
          morph.append("_")
  elif pos=='ADP':
          
          morph.append("AdpType=Post")
  elif pos=='VERB' or pos=='AUX':
        if(word.endswith(k) or word.endswith(t)):
            morph.append('Number=Plur')
        else:
            morph.append('Number=Sing')
        if(word.endswith(Pe1)):
             
             morph.append("Person=1")
        elif(word.endswith(Pe2)):
             
              morph.append("Person=2")
        else:
              
              morph.append("Person=3")

        if(word.endswith(n) or word in po1):
           
            morph.append("Polarity=Neg")
        else:
              
              morph.append("Polarity=Pos")
        if(word.endswith(s1)):
            
            morph.append('Tense=Present')
        elif(word.endswith(s2)):
             
              morph.append('Tense=Past')
        elif(word.endswith(s3)):
             
              morph.append('Tense=Future')
        else:
              
              morph.append('Tense=Unknown')
        
  elif pos=='NOUN' or pos=='PROPN' or pos=='PRON': 
        if(word.endswith(case1)):
            
            morph.append('Case=Dat')
        elif(word.endswith(case2)):
             
              morph.append('Case=Acc')
        elif(word.endswith(case3) or word.endswith(case4)):
             
              morph.append('Case=Loc')
        elif(word.endswith(case5) or word.endswith(case7)):
              
              morph.append('Case=Gen')
        elif(word.endswith(case9) or word.endswith(case10)):
          
              morph.append('Case=Com')
        elif(word.endswith(case6)):
              
              morph.append('Case=Ins')
        elif(word.endswith(case8)):
              
              morph.append('Case=Ben')
        elif(word.endswith(case11)):
              
              morph.append('Case=Abl')
        else:
              
              morph.append('Case=Nom')
        if(word.endswith(k)):
            morph.append('Number=Plur')
        else:
            morph.append('Number=Sing')
        if pos=='PRON':
            if(word.endswith(P1)):
                  
                  morph.append("Person=1")
            elif(word.endswith(P2)):
                  
                  morph.append("Person=2")
            else:
                  
                  morph.append("Person=3")

  elif pos=='PUNCT':
       
       punct= get_punctType(pos,word)
       if punct is not None:
          morph.append(f'PunctType={punct}')
       else:
          morph.append('PunctType=UNKNOWN')
  elif pos=='DET':
       
       if(word.endswith(n) or word in po1):
          morph.append("Polarity=Neg")
       else:
            
            morph.append("Polarity=Pos")
  elif pos=='NUM':
       if(word.isdigit()):
            morph.append("Number=Count")
            morph.append("NumForm=Digit")
       elif(is_roman_numeral(word)):
            morph.append("Number=Count")
            morph.append("NumForm=Roman")
       else:
            morph.append("Number=Count")
            morph.append("NumForm=Word")
 
  return morph  