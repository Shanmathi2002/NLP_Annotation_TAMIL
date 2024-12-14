
import pickle
from tensorflow.keras.models import load_model
import numpy as np


# Load the LSTM model and dictionaries
model_2 = load_model('rnn_model_2.h5')
with open('X1_dict.pkl', 'rb') as f:
    X1_dict = pickle.load(f)

with open('X2_dict.pkl', 'rb') as f:
    X2_dict = pickle.load(f)

with open('Y_dict.pkl', 'rb') as f:
    Y_dict = pickle.load(f)
# Default values for unknown words and UPOS tags
UNK_TOKEN = 'UNK'
UNK_INDEX = X1_dict.get(UNK_TOKEN, 0)


def convert_input_to_indices(word, upos):
    # Get indices from the dictionaries, return a default index for unknown words or UPOS tags
    word_index = X1_dict.get(word, UNK_INDEX)
    upos_index = X2_dict.get(upos, 0)
    return word_index, upos_index

def prediction(word, upos):
    # Get data from the POST request
    
   

    word_index, upos_index = convert_input_to_indices(word, upos)
    prediction = model_2.predict([np.array([word_index]), np.array([upos_index])])  # Use double brackets for multi-input models
    predicted_xpos_index = np.argmax(prediction)
    
    #predicted_xpos = list(Y_dict.keys())[list(Y_dict.values()).index(predicted_xpos_index)]
        # Assuming you have index_to_xpos dictionary
    try:
        predicted_xpos = list(Y_dict.keys())[list(Y_dict.values()).index(predicted_xpos_index)]
    except ValueError:  # Handle the case where predicted_xpos_index is not found in Y_dict
        predicted_xpos = upos  # If not found, return UPOS
    
    return predicted_xpos

    