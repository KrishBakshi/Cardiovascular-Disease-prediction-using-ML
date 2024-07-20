from flask import Flask, request, jsonify
import util


app = Flask(__name__)

@app.route('/predict', methods=['GET','POST'])
def predict():
    general_health = int(request.form['general_health']),
    checkup = int(request.form['checkup']),
    exercise = int(request.form['exercise']),
    skin_cancer = int(request.form['skin_cancer']),
    other_cancer = int(request.form['other_cancer']),
    depression = int(request.form['depression']),
    diabetes = int(request.form['diabetes']),
    arthritis = int(request.form['arthritis']),
    age_category = int(request.form['age_category']),
    height = float(request.form['height']),
    weight = float(request.form['weight']),
    bmi = float(request.form['bmi']),
    smoking_history = int(request.form['smoking_history']),
    alcohol_consumption = int(request.form['alcohol_consumption']),
    fruit_consumption = int(request.form['fruit_consumption']),
    green_vegetables_consumption = int(request.form['green_vegetables_consumption']),
    friedpotato_consumption = int(request.form['friedpotato_consumption']),
    sex_female = int(request.form['sex_female'])


    response = jsonify({
        'Cardio-Vascular presence': util.predict(general_health,checkup,exercise,skin_cancer,other_cancer,depression,diabetes,arthritis,
                                        age_category,height,weight,bmi,smoking_history,alcohol_consumption,fruit_consumption,green_vegetables_consumption,
                                        friedpotato_consumption,sex_female)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()