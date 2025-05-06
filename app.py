from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

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

         # Separate numerical and categorical
        cat_cols.append("smoking_status")
        X_num = df[num_cols]
        full_cat_cols = list(cat_cols) + ["smoking_status"] if "smoking_status" not in cat_cols else list(cat_cols)
        X_cat = df[full_cat_cols]
    
        # Transform categorical variables
        X_cat_transformed = preprocessor.transform(X_cat)

        # Concatenate numerical + transformed categorical
        import numpy as np
        x_train = np.concatenate([X_num.values, X_cat_transformed], axis=1)

        # Make prediction
        prediction = model.predict(x_train)

        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
