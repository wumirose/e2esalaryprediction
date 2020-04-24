#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


# In[6]:


app = Flask(__name__) #initialize Flask
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')  # Allows us to '/' creates any number of URL with respect to the API
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    features = [int(i) for i in request.form.values()]
    feature_array = [np.array(features)]
    pred = model.predict(feature_array)
    prediction = round(pred[0], 2)
   
    return render_template('index.html', prediction_text = 'The salary of the employee should be #{}'.format(prediction))

@app.route('/predict_api', methods = ['POST'])
def predict_api():
    dt = request.get_json(force = True)
    feature_array = [np.array(list(dt.values()))]
    pred = model.predict(feature_array)
    
    prediction = pred[0]
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug = True)


# In[ ]:




