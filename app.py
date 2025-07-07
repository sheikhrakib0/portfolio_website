from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os
from sklearn.compose import ColumnTransformer

app = Flask(__name__)
CORS(app)  # Allow frontend to call this backend

# Load the saved model and components
model_data = joblib.load('model.joblib')

model = model_data['model']
preprocessor = model_data['preprocessor']
num_cols = model_data['numerical_cols']
cat_cols = model_data['categorical_cols']
encoded_cols = model_data['encoded_cols']


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from frontend
        input_data = request.get_json()

        # Convert dict to DataFrame
        df = pd.DataFrame([input_data])
        df[encoded_cols] = preprocessor.transform(df)
        X = df[num_cols + encoded_cols]
        # Make prediction
        prediction = model.predict(X)
        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))