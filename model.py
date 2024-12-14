import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from sklearn.model_selection import train_test_split
import pickle

def isNaN(val):
    return val!=val
df = pd.read_csv("full dataset.csv",dtype=str)

df['WORD'] = df['WORD'].astype('str')
words = []
pos = []
X = []
Y = []
for i in range(len(df)):
    if df['UPOS'].iloc[i] != "_" and isNaN(df['UPOS'].iloc[i]) == False:
        words.append(df['WORD'].iloc[i])
        pos.append(df['UPOS'].iloc[i])
    elif isNaN(df['ID'].iloc[i]) == True:
        X.append(words)
        Y.append(pos)
        words = []
        pos= []
n = len(X)
X = X[1:n-1]
Y = Y[1:n-1]
X1 = [word for sublist in [sentence for sentence in X] for word in sublist]
Y1 = [word for sublist in [sentence for sentence in Y] for word in sublist]
data={
    'X':X1,
    'Y':Y1
}
column_names = ['X','Y']
df1 = pd.DataFrame(data, columns=column_names)

vocab = set()
word_to_index = {}  # Dictionary for words to numerical indices
pos_to_index = {}   # Dictionary for POS tags to numerical indices
train_data = []

# Populate vocab, word_to_index, pos_to_index, and train_data
for index, row in df1.iterrows():
    word = row['X']
    pos = row['Y']
    if pos is not None:
        vocab.add(word)
        vocab.add(pos)
        if word not in word_to_index:
            word_to_index[word] = len(word_to_index)  # Assign a unique index to each unique word
        if pos not in pos_to_index:
            pos_to_index[pos] = len(pos_to_index)  # Assign a unique index to each unique POS tag
        train_data.append((word, pos))

# Create training data
X_train = []
y_train = []
for word, pos in train_data:
    X_train.append([word_to_index[word]])  
    y_train.append(pos_to_index[pos]) 
X_train = np.array(X_train)
y_train = np.array(y_train)

X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.1, random_state=42)


model_rnn = Sequential()
model_rnn.add(Embedding(input_dim=len(vocab), output_dim=128, input_length=1))
model_rnn.add(SimpleRNN(64, return_sequences=True))  # return_sequences=True for stacking RNN layers
model_rnn.add(SimpleRNN(64))  # Another SimpleRNN layer
model_rnn.add(Dense(128, activation='relu'))  # Additional Dense layer with 128 neurons and ReLU activation
model_rnn.add(Dense(len(vocab), activation='softmax'))

model_rnn.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# Train the model
model_rnn.fit(X_train, y_train, epochs=15,batch_size=256,verbose=2)

test_loss, test_accuracy = model_rnn.evaluate(X_test, y_test, verbose=2)
print(f'Test Loss: {test_loss}, Test Accuracy: {test_accuracy}')
train_loss, train_accuracy = model_rnn.evaluate(X_train, y_train, verbose=2)

print(f'Train Loss: {train_loss}, Train Accuracy: {train_accuracy}')

model_rnn.save('rnn_model.h5')

with open('word_to_index.pkl', 'wb') as f:
    pickle.dump(word_to_index, f)

with open('pos_to_index.pkl', 'wb') as f:
    pickle.dump(pos_to_index, f)