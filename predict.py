
# ## Load the model

import pickle

from flask import Flask
from flask import request
from flask import jsonify

input_file = 'model_C=1.0.bin'

with open(input_file, 'rb') as f_in: 
    dv, model = pickle.load(f_in)


# model

# # to test the model is loaded and working properly or not
# customer = {'age': '26-39',
#   'gender': 'male',
#   'driving_experience': '0-9y',
#   'education': 'none',
#   'income': 'middle_class',
#   'vehicle_ownership': 1.0,
#   'married': 1.0,
#   'children': 0.0,
#   'postal_code': 10238,
#   'speeding_violations': 2,
#   'duis': 0,
#   'past_accidents': 0,
#   'vehicle_year': 'after_2015',
#   'type_of_vehicle': 'sports_car',
#   'id': 18647,
#   'credit_score': 0.7179927843792123,
#   'annual_mileage': 9000.0}

app = Flask('decision')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    decision =  y_pred >= 0.5

    outcome = 'Yes' if (bool(decision)==1) else 'No'

    result = {
    'decision_probability': float(y_pred),
    'accept_or_reject': outcome
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)