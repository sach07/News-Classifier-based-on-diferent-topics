from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle

app = Flask(__name__)

# load trained classifier
#clf_path = 'Desktop/Unfound Assignment/classifier.pickle'
with open('classifier.pickle','rb') as f:
    classifier = pickle.load(f)
    
with open('tfidfmodel.pickle','rb') as f:
    vectorizer = pickle.load(f)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = vectorizer.transform(data).toarray()
		my_prediction = classifier.predict(vect)
	return render_template('result.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True)
