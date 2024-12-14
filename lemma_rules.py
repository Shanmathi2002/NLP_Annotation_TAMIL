from transliterate import Ta2EnTransliterate
from tokenization import perform_transiliteration
from tokenization import convert_to_tamil,is_english_word

sl1=('ai','kaḷ','āl','ukku','kku', 'iṉ', 'kaṇ','iṭam','ōṭu','uṭaiya','ē','āka','āṉa','il')
def tokenizing_with_clitics(input_list):
        new_list = []
        def split_word_from_end(word):
            for search_word in sl1:
                if word.endswith(search_word):
                    split_index = word.rfind(search_word)
                    if split_index != -1:
                        split1 = word[:split_index]
                        split2 = word[split_index:]
                        return [split1, split2]
            return [word]

        for word in input_list:
            splits = split_word_from_end(word)
            new_list.extend(splits)

        return new_list[0]

common_value1='āku'
common_value2='il'
common_value3='pār'
common_value4='iru'
common_value5='vā'
common_value6='paṭu'
common_value7='uḷ'
common_value8='cey'
common_value9='viṭu'
common_value10='kāṇ'
common_value11='vēṇṭu'
common_value12='vai'
common_value13='peṟu'
common_value14='koṭu'
common_value15='koḷ'
common_value16='kūṟu'
common_value17='taṭṭu'
common_value18='niṟai'
common_value19='pō'
keys_list1 = ['ākiṟār', 'āṉārkaḷ', 'āṉatu','āki','ākiṟāṉ','ākiṟāḷ','āṉār','āṉāḷ','āvar','āvēṉ','āvāṉ','āvār','āvāḷ','āka','ākak','ākiṭuccu','āṉatu','ākum','ākiṟatu',
              'ākiṉṟatu','āṉavai','ākiyatu','āṉavar','ākiya','ākalām','āvatu','āṉavai','ākiyavai','āyiṟṟu','ākiṉṟaṉar','āyiṉar','ākiṉṟaṉa','ākātu','ākavē','āṉārkaḷ',
              'ākiṟārkaḷ','āṉatai','āṉatumāṉa','āṉavaṉ','āyiṉa','ākiṉar','āyiṉāy','āyiṭuttu']

keys_list2 = ['illai', 'illāmal', 'iṉṟi','illi','illāta','villai','il','illāmaṟ','illa']

keys_list3 = ['pārttār','pārttāṉ','pārttāḷ','pārttatu','pārttuk','pārttu','pārttaṉar','pārkkiṟōm','pāruṅkaḷ','pārkkum','pārttāl','pārtta','pārkkiṟāḷ','pārkkiṟāṉ','pārppatāl',
              'pārkkiṟār','pārppataṟkāka','pārttavāṟē','pārkka','pārppōm','pārkkalām','pārppatu','pārkkap','pārttōm','pārppataṟku','pārttatāka','pārttatum','pārttal','pārttatāl',
              'pārkkaiyiṟ','pārkkiṉṟaṉar','pārkkiṟatu','pārttukkaṟōm','pārkkiṟēṉ','pārttēṉ','pārttāy','pārkkavē','pārkkat','pārppataṟkuk','pārttum','pārttup','pārttuc',
              'pārkkiṉṟaṉa']

keys_list4=['iruntār','iruntāḷ','iruntāṉ','irukiṟēṉ','iruppēṉ','iruntēṉ','irukiṟāṉ','irukkiṟāḷ','irukkiṟār','irukkiṉṟāṉ','irukkiṉṟēṉ','irukkiṉṟār','irukkiṉṟāḷ','iruppāḷ','iruppatāl',
           'iruppār','iruppāṉ','irutatu','irukkiṟatu','irukkiṉṟatu','iruppatu','irukkum','iruntu','iruntōm','iruntārkaḷ','irukkiṟārkaḷ','irukkiṉṟārkaḷ','irukkiṟōm','iruppōm','iruntatāl',
          'iruppārkaḷ','irukkiṟīrkaḷ','irukkiṉṟīrkaḷ','irukkiṉṟaṉa','irukkiṟaṉa','irunta','iruntap','iruntavai','iruppatai','irukka','irupavar','irupavaḷ','irupavaṉ','irupavarkaḷ',
          'irukkiṉṟavar','irukkiṉṟavaṉ','irukkiṉṟavaḷ','irukkiṟavar','irukkiṟavaṉ','irukkiṟavaḷ','iruntaṉa','iruppaṉa','iruntavar','iruntavaṉ','iruntavaḷ','irukkalām','irukkēṉ','iruppāy']

keys_list5=['vantār','vantāḷ','vantāṉ','varukiṟēṉ','varuvēṉ','vantēṉ','varukiṟāṉ','varukiṟāḷ','varukiṟār','varukiṉṟāṉ','varukiṉṟēṉ','varukiṉṟār','varukiṉṟāḷ','varuvāḷ','varuvatāl',
            'varuvār','varuvāṉ','vantatu','varukiṟatu','varukiṉṟatu','varuvatu','varum','vantu','vantōm','vantārkaḷ','varukiṟārkaḷ','varukiṉṟārkaḷ','varukiṟōm','varuvōm','vantatāl',
            'varuvārkaḷ','varukiṟīrkaḷ','varukiṉṟīrkaḷ','varukiṉṟaṉa','varukiṟaṉa','vanta','vantap','vantavai','varuvatu','varuvatai','vara','varupavar','varupavaḷ','varupavaṉ','varupavarkaḷ',
            'varukiṉṟavar','varukiṉṟavaṉ','varukiṉṟavaḷ','varukiṟavar','varukiṟavaṉ','varukiṟavaḷ','vantaṉa','varuvaṉa','vantavar','vantavaṉ','vantavaḷ','varalām','varēṉ','varu','varuvāy','vantaṉar']

keys_list6=['paṭṭār','paṭṭāḷ','paṭṭāṉ','paṭukiṟēṉ','paṭuvēṉ','paṭṭēṉ','paṭukiṟāṉ','paṭukiṟāḷ','paṭukiṟār','paṭukiṉṟāṉ','paṭukiṉṟēṉ','paṭukiṉṟār','paṭukiṉṟāḷ','paṭuvāḷ','paṭuvatāl',
            'paṭuvār','paṭuvāṉ','paṭṭatu','paṭukiṟatu','paṭukiṉṟatu','paṭuvatu','paṭum','paṭṭu','paṭṭōm','paṭṭārkaḷ','paṭukiṟārkaḷ','paṭukiṉṟārkaḷ','paṭukiṟōm','paṭuvōm','paṭṭatāl',
            'paṭupavarkaḷ','paṭukiṟīrkaḷ','paṭukiṉṟīrkaḷ','paṭukiṉṟaṉa','paṭukiṟaṉa','paṭṭa','paṭṭap','paṭṭavai','paṭuvatu','paṭuvatai','paṭa','paṭupavar','paṭupavaḷ','paṭupavaṉ','paṭupavarkaḷ',
            'paṭukiṉṟavar','paṭukiṉṟavaṉ','paṭukiṉṟavaḷ','paṭukiṟavar','paṭukiṟavaṉ','paṭukiṟavaḷ','paṭṭaṉa','paṭuvaṉa','paṭṭavar','paṭṭavaṉ','paṭṭavaḷ','paṭalām','paṭu','paṭuvāy']

keys_list7=['uḷḷār','uḷḷāḷ','uḷḷāṉ','uḷkiṟēṉ','uḷvēṉ','uḷḷēṉ','uḷkiṟāṉ','uḷkiṟāḷ','uḷkiṟār','uḷkiṉṟāṉ','uḷkiṉṟēṉ','uḷkiṉṟār','uḷkiṉṟāḷ','uḷvāḷ','uḷḷatāl',
            'uḷvār','uḷvāṉ','uḷḷatu','uḷkiṟatu','uḷkiṉṟatu','uḷvatu','uḷḷum','uḷḷu','uḷḷōm','uḷḷārkaḷ','uḷkiṟārkaḷ','uḷkiṉṟārkaḷ','uḷkiṟōm',
            'uḷvārkaḷ','uḷkiṟīrkaḷ','uḷkiṉṟīrkaḷ','uḷkiṉṟaṉa','uḷkiṟaṉa','uḷḷa','uḷḷap','uḷḷavai','uḷvatai','uḷpavar','uḷpavaḷ','uḷpavaṉ',
            'uḷkiṉṟavar','uḷkiṉṟavaṉ','uḷkiṉṟavaḷ','uḷkiṟavar','uḷkiṟavaṉ','uḷkiṟavaḷ','uḷḷaṉa','uḷvaṉa','uḷḷavar','uḷḷavaṉ','uḷḷavaḷ','uḷḷalām','uḷḷē','uḷḷāy']

keys_list8=['ceytār', 'ceytāḷ', 'ceytāṉ', 'ceykiṟēṉ', 'ceyvēṉ', 'ceytēṉ', 'ceykiṟāṉ', 'ceykiṟāḷ', 'ceykiṟār', 'ceykiṉṟāṉ', 'ceykiṉṟēṉ', 'ceykiṉṟār', 'ceykiṉṟāḷ', 'ceyvāḷ','ceyvatāl',
            'ceyvār', 'ceyvāṉ', 'ceytatu', 'ceykiṟatu', 'ceykiṉṟatu', 'ceyvatu', 'ceyyum', 'ceytu', 'ceytōm', 'ceytārkaḷ', 'ceykiṟārkaḷ', 'ceykiṉṟārkaḷ', 'ceykiṟōm', 'ceyvōm','ceytatāl',
            'ceyvārkaḷ', 'ceykiṟīrkaḷ', 'ceykiṉṟīrkaḷ', 'ceykiṉṟaṉa', 'ceykiṟaṉa', 'ceyta', 'ceytappa', 'ceytavai', 'ceyvatu', 'ceyvatai', 'ceyya', 'ceypavar', 'ceypavaḷ', 'ceypavaṉ','ceypavarkaḷ',
            'ceykiṉṟavar', 'ceykiṉṟavaṉ', 'ceykiṉṟavaḷ', 'ceykiṟavar', 'ceykiṟavaṉ', 'ceykiṟavaḷ', 'ceytaṉa', 'ceyvaṉa', 'ceytavar', 'ceytavaṉ', 'ceytavaḷ', 'ceyyalām', 'ceyṟēṉ','ceyvāy']

keys_list9=['viṭṭār','viṭṭāḷ','viṭṭāṉ','viṭukiṟēṉ','viṭuvēṉ','viṭṭēṉ','viṭukiṟāṉ','viṭukiṟāḷ','viṭukiṟār','viṭukiṉṟāṉ','viṭukiṉṟēṉ','viṭukiṉṟār','viṭukiṉṟāḷ','viṭuvāḷ','viṭuvatāl',
            'viṭuvār','viṭuvāṉ','viṭṭatu','viṭukiṟatu','viṭukiṉṟatu','viṭuvatu','viṭum','viṭṭu','viṭṭōm','viṭṭārkaḷ','viṭukiṟārkaḷ','viṭukiṉṟārkaḷ','viṭukiṟōm','viṭuvōm','viṭṭatāl',
            'viṭuvārkaḷ','viṭukiṟīrkaḷ','viṭukiṉṟīrkaḷ','viṭukiṉṟaṉa','viṭukiṟaṉa','viṭṭa','viṭṭap','viṭṭavai','viṭuvatu','viṭuvatai','viṭa','viṭupavar','viṭupavaḷ','viṭupavaṉ','viṭupavarkaḷ',
            'viṭukiṉṟavar','viṭukiṉṟavaṉ','viṭukiṉṟavaḷ','viṭukiṟavar','viṭukiṟavaṉ','viṭukiṟavaḷ','viṭṭaṉa','viṭuvaṉa','viṭṭavar','viṭṭavaṉ','viṭṭavaḷ','viṭalām','viṭēṉ','viṭuttār']

keys_list10=['kaṇṭār','kaṇṭāḷ','kaṇṭāṉ','kāṇkiṟēṉ','kāṇvēṉ','kaṇṭēṉ','kāṇkiṟāṉ','kāṇkiṟāḷ','kāṇkiṟār','kāṇkiṉṟāṉ','kāṇkiṉṟēṉ','kāṇkiṉṟār','kāṇkiṉṟāḷ','kāṇvāḷ','kāṇpatāl','kaṇṭatāl',
            'kāṇvār','kāṇvāṉ','kāṇpēṉ','kaṇṭatu','kāṇkiṟatu','kāṇkiṉṟatu','kāṇvatu','kāṇpatu','kāṇum','kaṇṭu','kaṇṭōm','kaṇṭārkaḷ','kāṇkiṟārkaḷ','kāṇkiṉṟārkaḷ','kāṇkiṟōm','kāṇpōm',
            'kāṇvōm','kāṇvārkaḷ','kāṇkiṟīrkaḷ','kāṇkiṉṟīrkaḷ','kāṇkiṉṟaṉa','kāṇkiṟaṉa','kaṇṭa','kaṇṭap','kaṇtavai','kāṇvatu','kāṇvatai','kāṇpavar','kāṇpavaḷ','kāṇpavaṉ','kāṇpavarkaḷ',
            'kāṇkiṉṟavar','kāṇkiṉṟavaṉ','kāṇkiṉṟavaḷ','kāṇkiṟavar','kāṇkiṟavaṉ','kāṇkiṟavaḷ','kaṇtaṉa','kāṇvaṉa','kaṇtavar','kaṇtavaṉ','kaṇtavaḷ','kāṇalām','kaṇṭum','kāṇap','kāṇa'
            ,'kaṇtāy']

keys_list11= ['vēṇṭiṉār', 'vēṇṭiṉāḷ', 'vēṇṭiṉāṉ', 'vēṇṭiṉēṉ', 'vēṇṭuvēṉ','vēṇṭukiṟāṉ', 'vēṇṭukiṟāḷ', 'vēṇṭukiṟār', 'vēṇṭukiṉṟēṉ', 'vēṇṭukiṉṟēṉ','vēṇṭukiṉṟār', 'vēṇṭukiṉṟāḷ', 'vēṇṭuvatāl',
            'vēṇṭuvāḷ', 'vēṇṭuvār', 'vēṇṭuvāṉ','vēṇṭātu', 'vēṇṭukiṟatu', 'vēṇṭukiṉṟatu', 'vēṇṭuvatu', 'Vēṇṭum', 'vēṇṭu', 'vēṇṭiṉōm', 'vēṇṭiṉārkaḷ', 'vēṇṭukiṟārkaḷ','vēṇṭiyatāl',
            'vēṇṭukiṉṟārkaḷ', 'vēṇṭukiṟōm', 'vēṇṭuvōm', 'vēṇṭuvārkaḷ','vēṇṭukiṟīrkaḷ', 'vēṇṭukiṉṟīrkaḷ', 'vēṇṭukiṉṟaṉa', 'vēṇṭukiṟāṉā','vēṇṭiya', 'vēṇṭiyappa', 'vēṇṭiyavai',
            'vēṇṭuvatu', 'vēṇṭuvatai', 'vēṇṭa','Vēṇṭupavar', 'vēṇṭupavaḷ', 'vēṇṭupavaṉ', 'vēṇṭupavarkaḷ','vēṇṭukiṉṟavar','vēṇṭukiṉṟavaṉ', 'vēṇṭukiṉṟavaḷ', 'vēṇṭukiṟavar', 'vēṇṭukiṟavaṉ',
            'vēṇṭukiṟavaḷ', 'vēṇṭiṉāṉā', 'vēṇṭiyavar', 'vēṇṭiyavaṉ','vēṇṭiyavaḷ', 'vēṇṭalām', 'vēṉṟēṉ']

keys_list12=['vaittār','vaittāḷ','vaittāṉ','vaikkiṟēṉ','vaippēṉ','vaittēṉ','vaikkiṟāṉ','vaikkiṟāḷ','vaikkiṟār','vaikkiṉṟāṉ','vaikkiṉṟēṉ','vaikkiṉṟār','vaikkiṉṟāḷ','vaippāḷ','vaittatāl',
            'vaippār','vaippāṉ','vaittatu','vaikkiṟatu','vaikkiṉṟatu','vaippatu','vaikkum','vaittu','vaittōm','vaittārkaḷ','vaikkiṟārkaḷ','vaikkiṉṟārkaḷ','vaikkiṟōm','vaippōm','vaippatāl',
            'vaippārkaḷ','vaikkiṟīrkaḷ','vaikkiṉṟīrkaḷ','vaikkiṉṟaṉa','vaikkiṟaṉa','vaitta','vaittap','vaittavai','vaippatai','vaipavar','vaipavaḷ','vaipavaṉ','vaipavarkaḷ',
            'vaikkiṉṟavar','vaikkiṉṟavaṉ','vaikkiṉṟavaḷ','vaikkiṟavar','vaikkiṟavaṉ','vaikkiṟavaḷ','vaittaṉa','vaippaṉa','vaittavar','vaittavaṉ','vaittavaḷ','vaikkalām',
             'vaikka','vaippar','vaittāy']

keys_list13=['peṟṟār','peṟṟāḷ','peṟṟāṉ','peṟukiṟēṉ','peṟuvēṉ','peṟṟēṉ','peṟukiṟāṉ','peṟukiṟāḷ','peṟukiṟār','peṟukiṉṟāṉ','peṟukiṉṟēṉ','peṟukiṉṟār','peṟukiṉṟāḷ','peṟuvāḷ','peṟuvatāl'
            'peṟuvār','peṟuvāṉ','peṟṟatu','peṟukiṟatu','peṟukiṉṟatu','peṟuvatu','peṟukkum','peṟṟu','peṟṟuk','peṟṟōm','peṟṟārkaḷ','peṟukiṟārkaḷ','peṟukiṉṟārkaḷ','peṟukiṟōm','peṟuvōm','peṟṟatāl',
            'peṟuvārkaḷ','peṟukiṟīrkaḷ','peṟukiṉṟīrkaḷ','peṟukiṉṟaṉa','peṟukiṟaṉa','peṟṟa','peṟṟap','peṟṟavai','peṟuvatai','peṟupavar','peṟupavaḷ','peṟupavaṉ','peṟupavarkaḷ',
            'peṟukiṉṟavar','peṟukiṉṟavaṉ','peṟukiṉṟavaḷ','peṟukiṟavar','peṟukiṟavaṉ','peṟukiṟavaḷ','peṟṟaṉa','peṟuvaṉa','peṟṟavar','peṟṟavaṉ','peṟṟavaḷ','peṟalām','peṟṟēṉ',
             'peṟukka','peṟuvar','peṟum','peṟuvāy']

keys_list14=['koṭuttār','koṭuttāḷ','koṭuttāṉ','koṭukkiṟēṉ','koṭuppēṉ','koṭuttēṉ','koṭukkiṟāṉ','koṭukkiṟāḷ','koṭukkiṟār','koṭukkiṉṟāṉ','koṭukkiṉṟēṉ','koṭukkiṉṟār','koṭukkiṉṟāḷ','koṭuppāḷ','koṭuttatāl',
            'koṭuppār','koṭuppāṉ','koṭuttatu','koṭukkiṟatu','koṭukkiṉṟatu','koṭuppatu','koṭukkum','koṭuttu','koṭuttōm','koṭuttārkaḷ','koṭukkiṟārkaḷ','koṭukkiṉṟārkaḷ','koṭukkiṟōm','koṭuppōm','koṭuttatāl',
            'koṭuppārkaḷ','koṭukkiṟīrkaḷ','koṭukkiṉṟīrkaḷ','koṭukkiṉṟaṉa','koṭukkiṟaṉa','koṭutta','koṭuttap','koṭuttavai','koṭuppatai','koṭupavar','koṭupavaḷ','koṭupavaṉ','koṭupavarkaḷ',
            'koṭukkiṉṟavar','koṭukkiṉṟavaṉ','koṭukkiṉṟavaḷ','koṭukkiṟavar','koṭukkiṟavaṉ','koṭukkiṟavaḷ','koṭuttaṉa','koṭuppaṉa','koṭuttavar','koṭuttavaṉ','koṭuttavaḷ','koṭukkalām',
             'koṭukka','koṭuppar','koṭuttāy']

keys_list15=['koṇṭār', 'koṇṭāḷ', 'koṇṭāṉ', 'koḷkiṟēṉ', 'koḷvēṉ','koṇṭēṉ', 'koḷkiṟāṉ', 'koḷkiṟāḷ', 'koḷkiṟār', 'koḷkiṉṟāṉ','koḷkiṉṟēṉ', 'koḷkiṉṟār', 'koḷkiṉṟāḷ', 'koḷvāḷ', 'koḷvār',
             'koḷvāṉ', 'koṉṟatu', 'koḷkiṟatu', 'koḷkiṉṟatu', 'koḷvatu', 'koḷḷum','koṉṟu', 'koṉṟōm', 'koṉṟārkaḷ', 'koḷkiṟārkaḷ', 'koḷkiṉṟārkaḷ','koḷkiṟōm', 'koḷvōm', 'koḷvārkaḷ','koḷvatāl',
             'koḷkiṟīrkaḷ', 'koḷkiṉṟīrkaḷ','koḷkiṟaṉa', 'koḷkiṉṟaṉa', 'koṉṟa', 'koṇṟappa', 'koṇṟatai','koḷvatu', 'koḷvatai', 'koḷḷa', 'koḷpavar', 'koḷpavaḷ','koḷpavaṉ',
             'koḷkiṉṟavar','koḷkiṉṟavaṉ', 'koḷkiṉṟavaḷ', 'koḷkiṉṟavar', 'koḷkiṉṟavaṉ', 'koḷkiṉṟavaḷ','koṉṟaṉa', 'koḷvaṉa', 'koṉṟavar', 'koṉṟavaṉ', 'koḷḷalām', 'kolṟēṉ','koṇṭu']

keys_list16=['kūṟa','kūṟi','kūṟiṉār','kūṟiṉāḷ','kūṟiṉāṉ','kūṟukiṟēṉ','kūṟuvēṉ','kūṟiṉēṉ','kūṟukiṟāṉ','kūṟukiṟāḷ','kūṟukiṟār','kūṟukiṉṟāṉ','kūṟukiṉṟēṉ','kūṟukiṉṟār','kūṟukiṉṟāḷ','kūṟuvāḷ','kūṟuvatāl',
            'kūṟuvār','kūṟuvāṉ','kūṟiyatu','kūṟukiṟatu','kūṟukiṉṟatu','kūṟuvatu','kūṟum','kūṟiṉōm','kūṟiṉārkaḷ','kūṟukiṟārkaḷ','kūṟukiṉṟārkaḷ','kūṟukiṟōm','kūṟuvōm','kūṟiyatāl',
            'kūṟuvārkaḷ','kūṟukiṟīrkaḷ','kūṟukiṉṟīrkaḷ','kūṟukiṉṟaṉa','kūṟukiṟaṉa','kūṟiṉa','kūṟiṉap','kūṟiya','kūṟiyavai','kūṟuvatai','kūṟap','kūṟupavar','kūṟupavaḷ','kūṟupavaṉ','kūṟupavarkaḷ',
            'kūṟukiṉṟavar','kūṟukiṉṟavaṉ','kūṟukiṉṟavaḷ','kūṟukiṟavar','kūṟukiṟavaṉ','kūṟukiṟavaḷ','kūṟiṉa','kūṟuvaṉa','kūṟiyavar','kūṟiyavaṉ','kūṟiyavaḷ','kūṟalām','kūṟuvāy']

keys_list17=['taṭṭa','taṭṭi','taṭṭiṉār','taṭṭiṉāḷ','taṭṭiṉāṉ','taṭṭukiṟēṉ','taṭṭuvēṉ','taṭṭiṉēṉ','taṭṭukiṟāṉ','taṭṭukiṟāḷ','taṭṭukiṟār','taṭṭukiṉṟāṉ','taṭṭukiṉṟēṉ','taṭṭukiṉṟār','taṭṭukiṉṟāḷ','taṭṭuvāḷ','taṭṭuvatāl',
            'taṭṭuvār','taṭṭuvāṉ','taṭṭiyatu','taṭṭukiṟatu','taṭṭukiṉṟatu','taṭṭuvatu','taṭṭum','taṭṭiṉōm','taṭṭiṉārkaḷ','taṭṭukiṟārkaḷ','taṭṭukiṉṟārkaḷ','taṭṭukiṟōm','taṭṭuvōm','taṭṭiyatāl',
            'taṭṭuvārkaḷ','taṭṭukiṟīrkaḷ','taṭṭukiṉṟīrkaḷ','taṭṭukiṉṟaṉa','taṭṭukiṟaṉa','taṭṭiṉa','taṭṭiya','taṭṭiyavai','taṭṭuvatai','taṭṭap','taṭṭupavar','taṭṭupavaḷ','taṭṭupavaṉ','taṭṭupavarkaḷ',
            'taṭṭukiṉṟavar','taṭṭukiṉṟavaṉ','taṭṭukiṉṟavaḷ','taṭṭukiṟavar','taṭṭukiṟavaṉ','taṭṭukiṟavaḷ','taṭṭuvaṉa','taṭṭiyavar','taṭṭiyavaṉ','taṭṭiyavaḷ','taṭṭalām','taṭṭuvāy']

keys_list18=['niṟainta','niṟaikira','niṟaintu','niṟaintār','niṟaintāḷ','niṟaintāṉ','niṟaikiṟēṉ','niṟaivēṉ','niṟaintēṉ','niṟaikiṟāṉ','niṟaikiṟāḷ','niṟaikiṟār','niṟaikiṉṟāṉ','niṟaikiṉṟēṉ','niṟaikiṉṟār','niṟaikiṉṟāḷ','niṟaivāḷ','niṟaivatāl',
            'niṟaivār','niṟaivāṉ','niṟaiyatu','niṟaikiṟatu','niṟaikiṉṟatu','niṟaivatu','niṟaiyum','niṟaintōm','niṟaintārkaḷ','niṟaikiṟārkaḷ','niṟaikiṉṟārkaḷ','niṟaikiṟōm','niṟaivōm','niṟaiyatāl',
            'niṟaivārkaḷ','niṟaikiṟīrkaḷ','niṟaikiṉṟīrkaḷ','niṟaikiṉṟaṉa','niṟaikiṟaṉa','niṟaiyaṉa','niṟaiya','niṟaiyavai','niṟaivatai','niṟaiyap','niṟaipavar','niṟaipavaḷ','niṟaipavaṉ','niṟaipavarkaḷ',
            'niṟaikiṉṟavar','niṟaikiṉṟavaṉ','niṟaikiṉṟavaḷ','niṟaikiṟavar','niṟaikiṟavaṉ','niṟaikiṟavaḷ','niṟaivaṉa','niṟaipavar','niṟaipavaṉ','niṟaipavaḷ','niṟaiyalām','niṟaivāy']
keys_list19 = ['pōkiṟēṉ', 'pōkiṉṟavaṉ', 'pōkiṉṟavaḷ','pōkiṟavar','pōvēṉ']
dict_list=[{key: common_value1 for key in keys_list1},
           {key: common_value2 for key in keys_list2},
           {key: common_value3 for key in keys_list3},
           {key: common_value4 for key in keys_list4},
           {key: common_value5 for key in keys_list5},
           {key: common_value6 for key in keys_list6},
           {key: common_value7 for key in keys_list7},
           {key: common_value8 for key in keys_list8},
           {key: common_value9 for key in keys_list9},
           {key: common_value10 for key in keys_list10},
           {key: common_value11 for key in keys_list11},
           {key: common_value12 for key in keys_list12},
           {key: common_value13 for key in keys_list13},
           {key: common_value14 for key in keys_list14},
           {key: common_value15 for key in keys_list15},
           {key: common_value16 for key in keys_list16},
           {key: common_value17 for key in keys_list17},
           {key: common_value18 for key in keys_list18},
           {key: common_value19 for key in keys_list19}]
my_dict={}
for dictionary in dict_list:
    my_dict.update(dictionary)

punctuation_string = ".,!?;’‘‘”“"


def lem_res(user_input):
    ex_case=["um","anta","ai","es","pi","vatu","pas","m","cella"]
    inp=str(user_input)
    k = perform_transiliteration(inp)
    if k in ".,!?;’‘‘”“" or k.isdigit() or ((is_english_word(k)==True) and k not in ex_case):
        tamil_lemma=k
    elif k in my_dict:
        corresponding_value = my_dict[k]
        tamil_lemma=convert_to_tamil(corresponding_value)
    elif k.endswith(sl1) and len(k)>1:
        result = tokenizing_with_clitics([k])
        tamil_lemma=convert_to_tamil(result)
    else:
        tamil_lemma=convert_to_tamil(k)
    return tamil_lemma