# WaterQualityAnalyses

This project aims to predict water quality based on various parameters. The system includes a web-based form allowing users to input specific water quality parameters, and a machine learning model implemented in Python and Flask predicts whether the water is of good quality or not.

## Usage

### Web Application

1. Open the `index.html` file in a web browser.
2. Fill in the form with the relevant parameters, including pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, and turbidity.
3. Click the "Submit" button to send the data to the server for prediction.
4. The prediction result will be displayed on the page, indicating whether the water is of good quality or not.

### Python Application

1. Ensure you have the required Python libraries installed. You can install them using:

    ```bash
    pip install flask numpy scikit-learn
    ```

2. Run the Flask application:

    ```bash
    python app.py
    ```

3. Open a web browser and go to http://127.0.0.1:5000/ to access the web form.

4. Follow steps 2-4 from the "Web Application" section above.

## Model Training

The machine learning model used for prediction is a Random Forest Classifier. The model is trained using a dataset (`processed_data.csv`) that includes water quality parameters and a target variable indicating water potability.

To retrain the model:

1. Open a Jupyter notebook or Python environment.
2. Execute the code in the "Model Training" section of the provided Python script (`model_training.py`).
3. The trained model will be saved to a file named `water_model.pkl`.

## Data Preprocessing

The dataset used for training may contain missing values, which are handled by imputing the mean values for the respective columns. Additionally, exploratory data analysis (EDA) is performed, and correlations between variables are visualized using various plots and the `corrplot` library in R.

## Dependencies

- Flask
- NumPy
- Scikit-learn
- Pandas
- Pickle
- ggplot2 (R package)
- corrplot (R package)
- skimr (R package)

## Additional Notes

- The `style.css` file contains styles for the HTML elements.
- The application includes visualizations generated using ggplot2 and corrplot in R. These visualizations provide insights into the dataset's distribution and correlations between variables.
