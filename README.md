# WaterQualityAnalyses
Water Quality Prediction
This project focuses on predicting water quality based on various parameters. The application includes a web-based form where users can input specific water quality parameters, and the system will predict whether the water is of good quality or not. The prediction is made using a machine learning model implemented in Python and Flask.

Usage
Web Application
Open the index.html file in a web browser.
Fill in the form with the relevant parameters, including pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, and turbidity.
Click the "Submit" button to send the data to the server for prediction.
The prediction result will be displayed on the page, indicating whether the water is of good quality or not.
Python Application
Ensure you have the required Python libraries installed. You can install them using:

bash
Copy code
pip install flask numpy scikit-learn
Run the Flask application:

bash
Copy code
python app.py
Open a web browser and go to http://127.0.0.1:5000/ to access the web form.

Follow steps 2-4 from the "Web Application" section above.

Model Training
The machine learning model used for prediction is a Random Forest Classifier. The model is trained using a dataset (processed_data.csv) that includes water quality parameters and a target variable indicating water potability.

To retrain the model:

Open a Jupyter notebook or Python environment.
Execute the code in the "Model Training" section of the provided Python script (model_training.py).
The trained model will be saved to a file named water_model.pkl.
Data Preprocessing
The dataset used for training may contain missing values, which are handled by imputing the mean values for the respective columns. Additionally, exploratory data analysis (EDA) is performed, and correlations between variables are visualized using various plots and the corrplot library in R.

Dependencies
Flask
NumPy
Scikit-learn
Pandas
Pickle
ggplot2 (R package)
corrplot (R package)
skimr (R package)
Additional Notes
The style.css file contains styles for the HTML elements.
The application includes visualizations generated using ggplot2 and corrplot in R. These visualizations provide insights into the dataset's distribution and correlations between variables.
