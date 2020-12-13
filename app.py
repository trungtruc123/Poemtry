from flask import Flask, render_template, url_for, request, send_file, url_for
import torch
import transformers
from transformers import pipeline
from transformers import AutoTokenizer


#-------Load model saved-----------------#
def predict(in_text, max_length):
	custokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base", use_fast=False)
	poem = pipeline('text-generation', model="./checkpoint-40000", tokenizer=custokenizer, config={'max_length':1024})

	input_raw = '<s>'+in_text
	# a = poem(input_raw)
	a = poem(input_raw)
	out = a[0]['generated_text']
	out = out.strip('<s>')
	out = out.strip('</s>')
	out = out.split('<unk>')
	print('out:', out)
	return out



app = Flask(__name__)

@app.route('/')
def index():
	return render_template("poem.html")

@app.route('/', methods=['GET', 'POST'])
def classify2():
	if request.method == 'POST':
		raw_text = request.form['rawtext']
		
		results = predict(raw_text,max_length = 500)
	return render_template("poem.html", results=results,raw_text=raw_text)

if __name__ == '__main__':
	 app.run(debug= True, threaded=True)	