
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "API is working!"


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = request.json
    else:
        data = request.args

    
    def to_bool(x):
        return str(x).lower() in ['1', 'true', 'yes']

  
    fever = to_bool(data.get('fever'))
    cough = to_bool(data.get('cough'))
    fatigue = to_bool(data.get('fatigue'))
    headache = to_bool(data.get('headache'))
    sore_throat = to_bool(data.get('sore_throat'))
    body_pain = to_bool(data.get('body_pain'))

    
    if fever and cough and fatigue:
        disease = "Flu"
    elif cough and sore_throat:
        disease = "Common Cold"
    elif headache and fatigue:
        disease = "Migraine"
    elif fever and body_pain:
        disease = "Viral Infection"
    else:
        disease = "No major disease"

    # Return the result as JSON
    return jsonify({
        "predicted_disease": disease,
        "symptoms_received": {
            "fever": fever,
            "cough": cough,
            "fatigue": fatigue,
            "headache": headache,
            "sore_throat": sore_throat,
            "body_pain": body_pain
        }
    })


if __name__ == '__main__':
    app.run(debug=True)