import pandas as pd
import numpy as np
import re
from tokenization import perform_transiliteration,fin_res

def split_word_by_regex(sentence):
    tokens = re.findall(r'\b\w+\b|[.,!?;’‘‘”“]', sentence)
    return tokens

def check_space_after_tokens(string, tokens):
    result = []
    for i in range(len(tokens)):
        if i < len(tokens) - 1:
            if string.find(tokens[i] + tokens[i + 1]) != -1:
                result.append("SpaceAfter=No")
            else:
                result.append("")
    result.append("")

    return result

def NER(input1,input2): #input2 can be used from output of tokenization
    input1=perform_transiliteration(input1)
    st=input1.lower()
    tokens = split_word_by_regex(st)
    res= check_space_after_tokens(st, tokens)
    token_result_pairs = [(token, res[i]) for i, token in enumerate(tokens)]
    tr2=perform_transiliteration(" ".join(input2))
    tr2=tr2.lower()
    TL2 =split_word_by_regex(tr2)
    new_ans = []
    used_tokens = set()  # Keep track of used tokens
    for word in TL2:
        result = ""
        for token, token_result in token_result_pairs:
            if token.startswith(word) and (token, token_result) not in used_tokens:
                result = token_result
                used_tokens.add((token, token_result))
                break
        new_ans.append(result)
    return new_ans

# input1=input("enter tamil text: ")
# input2=fin_res(input1)
# print(input1,input2)
# new_ans=NER(input1,input2)
# print(len(new_ans),len(input2))
# for i in range(len(input2)):
#     print(input2[i],"               ",new_ans[i])
#     print()