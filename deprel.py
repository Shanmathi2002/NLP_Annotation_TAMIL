import tensorflow
from tensorflow import keras
from tensorflow.keras.models import load_model
import numpy as np
import joblib
model_3= load_model('rnn_model_3.h5')
with open('word_v1.pkl', 'rb') as f:
    word_v1 = joblib.load(f)

with open('upos_v1.pkl', 'rb') as f:
    upos_v2 = joblib.load(f)

with open('xpos_v3.pkl', 'rb') as f:
    xpos_v3 = joblib.load(f)

with open('deprel_v1.pkl', 'rb') as f:
    deprel_v1 = joblib.load(f)

def convert_to_list_dep(input_list):
    unpacked_list = [item for sublist in input_list for item in sublist]
    split_list = unpacked_list[0].split() 
    return split_list
def deprel_pred(fin,upos,xpos):
        X1 = fin
        X2 = upos
        X3 = xpos
        X1_encoded = word_v1.texts_to_sequences([X1])
        X1_padded = keras.preprocessing.sequence.pad_sequences(X1_encoded, maxlen=37)
        X2_encoded = upos_v2.texts_to_sequences([X2]) 
        X2_padded = keras.preprocessing.sequence.pad_sequences(X2_encoded, maxlen=37)
        X3_encoded = xpos_v3.texts_to_sequences([X3])  
        X3_padded =keras.preprocessing.sequence.pad_sequences(X3_encoded, maxlen=37)
        predictions = model_3.predict([X1_padded, X2_padded, X3_padded])
        predicted_Y2_text = []
        for sequence in predictions:
            predicted_Y2_text.append(deprel_v1.sequences_to_texts([[np.argmax(token) for token in sequence]]))
        deprel=convert_to_list_dep(predicted_Y2_text)
        return deprel

# fin = ['பவுத்தர்கள்', 'நிறைந்த', 'தனி', 'நாடு', '.']
# upos = ['noun','verb','adj','noun','punct']
# xpos= ['noun','in','adj','noun','punct']
# print(deprel_pred(fin,upos,xpos))