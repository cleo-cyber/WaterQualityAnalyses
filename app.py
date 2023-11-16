import numpy as np
from sklearn.preprocessing import StandardScaler

from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
# Load the model
model = pickle.load(open('water_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
        
        # Get the data from the POST request.
        sc=StandardScaler()
        if request.method == 'POST':
            ph = float(request.form['ph'])
            Hardness = float(request.form['hardness'])
            Solids = float(request.form['solids'])
            Chloramines = float(request.form['chloramines'])
            Sulfate = float(request.form['sulfate'])
            Conductivity = float(request.form['conductivity'])
            Organic_carbon = float(request.form['organic_carbon'])
            Trihalomethanes = float(request.form['trihalomethanes'])
            Turbidity = float(request.form['turbidity'])
            data = np.array([[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])
            # Scale data to be fed to model
            data = sc.fit_transform(data)
            my_prediction = model.predict(data)
            return render_template('index.html', prediction=my_prediction)
        

if __name__ == "__main__":
    app.run(debug=True)

