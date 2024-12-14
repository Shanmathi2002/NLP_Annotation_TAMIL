import pandas as pd
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input,Embedding, SimpleRNN, Dense,concatenate
from sklearn.model_selection import train_test_split
import pickle

def isNaN(val):
    return val!=val
df = pd.read_csv("full dataset.csv",dtype=str)

df['WORD'] = df['WORD'].astype('str')
words = []
upos = []
xpos=[]
X1 = []
X2=[]
Y = []
for i in range(len(df)):
    if df['UPOS'].iloc[i] != "_" and isNaN(df['UPOS'].iloc[i]) == False:
        words.append(df['WORD'].iloc[i])
        upos.append(df['UPOS'].iloc[i])
        xpos.append(df['XPOS'].iloc[i])
    elif isNaN(df['ID'].iloc[i]) == True:
        X1.append(words)
        X2.append(upos)
        Y.append(xpos)
        words = []
        upos= []
        xpos=[]
n = len(X1)
X1 = X1[1:n-1]
X2 = X2[1:n-1]
Y = Y[1:n-1]
X1_S = [word for sublist in [sentence for sentence in X1] for word in sublist]
X2_S = [word for sublist in [sentence for sentence in X2] for word in sublist]
Y1 = [word for sublist in [sentence for sentence in Y] for word in sublist]
data={
    'X1':X1_S,
    'X2':X2_S,
    'Y':Y1
}
column_names = ['X1','X2','Y']
df1 = pd.DataFrame(data, columns=column_names)
X1_dict = {word: idx for idx, word in enumerate(set(df1['X1']))}
X2_dict = {word: idx for idx, word in enumerate(set(df1['X2']))}
Y_dict = {word: idx for idx, word in enumerate(set(df1['Y']))}

# Map words to numerical indices using the dictionaries
df1['X1_index'] = df1['X1'].map(X1_dict)
df1['X2_index'] = df1['X2'].map(X2_dict)
df1['Y_index'] = df1['Y'].map(Y_dict)

# Prepare input and output data
X1_train = df1['X1_index'].values.reshape(-1, 1)
X2_train = df1['X2_index'].values.reshape(-1, 1)
Y_train = df1['Y_index'].values
X1_train, X1_test, X2_train, X2_test, Y_train, Y_test = train_test_split(X1_train, X2_train, Y_train, test_size=0.1, random_state=42)
word_input = Input(shape=(1,))
upos_input = Input(shape=(1,))



# Add embedding layer for X1 feature
word_embedding = Embedding(input_dim=len(X1_dict), output_dim=128)(word_input)
upos_embedding = Embedding(input_dim=len(X2_dict), output_dim=128)(upos_input)

merged_embeddings = concatenate([word_embedding, upos_embedding], axis=-1)

# Apply SimpleRNN layer
rnn_output = SimpleRNN(128)(merged_embeddings)
# Add embedding layer for X2 feature

  # LSTM layer for sequential data

# Output layer with softmax activation for predicting Y
output =Dense(len(Y_dict), activation='softmax')(rnn_output)
model_2 = Model(inputs=[word_input, upos_input], outputs=output)

model_2.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model using X1_train, X2_train as input features, and Y_train as output labels
model_2.fit([X1_train, X2_train], Y_train, epochs=10, batch_size=256, validation_data=([X1_test, X2_test], Y_test))
test_loss, test_accuracy = model_2.evaluate([X1_test, X2_test], Y_test, verbose=2)
print(f'Test Loss: {test_loss}, Test Accuracy: {test_accuracy}')
train_loss, train_accuracy = model_2.evaluate([X1_train, X2_train], Y_train, verbose=2)
print(f'Train Loss: {train_loss}, Train Accuracy: {train_accuracy}')

model_2.save('rnn_model_2.h5')

# Save the input and output dictionaries
with open('X1_dict.pkl', 'wb') as f:
    pickle.dump(X1_dict, f)

with open('X2_dict.pkl', 'wb') as f:
    pickle.dump(X2_dict, f)

with open('Y_dict.pkl', 'wb') as f:
    pickle.dump(Y_dict, f)

