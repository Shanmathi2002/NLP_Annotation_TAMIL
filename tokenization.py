import re
from transliterate import Ta2EnTransliterate
import enchant#pyenchant
search_list_1 = ["paṭa","paṭṭār","paṭu","paṭukiṉṟatu","paṭṭu","paṭṭaṉar", "paṭṭatu","paṭum","paṭukiṟāḷ","paṭukiṟāṉ","paṭukiṟōm","paṭukiṟār","paṭukiṟārkaḷ","paṭukiṟēṉ",
                       "paṭṭāḷ", "paṭṭāṉ","paṭukiṟatu",
                 "irukkum","irukkātu","iruntu", "iru", "irukkiṉṟatu","irunta", "iruntatu", "iruntuḷḷa","iruntēṉ","irukkiṟatu","irukkiṉṟīrkaḷ","irukkiṟatu","irukkiṟīrkaḷ",
                       "irukkiṟṟa", "irukkiṟṟaṉa","irukkiṟārkaḷ","irukkiṟṟaṉar","irukkiṟāṉ", "irukkiṟāḷ",
                 "koṇṭār","koṇṭa", "koṇṭu","koṇṭīrkaḷ","koḷḷa","koṇṭāṉ","koṇṭāḷ",
                 "viṭa", "viṭu", "viṭukiṉṟa", "viṭukiṉṟatu","viṭṭa","viṭṭu","viṭṭatu", "viṭavum","viṭṭaṉar","viṭṭaṉa","viṭṭār", "viṭṭāṉ", "viṭṭāḷ",
                 "vā", "vanta","varum","vara",
                 "uḷḷaṉar","uḷḷatu","uḷḷār","uḷḷē","uḷḷa","uḷḷaṉa",
                 "illāta","illai",
                 "vēṇṭum","vēṇṭu","vēṇṭiyatāka","paṭṭ",
                 "vaittu","vaittatu",
                 "ākiṟatu", "āṉāṉ", "āṉāḷ","āvār","āvāṉ","āvāḷ"]

search_list_2 = ["um", "ē", "ā", "āṉatu", "ō", "ām", "āki", "tāṉ","āvatu"]

tamil_transliteration = {
    'k': 'க்', 'kā': 'கா', 'ki': 'கி', 'kī': 'கீ', 'ku': 'கு', 'kū': 'கூ', 'ke': 'கெ', 'kē': 'கே', 'kai': 'கை', 'ko': 'கொ', 'kō': 'கோ', 'kau': 'கௌ',
    'ṅ': 'ங்', 'ṅā': 'ஙா', 'ṅi': 'ஙி', 'ṅī': 'ஙீ', 'ṅu': 'ஙு', 'ṅū': 'ஙூ', 'ṅe': 'ஙெ', 'ṅē': 'ஙே', 'ṅai': 'ஙை', 'ṅo': 'ஙொ', 'ṅō': 'ஙோ', 'ṅau': 'ஙௌ',
    'c': 'ச்', 'cā': 'சா', 'ci': 'சி', 'cī': 'சீ', 'cu': 'சு', 'cū': 'சூ', 'ce': 'செ', 'cē': 'சே', 'cai': 'சை', 'co': 'சொ', 'cō': 'சோ', 'cau': 'சௌ',
    'ñ': 'ஞ்', 'ñā': 'ஞா', 'ñi': 'ஞி', 'ñī': 'ஞீ', 'ñu': 'ஞு', 'ñū': 'ஞூ', 'ñe': 'ஞெ', 'ñē': 'ஞே', 'ñai': 'ஞை', 'ño': 'ஞொ', 'ñō': 'ஞோ', 'ñau': 'ஞௌ',
    'ṭ': 'ட்', 'ṭā': 'டா', 'ṭi': 'டி', 'ṭī': 'டீ', 'ṭu': 'டு', 'ṭū': 'டூ', 'ṭe': 'டெ', 'ṭē': 'டே', 'ṭai': 'டை', 'ṭo': 'டொ', 'ṭō': 'டோ', 'ṭau': 'டௌ',
    'ṇ': 'ண்', 'ṇā': 'ணா', 'ṇi': 'ணி', 'ṇī': 'ணீ', 'ṇu': 'ணு', 'ṇū': 'ணூ', 'ṇe': 'ணெ', 'ṇē': 'ணே', 'ṇai': 'ணை', 'ṇo': 'ணொ', 'ṇō': 'ணோ', 'ṇau': 'ணௌ',
    't': 'த்', 'tā': 'தா', 'ti': 'தி', 'tī': 'தீ', 'tu': 'து', 'tū': 'தூ', 'te': 'தெ', 'tē': 'தே', 'tai': 'தை', 'to': 'தொ', 'tō': 'தோ', 'tau': 'தௌ',
    'n': 'ந்', 'nā': 'நா', 'ni': 'நி', 'nī': 'நீ', 'nu': 'நு', 'nū': 'நூ', 'ne': 'நெ', 'nē': 'நே', 'nai': 'நை', 'no': 'நொ', 'nō': 'நோ', 'nau': 'நௌ',
    'p': 'ப்', 'pā': 'பா', 'pi': 'பி', 'pī': 'பீ', 'pu': 'பு', 'pū': 'பூ', 'pe': 'பெ', 'pē': 'பே', 'pai': 'பை', 'po': 'பொ', 'pō': 'போ', 'pau': 'பௌ',
    'm': 'ம்', 'mā': 'மா', 'mi': 'மி', 'mī': 'மீ', 'mu': 'மு', 'mū': 'மூ', 'me': 'மெ', 'mē': 'மே', 'mai': 'மை', 'mo': 'மொ', 'mō': 'மோ', 'mau': 'மௌ',
    'y': 'ய்', 'yā': 'யா', 'yi': 'யி', 'yī': 'யீ', 'yu': 'யு', 'yū': 'யூ', 'ye': 'யெ', 'yē': 'யே', 'yai': 'யை', 'yo': 'யொ', 'yō': 'யோ', 'yau': 'யௌ',
    'r': 'ர்', 'rā': 'ரா', 'ri': 'ரி', 'rī': 'ரீ', 'ru': 'ரு', 'rū': 'ரூ', 're': 'ரெ', 'rē': 'ரே', 'rai': 'ரை', 'ro': 'ரொ', 'rō': 'ரோ', 'rau': 'ரௌ',
    'l': 'ல்', 'lā': 'லா', 'li': 'லி', 'lī': 'லீ', 'lu': 'லு', 'lū': 'லூ', 'le': 'லெ', 'lē': 'லே', 'lai': 'லை', 'lo': 'லொ', 'lō': 'லோ', 'lau': 'லௌ',
    'v': 'வ்', 'vā': 'வா', 'vi': 'வி', 'vī': 'வீ', 'vu': 'வு', 'vū': 'வூ', 've': 'வெ', 'vē': 'வே', 'vai': 'வை', 'vo': 'வொ', 'vō': 'வோ', 'vau': 'வௌ',
    'ḻ': 'ழ்', 'ḻā': 'ழா', 'ḻi': 'ழி', 'ḻī': 'ழீ', 'ḻu': 'ழு', 'ḻū': 'ழூ', 'ḻe': 'ழெ', 'ḻē': 'ழே', 'ḻai': 'ழை', 'ḻo': 'ழொ', 'ḻō': 'ழோ', 'ḻau': 'ழௌ',
    'ḷ': 'ள்', 'ḷā': 'ளா', 'ḷi': 'ளி', 'ḷī': 'ளீ', 'ḷu': 'ளு', 'ḷū': 'ளூ', 'ḷe': 'ளெ', 'ḷē': 'ளே', 'ḷai': 'ளை', 'ḷo': 'ளொ', 'ḷō': 'ளோ', 'ḷau': 'ளௌ',
    'ṟ': 'ற்', 'ṟā': 'றா', 'ṟi': 'றி', 'ṟī': 'றீ', 'ṟu': 'று', 'ṟū': 'றூ', 'ṟe': 'றெ', 'ṟē': 'றே', 'ṟai': 'றை', 'ṟo': 'றொ', 'ṟō': 'றோ', 'ṟau': 'றௌ',
    'ṉ': 'ன்', 'ṉā': 'னா', 'ṉi': 'னி', 'ṉī': 'னீ', 'ṉu': 'னு', 'ṉū': 'னூ', 'ṉe': 'னெ', 'ṉē': 'னே', 'ṉai': 'னை', 'ṉo': 'னொ', 'ṉō': 'னோ', 'ṉau': 'னௌ',
    'ka': 'க', 'ṅa': 'ங', 'ca': 'ச', 'ña': 'ஞ', 'ṭa': 'ட', 'ṇa': 'ண', 'ta': 'த', 'na': 'ந', 'pa': 'ப', 'ma': 'ம', 'ya': 'ய', 'ra': 'ர', 'la': 'ல', 'va': 'வ',
    'ḻa': 'ழ', 'ḷa': 'ள', 'ṟa': 'ற', 'ṉa': 'ன', 'a': 'அ', 'ā': 'ஆ', 'i': 'இ', 'ī': 'ஈ', 'u': 'உ', 'ū': 'ஊ', 'e': 'எ', 'ē': 'ஏ', 'ai': 'ஐ', 'o': 'ஒ', 'ō': 'ஓ', 'au': 'ஔ', 'ḥ.': 'ஃ',
    'ś': 'ஶ்', 'śa': 'ஶ', 'śā': 'ஶா', 'śi': 'ஶி', 'śī': 'ஶீ', 'śu': 'ஶு', 'śū': 'ஶூ', 'śe': 'ஶெ', 'śē': 'ஶே', 'śai': 'ஶை', 'śo': 'ஶொ', 'śō': 'ஶோ', 'śau': 'ஶௌ',
    'j': 'ஜ்', 'ja': 'ஜ', 'jā': 'ஜா', 'ji': 'ஜி', 'jī': 'ஜீ', 'ju': 'ஜு', 'jū': 'ஜூ', 'je': 'ஜெ', 'jē': 'ஜே', 'jai': 'ஜை', 'jo': 'ஜொ', 'jō': 'ஜோ', 'jau': 'ஜௌ',
    'ṣ': 'ஷ்', 'ṣa': 'ஷ', 'ṣā': 'ஷா', 'ṣi': 'ஷி', 'ṣī': 'ஷீ', 'ṣu': 'ஷு', 'ṣū': 'ஷூ', 'ṣe': 'ஷெ', 'ṣē': 'ஷே', 'ṣai': 'ஷை', 'ṣo': 'ஷொ', 'ṣō': 'ஷோ', 'ṣau': 'ஷௌ',
    's': 'ஸ்', 'sa': 'ஸ', 'sā': 'ஸா', 'si': 'ஸி', 'sī': 'ஸீ', 'su': 'ஸு', 'sū': 'ஸூ', 'se': 'ஸெ', 'sē': 'ஸே', 'sai': 'ஸை', 'so': 'ஸொ', 'sō': 'ஸோ', 'sau': 'ஸௌ',
    'h': 'ஹ்', 'ha': 'ஹ', 'hā': 'ஹா', 'hi': 'ஹி', 'hī': 'ஹீ', 'hu': 'ஹு', 'hū': 'ஹூ', 'he': 'ஹெ', 'hē': 'ஹே', 'hai': 'ஹை', 'ho': 'ஹொ', 'hō': 'ஹோ', 'hau': 'ஹௌ',
    'kṣ': 'க்ஷ்', 'kṣa': 'க்ஷ', 'kṣā': 'க்ஷா', 'kṣi': 'க்ஷி', 'kṣī': 'க்ஷீ', 'kṣu': 'க்ஷு', 'kṣū': 'க்ஷூ', 'kṣe': 'க்ஷெ', 'kṣē': 'க்ஷே', 'kṣai': 'க்ஷை', 'kṣo': 'க்ஷொ', 'kṣō': 'க்ஷோ', 'kṣau': 'க்ஷௌ',
    'srī':'ஸ்ரீ'
}

def split_word_by_regex(sentence):
    tokens = re.findall(r'\b\w+\b|[.,!?;’‘‘”“]', sentence)
    return tokens

def tokenizing_without_clitics(input_list):
    new_sentence_list = []
    def split_word_from_end(word):
        for search_word in search_list_1:
            if word.endswith(search_word):
                split_index = word.rfind(search_word)
                if split_index != -1:
                    split1 = word[:split_index]
                    split2 = word[split_index:]
                    return split1, split2
        return word, None

    prev_output = input_list

    while True:
        output = []
        for word in prev_output:
            split1, split2 = split_word_from_end(word)
            if split1:
                output.append(split1)
            if split2:
                output.append(split2)

        if output == prev_output:
            break

        prev_output = output

    return output


def tokenizing_with_clitics(input_list):
    new_list = []

    def split_word_from_end(wor):
        if wor in search_list_2 or wor in search_list_1:
            return [wor]

        for search_word in search_list_2: 
            if wor.endswith(search_word):
                split_index = wor.rfind(search_word)
                if split_index != -1:
                    split1 = wor[:split_index]
                    split2 = wor[split_index:]
                    return [split1, split2]
        return [word]

    for word in input_list:
        splits = split_word_from_end(word)
        new_list.extend(splits)

    return new_list


def is_english_word(word):
    english_dictionary = enchant.Dict("en_US")
    return english_dictionary.check(word)

def convert_to_tamil(input_word):
    output = ""
    if input_word and len(input_word) > 0: 
        input_word = input_word.lower()
        temp = input_word[0]
        for char in input_word[1:]:
            temp += char
            if temp in tamil_transliteration:
                continue
            else:
                output += tamil_transliteration[temp[:-1]]
                temp = char

        if temp in tamil_transliteration:
            output += tamil_transliteration[temp]
    else:
         output=" "
        
    return output


def perform_transiliteration(line):
        transl_model = Ta2EnTransliterate()
        with open('transliteration-mapping.csv','r',encoding='utf-8') as f:
            trans_text = f.read()
        transl_model.formDictFromCommaSepTxt(trans_text)
        x = transl_model.transliterate(line)
        # print(x)
        transliterated_text = x 
        return transliterated_text


def fin_res(user_input):
    inp=str(user_input)
    input_sentence = perform_transiliteration(inp)
    out1 = split_word_by_regex(input_sentence)
    out2 = tokenizing_with_clitics(out1)
    out3 = tokenizing_without_clitics(out2)

    ex_case=["um","anta","ai","es","pi","pas","m","cella"]
    kcdtpr=['k', 'c','ṭ','t','p','r']
    uyir_eluthu=['a', 'ā', 'i', 'ī', 'u', 'ū', 'e', 'ē', 'ai', 'o', 'ō', 'au']
    input_list = out3
    tamil_word=[]
    for i in range(len(input_list)):
        input_word=input_list[i].lower()
        if input_word in ".,!?;’‘‘”“" or input_word.isdigit() or ((is_english_word(input_word)==True) and (input_word not in ex_case)):
            tamil_word.append(input_word)
        elif input_word[-1]=='v' or input_word[-1]=='y': #udampadu mei
            input_word=input_word[:len(input_word)-1]
            tamil_word.append(convert_to_tamil(input_word))
        elif(input_word[-1] in kcdtpr):
            if input_word[-1] in kcdtpr[:-1] and input_list[i+1][0] in uyir_eluthu:
                input_word=input_word+"u"
                tamil_word.append(convert_to_tamil (input_word))     
            else:
                tamil_word.append(convert_to_tamil(input_word))
        else:
           tamil_word.append(convert_to_tamil(input_word))
    return tamil_word

# inp=input("Enter text: ")
# fin=fin_res(inp)
# print(fin)