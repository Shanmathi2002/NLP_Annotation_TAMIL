from flask import Flask, request, jsonify,render_template
import pickle
from tensorflow.keras.models import load_model
from sklearn.metrics import cohen_kappa_score
from tokenization import perform_transiliteration
from flask_cors import cross_origin
import numpy as np
from tokenization import fin_res
from lemma_rules import lem_res
from morph import morph
from xpos import prediction
from deprel import deprel_pred
from spaceafter import NER
import traceback
from googletrans import Translator
app = Flask(__name__)

# Load the LSTM model and dictionaries
model = load_model('rnn_model.h5')
translator = Translator()

with open('word_to_index.pkl', 'rb') as f:
    word_to_index = pickle.load(f)

with open('pos_to_index.pkl', 'rb') as f:
    pos_to_index = pickle.load(f)


global_value=[]
@app.route("/")
@app.route('/home')
@app.route('/index')
@cross_origin()
def home():
    return render_template("index.html")

@app.route('/rules')
def home2():
    return render_template("rules.html")

@app.route("/annotation", methods=["GET", "POST"])
def annotation():
    if request.method == "GET":
        return render_template('annotation.html')
    if request.method == "POST":
            user_input = request.form['user_input']
            translation=translator.translate(user_input, src='ta', dest='en')
            translate=translation.text
            transliteration=perform_transiliteration(user_input)
            word_list = fin_res(user_input)
            lemma_list=[]
            pos_list=[]
            m=[]
            xpos_list=[]
            # Convert word to numerical index using word_to_index dictionary
            for word in word_list:
                le=lem_res(word)
                lemma_list.append(le)
                if word in word_to_index:
                    word_index = word_to_index[word]
                    predicted_pos_index = model.predict([[word_index]])
                    predicted_pos_index = np.argmax(predicted_pos_index)
                    predicted_pos = [pos for pos, index in pos_to_index.items() if index == predicted_pos_index][0]
                    pos_list.append(predicted_pos)
                    xpos_list.append(prediction(word,predicted_pos)) 
                    m.append(morph(predicted_pos,perform_transiliteration(word)))
                else:
                    output="NOUN"
                    pos_list.append(output)
                    xpos_list.append(output)
                    m.append(morph(output,perform_transiliteration(word)))
            dep=deprel_pred(word_list,pos_list,xpos_list) 
            ner=NER(user_input,word_list)
            value=[word_list,lemma_list,pos_list,xpos_list,m,dep,ner]
            global global_value
            global_value = value
            return render_template('annotation.html', sent=user_input,translit=transliteration,transla=translate,ver1=word_list,ver2=lemma_list, ver3=pos_list,ver4=xpos_list,ver5=m,ver6=dep,ver7=ner)    
            
@app.route("/iaa_score",  methods=["GET", "POST"])
def iaa_score():
    if request.method == "GET":
        return render_template('iaa_score.html')
    
    if request.method == "POST":
        user_input = request.form['user_input']
        
        # Translate and transliterate the input
        translation=translator.translate(user_input, src='ta', dest='en')
        translate=translation.text
        transliteration = perform_transiliteration(user_input)
        
        tokens = request.form.getlist("tokens[]")
        lemma = request.form.getlist("lemma[]")
        upos = request.form.getlist("upos[]")
        xpos = request.form.getlist("xpos[]")
        deprel = request.form.getlist("deprel[]")
        
        data = [tokens, lemma, upos, xpos, deprel]
        
        # Calculate predicted annotations
        word_list = fin_res(user_input)
        lemma_list = []
        pos_list = []
        xpos_list = []

        for word in word_list:
            le = lem_res(word)
            lemma_list.append(le)
            if word in word_to_index:
                word_index = word_to_index[word]
                predicted_pos_index = model.predict([[word_index]])
                predicted_pos_index = predicted_pos_index.argmax()
                predicted_pos = [pos for pos, index in pos_to_index.items() if index == predicted_pos_index][0]
                pos_list.append(predicted_pos)
                xpos_list.append(prediction(word, predicted_pos))
            else:
                output = "NOUN"
                pos_list.append(output)
                xpos_list.append(output)

        dep = deprel_pred(word_list, pos_list, xpos_list)
        predicted_annotations = [word_list, lemma_list, pos_list, xpos_list, dep]
        
        # Calculate IAA score
        try:
            k = []
            if not all(len(lst) == len(tokens) for lst in [lemma, upos, xpos, deprel]):
                raise ValueError("All lists must have the same length as tokens list")
            else:
                for i in range(len(predicted_annotations)):
                    kappa_score = cohen_kappa_score(predicted_annotations[i], data[i])
                    if kappa_score < 0:
                        k.append(0)
                    else:
                        k.append(round(kappa_score, 3))
            
            response_data = {
                "translation": translate,
                "transliteration": transliteration,
                "predictedAnnotations": predicted_annotations,
                "iaaScore": k
            }
            print(response_data)
            return jsonify(response_data)

        except Exception as e:
            error_message = "Recheck your Tokenization again !!"
            traceback.print_exc()
            return jsonify(error=str(error_message)), 500
    
if __name__=="__main__":
   app.run(debug=True)